# Develop Mode Permission Levels

Permission levels apply only to Develop Mode — they control how far the model may reach beyond the approved Sprint Pack scope.

## Table of contents

1. [The permission level scale](#the-permission-level-scale)
2. [How levels are used](#how-levels-are-used)
3. [How to authorize a level](#how-to-authorize-a-level)
4. [Escalation rules](#escalation-rules)

---

## The permission level scale

| Level | Name | Meaning |
|---|---|---|
| 0 | Dry Run Only | Read-only analysis of intended changes. No implementation. |
| 1 | Approved Sprint Scope | Modify only files approved in `blueprint.md` and `dry_run.md`. |
| 2 | Approved Expansion | Add minor helper files surfaced in the dry run and explicitly approved. |
| 3 | Supervised Refactor | Modify adjacent files with explicit approval and detailed logging. |
| 4 | Migration / High-Risk Change | Structural changes, migrations, or architecture-heavy work. Requires a rollback plan. |

**Rule:** Permission level controls Develop Mode freedom.

---

## How levels are used

Every Develop Mode session begins at Level 0 — Dry Run Only. The model reads the Sprint Pack and produces `dry_run.md`. Implementation starts only after the human (or Design Mode review) upgrades the level.

Level 1 covers the vast majority of sprint work: modify only the files listed in `blueprint.md` and `dry_run.md`. When in doubt, use Level 1 and escalate only if the dry run review surfaces a legitimate need for broader scope.

Levels 2–4 require progressively stronger justification:

- Level 2 is appropriate when the dry run identifies a small helper file — a utility, a constant, a test fixture — not in the original blueprint but needed for the implementation to work.
- Level 3 is appropriate for controlled refactoring that touches files adjacent to the sprint scope. Requires detailed logging.
- Level 4 is appropriate for database migrations, schema changes, or architectural restructuring. Requires a pre-written rollback procedure before implementation begins.

---

## How to authorize a level

The human sends the authorization message to the open Develop Mode session after the dry run review passes:

```
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

This exact pattern is the authorization gate. Develop Mode may not proceed without it. See [Sprint Loop — Step 7](sprint-loop.md#step-7--authorize-development) and [Prompt Catalog](prompt-catalog.md) for the full authorization prompt.

---

## Escalation rules

The model cannot self-authorize a higher Permission Level. If implementation reveals a need for a higher level mid-session, the model must stop and report the need. The human then decides whether to authorize the escalation.

Escalation requires explicit human instruction — not an implicit inference by the model that "the work seems to require it."

**Rule:** Develop Mode does not self-authorize.

---

[← Develop Mode](modes/develop-mode.md) · [← Wiki Home](index.md) · ADDF v3.5
