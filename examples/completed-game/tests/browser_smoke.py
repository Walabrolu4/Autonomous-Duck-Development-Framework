"""Optional browser smoke for the real index.html/style.css/game.js.
Requires Python Playwright and Chromium *outside* the zero-dependency game.

Some sandboxed Chrome instances forbid navigation to file:// or localhost.
This harness injects the EXACT committed HTML, CSS and JS into an isolated
about:blank browser page. It tests behavior, but not direct local-file launch.

Run: python tests/browser_smoke.py
"""
from pathlib import Path
from shutil import which
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
errors = []
with sync_playwright() as p:
    local_chromium = which("chromium") or which("chromium-browser")
    browser = (
        p.chromium.launch(headless=True, executable_path=local_chromium)
        if local_chromium else p.chromium.launch(headless=True)
    )
    page = browser.new_page(viewport={"width": 1080, "height": 900})
    page.on("pageerror", lambda error: errors.append(str(error)))

    html = (root / "index.html").read_text(encoding="utf-8")
    html = html.replace('<link rel="stylesheet" href="style.css">', "")
    html = html.replace('<script src="game.js"></script>', "")
    page.set_content(html)
    page.add_style_tag(content=(root / "style.css").read_text(encoding="utf-8"))
    page.add_script_tag(content=(root / "game.js").read_text(encoding="utf-8"))

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
    print("PASS: isolated browser page loaded actual source; start, keys, pause/resume, restart, no JS errors")
    browser.close()
