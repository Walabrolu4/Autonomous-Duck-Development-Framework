# Stage 05 — Pilot Games and End-to-End Test Review

**Status:** Artifacts implemented and automated pilot checks executed; **awaiting the human's manual review / acceptance**  
**Branch:** `ADDF_light_games`  
**Previous stage:** Stage 4 approved by the human on 2026-11-17 before Stage 5 work  
**Stage boundary:** Only `examples/` files added/modified. Original `main`, prior `spec/`, `prompts/`, `integrations/`, starter kit, website and deployments remain unchanged.

## 1. Stage 5 deliverables

- [Pilot Index](README.md): navigation and honest status classification.
- [No-idea and one-sentence scenarios](from-zero/README.md): explicitly fictional onboarding examples and required stop conditions.
- [Playable Duck Dodge](completed-game/README.md): actual HTML, CSS and JavaScript browser game, pure simulation tests, optional Chromium smoke.
- [Existing-project adoption](existing-project/README.md): synthetic legacy game fixture and read-only audit with an `AGENTS.md` collision.
- [Synthetic Gate D/I/A and resumption tests](tests/policy-scenarios.test.cjs): deterministic reference model, not actual LLM enforcement.
- [Test Matrix](TEST_MATRIX.md): executed versus tabletop versus manual versus provider-runtime checks.
- [Actual Game Test Results](completed-game/TEST_RESULTS.md): environment, commands, observed results, source hashes, limitations.

## 2. Actual automated results — verified in isolated container

| Check | Observed result | Caveat |
| --- | --- | --- |
| Browser game logic, Node `v22.16.0` | **10/10 PASS** | Deterministic simulation, not a human |
| Synthetic approval and resumption predicate tests | **18/18 PASS** | Model fixture, not a real coding agent |
| Chromium / Playwright UI smoke | **PASS** | Loaded actual HTML/CSS/JS by browser injection; sandbox forbade direct file/localhost navigation |
| Game source and test provenance | **MATCH** | Six core files + browser test matched GitHub blob hashes |
| Original ADDF `main` protection | **Unchanged** | Verified via GitHub reference and branch comparison |

These results mean an actual playable artifact and executable pilot tests exist. They do **not** mean an actual human enjoyed, understood, or approved the game, nor that all agent runtime integrations were exercised.

## 3. Repository file verification

- [ ] Open `ADDF_light_games`, then `examples/`.
- [ ] Confirm `from-zero/`, `completed-game/`, `existing-project/`, and `tests/` exist.
- [ ] Confirm `completed-game/` includes `index.html`, `style.css`, `game.js`, `README.md`, `TEST_RESULTS.md`, plus tests.
- [ ] Confirm `existing-project/fixture/` still has its **original** `AGENTS.md`, `README.md`, `paddle.js`.
- [ ] Confirm the fixture audit recommends a **reviewed merge**, not overwriting the existing agent rules.
- [ ] Confirm the `from-zero/` scenario clearly labels imaginary user replies as fictional.
- [ ] Confirm `tests/policy-scenarios.test.cjs` never claims synthetic signatures as actual approvals.
- [ ] Confirm test reports mark provider/runtime and human Gate A checks as **not verified**.
- [ ] Confirm prior Stages 1–4 files and the original `main` are intact.

## 4. Your actual Duck Dodge playtest (required before human acceptance)

From a clone/download of `ADDF_light_games`, open `examples/completed-game/index.html` in a normal desktop browser. Or use a separately provided Stage 5 review-only ZIP containing the same three game files.

### Checklist

- [ ] Game opens locally without needing an account, CDN, package install or server.
- [ ] **Start game** begins gameplay and timer.
- [ ] Arrow keys and **W A S D** move the duck responsively in four directions.
- [ ] Duck stays inside the playfield, including corners.
- [ ] Red hazards enter from the right; touching one shows **GAME OVER**.
- [ ] **Pause** freezes time; **Resume** continues.
- [ ] **Play again** resets survival time and starts another round.
- [ ] Instructions, controls and hazards are readable and understandable.
- [ ] Optional: touch controls work on your target device/narrow browser.

Write one or two observations about movement feel and hazard readability. If any check fails, describe the input and device/browser so it can be reproduced.

**Human Gate A is still pending.** Even if the automated checks passed, only the human can say whether the playable milestone is acceptable.

## 5. Framework workflow verification

- [ ] No-idea route asks a small question, not a long questionnaire.
- [ ] One-sentence route distinguishes observed user intent from assumptions and selects one slice.
- [ ] Significant design choices and exact technical implementation plans are **different approvals**.
- [ ] Extra files, packages, risky commands or different revisions invalidate prior Gate I in the synthetic tests.
- [ ] Browser/Node test success does **not** create a fake Gate A.
- [ ] Legacy project onboarding is read-only and does not overwrite prior instructions.
- [ ] Resumption cannot keep editing with a stale plan or unverified worktree.
- [ ] Live Claude/Codex/OpenClaw runtime tests remain on the follow-up list rather than being marked passed.

## 6. What remains unverified

1. **Your real playtest** of Duck Dodge and the final Stage 5 verdict.
2. Direct opening of `index.html` on your own Mac/Windows browser; the sandboxed Chrome used for automation blocked file and localhost navigation.
3. Live skill invocation and policy compliance on your installed Claude Code, Codex and (optionally) OpenClaw.
4. Full multi-session, multi-agent game implementation and handoff in your own repository and environment.
5. Browser/device compatibility beyond the isolated Chromium injection smoke.
6. General-purpose automated Markdown contract checking (intentionally Stage 6).

You may approve Stage 5 **as an implementation and pilot-artifact milestone** with the provider-runtime checks recorded as open, or request that live validations be performed before approval. Do not claim a fully validated end-to-end human/agent workflow until its actual gates have been exercised.

## 7. Decision requested from the human

Once you verify files and play the game, respond with your *real* observations and one of:

- **Approve Stage 5** as a candidate milestone with the documented pending provider/runtime coverage, and authorize Stage 6;
- **Request Stage 5 changes** with specific game or contract defects;
- **Keep Stage 5 open** pending further live Claude Code/Codex/OpenClaw tests.

**Do not start Stage 6** without a new explicit instruction.
