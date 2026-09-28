#!/usr/bin/env python3
"""Capture mobile + desktop screenshots of the locally served app (headless Chromium via Playwright).
Run with the venv that has playwright:  /workspace/.venv-pw/bin/python screenshot.py [url]"""
import sys, os
from playwright.sync_api import sync_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp, mobile in [("mobile", {"width": 390, "height": 844}, True), ("desktop", {"width": 1366, "height": 900}, False)]:
        ctx = b.new_context(viewport=vp, device_scale_factor=2 if mobile else 1, is_mobile=mobile, has_touch=mobile)
        pg = ctx.new_page()
        pg.goto(URL, wait_until="networkidle")
        pg.wait_for_selector("#events article, #events p", timeout=15000)
        pg.screenshot(path=os.path.join(OUT, f"{name}.png"), full_page=False)
        pg.screenshot(path=os.path.join(OUT, f"{name}-full.png"), full_page=True)
        print("saved", name)
        ctx.close()
    b.close()
