#!/usr/bin/env python3
"""Screenshots + checks for the Spin the Wheel section. Run: /workspace/.venv-pw/bin/python screenshot_wheel.py [url]"""
import sys, os, re
from playwright.sync_api import sync_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(OUT, exist_ok=True)
rot = lambda pg: pg.evaluate("document.getElementById('wheel-rot').style.transform")
with sync_playwright() as p:
    b = p.chromium.launch()
    # desktop: before spin, then spin (click twice fast: 2nd must be ignored), reveal
    ctx = b.new_context(viewport={"width": 1366, "height": 900}); pg = ctx.new_page()
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
    pg.goto(URL, wait_until="networkidle"); pg.wait_for_selector("#wheel .wheel-svg")
    pg.wait_for_timeout(600)
    pg.evaluate("window.scrollTo(0, document.getElementById('wheel').offsetTop - 110)"); pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(OUT, "wheel-desktop.png"))
    pg.locator("#wheel-btn").click(); pg.wait_for_timeout(150); r1 = rot(pg)
    pg.locator("#wheel-btn").click(force=True); pg.wait_for_timeout(150); r2 = rot(pg)
    pg.wait_for_selector("#wheel-result .wheel-card", timeout=9000); pg.wait_for_timeout(700)
    landed = pg.get_attribute("#wheel-btn", "data-landed")
    label = pg.locator("#wheel-result .potd-label").inner_text()
    pg.set_viewport_size({"width": 1366, "height": 1180})
    pg.evaluate("window.scrollTo(0, document.getElementById('wheel').offsetTop - 110)"); pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(OUT, "wheel-result.png"))
    # keyboard spin again
    pg.locator("#wheel-btn").focus(); pg.keyboard.press("Enter"); pg.wait_for_timeout(200); r3 = rot(pg)
    print("desktop: ignored-during-spin:", r1 == r2, "| landed:", landed, "| card label:", label, "| Enter spins:", r3 != r2,
          "| role:", pg.get_attribute("#wheel-btn", "role"), "| cursor:", pg.evaluate("getComputedStyle(document.getElementById('wheel-btn')).cursor"))
    ctx.close()
    # mobile, reduced motion (short spin)
    ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True, reduced_motion="reduce"); pg = ctx.new_page()
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until="networkidle"); pg.wait_for_selector("#wheel .wheel-svg"); pg.wait_for_timeout(400)
    pg.evaluate("window.scrollTo(0, document.getElementById('wheel').offsetTop - document.querySelector('header').offsetHeight - 12)"); pg.wait_for_timeout(200)
    pg.screenshot(path=os.path.join(OUT, "wheel-mobile.png"))
    pg.locator("#wheel-btn").tap(); pg.wait_for_selector("#wheel-result .wheel-card", timeout=3000)
    pg.locator("#wheel-result .wheel-card").screenshot(path=os.path.join(OUT, "wheel-mobile-result.png"))
    print("mobile reduced-motion: revealed", pg.locator("#wheel-result .potd-label").inner_text(), "| duration", pg.evaluate("document.getElementById('wheel-rot').style.transitionDuration"))
    ctx.close(); b.close()
    print("js errors:", errs)
