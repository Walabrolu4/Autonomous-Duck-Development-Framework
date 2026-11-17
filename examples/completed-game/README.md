# Duck Dodge — Playable ADDF Light Games Pilot

**Edition:** Stage 5 game-development methodology pilot  
**Technology:** HTML5 canvas, plain JavaScript and CSS. **No dependencies, accounts, CDNs, telemetry or network requests.**  
**Human acceptance:** Pending the user's playtest and Stage 5 review.  
**Framework authorization:** This demonstration was created as part of the user's explicit instruction to implement **Stage 5**. It is **not evidence of a separate game's Gate D or Gate I**.

## Play it locally

From a clone or downloaded ZIP of the `ADDF_light_games` branch:

1. Find `examples/completed-game/index.html`.
2. Open it in a desktop browser (no web server required).
3. Click **Start game**.
4. Move the duck with **arrow keys** or **W A S D**. On touch devices use the directional buttons.
5. Dodge the red rectangles, which travel from right to left. Survival time increases while you're alive; a collision ends the round.
6. Try **Pause**, **Resume**, and **Play again**. Restart must reset the current time to zero.

The interface uses the original ADDF's Yolk/Ink/Paper/Pond palette, without claiming to be the finalized Stage 8 logo.

## Pilot acceptance criteria

| ID | Test | Observable pass condition | Evidence |
| --- | --- | --- | --- |
| **AC-01** | Move duck with keys | Duck moves up/down/left/right and stays inside the 720 × 420 arena | Node unit test + automated browser movement + human feel |
| **AC-02** | Dodge hazardous obstacles | Hazards spawn and move; collision changes status to Game over | Node unit test + human gameplay test |
| **AC-03** | Control loop | Start, pause/resume, and restart work without browser errors; survival resets | Automated browser smoke + human test |
| **AC-04** | Small/safe distribution | Static files run offline with no package installation or API keys | Source inspection + manual offline test |
| **AC-05** | Player comprehension | Controls and hazard readability are clear to first-time player | **Human only — pending** |

Automated tests do not independently prove “fun,” readability or accessibility. The final verdict belongs to the reviewer.

## Run tests

From `examples/completed-game/`:

```bash
node --test tests/game.test.cjs
```

Optional browser smoke test (requires Python Playwright and installed Chromium):

```bash
python tests/browser_smoke.py
```

These commands are **instructions**, not permission for an agent to run them in an unrelated user's repo. Within a real game project, first record approved commands in `PLAN.md`.

The browser smoke script saves `tests/browser-smoke.png` *locally*. The screenshot is evidence only if the test actually runs; no generated screenshot is committed as an approval.

## Code organization

- `index.html` — semantic UI and canvas.
- `style.css` — responsive controls and palette.
- `game.js` — simulation, collision, movement, rendering, keyboard/touch inputs. The pure simulation functions export to Node for testing. Browser exposes a read-only `DuckDodge.snapshot()` for smoke assertions.
- `tests/game.test.cjs` — actual JavaScript logic tests.
- `tests/browser_smoke.py` — actual browser automation when optional runtime exists.
- `TEST_RESULTS.md` — results recorded **only after execution**, with environment and limitations.

## Human playtest script (Gate A still pending)

Try the following and report specific observations:

1. Press all arrow keys and W/A/S/D; do movements feel immediate and predictable?
2. Stay in the top-left / bottom-right corners; can the duck ever leave the canvas?
3. Survive a few obstacles, then intentionally collide; does the game clearly indicate why the round ended?
4. Pause, resume, and restart; does the timer behave as expected?
5. On a narrow window or phone, do the touch controls work and remain legible?
6. Is the hazard sufficiently readable against the green arena?

Verdict options: **accepted**, **accepted with conditions**, **needs refinement**, **rejected**, or **paused**. State your real observations and any blockers; do not claim playtesting occurred until you have actually tried the game.

## Honest constraints

- This is a **minimal first-slice demo**, not a polished production game. No saved high scores or cloud sync.
- The score is elapsed survival time; it resets on Play again. Best is kept in memory for this page session.
- The engine-agnostic prototype uses plain canvas rather than Phaser because offline, zero-install testing is the scope of this pilot. Phaser/Unity/Godot-specific implementations remain future examples.
- Provider-specific end-to-end agent behavior is **not verified** by Node or Chromium tests. Real Claude Code/Codex/OpenClaw tests must be run in their host installations.
- No project-level Gate D/I is claimed; this repo is a **framework example** created during the Stage 5 work you requested.

Return to [Stage 5 index](../README.md) and [review checklist](../STAGE_05_REVIEW.md).
