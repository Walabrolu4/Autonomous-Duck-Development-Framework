# Stage 4 — Refine

Refinement applies **evidence from tests and human playtesting** to correct a bounded gameplay slice. It is not permission to expand the feature or edit source outside the approved technical plan.

## When to use

Use after a build fails, an acceptance criterion is unmet, a player reports confusing feedback or the first prototype reveals an incorrect design hypothesis.

## The diagnosis loop

1. **Observation:** What exactly failed? Quote a real test or user's first-hand report; do not invent it.
2. **Reproduction:** What input, build, browser/device, sequence and expected behavior are known?
3. **Classification:** Is it a verified bug inside current scope, a hypothesis requiring investigation, or a new requirement/design choice?
4. **Permission:** Does existing Gate I still authorize the paths, commands, packages and risk necessary to fix it?
5. **Correction:** If in scope, make the smallest change and run approved checks. If out of scope, revise `PLAN.md` and request new Gate I.
6. **Preserve history:** Record `round-N` in `REVIEW.md`, old observations, correction, evidence and next human retest.
7. **Reassess:** Present updated test results and invite actual human evaluation.

A changed *design* may require returning to Gate D before another Gate I.

## Three categories of change

| Classification | Example | Correct action |
| --- | --- | --- |
| **In scope** | Approved movement code has an off-by-one boundary bug | Correct within valid Gate I, test, log |
| **Scope expansion** | Requires a new collision library not in the plan | Stop, revise plan and seek Gate I |
| **New design decision** | Player now wants a dash mechanic instead of only movement | Record/design choice, update acceptance checks, then new plan approval |

**Never** label an entire second game system “just polish.”

## Example: unreadable hazard

The player says: “I cannot tell that the red block is dangerous until I hit it.” The agent should record this as a human observation and investigate contrast, size, motion cues or onboarding. A revised border or shape within already approved CSS/canvas scope may be an in-scope refinement; adding sound assets, packages or a tutorial overlay beyond the plan may need new approval.

A learning checkpoint can ask whether the user expected color alone to be enough, then compare the next retest with that prediction. This is meaningful education, not an artificial quiz.

## Rejection is not erasure

If the user rejects a playtest, keep the original verdict, failing criteria and feedback in `REVIEW.md`. Later `round-2` can contain a new, specific result. Do not backdate or overwrite `round-1` to make the history appear continuously successful.

## Exit criteria

The refined outcome is ready for human Acceptance only when it is actually runnable/inspectable, technical checks and known defects are reported accurately, and the human has concise steps aligned with the original criteria.

## Common failures

**AI reacts to criticism by redesigning the entire game:** Ask which experience needs to change; keep out-of-scope ideas in backlog.

**Partial approval forgotten:** The human authorized code but not new audio assets. Keep that boundary.

**Fake retest:** “It should work now” is prediction, not evidence. Run actual checks or label unverified.

## Related

[Human acceptance](acceptance.md) · [Review records](../sprints/review.md) · [Failure recovery](../quality/failure-recovery.md)
