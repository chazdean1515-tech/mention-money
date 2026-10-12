#!/usr/bin/env python3
"""Build data/coins.js: hot meme coins on Solana, Base, BNB Chain and Robinhood Chain.

Free, no-key sources (read-only):
  - GeckoTerminal  /networks/{net}/trending_pools?duration=24h  (ranking, volume, price change, liquidity)
  - DexScreener    /token-boosts/top/v1 and /token-boosts/latest/v1 (paid "boost" flag; promotion, not demand)
X mentions: optional. Read from data/mentions.json ({"SYMBOL": count_24h, ...}) written by a separate
step (e.g. the agent's X post-count tool, or X API recent counts if X_BEARER_TOKEN is set).
Usage: python3 build_coins.py [--per-chain 10]
"""
import json, os, sys, time, urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, "data")
ET = ZoneInfo("America/New_York")
CHAINS = [("solana", "Solana", "solana"), ("base", "Base", "base"), ("bsc", "BNB Chain", "bsc"), ("robinhood", "Robinhood Chain", "robinhood")]
# Not meme coins: majors, stables, wrapped assets, DEX/infra tokens.
SKIP = {"SOL","WSOL","ETH","WETH","CBETH","BNB","WBNB","USDC","USDT","USD1","DAI","FDUSD","USDE","BTC","WBTC","CBBTC","BTCB",
        "AERO","CAKE","JUP","RAY","ORCA","JITOSOL","MSOL","LINK","UNI","VIRTUAL","ZORA","EURC","PYUSD","XAUT","W","ZRO","ICP","XDP","PENGU","TRUMP","HYPE","WLD"}
import re
MIN_LIQ = 50_000  # USD in top pool; thinner pools are too easy to fake
NONMEME = re.compile(r"tokeni[sz]ed|xstock|wrapped|bridged|stock|etf|treasury|usd", re.I)
STOCK = re.compile(r"^[A-Z]{2,5}[cB]$")  # e.g. NVDAc, SKHYB tokenized equities
def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "mentionmoney/0.1 (read-only)"})
            with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)
        except Exception as e:
            if i == 3: print("fail", url, e, file=sys.stderr); return None
            time.sleep(3 * (i + 1))
def f(x):
    try: return float(x)
    except (TypeError, ValueError): return None
def main():
    global OLD
    from datetime import timedelta
    OLD = (datetime.now(ET) - timedelta(days=365)).strftime("%Y-%m-%d")
    per = int(sys.argv[sys.argv.index("--per-chain") + 1]) if "--per-chain" in sys.argv else 10
    boosted = set()
    for u in ("https://api.dexscreener.com/token-boosts/top/v1", "https://api.dexscreener.com/token-boosts/latest/v1"):
        for b in get(u) or []: boosted.add((b.get("chainId"), (b.get("tokenAddress") or "").lower()))
    mpath = os.path.join(DATA, "mentions.json")
    mentions = json.load(open(mpath)) if os.path.exists(mpath) else {}
    out = {"generated_et": datetime.now(ET).strftime("%Y-%m-%d %H:%M ET"), "generated_ts": int(time.time()), "chains": [], "mentions_source": mentions.get("_source") if mentions else None}
    for net, name, ds in CHAINS:
        seen, rows = set(), []
        for page in (1, 2):
            d = get(f"https://api.geckoterminal.com/api/v2/networks/{net}/trending_pools?duration=24h&page={page}&include=base_token")
            time.sleep(2.5)  # GeckoTerminal free tier ~30 calls/min
            if not d: continue
            toks = {t["id"]: t["attributes"] for t in d.get("included", [])}
            for p in d.get("data", []):
                a = p["attributes"]; tid = p["relationships"]["base_token"]["data"]["id"]; t = toks.get(tid, {})
                sym = (t.get("symbol") or a["name"].split(" / ")[0]).strip(); addr = t.get("address") or tid.split("_", 1)[1]
                fdv = f(a.get("fdv_usd")); created = (a.get("pool_created_at") or "")[:10]
                # meme heuristic: not a known major, FDV under $500M, pool younger than ~1 year
                if sym.upper() in SKIP or addr.lower() in seen or (fdv or 0) > 5e8 or (created and created < OLD): continue
                liq = f(a.get("reserve_in_usd"))
                if (liq or 0) < MIN_LIQ: continue
                if NONMEME.search(t.get("name") or "") or STOCK.match(sym): continue
                seen.add(addr.lower())
                rows.append({"symbol": sym, "name": t.get("name") or sym, "address": addr, "chain": name,
                    "price_usd": f(a.get("base_token_price_usd")), "vol24": f((a.get("volume_usd") or {}).get("h24")),
                    "chg24": f((a.get("price_change_percentage") or {}).get("h24")), "liq": f(a.get("reserve_in_usd")),
                    "fdv": f(a.get("fdv_usd")), "created": (a.get("pool_created_at") or "")[:10],
                    "is_new": bool(a.get("pool_created_at")) and (datetime.now(timezone.utc) - datetime.fromisoformat(a["pool_created_at"].replace("Z","+00:00"))).total_seconds() < 86400,
                    "boosted": (ds, addr.lower()) in boosted, "mentions": mentions.get(sym.upper()),
                    "url": f"https://dexscreener.com/{ds}/{a.get('address')}"})
        rows.sort(key=lambda r: r["vol24"] or 0, reverse=True)
        out["chains"].append({"id": net, "name": name, "coins": rows[:per]})
        print(name, len(rows))
    js = "window.MM_COINS=" + json.dumps(out, separators=(",", ":")) + ";\n"
    open(os.path.join(DATA, "coins.js"), "w").write(js)
if __name__ == "__main__": main()
