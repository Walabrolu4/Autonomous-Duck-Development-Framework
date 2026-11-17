"""Optional browser test using Python Playwright and Chromium.
Requires external Playwright/Chromium to be installed *outside* the game;
not part of the no-dependencies gameplay package.

Run from this folder: python tests/browser_smoke.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
page_url = (root / "index.html").as_uri()
errors = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1080, "height": 900})
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(page_url)
    assert page.title() == "Duck Dodge — ADDF Light Games Pilot"
    assert page.locator("#status").inner_text() == "Ready"
    assert page.locator("#start").inner_text() == "Start game"
    page.locator("#start").click()
    assert page.locator("#status").inner_text() == "Playing"
    start_x = page.evaluate("window.DuckDodge.snapshot().player.x")
    page.keyboard.down("ArrowRight")
    page.wait_for_timeout(250)
    page.keyboard.up("ArrowRight")
    after_x = page.evaluate("window.DuckDodge.snapshot().player.x")
    assert after_x > start_x + 10, (start_x, after_x)
    page.locator("#pause").click()
    assert page.locator("#status").inner_text() == "Paused"
    paused_seconds = page.evaluate("window.DuckDodge.snapshot().seconds")
    page.wait_for_timeout(180)
    assert page.evaluate("window.DuckDodge.snapshot().seconds") == paused_seconds
    page.locator("#pause").click()
    assert page.locator("#status").inner_text() == "Playing"
    page.locator("#start").click()
    assert page.locator("#status").inner_text() == "Playing"
    assert page.evaluate("window.DuckDodge.snapshot().seconds") < 0.20
    assert not errors, errors
    page.screenshot(path=str(root / "tests" / "browser-smoke.png"), full_page=True)
    print("PASS: browser load, start, keyboard, pause/resume, restart, JS errors = 0")
    browser.close()
