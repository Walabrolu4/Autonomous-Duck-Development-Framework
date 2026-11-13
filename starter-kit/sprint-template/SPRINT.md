# Sprint NNN — [outcome title]

> **Distribution template only.** This is not an active sprint and carries **no human design approval**. Copy to `planning/sprints/sprint-001/SPRINT.md` only after selecting the first milestone, change the sprint ID, replace the placeholders, and obtain Gate D if there are consequential choices. For subsequent sprints increment `NNN`.

## Sprint metadata

- sprint_id: sprint-001
- sprint_kind: playable-slice
- project_id: undecided
- file_revision: r1
- status: draft

`sprint_kind` can be `playable-slice`, `research-spike` or `maintenance`. `status` here is the **file** status (`draft`, `in_review`, `approved`, `active`, `closed`), not the project's `sprint_status` in `STATE.md`. Update project ID from `GAME.md`; do not claim the selected sprint is approved just because these fields exist.

## Why this sprint

- Linked backlog item: none selected yet.
- Problem or opportunity: unknown.
- Why now: unknown.
- Player/learning value: unknown.

If this is a research spike, state the precise question and the evidence deliverable; **do not imply a playable result**.

## Player-facing outcome

- One concrete user-visible or playable outcome: unknown.
- Person performing the action: unknown.
- Observable response: unknown.

Draft **one** bounded goal rather than a complete game. A research-spike goal describes a reproducible answer or experiment, not gameplay.

## Scope

### In scope

- Pending user-selected slice.
- Limit to the smallest meaningful implementation and verification.

### Out of scope

- All other features until the human approves them.
- Deployment/public publishing, paid services, extra dependencies and external accounts by default.

Replace these broad defaults with precise boundaries before asking Gate D or preparing Gate I.

## Research and evidence

- Main uncertainty: unknown.
- Current facts: not_verified.
- Evidence links, file observations or command results: none.
- Evidence classification: unknown.
- Tradeoff or experiment needed: unknown.

Separate `verified`, `inferred`, `proposed`, and `unknown`; include actual sources. Do not invent benchmark values, platform compatibility or documentation citations. Keep research relevant to the **current slice**.

## Design alternatives and learning checkpoint

- Consequential decision question: pending.
- Option A: pending.
- Option B: pending.
- Tradeoffs for player feel, complexity, accessibility, performance and reversibility: pending.
- Agent recommendation (not a human decision): pending.
- Human choice: pending.
- Learning focus: pending.
- Optional prediction to test when playing: pending.

If there is genuinely no material T1/T2 design choice, explain `No material design fork` instead of inventing options. “I don't know yet” means research more or propose a reversible prototype, not silently accept the recommendation.

## Selected design and decisions

- Selected behavior/approach: pending.
- Related decision IDs: none.
- Confirmed human constraints: none recorded.
- Deferred/experimental choices: none recorded.

Cross-reference **real** `D-###` entries in `DECISIONS.md`. Do not write “selected” merely because the agent recommended an option.

## Acceptance criteria

No criteria have been agreed yet. Before Gate I, replace this note with one or more uniquely identified **observable** `AC-##` entries, with:
- `method: automated | manual-playtest | manual-inspection`
- `setup:` concrete environment/input (or explicitly unknown pending research)
- `action:` what the tester does
- `pass_condition:` reproducible expected outcome
- `evidence:` what result will be recorded in `REVIEW.md`
- `release_blocking: yes | no`

An example **format only**, not an approved criterion:

```md
### AC-01 — Example player movement
- method: manual-playtest
- setup: A verified keyboard-capable browser preview
- action: Press each movement input
- pass_condition: The avatar moves consistently and stays inside the arena
- evidence: Human observations in REVIEW.md
- release_blocking: yes
```

Do not request implementation authorization while the actual criterion list is empty.

## Constraints, risks and assumptions

- Environment/engine/device constraints: unknown.
- Accessibility/playtest considerations: unknown.
- Major risks and mitigations: unknown.
- Assumptions awaiting verification: none established.
- Out-of-scope and rollback considerations: pending PLAN.md.

## Design approval — Gate D

- gate_d_status: pending
- decision_references: none
- human_response: pending
- recorded_from: pending
- approved_sprint_revision: none
- conditions: none

A valid Gate D requires an **actual** human design response and precise sprint revision. If the sprint needs no significant design decision, `gate_d_status: not_required` must explain why. Gate D does **not** authorize source edits. No approval can be supplied by this template or asserted from a passing test.

**Next:** Once design is chosen, the agent drafts `PLAN.md` as a dry run and requests separate Gate I before code changes.
