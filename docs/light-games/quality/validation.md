# Automated Contract Validation

Stage 6 introduced a **read-only Python validator** for the six core project-brain files and, when active, the three sprint files. It is intended to catch obvious missing, inconsistent or overbroad records—not to certify a safe agent or authenticated consent.

## When to use

Run after installing the starter kit, changing core project records, resuming a sprint with uncertain state, before implementation, or in CI for framework templates.

## Run from the framework clone

For a blank distributed kit:

```bash
python3 scripts/validate_light.py starter-kit/minimal --mode template --sprint-template starter-kit/sprint-template
```

For your separate game repository:

```bash
python3 /path/to/ADDF/scripts/validate_light.py /path/to/my-game
```

Machine-readable output: add `--format json`. To make warnings exit nonzero in automation: add `--strict`.

No pip packages are required; Python 3.10+ and the local files suffice. The validator does not read arbitrary game source, run game tests, install dependencies or access secrets intentionally.

## What errors look like

The validator reports rule IDs:
- `L-F001`: missing required file;
- `L-F002`: missing/duplicate required heading/key;
- `L-F003`: invalid project/sprint ID;
- `L-F004`: invalid enum or state;
- `L-F005`: duplicate decision/backlog/criteria IDs;
- `L-F006`: broken relative Markdown links;
- `L-F007`: unsafe/broad authorized operation;
- `L-F008`: acceptance-criterion coverage missing;
- `L-F009`: active Gate I/revision mismatch;
- `L-F010`: incomplete recorded human gate;
- `L-F011`: cross-file consistency issue.

Warnings `L-H001` and `L-H002` explicitly say that alleged human consent and historic authorized scope cannot be independently authenticated from text.

## Interpret results honestly

**PASS** means the checked file structure and recorded state are internally consistent. It is **not** proof the current user approved, a game works, or all optional integrations are safe.

**WARN** means structure passed but an important limit remains; use judgment and real evidence before coding.

**FAIL** means the project record needs correction. Do not “fix” a failed Gate I by inventing approval text.

## CI and regression tests

The Light-only `.github/workflows/validate-light-games.yml` checks the starter templates, Stage 6 Python tests and Stage 5 Node tests. It runs on the `ADDF_light_games` branch, not original ADDF `main`. It does **not** deploy GitHub Pages or publish games.

Stage 7 adds **documentation/manual drift checks** separately; they do not expand the game project's write authority.

## Example failure

If `STATE.md` says `implementing` but `PLAN.md` still shows `gate_i_status: pending`, the validator fails. The agent should inspect real approval evidence and return to a safe state, **not** mark the plan authorized to make the test pass.

## Common failures

**Validator as security tool:** Assume Python checks prove consent or absence of secrets. They don't.

**Optional docs made mandatory:** Reject a novice project for not having release architecture files. Only the minimal contracts are required.

**Self-repair of human records:** A model fills in fabricated responses to silence warnings. Keep the warning and ask the person.

## Related

[Stage 6 validator guide](../../../scripts/README.md) · [Approval gates](../sprints/approvals.md) · [Security](security.md)
