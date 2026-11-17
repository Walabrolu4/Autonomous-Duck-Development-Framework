# Duck Dodge — Stage 5 Actual Test Results

**Executed:** 2026-11-17  
**Status:** Automated checks passed; human Gate A / final playtest **pending**  
**Branch:** `ADDF_light_games`  
**Environment:** isolated Linux container; Node.js `v22.16.0`; Python Playwright with system Chromium `/usr/bin/chromium`

## Provenance

The exact local copies of the following files were verified with `git hash-object`, and their Git blob SHA-1 values matched GitHub's fetched content hashes:

| GitHub file | Verified blob SHA |
| --- | --- |
| `game.js` | `2b275d50e2f5d19d57bf9f9f62c87362dde2bb6d` |
| `index.html` | `af7baf6a64591b4ae0e8eda5a4e756e1d5d584f1` |
| `style.css` | `b0eac3af560243a635dcb84c9790090cf0ded14c` |
| `tests/game.test.cjs` | `2c3a406412520fa394a87be76445f39e37b3b780` |
| `tests/browser_smoke.py` | `eeaedce325d66f24e801c2db0bbeabea9714239d` |

These hashes establish source equivalence for the executed automated checks; they do **not** prove runtime behavior on other systems or genuine user acceptance.

## 1. Node.js game-logic tests — PASS

**Command (executed from `examples/completed-game/`):**

```bash
node --test tests/game.test.cjs
```

**Observed:** `10 tests, 10 pass, 0 fail`.

Covered:
1. Initial game state is Ready with no hazards.
2. Simulation stays idle until Start.
3. Keyboard movement and bounded arena coordinates.
4. Diagonal movement is speed-normalized.
5. Obstacles appear after the intended interval.
6. Invalid time delta does not corrupt state.
7. Overlapping hazard causes Game over.
8. Non-overlapping hazard causes no collision.
9. Game-over simulation is frozen and fresh state resets.
10. Paused simulation does not advance or spawn.

**Interpretation:** Pure simulation logic passed in Node. This does not replace a browser interaction test or human playtest.

## 2. Chromium browser smoke — PASS (with environment limitation)

**Command (executed):**

```bash
python tests/browser_smoke.py
```

**Observed:** `PASS: isolated browser page loaded actual source; start, keys, pause/resume, restart, no JS errors`.

The browser test loaded the actual committed HTML, CSS and JavaScript into a Chromium page, then checked:
- Ready state and Start game button.
- Start changes status to Playing.
- ArrowRight visibly advances duck position.
- Pause stops survival time.
- Resume restarts gameplay.
- Play again resets survival time.
- No JavaScript page exceptions observed during the smoke test.

**Important limitation:** This container's browser policy blocked direct navigation to `file://` and `http://127.0.0.1` with `ERR_BLOCKED_BY_ADMINISTRATOR`. The smoke script therefore loads the contents of those **same** files into an isolated `about:blank` page using Playwright's `set_content`, `add_style_tag` and `add_script_tag`. It verifies browser behavior but **does not establish that a user's desktop browser can double-click the HTML file successfully**. That is explicitly a manual check.

A screenshot was generated locally during testing; screenshot existence is **not** a human acceptance record and is not published as a website preview.

## 3. Acceptance criterion coverage

| Criterion | Automated result | Still required |
| --- | --- | --- |
| AC-01 Movement and bounds | Pass — unit test and keyboard browser smoke | Human feel and additional controls |
| AC-02 Hazards, hit and game over | Pass — deterministic unit simulation | Actual human survival/collision playthrough |
| AC-03 Start/pause/restart | Pass — Chromium smoke | Human on own browser and optional mobile touch |
| AC-04 Zero-dependency static source | Source verifies no imports/CDNs/API calls | Direct local-file launch/offline user check |
| AC-05 First-time comprehension/readability | **Not tested automatically** | Human reports clarity and player experience |

## 4. Limitations and outstanding work

- **Gate A: pending.** No person has provided a first-hand playtest verdict in this conversation.
- No full Claude Code / Codex / OpenClaw installation was executed against the example.
- No hosted gameplay preview was deployed, and no GitHub Pages settings were changed.
- No reliable cross-browser compatibility matrix or touchscreen-device run was executed.
- No claim is made that a third-party AI agent obeyed Gate D/I/A in a live long-running session.
- No real new-user interview was conducted; the no-idea/one-sentence walkthrough is explicitly fictional.

**Next:** Human downloads/clones the Light branch and opens `examples/completed-game/index.html`, plays and reports what succeeds or fails. See [README](README.md) and [Stage 5 Review](../STAGE_05_REVIEW.md).
