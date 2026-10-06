#!/usr/bin/env python3
"""Pull open Kalshi Mentions markets into data/markets.json (read-only, public API).

The public API rate-limits unauthenticated clients hard (HTTP 429), and there are ~450
Mentions series. So this script:
  1. lists all series in category=Mentions (1 call),
  2. scans series in priority order (priority list + most-recently-updated + highest volume)
     with /markets?series_ticker=...&status=open, caching each series result in
     data/cache/<SERIES>.json with its own fetch timestamp,
  3. stops when --budget seconds are used (scan resumes where it left off next run,
     because fresh cache entries younger than --max-age minutes are skipped),
  4. builds data/markets.json from the cache: events whose expected expiration
     (≈ event time) is within --days, each market tagged with the ET time its price was fetched.

Usage:
  python3 fetch.py                    # default: 7 days, 15 min budget
  python3 fetch.py --budget 3600      # longer scan (covers more series)
  python3 fetch.py --only KXTRUMPMENTIONB,KXMTPMENTION   # refresh specific series quickly
  python3 fetch.py --build-only       # rebuild markets.json from cache, no API calls
"""
import argparse, glob, json, os, re, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

BASE = "https://api.elections.kalshi.com/trade-api/v2"
SEARCH = "https://api.elections.kalshi.com/v1/search/series"
ET = ZoneInfo("America/New_York")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CACHE = os.path.join(DATA, "cache")
PACE = 1.0
PRIORITY = [  # high-traffic political/media series, then earnings calls known to report this week
    "KXTRUMPMENTION", "KXTRUMPMENTIONB", "KXTRUMPSAY", "KXDJTRALLY", "KXSECPRESSMENTION",
    "KXLEAVITTMENTION", "KXVANCEMENTION", "KXMTPMENTION",
    # week of 2026-09-28/29: CCL call Tue 9/29 (ticker SEP28); MU Wed 9/30; NKE Thu 10/1 (ticker SEP29); STZ ~10/5
    "KXEARNINGSMENTIONCCL", "KXMENTIONEARNCCL", "KXEARNINGSMENTIONMTN", "KXEARNINGSMENTIONMU", "KXMENTIONEARNMU",
    "KXEARNINGSMENTIONNKE", "KXMENTIONEARNNKE", "KXEARNINGSMENTIONSTZ",
    "KXWORLDNEWSMENTION", "KXFTNMENTION", "KXTRUMPSAYNICKNAME", "KXTRUMPSAYCOMPANY", "KXTRUMPSAYMONTH",
    "KXPOWELLMENTION", "KXFEDMENTION",
]


def now_et():
    return datetime.now(ET)


def get(path, params=None, deadline=None):
    q = "&".join(f"{k}={v}" for k, v in (params or {}).items() if v not in (None, ""))
    url = f"{BASE}{path}" + (f"?{q}" if q else "")
    attempt = 0
    while True:
        if deadline and time.time() > deadline:
            raise TimeoutError("budget exhausted")
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "mentions-app/0.1 (read-only)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = json.load(r)
            time.sleep(PACE)
            return body
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                attempt += 1
                if attempt > 40:
                    raise RuntimeError(f"gave up after {attempt} retries: {url}")
                time.sleep(min(20, 4 + 2 * attempt))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, OSError):
            attempt += 1
            if attempt > 40:
                raise
            time.sleep(5)


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def to_et(iso):
    if not iso:
        return None
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(ET).isoformat()


def slim(m, fetched):
    return {
        "ticker": m["ticker"],
        "event_ticker": m["event_ticker"],
        "word": m.get("yes_sub_title") or m.get("title"),
        "title": m.get("title"),
        "yes_bid": fnum(m.get("yes_bid_dollars")),
        "yes_ask": fnum(m.get("yes_ask_dollars")),
        "no_bid": fnum(m.get("no_bid_dollars")),
        "no_ask": fnum(m.get("no_ask_dollars")),
        "last_price": fnum(m.get("last_price_dollars")),
        "volume": fnum(m.get("volume_fp")),
        "volume_24h": fnum(m.get("volume_24h_fp")),
        "open_interest": fnum(m.get("open_interest_fp")),
        "status": m.get("status"),
        "close_time": m.get("close_time"),
        "close_time_et": to_et(m.get("close_time")),
        "expected_expiration_et": to_et(m.get("expected_expiration_time")),
        "rules_primary": m.get("rules_primary"),
        "rules_secondary": m.get("rules_secondary"),
        "price_fetched_at_et": fetched,
    }


def scan_series(ticker, deadline):
    mkts, cursor = [], ""
    while True:
        d = get("/markets", {"series_ticker": ticker, "status": "open", "limit": 1000, "cursor": cursor}, deadline)
        fetched = now_et().isoformat(timespec="seconds")
        mkts += [slim(m, fetched) for m in d.get("markets", [])]
        cursor = d.get("cursor")
        if not cursor or not d.get("markets"):
            break
    return mkts



def get_abs(url, deadline=None):
    """Same retry behavior as get(), for a full URL (the public search API)."""
    attempt = 0
    while True:
        if deadline and time.time() > deadline:
            raise TimeoutError("budget exhausted")
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "mentions-app/0.1 (read-only)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = json.load(r)
            time.sleep(PACE)
            return body
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                attempt += 1
                if attempt > 8:
                    raise RuntimeError(f"gave up after {attempt} retries: {url}")
                time.sleep(min(20, 4 + 2 * attempt))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, OSError):
            attempt += 1
            if attempt > 8:
                raise
            time.sleep(5)


def scan_event(event_ticker, deadline):
    mkts, cursor = [], ""
    while True:
        d = get("/markets", {"event_ticker": event_ticker, "status": "open", "limit": 1000, "cursor": cursor}, deadline)
        fetched = now_et().isoformat(timespec="seconds")
        mkts += [slim(m, fetched) for m in d.get("markets", [])]
        cursor = d.get("cursor")
        if not cursor or not d.get("markets"):
            break
    return mkts


def open_mention_events(deadline):
    """One search call returns each open Mentions series with its current event ticker.
    The daily board uses this instead of walking all ~450 series."""
    d = get_abs(SEARCH + "?status=open&category=Mentions&order_by=trending&page_size=200", deadline)
    out = []
    for e in d.get("current_page") or []:
        et = e.get("event_ticker")
        st = e.get("series_ticker")
        if et and st:
            out.append({
                "event_ticker": et,
                "series_ticker": st,
                "title": e.get("event_title") or e.get("series_title"),
                "sub_title": e.get("event_subtitle") or "",
            })
    return out


def cache_path(t):
    return os.path.join(CACHE, f"{t}.json")


def load_cache(t):
    try:
        with open(cache_path(t)) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def save_json(path, obj):
    with open(path + ".tmp", "w") as fh:
        json.dump(obj, fh, indent=1)
    os.replace(path + ".tmp", path)


MONTHS = {m: i for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split(), 1)}


def event_date(event_ticker):
    """Mentions event tickers embed the event date, e.g. KXTRUMPMENTION-26SEP29 -> 2026-09-29.
    (expected_expiration is typically ~2 weeks AFTER the event, so it's not a good event-time proxy.)"""
    m = re.search(r"-(\d{2})(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(\d{2})", event_ticker)
    if not m:
        return None
    try:
        return datetime(2000 + int(m.group(1)), MONTHS[m.group(2)], int(m.group(3))).date()
    except ValueError:
        return None


def build(series_meta, days, event_titles):
    now = datetime.now(timezone.utc)
    horizon = now + timedelta(days=days)
    # Count cache files separately from the series list. An earlier build reported
    # series_scanned/series_total as 103/16: scanned was every cache file, and the
    # total was a short series list (the --today path reuses data/series.json).
    by_event, cached_series, oldest = {}, set(), None
    for path in glob.glob(os.path.join(CACHE, "*.json")):
        c = json.load(open(path))
        cached_series.add(c.get("series_ticker") or os.path.splitext(os.path.basename(path))[0])
        oldest = min(oldest or c["fetched_at_et"], c["fetched_at_et"])
        s = series_meta.get(c["series_ticker"], {"ticker": c["series_ticker"], "title": c["series_ticker"]})
        for m in c["markets"]:
            if m.get("status") not in ("active", "open"):
                continue
            by_event.setdefault(m["event_ticker"], {"series": s, "markets": []})["markets"].append(m)
    events = []
    for et, blob in by_event.items():
        mkts = blob["markets"]; s = blob["series"]
        closes = [datetime.fromisoformat(m["close_time"].replace("Z", "+00:00")) for m in mkts if m.get("close_time")]
        exps = [datetime.fromisoformat(m["expected_expiration_et"]) for m in mkts if m.get("expected_expiration_et")]
        first_close = min(closes) if closes else None
        exp = min(exps) if exps else None
        ed = event_date(et)
        today = now.astimezone(ET).date()
        if ed is not None:
            # Kalshi ticker dates can lag the real speaking time by 1–2 days (CCL: SEP28→call Sep 29;
            # Nike: SEP29→call Oct 1). Keep ticker dates up to 2 days behind today if markets are still open.
            if ed < today - timedelta(days=2) or ed > (now + timedelta(days=days)).astimezone(ET).date():
                continue
        else:
            key = first_close or exp
            if key is None or key > horizon:
                continue
        if first_close and first_close < now:
            continue
        t = event_titles.get(et, {})
        events.append({
            "event_ticker": et,
            "series_ticker": s["ticker"],
            "series_title": s.get("title"),
            "title": t.get("title") or s.get("title"),
            "sub_title": t.get("sub_title"),
            "event_date": ed.isoformat() if ed else None,
            "first_close_et": first_close.astimezone(ET).isoformat() if first_close else None,
            "expected_expiration_et": exp.astimezone(ET).isoformat() if exp else None,
            "price_fetched_at_et": max(m["price_fetched_at_et"] for m in mkts),
            "decided": all((m["yes_ask"] is not None and m["yes_ask"] <= 0.02) or (m["yes_bid"] or 0) >= 0.98 for m in mkts),
            "total_volume": sum(m["volume"] or 0 for m in mkts),
            "total_volume_24h": sum(m["volume_24h"] or 0 for m in mkts),
            "markets": sorted(mkts, key=lambda m: -(m["last_price"] or 0)),
        })
    events.sort(key=lambda e: (e["event_date"] or "9999", -e["total_volume"]))
    return events, cached_series, oldest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=7)
    ap.add_argument("--budget", type=float, default=900, help="seconds of API scanning")
    ap.add_argument("--max-age", type=float, default=60, help="skip series cached within N minutes")
    ap.add_argument("--only", default="", help="comma-separated series tickers to (re)fetch")
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--today", action="store_true",
                    help="fast path: only mention events whose ticker date is today or up to 2 days behind")
    a = ap.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    deadline = time.time() + a.budget

    sfile = os.path.join(DATA, "series.json")
    # --today must not walk the catalog. Reuse the cached series list; one search call finds today's events.
    if (a.build_only or a.today) and os.path.exists(sfile):
        series = json.load(open(sfile))
    else:
        series = get("/series", {"category": "Mentions", "include_volume": "true"}).get("series", [])
        save_json(sfile, series)
    meta = {s["ticker"]: s for s in series}
    print(f"{len(series)} Mentions series", file=sys.stderr)

    if a.today:
        a.days = 0  # ticker date today, or up to 2 days behind; never tomorrow
    if not a.build_only and a.today:
        today = now_et().date()
        lo, hi = today - timedelta(days=2), today
        found = {}
        for e in open_mention_events(deadline):
            ed = event_date(e["event_ticker"])
            if ed and lo <= ed <= hi:
                found[e["event_ticker"]] = e
        # Search shows one event per series. Pull sibling events in the same window.
        for series in sorted({e["series_ticker"] for e in found.values()}):
            try:
                evs = get("/events", {"series_ticker": series, "status": "open", "limit": 200}, deadline).get("events", [])
            except Exception as ex:
                print(f"  WARN events {series}: {ex}", file=sys.stderr)
                continue
            for ev in evs:
                et = ev.get("event_ticker")
                ed = event_date(et or "")
                if et and ed and lo <= ed <= hi and et not in found:
                    found[et] = {"event_ticker": et, "series_ticker": series,
                                 "title": ev.get("title"), "sub_title": ev.get("sub_title") or ""}
        print(f"today window {lo}..{hi}: {len(found)} events", file=sys.stderr)
        by_series = {}
        for e in found.values():
            by_series.setdefault(e["series_ticker"], []).append(e["event_ticker"])
        for series, tickers in by_series.items():
            mk = []
            for et in tickers:
                try:
                    got = scan_event(et, deadline)
                except Exception as ex:
                    print(f"  WARN {et}: {ex}", file=sys.stderr)
                    continue
                print(f"  {et}: {len(got)} open markets", file=sys.stderr, flush=True)
                mk.extend(got)
            if mk:
                save_json(cache_path(series), {"series_ticker": series, "fetched_at_et": now_et().isoformat(timespec="seconds"), "markets": mk})
        tfile = os.path.join(DATA, "event_titles.json")
        titles = json.load(open(tfile)) if os.path.exists(tfile) else {}
        for e in found.values():
            if e.get("title"):
                titles[e["event_ticker"]] = {"title": e.get("title"), "sub_title": e.get("sub_title") or ""}
        save_json(tfile, titles)
    elif not a.build_only:
        if a.only:
            order = [t.strip() for t in a.only.split(",") if t.strip()]
        else:
            pr = {t: i for i, t in enumerate(PRIORITY)}
            order = [s["ticker"] for s in sorted(series, key=lambda s: (
                pr.get(s["ticker"], 999), "" if False else "~", ))]
            # priority list, then most recently updated, then by lifetime volume
            # then series touched after the 2026-09-23 bulk metadata update (likely new events), then by volume
            order = [t for t in PRIORITY if t in meta] + [s["ticker"] for s in sorted(
                (s for s in series if s["ticker"] not in pr),
                key=lambda s: ((s.get("last_updated_ts") or "") > "2026-09-23T17", fnum(s.get("volume_fp")) or 0), reverse=True)]
        done = skipped = 0
        for t in order:
            c = load_cache(t)
            if c and not a.only:
                age = (now_et() - datetime.fromisoformat(c["fetched_at_et"])).total_seconds() / 60
                if age < a.max_age:
                    skipped += 1
                    continue
            try:
                mk = scan_series(t, deadline)
            except TimeoutError:
                print("  time budget used; rerun to continue scanning", file=sys.stderr)
                break
            except Exception as ex:
                print(f"  WARN {t}: {ex}", file=sys.stderr)
                continue
            save_json(cache_path(t), {"series_ticker": t, "fetched_at_et": now_et().isoformat(timespec="seconds"), "markets": mk})
            done += 1
            if mk:
                print(f"  {t}: {len(mk)} open markets", file=sys.stderr, flush=True)
            if done % 10 == 0:
                print(f"  ...{done} series fetched this run ({skipped} fresh in cache)", file=sys.stderr, flush=True)

    # event titles (cached; one call per new in-window event)
    tfile = os.path.join(DATA, "event_titles.json")
    titles = json.load(open(tfile)) if os.path.exists(tfile) else {}
    events, cached_series, oldest = build(meta, a.days, titles)
    if not a.build_only:
        for e in events:
            if e["event_ticker"] in titles:
                continue
            try:
                ev = get(f"/events/{e['event_ticker']}", deadline=time.time() + 120).get("event", {})
                titles[e["event_ticker"]] = {"title": ev.get("title"), "sub_title": ev.get("sub_title")}
            except Exception as ex:
                print(f"  WARN title {e['event_ticker']}: {ex}", file=sys.stderr)
        save_json(tfile, titles)
        events, cached_series, oldest = build(meta, a.days, titles)

    snapshot_series = {e["series_ticker"] for e in events}
    out = {
        "fetched_at_et": now_et().isoformat(timespec="seconds"),
        "oldest_price_et": oldest,
        "source": BASE,
        "horizon_days": a.days,
        # series_in_snapshot is the count to show. series_catalog_count is only the
        # length of the series list this run used, which can be partial. Do not print
        # those two numbers as a scanned/total fraction.
        "series_in_snapshot": len(snapshot_series),
        "series_catalog_count": len(series),
        "series_cache_files": len(cached_series),
        "event_count": len(events),
        "market_count": sum(len(e["markets"]) for e in events),
        "events": events,
    }
    save_json(os.path.join(DATA, "markets.json"), out)
    print(f"wrote data/markets.json: {out['event_count']} events, {out['market_count']} markets "
          f"({out['series_in_snapshot']} series in snapshot, {out['series_cache_files']} cache files, "
          f"series list {out['series_catalog_count']})", file=sys.stderr)


if __name__ == "__main__":
    main()
