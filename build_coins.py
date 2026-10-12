#!/usr/bin/env python3
"""The Mention Board builder -> data/coins.js, data/history/<date>.json, reports/<date>.html.

Stages (the 5 AM routine runs them in order):
  python3 build_coins.py --stage candidates   # GeckoTerminal trending pools -> data/candidates.json + data/x_queries.json
  (collect X data: scripts/ingest_x.py, see README)  -> data/mentions.json
  python3 build_coins.py                      # enrich (sparklines, safety), score, sections, history, reports
Free, keyless sources: GeckoTerminal (pools, OHLCV, token price), DexScreener (boosts), RugCheck (Solana safety),
GoPlus (EVM safety: Base 8453, BNB 56, Robinhood 4663). Mentions are never invented: without data/mentions.json
for a coin, its score is 'volume-only'.
"""
import json, math, os, re, sys, time, glob, html, urllib.request
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, "data")
ET = ZoneInfo("America/New_York"); NOW = datetime.now(timezone.utc)
CHAINS = [  # gecko id, display, short tab, dexscreener id, goplus id, gmgn id, bullx chain id
    ("solana", "Solana", "Solana", "solana", None, "sol", "1399811149"),
    ("base", "Base", "Base", "base", "8453", "base", "8453"),
    ("bsc", "BNB Chain", "BNB", "bsc", "56", "bsc", "56"),
    ("robinhood", "Robinhood Chain", "Robinhood", "robinhood", "4663", None, None)]
SKIP = {"SOL","WSOL","ETH","WETH","CBETH","BNB","WBNB","USDC","USDT","USD1","DAI","FDUSD","USDE","BTC","WBTC","CBBTC","BTCB",
        "AERO","CAKE","JUP","RAY","ORCA","JITOSOL","MSOL","LINK","UNI","VIRTUAL","ZORA","EURC","PYUSD","XAUT","W","ZRO","ICP","XDP",
        "PENGU","TRUMP","HYPE","WLD"}
MIN_LIQ = 50_000; PER_CHAIN = 12
NONMEME = re.compile(r"tokeni[sz]ed|xstock|wrapped|bridged|stock|etf|treasury|usd", re.I)
STOCK = re.compile(r"^[A-Z]{2,5}[cB]$")

def get(url, pause=0.0):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "mentionmoney/0.2 (read-only)"})
            with urllib.request.urlopen(req, timeout=30) as r: out = json.load(r)
            if pause: time.sleep(pause)
            return out
        except Exception as e:
            if i == 3: print("fail", url[:100], e, file=sys.stderr); return None
            time.sleep(4 * (i + 1))
def f(x):
    try: return float(x)
    except (TypeError, ValueError): return None
def jload(p, default=None):
    try: return json.load(open(p))
    except Exception: return default
def jsave(p, obj): os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(obj, open(p, "w"), indent=1)

# ---------- stage 1: candidates
def candidates():
    old = (NOW - timedelta(days=365)).strftime("%Y-%m-%d"); out = []
    for net, name, short, ds, gp, gm, bx in CHAINS:
        seen, rows = set(), []
        for page in (1, 2):
            d = get(f"https://api.geckoterminal.com/api/v2/networks/{net}/trending_pools?duration=24h&page={page}&include=base_token", 2.2)
            if not d: continue
            toks = {t["id"]: t["attributes"] for t in d.get("included", [])}
            for p in d.get("data", []):
                a = p["attributes"]; tid = p["relationships"]["base_token"]["data"]["id"]; t = toks.get(tid, {})
                sym = (t.get("symbol") or a["name"].split(" / ")[0]).strip(); addr = t.get("address") or tid.split("_", 1)[1]
                fdv = f(a.get("fdv_usd")); liq = f(a.get("reserve_in_usd")); created = a.get("pool_created_at") or ""
                if sym.upper() in SKIP or addr.lower() in seen or (fdv or 0) > 5e8 or (created and created[:10] < old): continue
                if (liq or 0) < MIN_LIQ or NONMEME.search(t.get("name") or "") or STOCK.match(sym): continue
                seen.add(addr.lower())
                age_h = (NOW - datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds() / 3600 if created else None
                rows.append({"key": f"{net}:{addr}", "chain_id": net, "chain": name, "symbol": sym, "name": t.get("name") or sym,
                    "address": addr, "pool": a.get("address"), "price_usd": f(a.get("base_token_price_usd")),
                    "vol24": f((a.get("volume_usd") or {}).get("h24")), "chg24": f((a.get("price_change_percentage") or {}).get("h24")),
                    "chg1": f((a.get("price_change_percentage") or {}).get("h1")), "liq": liq, "fdv": fdv,
                    "pool_created": created, "age_h": round(age_h, 1) if age_h is not None else None})
        rows.sort(key=lambda r: r["vol24"] or 0, reverse=True)
        out += rows[:PER_CHAIN]; print(name, len(rows), "->", min(len(rows), PER_CHAIN))
    jsave(os.path.join(DATA, "candidates.json"), {"ts": int(time.time()), "coins": out})
    # X queries: contract address first; add the cashtag only if it is specific enough (>=4 chars, not a common word).
    COMMON = {"FARM","CASH","DOGE","PEPE","MOON","CAT","DOG","SHARE","CAP","ZEST","DEBIT","NUTS","STONK","SEAN","WISP","PONS","EDEL","POD"}
    qs = []
    for c in out:
        q = c["address"]; s = re.sub(r"[^A-Za-z0-9_]", "", c["symbol"])
        if len(s) >= 4 and s.upper() not in COMMON and not s.isdigit(): q = f'{c["address"]} OR ${s}'
        qs.append({"key": c["key"], "query": q, "symbol": c["symbol"]})
    jsave(os.path.join(DATA, "x_queries.json"), {"ts": int(time.time()), "start_time": (NOW - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ"), "queries": qs})

# ---------- enrichment
def sparkline(net, pool):
    d = get(f"https://api.geckoterminal.com/api/v2/networks/{net}/pools/{pool}/ohlcv/hour?aggregate=1&limit=24", 2.2)
    try: return [round(r[4], 12) for r in sorted(d["data"]["attributes"]["ohlcv_list"])]
    except Exception: return []
def safety(c, gp_id):
    s = {"source": None, "flags": [], "chips": []}
    if c["chain_id"] == "solana":
        d = get(f"https://api.rugcheck.xyz/v1/tokens/{c['address']}/report", 1.0)
        if not d: return s
        s["source"] = "RugCheck"; known = set((d.get("knownAccounts") or {}).keys())
        mk = {m.get("liquidityA") for m in d.get("markets") or []} | {m.get("liquidityB") for m in d.get("markets") or []} | {m.get("pubkey") for m in d.get("markets") or []}
        hold = [h for h in d.get("topHolders") or [] if h.get("owner") not in known and h.get("address") not in mk and h.get("owner") not in mk][:10]
        top10 = sum(h.get("pct") or 0 for h in hold); s["top10_pct"] = round(top10, 1)
        lp = max([((m.get("lp") or {}).get("lpLockedPct") or 0) for m in d.get("markets") or []] + [0])
        s["lp_locked_pct"] = round(lp, 1)
        s["mint_renounced"] = d.get("mintAuthority") in (None, ""); s["freeze_renounced"] = d.get("freezeAuthority") in (None, "")
        if not s["mint_renounced"]: s["flags"].append("Mint authority not renounced")
        if not s["freeze_renounced"]: s["flags"].append("Freeze authority not renounced")
        if d.get("rugged"): s["flags"].append("RugCheck marks rugged")
        for r in d.get("risks") or []:
            if r.get("level") == "danger": s["flags"].append(r.get("name"))
    else:
        d = get(f"https://api.gopluslabs.io/api/v1/token_security/{gp_id}?contract_addresses={c['address']}", 1.0)
        r = list(((d or {}).get("result") or {}).values())
        if not r: return s
        r = r[0]; s["source"] = "GoPlus"
        hold = [h for h in r.get("holders") or [] if not int(h.get("is_locked") or 0) and not int(h.get("is_contract") or 0)][:10]
        s["top10_pct"] = round(sum(f(h.get("percent")) or 0 for h in hold) * 100, 1) if r.get("holders") else None
        lps = r.get("lp_holders") or []
        if not lps: s["lp_unknown"] = True
        burned = sum(f(h.get("percent")) or 0 for h in lps if (h.get("address") or "").lower() in ("0x000000000000000000000000000000000000dead", "0x0000000000000000000000000000000000000000"))
        locked = sum(f(h.get("percent")) or 0 for h in lps if int(h.get("is_locked") or 0))
        s["lp_burned_pct"] = round(burned * 100, 1); s["lp_locked_pct"] = round((locked + burned) * 100, 1)
        s["mint_renounced"] = r.get("is_mintable") != "1" or r.get("owner_address") in ("", "0x0000000000000000000000000000000000000000", None)
        if r.get("is_honeypot") == "1" or r.get("cannot_sell_all") == "1": s["flags"].append("Honeypot check failed")
        if r.get("is_mintable") == "1" and not s["mint_renounced"]: s["flags"].append("Mintable, owner not renounced")
        if r.get("hidden_owner") == "1": s["flags"].append("Hidden owner")
        if (f(r.get("sell_tax")) or 0) > 0.1: s["flags"].append("Sell tax over 10%")
    if (s.get("top10_pct") or 0) > 50: s["flags"].append("Top 10 holders own over 50%")
    return s

# ---------- scoring
def z(vals):
    xs = [v for v in vals if v is not None]
    if len(xs) < 2: return [0.0 if v is not None else None for v in vals]
    m = sum(xs) / len(xs); sd = (sum((x - m) ** 2 for x in xs) / len(xs)) ** .5 or 1
    return [None if v is None else (v - m) / sd for v in vals]
def score(coins):
    by = {}
    for c in coins: by.setdefault(c["chain_id"], []).append(c)
    for grp in by.values():
        zV = z([math.log1p(c["vol24"] or 0) for c in grp])
        zM = z([math.log1p(c["mx"]["weighted_accounts"]) if c.get("mx") and c["mx"].get("weighted_accounts") is not None else None for c in grp])
        zA = z([math.log(c["mx"]["accel"]) if c.get("mx") else None for c in grp])
        for c, v, m, a in zip(grp, zV, zM, zA):
            L = min(1.0, (c["liq"] or 0) / 50000)
            terms = [(0.35, v)] + ([(0.40, m)] if m is not None else []) + ([(0.25, a)] if a is not None else [])
            wsum = sum(w for w, _ in terms)  # missing mention terms are dropped and the rest reweighted
            c["raw"] = sum(w * x for w, x in terms) / wsum * L
            c["score_kind"] = "full" if m is not None and a is not None else ("volume-only" if a is None else "no-account-sample")
            c["zV"], c["zM"] = v, (m if m is not None else a)
    raws = sorted(c["raw"] for c in coins)
    for c in coins:
        pct = sum(1 for r in raws if r <= c["raw"]) / len(raws)
        c["score"] = round(100 * pct * (0.5 if c["safety"]["flags"] else 1))
        c["tags"] = []
        if c.get("zM") is not None:
            if c["zM"] > 0.75 and c["zV"] < -0.25: c["tags"].append("Early or shilled")
            if c["zV"] > 0.75 and c["zM"] < -0.25: c["tags"].append("Whale-driven")
        for k in ("raw", "zV", "zM"): c.pop(k, None)

# ---------- receipts / history
def token_price(net, addr):
    d = get(f"https://api.geckoterminal.com/api/v2/networks/{net}/tokens/{addr}", 2.2)
    try: return f(d["data"]["attributes"]["price_usd"])
    except Exception: return None
def receipts(cur, today):
    out, cache = [], {c["key"]: c["price_usd"] for c in cur}
    for p in sorted(glob.glob(os.path.join(DATA, "history", "*.json")), reverse=True)[:14]:
        h = jload(p, {}); day = h.get("date")
        if not day or day == today: continue
        for pick in h.get("picks", []):
            now = cache.get(pick["key"])
            if now is None: now = cache[pick["key"]] = token_price(pick["chain_id"], pick["address"])
            chg = (now / pick["price_usd"] - 1) * 100 if now and pick.get("price_usd") else None
            out.append({**pick, "date": day, "price_now": now, "chg_since": None if chg is None else round(chg, 1)})
    return out

def main():
    if "--stage" in sys.argv and sys.argv[sys.argv.index("--stage") + 1] == "candidates": return candidates()
    cand = jload(os.path.join(DATA, "candidates.json"))
    if not cand or time.time() - cand["ts"] > 3 * 3600: candidates(); cand = jload(os.path.join(DATA, "candidates.json"))
    coins = cand["coins"]; gp = {c[0]: c[4] for c in CHAINS}
    boosted = set()
    for u in ("https://api.dexscreener.com/token-boosts/top/v1", "https://api.dexscreener.com/token-boosts/latest/v1"):
        for b in get(u) or []: boosted.add((b.get("chainId"), (b.get("tokenAddress") or "").lower()))
    ment = jload(os.path.join(DATA, "mentions.json"), {}) or {}
    mfresh = ment.get("ts") and time.time() - ment["ts"] < 6 * 3600
    for c in coins:
        c["boosted"] = (c["chain_id"], c["address"].lower()) in boosted
        c["is_new"] = c["age_h"] is not None and c["age_h"] < 24
        c["spark"] = sparkline(c["chain_id"], c["pool"]); c["safety"] = safety(c, gp[c["chain_id"]])
        m = (ment.get("coins") or {}).get(c["key"]) if mfresh else None
        if m and len(m.get("hourly") or []) >= 2:
            hrs = m["hourly"][-24:]; last = hrs[-1]; avg = sum(hrs) / len(hrs)
            m["accel"] = min(10.0, max(last / max(avg, 1), 0.1)); m["m24"] = sum(hrs)
            c["mx"] = m
        c["url"] = f"https://dexscreener.com/{dict((x[0], x[3]) for x in CHAINS)[c['chain_id']]}/{c['pool']}"
    score(coins)
    today = datetime.now(ET).strftime("%Y-%m-%d")
    # sections (mention-based sections are empty, and say why, when there is no mention data)
    has_m = any(c.get("mx") for c in coins)
    heating = sorted([c for c in coins if c.get("mx")], key=lambda c: c["mx"]["accel"], reverse=True)[:5] if has_m else []
    fresh = [c for c in coins if c["is_new"] and c.get("mx") and c["mx"]["m24"] > 0][:5]
    prev = None
    for p in sorted(glob.glob(os.path.join(DATA, "history", "*.json")), reverse=True):
        h = jload(p, {})
        if h.get("date") != today: prev = h; break
    cooling = []
    if prev and has_m:
        curm = {c["key"]: c["mx"]["m24"] for c in coins if c.get("mx")}
        for l in prev.get("mention_leaders", []):
            nowm = curm.get(l["key"], 0)
            if l["m24"] and nowm < l["m24"] * 0.7: cooling.append({**l, "m24_now": nowm, "drop_pct": round((1 - nowm / l["m24"]) * 100)})
    rec = receipts(coins, today)
    # today's picks for future Receipts: top Score per chain + top 5 overall
    ranked = sorted(coins, key=lambda c: c["score"], reverse=True)
    picks, seenk = [], set()
    for net, *_ in CHAINS:
        for c in ranked:
            if c["chain_id"] == net: picks.append(c); seenk.add(c["key"]); break
    for c in ranked[:5]:
        if c["key"] not in seenk: picks.append(c); seenk.add(c["key"])
    hist = {"date": today, "ts": int(time.time()),
        "picks": [{k: c[k] for k in ("key", "chain_id", "chain", "symbol", "address", "price_usd", "score", "score_kind")} for c in picks],
        "mention_leaders": [{"key": c["key"], "symbol": c["symbol"], "chain": c["chain"], "m24": c["mx"]["m24"]} for c in sorted([c for c in coins if c.get("mx")], key=lambda c: -c["mx"]["m24"])[:10]]}
    jsave(os.path.join(DATA, "history", f"{today}.json"), hist)
    out = {"generated_et": datetime.now(ET).strftime("%Y-%m-%d %H:%M ET"), "generated_ts": int(time.time()), "date": today,
        "mentions_status": "live" if has_m else "missing", "mentions_note": ment.get("note") if mfresh else None,
        "chains": [{"id": x[0], "name": x[1], "short": x[2], "gmgn": x[5], "bullx": x[6], "ds": x[3],
                    "coins": sorted([c for c in coins if c["chain_id"] == x[0]], key=lambda c: -c["score"])} for x in CHAINS],
        "heating": [c["key"] for c in heating], "fresh": [c["key"] for c in fresh], "cooling": cooling,
        "cooling_status": "ok" if prev and has_m else ("no-history" if not prev else "no-mentions"),
        "receipts": rec, "picks_today": hist["picks"],
        "referrals": jload(os.path.join(DATA, "referrals.json"), {}), "featured": jload(os.path.join(DATA, "featured.json"), {"enabled": False}),
        "reports": sorted([os.path.basename(p)[:-5] for p in glob.glob(os.path.join(HERE, "reports", "20*.html"))] + [today], reverse=True)[:60]}
    out["reports"] = sorted(set(out["reports"]), reverse=True)
    open(os.path.join(DATA, "coins.js"), "w").write("window.MM_COINS=" + json.dumps(out, separators=(",", ":")) + ";\n")
    write_report(out, ranked)
    print("coins", len(coins), "mentions", out["mentions_status"], "receipts", len(rec))

def write_report(out, ranked):
    e = html.escape; d = out["date"]
    rows = "".join(f'<tr><td>{i+1}</td><td>${e(c["symbol"])}</td><td>{e(c["chain"])}</td><td>{c["score"]}{" (volume-only)" if c["score_kind"]=="volume-only" else ""}</td><td>${(c["vol24"] or 0):,.0f}</td><td>{(c["chg24"] or 0):+.1f}%</td><td>{"" if not c.get("mx") else c["mx"]["m24"]}</td><td><code>{e(c["address"])}</code></td></tr>' for i, c in enumerate(ranked[:20]))
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mention Report {d}: top meme coins on Solana, Base, BNB Chain and Robinhood Chain · Mention Money</title>
<meta name="description" content="Mention Money daily report for {d}: the 20 highest Mention Money Scores across Solana, Base, BNB Chain and Robinhood Chain. Not financial advice.">
<link rel="canonical" href="https://mentionmoney.com/reports/{d}.html"><meta name="theme-color" content="#05060f">
<meta property="og:type" content="article"><meta property="og:url" content="https://mentionmoney.com/reports/{d}.html"><meta property="og:title" content="Mention Report {d}"><meta property="og:image" content="https://mentionmoney.com/assets/og-coins.jpg">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css?v=25">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="/neo.css?v=3"><link rel="stylesheet" href="/coins.css?v=3"></head><body class="coins">
<header><nav class="topnav" aria-label="Sections"><a href="/">The Mention Board</a><a href="/reports/">Reports</a><a href="/kalshi/">Kalshi Plays</a></nav>
<p class="brand-home"><a class="brand" href="/"><span class="dollar" aria-hidden="true">$</span><span class="brand-t">Mention Money</span></a></p></header>
<main class="doc"><h1>Mention Report: {d}</h1><p>Snapshot taken {e(out["generated_et"])}. X mention data: {"included" if out["mentions_status"]=="live" else "not available, so scores are volume-only"}.</p>
<p class="risk"><b>High risk. Not financial advice.</b> This report shows what was trading, not what to buy.</p>
<div class="tw"><table class="rep"><thead><tr><th>#</th><th>Coin</th><th>Chain</th><th>Score</th><th>24h volume</th><th>24h</th><th>X posts 24h</th><th>Contract</th></tr></thead><tbody>{rows}</tbody></table></div>
<p><a href="/reports/">All reports</a> · <a href="/#receipts">Receipts</a></p></main>
<footer><p>Not financial advice. 18+ only. Some trade links on the board may be referral links; they never affect rankings.</p></footer></body></html>'''
    os.makedirs(os.path.join(HERE, "reports"), exist_ok=True)
    open(os.path.join(HERE, "reports", f"{d}.html"), "w").write(page)
    items = "".join(f'<li><a href="/reports/{r}.html">Mention Report {r}</a></li>' for r in out["reports"])
    idx = page.split("<main")[0].replace(f"Mention Report {d}: top", "Mention Reports: daily top").replace(f"reports/{d}.html", "reports/") + f'<main class="doc"><h1>Mention Reports</h1><p>One page per day with the top 20 Mention Money Scores.</p><ul>{items}</ul></main></body></html>'
    open(os.path.join(HERE, "reports", "index.html"), "w").write(idx)

if __name__ == "__main__": main()
