#!/usr/bin/env python3
"""Turn raw X results into data/mentions.json for build_coins.py. Never invents numbers.

Input: data/x_queries.json (written by `build_coins.py --stage candidates`), one query per coin
(contract address, plus the cashtag when the ticker is specific enough).

Raw results per coin, either:
  A) --manifest FILE : JSON {coin_key: {"counts": path, "search": path}} pointing at saved results of
     the agent's X tools (x.get_posts_counts_recent granularity=hour start_time=<24h ago>, and
     x.search_posts_all max_results=100 expansions=author_id user.fields=public_metrics,created_at,username
     post.fields=created_at,author_id start_time=<24h ago>). This is how the 5 AM agent routine runs it.
  B) --api : calls the official X API v2 itself with $X_BEARER_TOKEN (/2/tweets/counts/recent and
     /2/tweets/search/recent). Needs a paid X API plan (Basic or higher) for counts.
Output per coin: hourly counts (24 full hours, oldest first), m24, weighted unique accounts (sample-based
estimate), top mentioners and first caller (only when the sample covers every post in the window).
"""
import json, os, re, sys, time, math, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); DATA = os.path.join(HERE, "data")
NOW = datetime.now(timezone.utc)

def parse(path):
    t = open(path).read(); m = re.search(r"\{.*\}", t, re.S)
    return json.loads(m.group(0)) if m else None
def weight(fol): return 0.5 if fol < 1000 else (1.0 if fol < 50000 else 2.0)
def botlike(u):
    pm = u.get("public_metrics") or {}; fol = pm.get("followers_count", 0); fing = pm.get("following_count", 0)
    try: age = (NOW - datetime.fromisoformat(u["created_at"].replace("Z", "+00:00"))).days
    except Exception: age = 9999
    return age < 30 or (fol < 10 and fing > 500) or (pm.get("tweet_count", 0) > 200000)

def summarize(counts, search):
    out = {}
    if counts and counts.get("data"):
        b = [x["tweet_count"] for x in counts["data"]]
        full = b[:-1] if len(b) > 24 else b  # last bucket is a partial hour
        out["hourly"] = full[-24:]; out["m24"] = sum(full[-24:]); out["partial_hour"] = b[-1] if len(b) > 24 else None
    if search is not None:
        posts = search.get("data") or []; users = {u["id"]: u for u in (search.get("includes") or {}).get("users", [])}
        seen, w, skipped = set(), 0.0, 0
        for p in posts:
            a = p.get("author_id"); u = users.get(a)
            if not u or a in seen: continue
            seen.add(a)
            if botlike(u): skipped += 1; continue
            w += weight((u.get("public_metrics") or {}).get("followers_count", 0))
        n = len(posts); total = out.get("m24") or n
        if n == 0 and total > 0:
            out["sample_note"] = "search sample returned no posts although counts did"; return out
        scale = (total / n) if n and total > n else 1.0
        out.update({"sample_posts": n, "sample_unique": len(seen), "sample_skipped_botlike": skipped,
                    "weighted_accounts_sample": round(w, 2), "weighted_accounts": round(w * scale, 2), "scaled": scale > 1})
        good = [users[a] for a in seen if a in users and not botlike(users[a])]
        good.sort(key=lambda u: -(u.get("public_metrics") or {}).get("followers_count", 0))
        out["top_mentioners"] = [{"u": u.get("username"), "f": (u.get("public_metrics") or {}).get("followers_count", 0)} for u in good[:3]]
        complete = n > 0 and n >= (out.get("m24") or 10**9)  # sample holds every post in the window
        if complete:
            first = min(posts, key=lambda p: p.get("created_at", "9"))
            fu = users.get(first.get("author_id"), {})
            out["first_caller"] = {"u": fu.get("username"), "at": first.get("created_at"), "url": first.get("url")}
    if search is None and out.get("m24") == 0:
        out.update({"sample_posts": 0, "weighted_accounts": 0.0, "top_mentioners": []})
    return out

def api_get(path, params):
    tok = os.environ.get("X_BEARER_TOKEN")
    url = "https://api.x.com/2/" + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + tok})
    with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)

def main():
    q = json.load(open(os.path.join(DATA, "x_queries.json"))); res = {}
    if "--manifest" in sys.argv:
        man = json.load(open(sys.argv[sys.argv.index("--manifest") + 1]))
        for qq in q["queries"]:
            m = man.get(qq["key"]); 
            if not m: continue
            c = parse(m["counts"]) if m.get("counts") else None
            s = parse(m["search"]) if m.get("search") else None
            if c is None and s is None: continue
            res[qq["key"]] = {"query": qq["query"], **summarize(c, s)}
        src = "X via agent tools (counts + 25-post sample)"
    elif "--api" in sys.argv:
        if not os.environ.get("X_BEARER_TOKEN"): sys.exit("X_BEARER_TOKEN not set")
        for qq in q["queries"]:
            try:
                c = api_get("tweets/counts/recent", {"query": qq["query"], "granularity": "hour", "start_time": q["start_time"]})
                s = api_get("tweets/search/recent", {"query": qq["query"], "start_time": q["start_time"], "max_results": 100,
                    "expansions": "author_id", "user.fields": "public_metrics,created_at,username", "tweet.fields": "created_at,author_id"})
                res[qq["key"]] = {"query": qq["query"], **summarize(c, s)}
            except Exception as e: print("x api fail", qq["symbol"], e, file=sys.stderr)
            time.sleep(1.1)
        src = "X API v2"
    else: sys.exit(__doc__)
    json.dump({"ts": int(time.time()), "window_start": q["start_time"], "source": src,
               "note": "Counts are posts matching the contract address or cashtag. Cashtags can collide across coins with the same ticker.",
               "coins": res}, open(os.path.join(DATA, "mentions.json"), "w"), indent=1)
    print("mentions for", len(res), "coins")
if __name__ == "__main__": main()
