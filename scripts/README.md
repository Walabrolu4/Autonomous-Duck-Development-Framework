# ADDF Light Games — Automated Validation

**Stage 6: implemented candidate · human review required**  
**Runtime:** Python 3.10+ standard library only. No pip packages, API keys, game engine, file writes, shell execution by the validator, or network calls required.

This folder contains executable checks for the Markdown project brain and active sprint contracts defined in:

- [Project File Contracts](../spec/PROJECT_FILE_CONTRACTS.md)
- [Sprint File Contracts](../spec/SPRINT_FILE_CONTRACTS.md)
- [Workflow States](../spec/WORKFLOW_STATES.md)
- [Approval Policy](../spec/APPROVAL_POLICY.md)
- [Stage 6 review](STAGE_06_REVIEW.md)

The validator **does not perform or authorize implementation**. It reads only the six known project-brain Markdown paths and, when there is an active sprint, its three known sprint paths. It does not walk arbitrary game code, open secret files, run tests in the user's project, install dependencies, deploy, merge, or change state.

## 1. Validate the distributed blank starter kit

From the **ADDF framework repository root**, on branch `ADDF_light_games`:

```bash
python3 scripts/validate_light.py starter-kit/minimal --mode template --sprint-template starter-kit/sprint-template
```

Expected result for the approved Stage 3 templates:

```text
ADDF Light Games validation: PASS (9 files read)
No recorded-state contract issues found; human consent and gameplay still require real verification.
```

Template mode checks the six blank-project files, three uninstantiated sprint templates, required headings and keys, safe initial state, and pending Gate I/A fields. It **rejects** a blank kit that already has an active sprint, authorization, or pre-created sprint folder.

## 2. Validate an actual game project

Point the validator at **your game's own project root**, which contains `AGENTS.md`, `GAME.md`, `SECURITY.md`, etc. This can be a different repository from the ADDF framework:

```bash
python3 /path/to/ADDF-repo/scripts/validate_light.py /path/to/my-game
```

For a machine-readable report:

```bash
python3 scripts/validate_light.py /path/to/my-game --format json
```

Optional stricter checks for automation:

```bash
python3 scripts/validate_light.py /path/to/my-game --strict
```

**Exit codes:** `0` means PASS (or WARN when not strict); `1` means FAIL, or WARN under `--strict`. Invalid command-line arguments are rejected by Python's argument parser.

Use `--format json` to get `status`, `files_checked`, and an array of findings with `level`, `code`, `file`, `message`.

A blank game with no sprint is valid. Once `STATE.md` names an active `sprint-NNN`, the corresponding `SPRINT.md`, `PLAN.md` and `REVIEW.md` are required.

## 3. What is validated?

| Rule | Enforced behavior |
| --- | --- |
| `L-F001` | Required known files exist and are readable without leaving the project root |
| `L-F002` | Required H1/H2 headings and metadata keys exist in contract order |
| `L-F003` | Game project IDs and sprint IDs use documented patterns |
| `L-F004` | State, stage, metadata, security and gate enum values are valid |
| `L-F005` | Decision/backlog/acceptance IDs are unique within their documents |
| `L-F006` | Relative Markdown links resolve inside the project folder |
| `L-F007` | Authorized plan operations are concrete, not blank/wildcard/traversal paths |
| `L-F008` | Advanced sprints define AC IDs; acceptance-ready review records cover them |
| `L-F009` | Active Gate I and plan revision/sprint reference agree; terminal states revoke active authorization |
| `L-F010` | Gate D/I/A cannot claim approval while their human response/evidence fields remain pending |
| `L-F011` | Project/sprint IDs and sprint kind agree across active documents |
| `L-H001` | WARN: claimed human choices/playtests cannot be independently authenticated from Markdown text |
| `L-H002` | WARN: current plan operations are checked, but a past human-approved plan snapshot cannot be independently authenticated |

**No fabricated `L-F012` success:** Missing *optional* advanced documents do not fail. This intentionally follows the Stage 2 rule that optional modules are never mandatory.

The parser ignores fenced Markdown code blocks, so illustrative `D-001`, `B-001`, `AC-01` records in templates do not count as real decisions or accepted requirements.

## 4. Interpreting PASS, WARN and FAIL

- **PASS:** The current documents satisfy the structural rules checked. It does *not* mean tests ran, the game works, or a human approved anything.
- **WARN:** No structural failure, but a material limit remains. Most importantly, the validator cannot authenticate whether an alleged human response in Markdown actually came from the user or reconstruct the historical scope that was shown to them.
- **FAIL:** Required file, schema, state, cross-reference, plan, or recorded-gate consistency is invalid. Do not proceed with risky source edits based on that state.

**Fail closed:** When a validator reports a missing/stale implementation authorization, the agent must **stop and ask the human**, not auto-generate an “approved” field. Never “fix” a failing test by fabricating human consent.

The validator is a QA helper **outside** the game-project authority structure. It does not add an extra approval level or replace Gate D, Gate I, or Gate A.

## 5. Run automated regression tests

From the framework repository root:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_*.py' -v
```

This checks positive blank and active-sprint cases, deliberately broken files, invalid state enums, stale plans, forged/missing recorded gates, wildcard operations, incomplete reviews, and JSON/strict-mode behavior. Test fixtures containing `SYNTHETIC` are **not** human approvals.

To verify the earlier Stage 5 game/policy examples:

```bash
node --test examples/completed-game/tests/game.test.cjs examples/tests/policy-scenarios.test.cjs
```

Node is optional **for game-project validation**; it is only needed for the Stage 5 JavaScript tests.

## 6. Automated GitHub Actions checks

A separate workflow exists at [`.github/workflows/validate-light-games.yml`](../.github/workflows/validate-light-games.yml).

It runs **only on `ADDF_light_games`** when validation scripts, starter templates, game examples, or the workflow itself change, plus manual `workflow_dispatch`.

The workflow:
1. Checks out the Light branch.
2. Validates the nine blank starter templates.
3. Runs all Stage 6 Python regression tests.
4. Runs the Stage 5 Node game-logic and synthetic approval tests.

**It does not deploy GitHub Pages, publish games, merge to `main`, use credentials, or call the game project's private services.**

Workflow runs can be reviewed at:

https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/actions/workflows/validate-light-games.yml

## 7. Known limits and further work

This script is not a security or runtime attestation mechanism. It cannot independently:
- prove a user really spoke the approval text in a file;
- prove a plan was unchanged since a prior human read it without a signed or versioned approval snapshot;
- compare authorized scope with an actual source-control diff or external deployment history;
- prove that all source files are safe to read or that private tokens are absent;
- playtest difficulty, accessibility, motion, feel or visual clarity;
- guarantee Claude Code, Codex or OpenClaw will follow prompts;
- validate optional advanced modules without their own future schemas.

Stage 5 live provider tests remain pending and are not converted into a false pass by Stage 6.

Stage 7 will document these controls in the wiki/full manual, but must not present this validator as an authentication system.

## 8. Review boundary

The files here and the isolated GitHub Actions workflow constitute **Stage 6 only**. No Stage 7 wiki or full manual has been created. Stop for the human's manual verification; see [Stage 6 review](STAGE_06_REVIEW.md).
