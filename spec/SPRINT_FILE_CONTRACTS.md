# ADDF Light — Sprint File Contracts

**Status:** Stage 2 approved specification · implementation deferred to Stage 3  
**Authority:** [Approval Policy](APPROVAL_POLICY.md), [Workflow States](WORKFLOW_STATES.md)  
**Relates to:** [Project File Contracts](PROJECT_FILE_CONTRACTS.md) · [Validation and Migration](VALIDATION_AND_MIGRATION.md)

## 1. Why three files instead of eight?

Original ADDF uses separate requirements, blueprint, acceptance, dry-run, implementation log, human review, and retrospective documents. Light preserves their **distinct responsibilities and permission boundaries** while consolidating them into:

| File | Question it answers | Human gate |
| --- | --- | --- |
| `SPRINT.md` | What are we learning/building, why, and how will we know it works? | **D** — consequential design |
| `PLAN.md` | What exactly will the agent change/run, and did the human authorize it? | **I** — precise implementation |
| `REVIEW.md` | What was actually tested, what did the user observe, and was it accepted? | **A** — human acceptance |

The consolidation reduces file navigation, **not** evidence quality. Each document has required independent sections; the agent must not say approval was obtained merely because a heading exists.

The triplet is created at `planning/sprints/sprint-NNN/` only after the next milestone has been identified. No placeholder packs for future sprints.

## 2. Shared metadata and conventions

Every sprint file contains a `## Sprint metadata` section with exact keys:

```md
## Sprint metadata
- sprint_id: sprint-001
- sprint_kind: playable-slice | research-spike | maintenance
- project_id: my-game
- file_revision: r1
- status: draft | in_review | approved | active | closed
```

These file-level `status` labels are **not** the project `sprint_status` state machine. The latter lives in `STATE.md` and has values defined in [Workflow States](WORKFLOW_STATES.md). `file_revision` must increment when its controlled content changes, but incrementing alone does not mean a human approved it.

- `sprint_id` matches the containing directory.
- `sprint_kind` stays consistent across all three docs unless the user approves a re-scoping.
- `project_id` matches `GAME.md` and `STATE.md`.
- Do not derive an approval from `status: approved` without a recorded human gate.
- Dates, durations, commits, devices and test results are recorded only when actually known.
- Generated templates can show `unknown` and `pending` values, but **cannot claim an action happened**.

## 3. `SPRINT.md` — Research + Design + Acceptance Specification

### Required headings in order

1. `# Sprint NNN — [outcome title]`
2. `## Sprint metadata`
3. `## Why this sprint`
4. `## Player-facing outcome`
5. `## Scope`
6. `## Research and evidence`
7. `## Design alternatives and learning checkpoint`
8. `## Selected design and decisions`
9. `## Acceptance criteria`
10. `## Constraints, risks and assumptions`
11. `## Design approval — Gate D`

### Required content

**Why:** link to a backlog item (e.g., `B-001`) or explain why a research spike is required.

**Player-facing outcome:** one testable sentence describing the user/player action and observable consequence. If `sprint_kind: research-spike`, explicitly state that no playable feature is promised and define the tangible research proof.

**Scope:** two explicit subsections `### In scope` and `### Out of scope`. A bounded feature is not a promise to implement every adjacent feature.

**Research and evidence:** focused findings, URL or file or actual command/measurement evidence, source date if known, evidence grade (`verified`, `inferred`, `proposed`, `unknown`), and remaining questions. Research may be short; do not pad with invented sources.

**Design alternatives:** at least two meaningful options for T1/T2 decisions when such alternatives exist, their tradeoffs, recommendation, and the user's actual answer or `pending`. Include one learning question or playtest prediction that helps the user understand this particular choice. For T0-only work, state `No material design fork`.

**Selected design:** cross-reference each relevant `D-###` decision entry. A proposal is not a final design.

**Acceptance criteria:** stable IDs `AC-01`, `AC-02`, ... each with:
- `Given / When / Then` or an equally observable description;
- method: `automated`, `manual-playtest`, or `manual-inspection`;
- environment/input or device constraints;
- pass/fail threshold, when measurable;
- what evidence will be recorded;
- whether the criterion is release-blocking.

Use clear measurable checks without inventing exact performance requirements the user has not chosen. Example:

```md
### AC-01 — Player movement
- method: manual-playtest
- setup: Browser preview on keyboard-capable desktop
- action: Hold arrow keys in each direction
- pass_condition: Avatar responds in all four directions and remains inside the arena
- evidence: Human verdict in REVIEW.md
- release_blocking: yes
```

**Constraints:** documented technical limits, excluded behaviors, dependencies, risks and reversible assumptions.

**Gate D record** (inside `## Design approval — Gate D`):
```md
- gate_d_status: pending | approved | rejected | not_required
- decision_references: D-001, D-002 | none
- human_response: pending | [actual user wording/reference]
- recorded_from: [source context reference, or pending]
- approved_sprint_revision: rN | none
- conditions: none | [explicit user conditions]
```

If no T1/T2 choice exists, `not_required` must be justified. Gate D does not grant Gate I.

### Authorized revisions

After Gate D, changing selected behavior, scope, risk or acceptance criteria invalidates the affected design approval and any later Gate I. Non-semantic formatting edits need not create a new gate; the agent must be transparent about anything that could change what was approved.

## 4. `PLAN.md` — Dry Run + Implementation Authorization

### Required headings in order

1. `# Sprint NNN — Implementation Plan`
2. `## Sprint metadata`
3. `## Inputs and assumptions`
4. `## Exact file operations`
5. `## Commands and external side effects`
6. `## Dependencies and assets`
7. `## Implementation sequence`
8. `## Verification plan`
9. `## Risks, rollback and stop conditions`
10. `## Open ambiguities`
11. `## Implementation approval — Gate I`
12. `## Execution record`

### Gate I preconditions

`SPRINT.md` must exist, its acceptance checks must be defined, and material design choices must be resolved/approved or specifically acknowledged as experiments. `PLAN.md` starts as a **dry run only**. No source changes may occur before explicit authorization.

### Exact file operations

Each operation must list:
- operation: `create | modify | move | delete`;
- path (exact path; narrow glob only if bounded and explained);
- rationale, linked `AC-##` or sprint requirement;
- permitted behavior/change;
- whether the operation can overwrite human work;
- rollback or recovery location.

Example:

```md
| Operation | Path | Purpose | Scope constraint |
| --- | --- | --- | --- |
| create | game/src/player.ts | Keyboard movement | No inventory, networking, or persistence |
| modify | game/package.json | Add specified build script | No new dependencies outside the list below |
| create | game/tests/player.test.ts | Verify arena bounds | Uses existing test runner |
```

A path never implicitly authorizes all children of an unrelated directory. “All files as needed” is invalid authorization.

### Commands and external side effects

Commands are enumerated with what they do: install, compile, test, export, publish, network fetch, file deletion, data write. Include working directory, expected inputs and outputs, and the requirement to stop on a materially different environment.

If no commands are needed, record `none`. If command behavior cannot be determined, mark an open ambiguity and do **not** run it.

### Dependencies and assets

List names, versions or resolution policy, source/provenance, license risks and expected download/storage/network effects. If none, state `none`.

### Sequence and verification

Break the approved work into a small, reviewable sequence: implement smallest unit, run deterministic build/tests, collect evidence, record changed paths, deliver a playable or inspectable output. A test cannot be declared passing before it is run.

### Risks/rollback

Include known risks, non-goals, what would trigger a stop, how to revert the scoped edits without deleting unrelated changes, and special-approval items (deployment, expenses, secrets, external communication).

### Gate I record

```md
- plan_revision: r1
- linked_sprint_revision: r1
- gate_i_status: pending | authorized | rejected | withdrawn | stale
- authorized_operations: [reference to exact operations above] | none
- authorized_commands: [reference to exact commands above] | none
- dependency_approvals: [list or none]
- separate_special_approvals: [list or none]
- human_response: pending | [actual user wording/reference]
- recorded_from: [actual evidence reference or pending]
- conditions: none | [explicit limits]
```

**Authorization validity:** valid only for the reviewed revision, the exact operations and commands, current risk envelope, and any specific conditions. See [Approval Policy](APPROVAL_POLICY.md). `STATE.md` may say `authorized: yes` only when this record is valid.

**Revision changes:** if a plan is updated to `r2` with materially different authorized scope, retain historical `r1` authorization in `### Prior authorization records` or in a clearly linked appendix. Set the current Gate I `stale` or `pending` until the human authorizes `r2`. Do not erase the evidence of old permission.

### Execution record

After Gate I, authorized Develop writes append:
- what actually changed (with diff/commit reference when available);
- commands actually run, result, and exact exit state;
- deviations and whether they required re-approval;
- remaining issues and evidence locations.

The existence of an execution record does not imply a passing test or accepted sprint.

## 5. `REVIEW.md` — Verification + Human Playtest + Acceptance

### Required headings in order

1. `# Sprint NNN — Review and Acceptance`
2. `## Sprint metadata`
3. `## Build and test evidence`
4. `## Acceptance criteria results`
5. `## Playtest instructions`
6. `## Human observations`
7. `## Refinement rounds`
8. `## Known limitations and deferred work`
9. `## Human acceptance — Gate A`
10. `## Sprint retrospective and handoff`

### Evidence requirements

For each `AC-##` in `SPRINT.md`, `REVIEW.md` must have a matching result:
- `result: pass | fail | partial | not_tested`;
- `method: automated | manual-playtest | manual-inspection`;
- `performed_by: agent | human | CI | unknown`;
- `environment: [observed environment or unknown]`;
- `evidence: [actual command output, screenshot path, URL, human notes, or not_recorded]`;
- `notes: [actual observation]`.

**The agent cannot write `performed_by: human` without receiving an actual user observation.** A screenshot and console logs are supplemental evidence; they do not establish gameplay feel or fun.

If the build is not playable, report the blockage and stop. Do not create a fictitious preview URL or claim that the user has tested it.

### Playtest checklist

Write concrete instructions a person can execute with the available environment:
- how to run or open the build and which command was verified;
- exactly what controls/actions to try;
- expected outcomes aligned to `AC-##`;
- suggested questions about feel/readability/accessibility;
- how to reproduce and record defects;
- how to provide a verdict.

Do not demand lengthy survey responses when a few observations suffice.

### Refinement rounds

For each `round-N`:
- trigger and human observation (or verified test failure);
- diagnosis marked `verified` or `hypothesis`;
- revised implementation plan reference (or explanation that unchanged Gate I covers the fix);
- changes and retest evidence;
- whether a new acceptance round was requested.

**Preserve history.** New refinements do not erase previous failed tests, user rejections or earlier verdicts.

### Gate A record

```md
- review_round: round-1
- gate_a_status: pending | accepted | accepted_with_conditions | needs_refinement | rejected | paused
- human_response: pending | [actual user wording/reference]
- recorded_from: [actual evidence reference or pending]
- conditions: none | [specific conditions]
- outstanding_release_blockers: none | [AC IDs / issue references]
- next_action: [clear and assigned]
```

Only a clear human verdict can populate the outcome. An agent may **transcribe** it from an actual interaction and preserve the source, but cannot self-sign. `accepted_with_conditions` must retain a list of conditions; any unresolved release-blocking condition prevents release or unconditional closure.

For `sprint_status: accepted`, require `gate_a_status: accepted` or explicitly human-approved `accepted_with_conditions` with **no** unresolved blocking conditions. Otherwise remain in a non-terminal state consistent with [Workflow States](WORKFLOW_STATES.md).

### Retrospective and handoff

Briefly capture:
- what changed from original intent and why;
- what evidence supports the claim that the sprint is done (or not);
- the learning outcome observed or `not_observed`;
- unresolved risks/decisions transferred to backlog;
- the single next proposed step.

The retrospective is not a substitute for Gate A.

## 6. Miniature cross-file example

**User:** “Make a browser dodge game where the character moves instantly and avoids one hazard.”

`SPRINT.md`:
- `sprint_id: sprint-001`, `sprint_kind: playable-slice`.
- `AC-01`: player moves in four directions and remains within arena.
- `AC-02`: approaching one repeating hazard is visible and collision is observable.
- `D-001`: user chooses immediate directional movement over acceleration after seeing tradeoffs.
- Gate D explicitly approved for `r1`.

`PLAN.md`:
- `r1` lists exactly: source file(s), package modification, test file, allowed build/test commands and approved package(s).
- Gate I **pending** initially. No coding.
- User explicitly authorizes `r1`. Gate I becomes `authorized`.
- Agent modifies only listed files, records actual commands/evidence.

`REVIEW.md`:
- Agent records passing/failing automated checks, but manual-playtest items remain `not_tested`.
- User runs the game and says the hazard is not readable.
- `round-1` records the observation, result `needs_refinement`, and a proposed correction.
- If correction needs a new asset outside `PLAN.md`, Gate I becomes stale and a new plan revision is required.
- User retests `round-2`; only then can a human-approved Gate A make `sprint-001` accepted.

## 7. What about bugs, spikes and maintenance?

**Minor bug within existing sprint:** preserve original acceptance criteria; record refinement round; use valid Gate I only within exactly approved paths/commands/risk.

**New feature disguised as bug:** add to backlog or revise sprint design; do not expand scope silently.

**Research spike:** acceptance criteria describe evidence quality, reproducibility or an implementation feasibility demonstration rather than “fun.” Read-only **pre-sprint discovery** needs no Gate I. A formal research-spike sprint still creates a bounded, potentially zero-code `PLAN.md` and receives Gate I for that exact plan before entering the implementation/execution status; authorization does **not** grant code changes when the plan specifies none. The human later reviews whether the evidence answers the question at Gate A. This retains the existing Stage 1 state machine without inventing an implementation permission.

**Maintenance sprint:** describe the observable result (e.g., build reproducibility or fixed crash), not a nonexistent player mechanic. Same authorization for file changes and same human acceptance principle.

## 8. Invariants and invalid states

| Invariant | Why it matters |
| --- | --- |
| Each sprint has exactly one `SPRINT.md`, `PLAN.md`, `REVIEW.md` once active | Clear navigation and handoff |
| `SPRINT.md` defines AC IDs before edits | Tests cannot be chosen to justify already-written code |
| Gate D reference links to actual human choice or valid nonrequired rationale | No invented project intent |
| Gate I records specific plan revision, paths, commands and actual consent | No blanket code permission |
| `PLAN.md` execution record states **actual** commands, not imagined verification | Reliability |
| `REVIEW.md` has one result per AC, with honest untested states | Traceability |
| Human Gate A is required for accepted sprint | No AI self-approval |
| `STATE.md` mirrors real gates and results | Resumption is safe |
| Revisions preserve history and invalidate stale approvals | No retroactive consent |
| All three docs agree on `sprint_id`, `project_id`, `sprint_kind` | No context confusion |

## 9. Stage 2 manual verification

- [ ] Each former ADDF sprint artifact has a home in one of three Light files.
- [ ] Scope, commands, dependency additions and side effects are visible **before** Gate I.
- [ ] Revision labels cannot retroactively expand authorization.
- [ ] Agent evidence and human playtesting are clearly distinguished.
- [ ] Rejected or repeated rounds preserve their history.
- [ ] The first-sprint example cannot “one-shot” code before human authorization.
- [ ] Research-only spikes and maintenance tasks are handled honestly.

**Status:** Specification for Stage 3 starter templates; not yet a template or executable validator.
