#!/usr/bin/env python3
"""Render a 1200x675 'Mention Board top 5' card from data/coins.js for an X post.
Usage: python3 scripts/top5_card.py [out.png]   (default /workspace/mm-top5.png)
Needs headless Chrome (google-chrome or chromium). Does not post anything."""
import json, os, sys, html, shutil, subprocess, tempfile
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "/workspace/mm-top5.png")
raw = open(os.path.join(HERE, "data", "coins.js")).read().strip()
D = json.loads(raw[len("window.MM_COINS="):-1])
coins = sorted([c for ch in D["chains"] for c in ch["coins"]], key=lambda c: -c["score"])[:5]
e = html.escape
def usd(v):
    if v is None: return "—"
    return f"${v/1e6:.2f}M" if v >= 1e6 else f"${v/1e3:.0f}K"
rows = "".join(f'''<div class="r"><span class="n">{i+1}</span><span class="s">${e(c["symbol"])}</span><span class="ch">{e(c["chain"].replace(" Chain",""))}</span>
<span class="sc">{c["score"]}</span><span class="v">{usd(c["vol24"])}</span><span class="p {'up' if (c['chg24'] or 0)>=0 else 'dn'}{' long' if abs(c['chg24'] or 0)>=10000 else ''}">{(c['chg24'] or 0):+.0f}%</span>
<span class="m">{(c.get("mx") or {}).get("m24","—")}</span></div>''' for i, c in enumerate(coins))
font = "file://" + os.path.join(HERE, "assets", "fonts", "cinzel-decorative-900.woff2")
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:C;src:url({font})}}
html,body{{margin:0;width:1200px;height:675px;overflow:hidden}}
body{{font-family:Inter,"Noto Sans",system-ui,sans-serif;color:#e6ecff;background:radial-gradient(700px 450px at 0 0,rgba(168,85,247,.45),transparent 60%),radial-gradient(700px 450px at 100% 100%,rgba(34,228,255,.32),transparent 60%),#05060f;padding:44px 64px;box-sizing:border-box}}
.top{{display:flex;justify-content:space-between;align-items:baseline}}
h1{{font-family:C;font-size:54px;margin:0;background:linear-gradient(90deg,#22e4ff,#a855f7);-webkit-background-clip:text;color:transparent}}
.d{{font-size:22px;color:#9fb0e8}} h2{{font-size:30px;margin:6px 0 18px;font-weight:800}}
.h,.r{{display:grid;grid-template-columns:50px 240px 160px 110px 170px 170px 1fr;align-items:center}}
.h{{font-size:16px;letter-spacing:.1em;color:#8fa0d8;text-transform:uppercase;padding:0 18px 6px}}
.r{{font-size:30px;font-weight:600;background:rgba(255,255,255,.05);border:1px solid rgba(140,160,255,.2);border-radius:16px;padding:12px 18px;margin-bottom:10px}}
.n{{color:#8fa0d8}} .s{{color:#22e4ff}} .ch{{font-size:20px;color:#b9c6ff}}
.sc{{background:linear-gradient(135deg,rgba(34,228,255,.25),rgba(168,85,247,.35));border-radius:10px;text-align:center;width:70px}}
.p{{white-space:nowrap;padding-right:12px}} .p.long{{font-size:24px}} .up{{color:#3dffb0}} .dn{{color:#ff5c8a}} .m{{color:#c4a5ff}}
.f{{position:absolute;bottom:26px;left:64px;right:64px;display:flex;justify-content:space-between;font-size:17px;color:#8fa0d8}}
</style></head><body><div class="top"><h1>$ Mention Money</h1><span class="d">{e(D["date"])}</span></div>
<h2>The Mention Board · Top 5 by Mention Money Score</h2>
<div class="h"><span>#</span><span>Coin</span><span>Chain</span><span>Score</span><span>24h vol</span><span>24h</span><span>X posts 24h</span></div>{rows}
<div class="f"><span>mentionmoney.com</span><span>Not financial advice. High risk. DYOR.</span></div></body></html>'''
tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False); tmp.write(page); tmp.close()
chrome = next((shutil.which(b) for b in ("google-chrome", "chromium", "chromium-browser") if shutil.which(b)), None)
if not chrome: sys.exit("headless Chrome not found")
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", f"--screenshot={out}",
                "--window-size=1200,675", "--force-device-scale-factor=1", "--virtual-time-budget=3000", "file://" + tmp.name],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
os.unlink(tmp.name); print(out)
