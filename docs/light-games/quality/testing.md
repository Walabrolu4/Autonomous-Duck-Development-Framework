# Testing: Prove Behavior, Not Permission

Technical tests are essential evidence for a game sprint, but they're not proof of player understanding, a valid human approval, or the quality of the entire game.

## When to use

Use while planning acceptance criteria, implementing authorized game behavior, triaging failed builds or preparing a sprint for human acceptance.

## Separate kinds of evidence

| Test type | Examples | What it can establish |
| --- | --- | --- |
| Unit | Collision geometry, inventory rule, movement bounds | Logic behaves as expected for covered inputs |
| Integration | Input event reaches player state; scene loads dependencies | Connected systems interact under tested conditions |
| Browser/engine smoke | Game starts, input works, pause/restart, no runtime errors | Runnable behavior in a known environment |
| Visual inspection | Obstacle visible, HUD text legible | Observed rendering, sometimes environment-specific |
| Human playtest | Control feel, clarity, difficulty and onboarding | A real person's experience, with limitations |
| Framework contract validation | Required Markdown files, approvals and state references | Recorded structural consistency only |

A passing unit test doesn't tell us whether a player recognizes a dangerous object; a screenshot doesn't tell us whether the game responds reliably to controls.

## Write criteria before implementation

`SPRINT.md` should define actual `AC-##` entries with method, setup, action, observable pass condition, evidence location and whether the criterion blocks release. The plan maps technical tests to these criteria and lists **approved commands**.

`REVIEW.md` then records what was actually run. Use `not_tested` for missing evidence, not a guessed `pass`.

## Scope and commands

A coding agent may only run verification commands allowed by the current Gate I. A command that downloads dependencies or changes lockfiles has side effects; it belongs in the exact plan. If the environment lacks the engine or required test runner, report that blocker and ask the user how to proceed.

A CI workflow on the framework branch validates framework material. It does **not** automatically authorize or execute tests in a separate user's private game repo.

## Stage 5 worked pilot

The browser Duck Dodge example includes pure JavaScript game logic tests, a Chromium interaction smoke test and a synthetic approval-policy test model. The executable checks cover movement, hazard collision and certain stop rules.

Those tests do **not** prove the user's individual browser can open the file, that the obstacle is readable or that live Claude/Codex/OpenClaw obey every gate. The example records these gaps rather than marking them green.

## Negative-case tests matter

Test what the framework **rejects**, not just what it accepts: missing `SECURITY.md`, stale plan revision, unbounded file operation, missing human Gate A, missing `AC-##` results and conflicting status.

For game code, test boundary conditions, failure paths, pauses, restarts and invalid input—not only an ideal playthrough.

## Common failures

**Build is green, sprint is done:** Request human Gate A.

**Predicted test result becomes evidence:** Actually execute the test or mark not verified.

**Silent side effect:** A test helper downloads packages without approval. Review commands and dependencies first.

## Related

[Human playtesting](playtesting.md) · [Validator](validation.md) · [Sprint review](../sprints/review.md)
