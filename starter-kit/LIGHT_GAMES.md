# ADDF Light Games — Starter Kit

**Status:** Stage 3 candidate; review required before Stage 4  
**Canonical branch:** `ADDF_light_games`

This document points to the **Light Games** kit. The inherited `starter-kit/README.md`, `starter-kit/blank/` and `starter-kit/example-filled/` still belong to the **original full ADDF** and are intentionally left unchanged until a later migration decision.

## Distribution files

| Path | Install into your game project? | Purpose |
| --- | --- | --- |
| `minimal/AGENTS.md` | Yes, to `AGENTS.md` | Agent rules and approval boundaries |
| `minimal/SECURITY.md` | Yes, to `SECURITY.md` | Context restrictions and risky side effects |
| `minimal/GAME.md` | Yes, to `GAME.md` | Player experience and scope |
| `minimal/STATE.md` | Yes, to `STATE.md` | Actual stage/status and next action |
| `minimal/DECISIONS.md` | Yes, to `DECISIONS.md` | Human choices and reversals |
| `minimal/planning/BACKLOG.md` | Yes, preserving directory | Future playable slices |
| `sprint-template/SPRINT.md` | **Only after milestone selected** | Research/design/acceptance criteria |
| `sprint-template/PLAN.md` | **Only after milestone selected** | Exact dry run and Gate I |
| `sprint-template/REVIEW.md` | **Only after milestone selected** | Evidence, playtesting, Gate A |

**Installation boundary:** Copy from `minimal/` into a **new project folder**, not the ADDF framework repo. Avoid copying this index file into a game project; it documents the distribution.

## Zero-idea and existing-project support

The initial `GAME.md` is intentionally undecided. It uses `project_origin: no-idea` as the **blank-project default only**; an agent changes that field to `idea` when the user brings an idea, or to `existing-project` only after an adoption audit. The rest of the unknowns remain unknown until confirmed.

Initial `STATE.md` is `research` / `discovering`, with `active_sprint: none`, no approved implementation and no test evidence. **A user does not have to complete a nine-file questionnaire to start.**

For an existing repository, use [EXISTING_PROJECTS.md](EXISTING_PROJECTS.md) instead of blindly copying the six files; conflicting names must be inventoried, compared and explicitly resolved before any write.

## First-session order

1. Confirm that the assistant or coding agent can read the intended project folder.
2. Load `SECURITY.md` first; avoid sensitive files and irrelevant directories.
3. Load `AGENTS.md`, `STATE.md`, and `GAME.md`.
4. Start with a short idea, or ask for two or three possible concepts.
5. Keep the discussion focused on one *small, observable game outcome*.
6. Let the agent draft and maintain the project brain. Human confirms meaningful design choices.
7. After a specific milestone is chosen, create `planning/sprints/sprint-NNN/` from `sprint-template/`, preserving all required headings and defaulting gates to pending.
8. Review and approve the sprint's design and **separately** approve the exact implementation plan. The agent cannot skip the dry run.
9. Test the resulting build personally; record a human verdict and any needed refinement.

For an explanation with the actual starter prompt, read [../QUICK_START.md](../QUICK_START.md).

## What counts as a first-sprint success?

Imagine the player can move in four directions to avoid one obstacle. That first slice is successful only if:
- The human has selected that objective and its acceptance conditions.
- The plan lists the exact changed paths, commands, dependencies and side effects before work starts.
- Any code was written within authorized scope.
- The agent recorded **actual** build/test results and any known failures.
- The human tried the playable result, recorded observations, and explicitly accepted or rejected it.
- Another session can recover the approved next action by reading the files.

**No game code or playable demo is included in Stage 3.** Actual examples and end-to-end agent trials belong to Stage 5.

## Directory ownership and source of truth

- `minimal/` contains the canonical **blank project** templates.
- `sprint-template/` contains the canonical **uninstantiated** sprint triplet.
- Later Stage 5 examples will contain **filled** projects. They must derive from and conform to these contracts, not become a second independently edited template set.
- `spec/PROJECT_FILE_CONTRACTS.md` and `spec/SPRINT_FILE_CONTRACTS.md` specify required headings, keys and approved values.
- Stage 6 will add executable validation. This stage uses explicit schema checks and manual review; it does **not** claim a production validator is installed.
- Provider adapters and the comprehensive prompt catalog come in Stage 4.

## Optional advanced files

Extra documents such as architecture maps, asset provenance, cross-sprint risks, release checklists and engine-specific commands are **optional**. Create them when complexity genuinely requires them, not as blank onboarding chores. The original ADDF remains the path for formal multi-team and high-risk engineering governance.

## Review

See [STAGE_03_REVIEW.md](STAGE_03_REVIEW.md) and [../spec/REPOSITORY_ARCHITECTURE.md](../spec/REPOSITORY_ARCHITECTURE.md). Do not declare this kit approved until the user manually verifies the files and semantics.
