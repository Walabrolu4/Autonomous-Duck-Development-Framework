[Home](../index.md) → [File Reference](index.md) → Sprint Files

# Sprint Files

## The Sprint Folder Sequence

Every sprint gets its own folder at `planning/sprints/sprint_NNN/`. Inside that folder, 9 files document the sprint from planning through retrospective. These files map directly to the 10 steps of the [Sprint Workflow](../sprint-workflow.md): the Architect produces `requirements.md`, `blueprint.md`, and `acceptance.md` in Steps 1–2; the Builder produces `dry_run.md` and `implementation_log.md` in Steps 3 and 6–7; the human produces `blueprint_feedback.md`, `human_review.md`, `retrospective.md`, and `rollback_log.md` across the remaining steps.

---

## requirements.md

**Purpose:** Defines what will and will not be built this sprint. The human and Architect agree on this scope boundary before any implementation begins.

```markdown
# Sprint [NUMBER] Requirements
**Sprint Goal:** [One sentence]
**Status:** Planning / In Progress / Complete
**Branch:** sprint/[NNN]-[description]

## Functional Requirements
1. [Requirement 1]

## Scope Boundaries
### In Scope
- [Feature A]

### Out of Scope (do not build this sprint)
- [Feature X]
```

---

## blueprint.md

**Purpose:** The technical implementation plan. Lists every file to create or modify, the step-by-step logic, and the Architect's assumptions. The human reviews every assumption before approving.

```markdown
# Sprint [NUMBER] Technical Blueprint
**Architect:** [LLM used]

## Implementation Plan

### Step 1: [Step Name]
What: [Description]
Files affected: [list]
Logic: [How it works]

## Architect Assumptions
- [List every assumption made. Human must verify each before approving.]
```

> **Note:** The Architect Assumptions section at the bottom of `blueprint.md` is critical. Read every assumption before approving — a wrong assumption produces a wrong build. If any assumption is incorrect, write your corrections in `blueprint_feedback.md` and return to Step 2.

---

## blueprint_feedback.md

**Purpose:** Used at Step 2B of the Sprint Workflow when the human finds a problem with the blueprint. Write corrections here and return to the Architect for a revised blueprint — do not try to patch a flawed blueprint by editing it directly.

```markdown
# Blueprint Feedback

## Sprint [NUMBER] Blueprint Issues

### Issue 1: [Short description]
**Section affected:** [Which part of blueprint.md]
**Problem:** [What is wrong or missing]
**Required correction:** [What the revised blueprint should say]
```

---

## acceptance.md {#acceptancemd}

**Purpose:** The checklist that defines done. All items must be checked before the sprint can be committed. Written by the Architect; reviewed by the human before the Builder starts work.

```markdown
# Sprint [NUMBER] Acceptance Criteria
All items must be checked before this sprint is considered complete.

## Functional Criteria
- [ ] [User can do X]
- [ ] [Feature Y works correctly]

## Technical Criteria
- [ ] No type errors
- [ ] Build completes successfully
- [ ] Test results pasted into implementation_log.md

## Verification Commands (run in order)
1. [test command]
2. [build command]
```

For a fully completed example, see [Sprint 001 Acceptance Criteria](../example.md#sprint-001-acceptance-criteria-full).

---

## dry_run.md {#dry_runmd}

**Purpose:** The Builder's read-only pre-flight report. Lists every file the Builder intends to create or modify before touching anything. The Builder produces this file and then **stops**.

```markdown
# Sprint [NUMBER] Builder Dry Run
**Date:** [YYYY-MM-DD]
**Builder Tool:** [Tool name]
**Permission Level Requested:** [0-4]

## Files I Intend to Create
| File Path         | Change Type | Reason        |
|-------------------|-------------|---------------|
| src/[path]        | Additive    | [Why needed]  |

## Files I Intend to Modify
| File Path         | Change Type | What Changes  |
|-------------------|-------------|---------------|
| src/[path]        | Refactor    | [What]        |

**STOPPED. Awaiting Architect approval and permission level assignment.**
```

> **The STOPPED line is required.** The Builder must not write a single line of implementation code until it receives explicit operator clearance. If the Builder proceeds past the dry run without stopping, the entire safety model of the framework is bypassed.

---

## implementation_log.md {#implementation_logmd}

**Purpose:** The audit trail of what the Builder actually did. Lists every file created or modified, and includes the raw terminal output from all verification commands.

```markdown
# Sprint [NUMBER] Implementation Log
**Date:** [YYYY-MM-DD]
**Builder Tool:** [Tool name]
**Permission Level Used:** [Level]

## Files Created / Modified
- src/[path]: [Description]

## Verification Results

### Test Output
[Paste terminal output here]
Result: Passed / Failed
```

> **Paste raw terminal output verbatim — do not summarize.** "Tests passed" in a summary can mean 1 test passed and 47 were skipped. The raw output tells you what actually ran. The Architect reviews this output in Step 8 of the Sprint Workflow.

---

## human_review.md

**Purpose:** The final human approval gate. All five gates must pass before committing the sprint.

```markdown
# Sprint [NUMBER] Human Approval Gate

## The Five Gates

### Gate 1: Scope
- [ ] implementation_log.md lists only files that appeared in dry_run.md

### Gate 2: Tests
- [ ] Passing test results are present in implementation_log.md

### Gate 3: Debt
- [ ] All known issues from this sprint are in planning/backlog.md

### Gate 4: Decisions
- [ ] All new dependencies have DECISIONS.md entries

### Gate 5: State
- [ ] STATE.md reflects completed sprint status

## Approved to commit: Yes / No
```

---

## retrospective.md

**Purpose:** Captures what went well, what broke, and any new constraints to add to `AGENTS.md`. This is the feedback loop that converts one-time mistakes into permanent guardrails.

```markdown
# Sprint [NUMBER] Retrospective

## What Went Well / What Broke or Was Unclear
- [Item]

## Blueprint Quality
- Was requirements.md clear? [Yes / No]
- Was blueprint.md accurate? [Yes / No]

## Time Estimate vs Actual
- Estimated: [X hours] / Actual: [Y hours]

## New Constraints Added to AGENTS.md
- [Any rule added as a result of this sprint's findings]
```

Any constraint listed under "New Constraints Added to AGENTS.md" must actually be added to [AGENTS.md](agents.md) before the next sprint begins.

---

## rollback_log.md

**Purpose:** Documents the rollback procedure before the Builder begins, and records what happened if a rollback was needed.

```markdown
# Sprint [NUMBER] Rollback Log

## Pre-Implementation (fill in before Builder begins - Level 4 required)
**Current clean commit hash:** [git log --oneline -1]
**Rollback command:** `git checkout [branch] && git revert HEAD~[N] --no-edit`

## Post-Implementation (fill in only if recovery was needed)
**Root cause identified:** [what went wrong]
**State after revert:** [Clean / Partial - describe]
```

**Level 4 (Migration) requires `rollback_log.md` to be pre-filled before the Builder begins.** For all other permission levels, pre-filling rollback_log.md is strongly recommended — if something goes wrong in production, you need to be able to revert in seconds, not minutes.

## See Also

- [Sprint Workflow](../sprint-workflow.md)
- [Mode 2: Feature Sprint](../modes/feature-sprint.md)
- [Mode 3: Refactor / Migration](../modes/refactor-migration.md)
