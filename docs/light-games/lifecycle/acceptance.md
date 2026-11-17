# Stage 5 — Human Acceptance

Acceptance evaluates **the actual player experience**. An agent can prepare tests, evidence and play instructions; only the human can supply the final verdict.

## When to use

Use after an implementation or refinement cycle has an inspectable/runnable outcome, or when deciding whether a research spike answered its question.

## Prepare a fair review

`REVIEW.md` should contain:
- the original `AC-##` criteria from `SPRINT.md`;
- commands actually run, test outcomes and device/environment where known;
- a runnable build or an honest blocker;
- short human test steps and expected observations;
- known defects, assumptions, accessibility/device limits and release blockers;
- empty Gate A verdict fields until the human responds.

An agent may pass its unit tests but fail to create a usable build. Don't pretend the human could play the game if there is no actual artifact.

## Playtest the experience

For a movement-and-obstacle sprint, ask the person to:
1. launch the game with the verified instructions;
2. move in each direction and test boundary collisions;
3. avoid and intentionally hit obstacles;
4. restart and observe response;
5. describe whether control feel and hazard readability matched expectations.

The person's answer can be concise: “Input feels instant, but I can't see the hazard against the background.” That is more informative than a fabricated “all good.”

## Record Gate A

Allowed verdicts:
- **accepted** — criteria meet the human's expectations;
- **accepted_with_conditions** — accepted subject to explicitly preserved conditions;
- **needs_refinement** — correct and retest;
- **rejected** — preserve reason and decide whether to revise or abandon;
- **paused** — insufficient evidence or external blocker.

Record the actual response and source in `REVIEW.md`. Conditional acceptance **with unresolved release-blocking conditions** is not unconditional completed/releasable status.

The framework's documented Stage 6 validator may recognize internally consistent entries, but it **cannot authenticate human consent or gameplay experience**. A human verdict is not replaceable by code.

## Closing the sprint

After genuine acceptance, update `STATE.md` and `planning/BACKLOG.md` to show what is done, what remains deferred, what was learned and the next possible slice. Preserve prior refinement rounds and past human feedback.

Do **not** auto-create Sprint 002 simply because Sprint 001 closed. The person chooses the next direction.

## Research-only acceptance

A formal research-spike sprint may have criteria such as “the test produced reproducible measurements” and “we can choose between two approaches.” Human Gate A evaluates whether those *evidence deliverables* answer the agreed question—not whether an imaginary game was playable.

## Common failures

**Test success equals approval:** CI is green but user hasn't tried it. Keep `awaiting_acceptance`.

**No evidence per criterion:** A broad “done” lacks test coverage. Map each original AC to pass/fail/partial/not-tested.

**Silencing negative feedback:** An earlier rejection is removed after fixes. Preserve round history.

## Related

[Playtesting](../quality/playtesting.md) · [Sprint review](../sprints/review.md) · [Refinement](refine.md)
