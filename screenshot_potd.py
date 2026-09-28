#!/usr/bin/env python3
"""Screenshots of the Play of the Day hero + the Tip the House panel (desktop + mobile), plus a copy-button check.
Run: /workspace/.venv-pw/bin/python screenshot_potd.py [url]"""
import sys, os
from playwright.sync_api import sync_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
ADDR = "APst4X6cmSQ3KAVBt4ZnQpSNcLH4gVJHDutXK8xhaDmR"
os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp, mobile in [("desktop", {"width": 1366, "height": 900}, False), ("mobile", {"width": 390, "height": 844}, True)]:
        ctx = b.new_context(viewport=vp, device_scale_factor=2 if mobile else 1, is_mobile=mobile, has_touch=mobile, reduced_motion="reduce")
        ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=URL.rstrip("/").rsplit("/", 0)[0])
        pg = ctx.new_page()
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(URL, wait_until="networkidle")
        pg.wait_for_selector("#potd .potd-card", timeout=15000)
        pg.screenshot(path=os.path.join(OUT, f"potd-{name}.png"), full_page=False)
        # tip panel
        pg.locator("header [data-tip-open]").click()
        pg.wait_for_selector("#tip[open]")
        shown = pg.locator("#sol-addr").inner_text().strip()
        pg.locator("#tip-copy").click()
        pg.wait_for_function("document.getElementById('tip-status').textContent.length > 0")
        status = pg.locator("#tip-status").inner_text()
        clip = pg.evaluate("navigator.clipboard.readText()")
        suffix = "" if name == "desktop" else "-mobile"
        pg.screenshot(path=os.path.join(OUT, f"potd-donate{suffix}.png"), full_page=False)
        print(name, "| addr ok:", shown == ADDR, "| status:", status, "| clipboard ok:", clip == ADDR, "| js errors:", errs)
        ctx.close()
    b.close()
