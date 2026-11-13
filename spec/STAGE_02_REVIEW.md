# Stage 02 — Manual Review and Sign-Off

**Milestone:** Repository information architecture and file contracts  
**Status:** Approved by the user on 2026-11-12; Stage 2 closed  
**Branch:** `ADDF_light_games`  
**Stage scope:** Specifications only — **no starter templates, agent prompts, scripts, logo or website changes**  
**Previous stage:** Stage 01 approved by the user before work began  
**Next stage, only upon separate instruction:** Stage 03 — starter kit and Quick Start

## 1. Files delivered

All files below must exist on the **Light branch**, under `spec/`:

1. [REPOSITORY_ARCHITECTURE.md](REPOSITORY_ARCHITECTURE.md) — separates framework distribution from game project; target tree, staged migration, authority, documentation sources, optional advanced modules.
2. [PROJECT_FILE_CONTRACTS.md](PROJECT_FILE_CONTRACTS.md) — canonical purpose, required headings/keys, ownership and startup rules for the six persistent project files and supporting backlog.
3. [SPRINT_FILE_CONTRACTS.md](SPRINT_FILE_CONTRACTS.md) — comprehensive `SPRINT.md`, `PLAN.md`, `REVIEW.md` schemas; approvals, revisions, test evidence and human playtest.
4. [VALIDATION_AND_MIGRATION.md](VALIDATION_AND_MIGRATION.md) — static and procedural invariants, stage validation, original ADDF mapping, recovery and special cases.
5. **This file:** `STAGE_02_REVIEW.md` — navigation, review cases and acceptance checklist.

The [Stage 01 specification](FRAMEWORK_SPEC.md), [workflow states](WORKFLOW_STATES.md), [approval policy](APPROVAL_POLICY.md), and [decision protocol](DECISION_PROTOCOL.md) remain applicable.

## 2. Key architectural decisions proposed

| Topic | Stage 02 choice | Why |
| --- | --- | --- |
| Framework vs. project | Separate distribution repository and a copied user game project | Prevent user game truth from mixing with framework authoring |
| Mandatory project files | Six persistent files + a three-file active sprint pack | Minimal onboarding but durable status, permission and evidence |
| Empty project | No sprint folder until a milestone is actually selected | Avoid blank-file forest |
| Sprint record | `SPRINT.md`, `PLAN.md`, `REVIEW.md` | Keep what / how / verified outcome distinct |
| Stage/status | User-facing five stages, canonical state enum in `STATE.md` | Readable process, unambiguous resumption |
| Approvals | D in `SPRINT.md` / decisions, I in `PLAN.md`, A in `REVIEW.md` | No one-shotting or agent self-acceptance |
| Revision tracking | `r1`, `r2`, ... and stable IDs | Changing plan cannot silently reuse older approval |
| Wiki and manual | `docs/` canonical source; manual generated, not reauthored | Prevent documentation drift |
| Existing projects | Read-only inventory first; reviewed migration | Prevent overwriting code and documentation |
| GitHub Pages | Original main deployment remains untouched | Keep parent ADDF public site safe |
| Optional complexity | Advanced files only when need is demonstrated | Light experience with thorough documentation |

**Note on research spikes:** A user can research before selecting a sprint with no Gate I. A formally tracked `research-spike` sprint uses its `PLAN.md` and Gate I even for zero-code activities, so the Stage 01 lifecycle remains traceable. Authorization covers **only** the listed research/artifact operations, not arbitrary source code.

## 3. Manual verification sequence

### A. Check branch and paths
- [ ] Visit `ADDF_light_games` (not `main`).
- [ ] Confirm this file and the other four Stage 02 files exist inside `spec/`.
- [ ] Confirm Stage 01 files remain present.
- [ ] Confirm no `starter-kit/minimal/`, new `prompts/START.md`, or new Light logo was created by Stage 02.
- [ ] Confirm original `main` files and deployment were not modified.

### B. Confirm the first-run experience
- [ ] A user with **no game idea** needs to say only a sentence or answer one question to begin.
- [ ] The user does **not** manually fill nine blank files.
- [ ] The six persistent files can contain `unknown` values initially.
- [ ] No sprint triplet exists until a milestone is chosen.
- [ ] The agent can work without OpenClaw/Canva/Notion/cloud hosting.
- [ ] Existing-project onboarding does not overwrite source or existing `AGENTS.md`.

### C. Check approvals and learning
- [ ] Human Gate D chooses meaningful design direction; T0 edits don't trigger constant questions.
- [ ] Gate I exposes exact files, commands, dependencies, scope and special side effects **before** game edits.
- [ ] Gate A requires actual human review; tests and screenshots never auto-accept.
- [ ] Changed plan scope/revision invalidates previous approval.
- [ ] Failed playtesting returns to refinement; repeated rounds preserve history.
- [ ] The sprint specifies a learning objective connected to an actual design tradeoff.
- [ ] Research-only spikes are not falsely described as playable game features.

### D. Check completeness and continuity
- [ ] Nine logical file contracts specify headings/fields and write owners.
- [ ] `STATE.md` statuses match Stage 01 `WORKFLOW_STATES.md`.
- [ ] Decisions, backlog and criteria use stable IDs (`D-###`, `B-###`, `AC-##`).
- [ ] The full-ADDF-to-Light mapping does not discard important responsibilities.
- [ ] Manual/wiki sources won't become two divergent truth sets.
- [ ] Stage 6 validation rules are described honestly as future implementation, not working scripts.

## 4. Six tabletop validation scenarios

These are **review exercises**, not reports of execution. For each, the expected behavior must be apparent from the contracts.

| Scenario | Expected outcome | Governing file |
| --- | --- | --- |
| New user says “I'd like to create a game” | Guided discovery; six-file scaffold can be draft; **no code** | Project contract + Stage 01 decision protocol |
| User selects immediate movement style | A `D-###` record captures actual choice; sprint criteria updated | `GAME.md`, `DECISIONS.md`, `SPRINT.md` |
| Agent proposes 5 changed files; user approves only 3 | Gate I limited to 3; remaining operations excluded/plan revised | `PLAN.md`, approval policy |
| Coding agent discovers it needs a new dependency | Stop; new `PLAN.md` revision; Gate I must be renewed | Sprint contract |
| Tests pass but user cannot play the game | `awaiting_acceptance` (or blocker); **not accepted** | `REVIEW.md`, state machine |
| User rejects the first playtest and later approves a retest | Keep both review rounds; new human Gate A tied to retest | `REVIEW.md`, `STATE.md` |

## 5. Out-of-scope work deliberately not started

- Creating actual project starter files in `starter-kit/minimal/`.
- Copying or replacing the root `AGENTS.md` or any existing full-ADDF project-brain file.
- Writing provider-specific Claude Code/Codex/OpenClaw agent instructions.
- Generating the full Markdown wiki and single-document manual.
- Adding executable validators, package installers or archive generation.
- Producing ADDF Light logo assets or changing the existing design system.
- Switching GitHub Pages, public website, releases, or deploy workflow.
- Updating the original `main` branch.

Any such changes require the appropriate later stage and human check.

## 6. Known implementation decisions deferred to Stage 03

The core document contracts are specified, but Stage 03 should make these concrete without contradicting them:

1. Choose whether starter templates use compact prompts in comments or a separate `START.md` inside the kit (recommended: external quick start, clean project-brain files).
2. Ensure a new user's first copied `STATE.md` is genuinely `discovering`, with no invented approvals.
3. Decide how the starter kit distinguishes **blank** templates from **example-filled** ones without a large folder duplication.
4. Design a safe migration prompt for existing projects with filename conflicts.
5. Prove the template has the **exact** headings/keys defined in these contracts; if a contract is genuinely too cumbersome, return to Stage 02 for revision rather than silently diverging.

## 7. Sign-off and branch scope

**Human approval received (2026-11-12):** The user stated, “Stage 2 looks good but close it off by changing the name of the branch to ADDF_light_games since this one is more for game dev than general dev.” The review checklists above remain available for future audits; they are not synthetic claims that each individual checkbox was performed.

**Disposition:** Stage 2 approved and closed. This branch is the game-development-focused ADDF Light edition. Stage 1 specifications are preserved, with their canonical branch and game-development scope updated accordingly. No Stage 3 deliverables are authorized by this sign-off.

**Branch handling:** A new branch named `ADDF_light_games` was created at the former `feature/addf-light` head to preserve all commits. Because the GitHub connector does not expose branch deletion or rename, the former branch may remain until a repository administrator removes it through GitHub's branch settings. That cleanup is separate from Stage 2 approval.

**Next:** Wait for a new, explicit user instruction before starting Stage 3.
