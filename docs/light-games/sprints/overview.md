# The Three-File Sprint Pack

A sprint is a **bounded experiment or playable increment** with a testable end. Light consolidates original ADDF's numerous sprint artifacts into `SPRINT.md`, `PLAN.md`, and `REVIEW.md` without deleting their responsibilities.

## When to use

Read when creating Sprint 001, teaching a student how to plan gameplay, or evaluating whether a sprint can be safely continued after an interruption.

## The minimum pack

```text
planning/sprints/sprint-001/
├── SPRINT.md    # what, why, tradeoffs, AC-##, Gate D
├── PLAN.md      # how exactly, commands, dependencies, Gate I, execution
└── REVIEW.md    # actual results, human playtest, refinement, Gate A
```

The **blank project** does not contain a sprint folder. The agent copies the three distribution templates only after the human selects a milestone; it updates IDs/revisions to match `STATE.md` and `GAME.md`.

## Responsibilities don't merge

`SPRINT.md` owns **experience intent**. It records why the sprint matters, evidence, design alternatives, learning checkpoint, in/out scope, selected direction, and `AC-##` criteria. Gate D belongs here and in significant `D-###` decisions.

`PLAN.md` owns **execution scope**. It enumerates exact create/modify/move/delete paths, commands and working directories, dependencies/assets with provenance, side effects, rollback and verification. Gate I belongs here. The agent's actual command results also live here.

`REVIEW.md` owns **evidence and verdicts**. Every acceptance criterion has a real result or `not_tested`. Human observations and each refinement round remain visible. Gate A belongs here, never in a model's unverified confidence.

## A good first sprint

A tiny dodge game could test:
- AC-01: four-direction control with arena bounds;
- AC-02: one repeating hazard clearly triggers failure;
- AC-03: restart resets the attempt.

It would exclude high-score services, audio, art-generation pipelines, multiplayer and future levels until needed. This makes a playable and inspectable outcome likely within one iteration.

## The sprint lifecycle

1. Choose one backlog candidate or focused question.
2. Research and design its player outcome; draft `SPRINT.md`.
3. Obtain Gate D for meaningful choices.
4. Draft the exact `PLAN.md` dry run; obtain Gate I.
5. Implement and test inside authorized scope, recording actual evidence.
6. Refine if tests or players expose defects, re-authorizing new scope.
7. Provide a runnable artifact and ask for human Gate A.
8. Preserve the verdict, retrospective and handoff; choose the next sprint later.

A formal no-code research-spike sprint still documents its bounded plan and evidence even though it authorizes **no game code**.

## Common failures

**Premature sprint folder:** The framework creates ten empty sprints at initialization. Keep only the active selected sprint.

**Approval conflation:** Design choice is treated as permission for commands. Split D and I.

**Missing history:** A correction erases an earlier negative playtest. Preserve review rounds.

## Related

[Planning](planning.md) · [Approval gates](approvals.md) · [Review and retrospective](review.md) · [File reference](../reference/file-reference.md)
