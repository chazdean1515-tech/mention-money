#!/usr/bin/env python3
"""Assemble data/analysis.json from per-event analysis modules in this folder (analysis_*.py),
then pick the deterministic "Play of the Day" from data/markets.json + those estimates."""
import glob, importlib.util, json, os, re
from datetime import datetime
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__))
ET = ZoneInfo("America/New_York")
NOW = datetime.now(ET)
MIN_EDGE = 0.05
out = {"updated_at_et": NOW.isoformat(timespec="seconds"),
       "min_edge": MIN_EDGE,
       "fee_model": "Kalshi taker fee ≈ ceil(0.07·C·p·(1−p)) dollars; edge = est − price − 0.07·p·(1−p) per contract",
       "events": {}}
for f in sorted(glob.glob(os.path.join(HERE, "analysis_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    out["events"][mod.EVENT] = mod.DATA

# ---------------- Play of the Day ----------------
# Rules (deterministic given markets.json + analysis modules + build time):
#  eligible  = analyzed word, event not decided, market active, close time and speaking window (event_time_et) still ahead,
#              a real two-sided quote on the side we'd buy (bid > 0, ask < 1, spread <= MAX_SPREAD), market has traded, edge >= MIN_EDGE.
#  tiers     = 1) confidence >= Medium and not flagged fragile, 2) any confidence, not fragile, 3) anything eligible.
#  within the best non-empty tier: take the top edge; any pick within CLOSE_EDGE of it counts as a tie and the one whose
#  event happens soonest wins; then larger edge, then ticker (stable).
MAX_SPREAD, CLOSE_EDGE = 0.10, 0.02
FEE = lambda p: 0.07 * p * (1 - p)

def conf_tier(s):
    s = (s or "").lower().replace("–", "-").replace("—", "-").split(".")[0].strip()
    return {"high": 4, "medium-high": 3.5, "medium": 3, "medium-low": 2, "low-medium": 2, "low": 1}.get(s, 1)

def ts(iso):
    return datetime.fromisoformat(iso) if iso else None

def strip_prices(text):
    """Drop sentences quoting a cent price (they go stale; the card shows the live price)."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    keep = [p for p in parts if not re.search(r"\d\s*¢", p)]
    return " ".join(keep) if keep else text.strip()

def eligible_candidates(mk, events):
    """Every (market, side) that passes the shared filters. Used by the Play of the Day and the wheel."""
    cands = []
    for e in mk.get("events", []):
        ea = events.get(e["event_ticker"])
        if not ea or e.get("decided"):
            continue
        ev_time = ts(ea.get("event_time_et"))
        if ev_time and ev_time <= NOW:  # speaking window already started/over: stale prices, not a live bet
            continue
        fragile_sides = ea.get("fragile_sides", {})
        for m in e["markets"]:
            w = ea.get("words", {}).get(m["ticker"]) or ea.get("words", {}).get(m["word"])
            if not w or w.get("p") is None or m.get("status") != "active":
                continue
            ct = ts(m.get("close_time_et"))
            if ct and ct <= NOW:
                continue
            if not (m.get("volume") or 0) > 0:
                continue
            p = w["p"]
            for side, ask, bid, pe in (("YES", m.get("yes_ask"), m.get("yes_bid"), p),
                                        ("NO", m.get("no_ask"), m.get("no_bid"), 1 - p)):
                if ask is None or bid is None or not (0 < ask < 1) or bid <= 0 or ask - bid > MAX_SPREAD + 1e-9:
                    continue
                edge = pe - ask - FEE(ask)
                if edge < MIN_EDGE:
                    continue
                fragile = w.get("fragile") or fragile_sides.get(side)
                tier_conf = conf_tier(ea.get("confidence"))
                tier = 3 if fragile else (1 if tier_conf >= 3 else 2)
                cands.append(dict(tier=tier, conf=tier_conf, edge=edge, side=side, ask=ask, pe=pe, e=e, ea=ea, m=m, w=w,
                                  fragile=fragile, when=ev_time or ct, key=(m["ticker"], side)))
    return cands

def record(c):
    """Card-ready dict for one candidate (shared by the Play of the Day and the wheel)."""
    e, ea, m, w = c["e"], c["ea"], c["m"], c["w"]
    reason = strip_prices(w.get("reason", ""))
    rationale = (f"{reason} Our {round(w['p']*100)}% YES estimate vs a {round(c['ask']*100)}¢ {c['side']} ask "
                 f"leaves about +{round(c['edge']*100)}¢ per contract after fees.")
    return {
        "event_ticker": e["event_ticker"], "series_ticker": e.get("series_ticker"), "ticker": m["ticker"],
        "event_title": ea.get("title") or e["title"], "speaker": ea.get("speaker"),
        "word": m["word"], "side": c["side"],
        "price": c["ask"], "yes_bid": m.get("yes_bid"), "yes_ask": m.get("yes_ask"),
        "est_yes": w["p"], "est_side": round(c["pe"], 4),
        "edge_raw": round(c["pe"] - c["ask"], 4), "fee": round(FEE(c["ask"]), 4), "edge": round(c["edge"], 4),
        "payout_multiple": round(1 / c["ask"], 2),
        "event_time_et": ea.get("event_time_et"), "close_time_et": m.get("close_time_et"),
        "price_fetched_at_et": m.get("price_fetched_at_et") or e.get("price_fetched_at_et"),
        "confidence": ea.get("confidence"), "fragile": c["fragile"] or None,
        "rationale": rationale, "reason": w.get("reason"),
        "url": f"https://kalshi.com/markets/{e['series_ticker'].lower()}" if e.get("series_ticker") else None,
    }

def previous_potd_ticker():
    """Ticker featured yesterday, so today can pick a different market when one exists."""
    path = os.path.join(HERE, "..", "data", "last_potd.json")
    try:
        prev = json.load(open(path))
    except (OSError, ValueError):
        return None
    prev_day = (prev.get("date") or "")[:10]
    if prev_day and prev_day < NOW.date().isoformat():
        return prev.get("ticker")
    return None

def pick_potd(cands):
    if not cands:
        return None, None
    skip = previous_potd_ticker()
    usable = [c for c in cands if c["m"]["ticker"] != skip] or cands
    best_tier = min(c["tier"] for c in usable)
    pool = [c for c in usable if c["tier"] == best_tier]
    top = max(c["edge"] for c in pool)
    close = [c for c in pool if c["edge"] >= top - CLOSE_EDGE - 1e-9]
    close.sort(key=lambda c: (c["when"], -c["edge"], c["m"]["ticker"], c["side"]))
    c = close[0]
    tier_note = {1: "medium-or-better confidence, not flagged fragile",
                 2: "no medium-confidence pick cleared the bar; best non-fragile pick",
                 3: "only fragile picks cleared the bar"}[best_tier]
    rec = record(c)
    rec["selection"] = {"tier": best_tier, "tier_note": tier_note, "candidates": len(usable),
                        "tied_within_2c": len(close),
                        "skipped_repeat": skip if skip and skip != c["m"]["ticker"] else None,
                        "rule": "max edge after fee; ties within 2¢ go to the soonest event; skip yesterday's ticker when another pick exists"}
    return rec, c

# ---------------- Spin the Wheel ----------------
# Four play types, each maps to one pick from the same eligible pool. Non-fragile picks always rank ahead of fragile ones.
# Each play stores a primary pick plus ranked alternates, so the page can skip a pick whose event has started since the build.
BOMB_MAX_PRICE, RETIRE_MIN_P, CASH_WINDOW_H = 0.30, 0.75, 48
N_ALTS = 3

def ranked(pool, key):
    """Sort non-fragile first, then by `key` (a tuple where smaller is better), then ticker/side so the order is stable."""
    return sorted(pool, key=lambda c: (bool(c["fragile"]),) + key(c) + c["key"])

def wheel(cands, potd_c):
    soon_cut = NOW.timestamp() + CASH_WINDOW_H * 3600
    soon = [c for c in cands if c["when"] and c["when"].timestamp() <= soon_cut]
    if soon:
        cash_pool, cash_rule = soon, f"best edge among picks whose event starts within {CASH_WINDOW_H}h"
    else:
        first = min((c["when"] for c in cands if c["when"]), default=None)
        cash_pool = [c for c in cands if c["when"] == first] or cands
        cash_rule = f"no event within {CASH_WINDOW_H}h, so the best edge on the soonest event"
    long = [c for c in cands if c["ask"] <= BOMB_MAX_PRICE]
    safe = [c for c in cands if c["pe"] >= RETIRE_MIN_P]
    prem = [c for c in cands if c["conf"] >= 3]
    specs = {  # type: (ranked list, rule text)
        "BOMB": (ranked(long, lambda c: (-c["edge"],)), f"biggest edge with price ≤ {round(BOMB_MAX_PRICE*100)}¢") if long
                else (ranked(cands, lambda c: (c["ask"], -c["edge"])), "no pick at ≤ 30¢, so the cheapest eligible pick"),
        "RETIREMENT": (ranked(safe, lambda c: (-c["pe"], -c["edge"])), f"highest win probability for our side (≥ {round(RETIRE_MIN_P*100)}%)") if safe
                else (ranked(cands, lambda c: (-c["pe"], -c["edge"])), "nothing at ≥ 75%, so the highest win probability"),
        "ROLLS-ROYCE": (ranked(prem, lambda c: (-c["edge"],)), "biggest edge among Medium-or-better confidence picks") if prem
                else (ranked(cands, lambda c: (-c["edge"],)), "no Medium-confidence pick, so the biggest edge overall"),
        "CASH": (ranked(cash_pool, lambda c: (-c["edge"],)), cash_rule),
    }
    meta = {"BOMB": ("💣", "Long shot: a cheap side with real edge and a big payout multiple."),
            "RETIREMENT": ("🏖️", "Safest pick: the highest estimated chance of winning, with edge still ≥ 5¢."),
            "ROLLS-ROYCE": ("👑", "Premium pick: the biggest edge with Medium-or-better confidence."),
            "CASH": ("💵", "Quickest money: best edge on an event happening soonest.")}
    potd_key = potd_c["key"] if potd_c else None
    out, taken = [], set()
    # Assign the narrowest categories first so they get their best pick; ROLLS-ROYCE skips the POTD if it can.
    for t in ("ROLLS-ROYCE", "BOMB", "RETIREMENT", "CASH"):
        lst, rule = specs[t]
        block = taken | ({potd_key} if t == "ROLLS-ROYCE" and potd_key else set())
        primary = ([c for c in lst if c["key"] not in block] or [c for c in lst if c["key"] not in taken] or lst)[0]
        alts = [c for c in lst if c is not primary and c["key"] not in taken][:N_ALTS]
        taken.add(primary["key"])
        emoji, blurb = meta[t]
        out.append({"type": t, "emoji": emoji, "blurb": blurb, "rule": rule,
                    "same_as_potd": primary["key"] == potd_key,
                    "picks": [record(primary)] + [record(c) for c in alts]})
    order = ["BOMB", "RETIREMENT", "ROLLS-ROYCE", "CASH"]
    return sorted(out, key=lambda x: order.index(x["type"]))

mk_path = os.path.join(HERE, "..", "data", "markets.json")
try:
    mk = json.load(open(mk_path))
except (OSError, ValueError):
    mk = {}
cands = eligible_candidates(mk, out["events"])
out["play_of_the_day"], potd_c = pick_potd(cands)
out["wheel_plays"] = wheel(cands, potd_c) if cands else []
path = os.path.join(HERE, "..", "data", "analysis.json")
json.dump(out, open(path, "w"), indent=1, ensure_ascii=False)
print("wrote", os.path.normpath(path), "events:", list(out["events"]))
fmt = lambda r: f"{r['word']} {r['side']} @ {round(r['price']*100)}¢, est {r['side']} {r['est_side']:.0%}, edge +{r['edge']*100:.1f}¢, {r['payout_multiple']}x ({r['event_ticker']}{', FRAGILE' if r['fragile'] else ''})"
potd = out["play_of_the_day"]
if potd:
    json.dump({"date": NOW.date().isoformat(), "ticker": potd["ticker"], "word": potd["word"], "side": potd["side"]},
              open(os.path.join(HERE, "..", "data", "last_potd.json"), "w"), indent=1)
print("play of the day:", fmt(potd) + f"; {len(cands)} candidates" if potd else "none")
for w in out["wheel_plays"]:
    print(f"wheel {w['type']:<12}", fmt(w["picks"][0]), "| rule:", w["rule"], "| alts:", ", ".join(f"{a['word']} {a['side']}" for a in w["picks"][1:]))
