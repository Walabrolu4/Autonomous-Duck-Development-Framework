# ADDF Light Games — Stage 5 Test Matrix

**Date:** 2026-11-17  
**Purpose:** Separate **executed evidence**, **deterministic model tests**, **documentary simulations**, and **unverified integration/manual work**. This is pilot-specific, not the Stage 6 general validator.

| Test ID | Question | Test artifact | Outcome | Evidence / limitation |
| --- | --- | --- | --- | --- |
| `T-01` | Does the browser game simulation advance, move, spawn, detect collisions, pause and reset? | [game.test.cjs](completed-game/tests/game.test.cjs) | **PASS** | `10/10` Node tests executed |
| `T-02` | Does the source run in Chromium and respond to controls without page exceptions? | [browser_smoke.py](completed-game/tests/browser_smoke.py) | **PASS** | Isolated browser injection of exact HTML/CSS/JS, not file navigation |
| `T-03` | Is implementation blocked by missing Gate D/I, stale revision, extra file, dependency or command? | [policy-scenarios.test.cjs](tests/policy-scenarios.test.cjs) | **PASS — synthetic model** | `18/18` reference-predicate tests; **not wired to a real LLM** |
| `T-04` | Can a no-idea user get small choices and one question? | [From Zero](from-zero/README.md) | **TABLETOP only** | Scripted fictional dialogue; needs a live human/agent trial |
| `T-05` | Can a one-sentence duck game become one bounded sprint with separated D/I/A? | [From Zero](from-zero/README.md) | **TABLETOP only** | Illustrative plan, not real project Gate I |
| `T-06` | Can existing game files be safely inventoried without overwriting AGENTS? | [Fixture](existing-project/fixture/) and [Audit](existing-project/READ_ONLY_AUDIT.md) | **DOCUMENTED read-only audit** | No migration or live agent run; fixture has an intentional `AGENTS.md` collision |
| `T-07` | Does a different agent resume from real `STATE.md` and approval evidence? | [RESUME prompt](../prompts/RESUME.md), policy tests | **PARTIAL** | Synthetic resumed-state predicates pass; cross-agent runtime not tested |
| `T-08` | Do Claude Code and Codex discover and obey their local skills? | [Integration docs](../integrations/LIGHT_GAMES.md) | **NOT RUN** | Requires supported user/local installations and opt-in configuration |
| `T-09` | Can optional OpenClaw coordinate with safe delegation? | [Coordinator playbook](../integrations/openclaw/COORDINATOR_PLAYBOOK.md) | **NOT RUN** | No workspace, remote host, messaging channel or unattended job configured |
| `T-10` | Does actual human playtest support Gate A and feedback? | [Duck Dodge playtest guide](completed-game/README.md) | **PENDING HUMAN** | Automated pass isn't acceptance |
| `T-11` | Does the game's index.html launch directly from downloaded files? | [index.html](completed-game/index.html) | **PENDING HUMAN** | Sandbox Chrome blocked file:// navigation; actual source did run when injected |
| `T-12` | Was original ADDF `main` preserved and Stage 4 left intact? | GitHub branch comparison | **PASS** | Stage 5 changes isolated to `examples/`; `main` SHA verified unchanged |

## Synthetic Gate I/A test coverage

The test file uses a small, deterministic [policy model](tests/policy-model.cjs) to check rules:
- missing D or I evidence blocks code;
- agent can't impersonate human;
- changed plan revision/paths/commands/dependency/risk breaks permission;
- unapproved external effects block action;
- a valid plan permits only its exact operations;
- build success without human Gate A never closes the sprint;
- rejected or incomplete review never closes;
- resumption with changed worktree/missing approval fails closed.

**The `SYNTHETIC_FIXTURE_ONLY` string is test data, not actual human permission.** These checks establish model predicates behave as expected, **not** that a provider LLM will obey every prompt. The full runtime and host-specific tests require further trials.

## Commands and replicability

```bash
# From the repository root
node --test examples/completed-game/tests/game.test.cjs
node --test examples/tests/policy-scenarios.test.cjs

# Optional, requires Python Playwright + Chromium installed
python examples/completed-game/tests/browser_smoke.py
```

The game itself needs no package manager. `browser_smoke.py` is a test helper only; do not install Playwright solely to play the game.

## Stage 5 exit boundary

The repository **pilot artifacts are implemented and structurally checked**, but user playtesting and live provider tests remain transparently unverified. The human may accept Stage 5 as a **pilot artifact milestone with documented open validations**, request a revision, or ask to conduct the remaining live trials before advancing.

Do not declare Stage 6 implemented based on this pilot-only test suite. See [STAGE_05_REVIEW.md](STAGE_05_REVIEW.md).
