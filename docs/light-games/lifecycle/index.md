# The Five-Stage Game Development Lifecycle

Every ADDF Light Games sprint works toward a **small, verifiable player-facing outcome**. The five stages are Research → Design / Ideation → Implement → Refine → Acceptance. They describe what the user experiences, while Research/Design/Develop *capabilities* determine which files an agent may write.

## When to use

Read when starting a sprint, training an agent, deciding a next prompt, or reconciling a status that doesn't match the current work.

## Lifecycle map

| Stage | Primary question | Persistent work | Exit |
| --- | --- | --- | --- |
| **Research** | What don't we yet know, and why does it matter? | Evidence, questions, game hypothesis | Enough information to propose an experiment/decision |
| **Design / Ideation** | What exact player behavior and test will this sprint target? | `SPRINT.md`, decisions, criteria, learning checkpoint | Human Gate D resolved or validly not required |
| **Implement** | What exact files and commands may be changed? | Approved `PLAN.md`, code/tests/assets, execution record | Report actual evidence or a blocker |
| **Refine** | What did the test/playtest reveal and what should change? | `REVIEW.md` rounds, bounded corrections, revised plan if needed | Retest ready or ask for new scope approval |
| **Acceptance** | Does the real outcome meet the human's expectations? | Criterion results, human verdict, retrospective | Human Gate A, or return to refinement/rejection/pause |

A sprint can loop from refinement to design when the intended experience changes. The workflow is not a waterfall of huge milestones.

## Status is not the same as stage

`STATE.md` also records one **sprint status**: `discovering`, `designing`, `awaiting_approval`, `implementing`, `refining`, `awaiting_acceptance`, `accepted`, `rejected`, `paused`. For example, `awaiting_approval` is a *status* during Design while the human evaluates a technical plan.

Formal allowed transitions and paused-state recovery are defined in the normative [Workflow States specification](../../../spec/WORKFLOW_STATES.md). Do not invent a new status just to describe a particular game-engine task.

## The permission rule

Research and Design may update permitted project-brain/sprint-planning Markdown; **they do not change game code, tests, assets, manifests or deployments**. Develop may alter only explicitly approved paths and commands after Gate I. A “Refine” stage does not waive this: code corrections still require valid Develop authorization.

The three gates are not interchangeable:
- Gate D: meaningful game design direction;
- Gate I: exact implementation plan revision;
- Gate A: first-hand human evaluation.

## A complete example

A user wants a tiny obstacle-dodging game. Research checks whether immediate controls and simple collision are feasible in a browser. Design narrows to one duck, one obstacle type and a restart, with `AC-01` to `AC-03`. The human selects immediate movement (Gate D). The agent proposes three source files, a unit test and an authorized Node command; the human approves that exact plan (Gate I). Implementation yields a runnable arena and test results. The human reports the red obstacle is too hard to notice, so refinement investigates color contrast and proposes an in-scope change or revised plan. The user finally retests and gives Gate A.

If tests pass but the user hasn't played, the proper status is `awaiting_acceptance`, **not** `accepted`.

## Common failures

**Stage drift:** The agent starts coding while `STATE.md` still says `designing` with no Gate I. Stop and reconcile.

**Automatic acceptance:** The coding agent marks the sprint complete because CI passed. Request actual user review.

**New feature as “refinement”:** A gameplay change creates a new system beyond the approved scope. Return to Design or backlog instead.

## Related

[Research](research.md) · [Design](design.md) · [Implement](implement.md) · [Refine](refine.md) · [Acceptance](acceptance.md)
