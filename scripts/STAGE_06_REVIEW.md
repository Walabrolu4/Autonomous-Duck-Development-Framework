# Stage 06 — Automated Validation Review and Human Sign-Off

**Status:** Stage 6 implemented and CI-tested; **human approval pending**  
**Branch:** `ADDF_light_games`  
**Previous stage:** Stage 5 approved after the human's local Duck Dodge playtest on 2026-11-17  
**Next stage:** Stage 7 — wiki and generated combined manual, **only after new human approval**

## 1. Files delivered

| Path | Responsibility |
| --- | --- |
| [`scripts/light_schema.py`](light_schema.py) | Auditable source of required Stage 2 headings, fields, enums, sprint statuses and IDs |
| [`scripts/validate_light.py`](validate_light.py) | Read-only Python validator for minimal game projects and active sprint packs |
| [`scripts/tests/test_validate_light.py`](tests/test_validate_light.py) | Twenty deterministic positive/negative regression tests |
| [`scripts/README.md`](README.md) | Installation, commands, rule IDs, limitations, safety and integration guide |
| [`.github/workflows/validate-light-games.yml`](../.github/workflows/validate-light-games.yml) | Branch-only GitHub Actions validation, with no deployment or write permissions |
| **This document** `scripts/STAGE_06_REVIEW.md` | Manual verification checklist and stage sign-off |

The original ADDF `main`, website deployment workflow, full ADDF starter kit, prior Stage 1–5 specs/prompts/game files are preserved.

## 2. Actual execution evidence

**GitHub Actions run:** https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/actions/runs/44189055924

**Run head:** `2f4abcc8446e06da4448b32de4302ba308e701fa` (later documentation-only changes also trigger the same workflow).  
**Environment:** GitHub-hosted `ubuntu-latest` runner, Python 3.14.4 plus preinstalled Node.js.

| Check | Actual observed result |
| --- | --- |
| Validate Stage 3 minimal + uninstantiated sprint templates | **PASS, 9 files read** |
| Stage 6 Python regression tests | **20 tests passed**, 0 failed |
| Stage 5 Node game and synthetic approval tests | **28 tests passed**, 0 failed |
| Workflow conclusion | **Success** |
| Original `main` commit | Unchanged from `63c7aa795ba61bd33d2333425210f2aa54de24c8` at initial verification |

This is actual GitHub Actions execution, **not a simulated test log**. The Node policy tests remain *synthetic approval models* even when run for real; they are not a live human or LLM safety guarantee.

## 3. Manual verification checklist

### A. GitHub file and branch check

- [ ] Open `ADDF_light_games`, not `main`.
- [ ] Under `scripts/`, confirm `light_schema.py`, `validate_light.py`, `tests/test_validate_light.py`, `README.md` and `STAGE_06_REVIEW.md`.
- [ ] Under `.github/workflows/`, confirm the new `validate-light-games.yml` exists alongside the inherited deployment workflow.
- [ ] Confirm the new validation workflow mentions **only** `ADDF_light_games` and cannot deploy or merge to `main`.
- [ ] Confirm the Stage 3 starter templates and Stage 5 game examples are unchanged.
- [ ] Confirm the original `main` branch is unchanged.

### B. Run the real validator

From the framework repository root, after cloning/downloading the Light branch:

```bash
python3 scripts/validate_light.py starter-kit/minimal --mode template --sprint-template starter-kit/sprint-template
```

Expected: `PASS (9 files read)`. This is independent of whether you have Claude Code, Codex, OpenClaw, Unity, Godot, Phaser or any game engine installed.

For machine-readable output:

```bash
python3 scripts/validate_light.py starter-kit/minimal --mode template --sprint-template starter-kit/sprint-template --format json
```

Run regression tests if desired:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_*.py' -v
node --test examples/completed-game/tests/game.test.cjs examples/tests/policy-scenarios.test.cjs
```

### C. Negative-case safety check

If you want a manual negative test, make a **copy** of `starter-kit/minimal/` into a throwaway folder (not the canonical template), then remove its `SECURITY.md`. Run:

```bash
python3 scripts/validate_light.py /path/to/throwaway-copy
```

Expected: `FAIL` with `L-F001` for missing `SECURITY.md`. Do not edit the canonical starter kit just to test a failure.

The automated regression suite already exercises missing headings, invalid state values, missing sprint packs, stale Gate I revisions, wildcard file scope, missing Gate A, incomplete acceptance coverage and a positive-but-**synthetic** accepted-state fixture.

### D. Semantics and limitation check

- [ ] The validator distinguishes `PASS`, `WARN`, `FAIL`, and outputs meaningful file/rule evidence.
- [ ] A blank project passes without requiring a fictitious sprint.
- [ ] A sprint in an advanced state requires the three sprint files and acceptance criteria.
- [ ] An `implementing` state with no matching Gate I fails.
- [ ] A plan revision mismatch or unsafe/wildcard file operation fails.
- [ ] A missing human Gate A cannot produce an accepted state.
- [ ] **WARN** acknowledges that text attributed to a human is **not authenticated**.
- [ ] The validator never invents approvals, runs game code, reads secrets, installs packages or deploys.
- [ ] Optional advanced project files remain optional, rather than blocking beginners.
- [ ] The original full ADDF and the new Light branch remain separate.

## 4. Known limitations, explicitly still open

The checks establish **file structure and internally consistent recorded status**. They do not prove:
- an alleged human approval or review actually happened;
- that a plan's file list is identical to the historical snapshot shown to the human (without extra versioned/signed evidence);
- that any agent host obeys ADDF Light when using real tools;
- that code diffs, asset licenses, browser gameplay, security practices or deployment permissions are correct;
- that an arbitrary advanced or legacy ADDF project can be safely converted automatically.

**Stage 5 live Claude Code, Codex and optional OpenClaw integration tests remain pending.** Stage 6 does not relabel them “passed.”

The browser Playwright smoke remains a separately optional Stage 5 test; it is not required for the Stage 6 static validation workflow.

## 5. Stop and human approval

Stage 6 code, tests, documentation and a branch-only CI workflow are implemented. **Stage 7 has not begun.**

After reviewing, the user may respond:

> “I manually verified Stage 6 and approve the automated validator and branch-only CI workflow. Proceed to Stage 7: full Markdown wiki and generated manual. Stop again for my review.”

Or request a targeted revision to rules, test cases or CI behavior first.

**Do not begin Stage 7 without explicit authorization.**
