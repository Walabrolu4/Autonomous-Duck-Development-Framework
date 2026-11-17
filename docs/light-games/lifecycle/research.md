# Stage 1 — Research

Research is a focused investigation of uncertainty that could change the next game-design or engineering decision. It is **not** permission to begin an unbounded technical implementation.

## When to use

Use Research when the idea is vague, a control model is unclear, a target engine/API may be unsupported, a performance constraint matters or a playtest exposed an unknown.

## Inputs and source discipline

Start with the safe project brain and the current question: `GAME.md`, `DECISIONS.md`, optional current `SPRINT.md`, the project's permitted source and actual documentation.

For each meaningful factual finding, record:
- **Question:** What would change our decision?
- **Evidence:** A specific source URL, repository artifact, versioned documentation or actual measurement.
- **Confidence:** Verified, inferred, proposed or unknown.
- **Tradeoff:** How the evidence affects player experience, scope or complexity.
- **Next action:** Choice, focused experiment, or known blocker.

No source? Say *not verified* and describe how to check; don't fabricate benchmark numbers, platform support or citations.

## Research should be bounded

Ask whether the uncertainty can be resolved before committing to a sprint. One example: “Can keyboard and touch inputs drive the same movement function in a simple browser prototype?” This can be answered with documentation or a **read-only** code inspection. If answering requires a new runtime script, package installation or experiment that edits game files, write a plan and obtain Gate I first.

A **formal research-spike sprint** still uses `SPRINT.md`, `PLAN.md`, `REVIEW.md`, and its Gate I is scoped to the actual research operations, even when no source code is authorized. Pre-sprint read-only discovery doesn't need a fictional Gate I.

## Outputs

Focus important findings in `SPRINT.md` under Research and evidence when the sprint exists. Project-wide unknowns may be summarized in `STATE.md` or the backlog. A separate `research/` folder is optional when material no longer fits a sprint.

Present the person with **two or three feasible alternatives when genuine choices exist**, a reasoned recommendation and one consequential question.

## Example: movement model

The agent compares:
- **Direct velocity:** immediate response, simple to test, possible abrupt feel;
- **Acceleration:** nuanced feel, requires tuning and more careful testing.

It might recommend direct movement for Sprint 001 because the first experiment is about obstacle legibility rather than motion physics. That recommendation is still **proposed**, not human-approved.

If the user says “I'm undecided,” offer a reversible pair of trials only after describing their file scope and obtaining authorization for any code.

## Exit criteria

Research is ready to advance when the problem and main unknown are clear, evidence/uncertainty is labeled, significant alternatives are visible and a meaningful decision or testable hypothesis can be proposed. It is not necessary to know every implementation detail.

## Common failures

**Research rabbit hole:** Reading fifty tutorials without narrowing a decision. Stop at the first material uncertainty.

**Assumption laundering:** “The engine supports this” without version/source. Mark unknown.

**Research bypass:** Running an unapproved install command because “it's only a spike.” Plan actual side effects first.

## Related

[Guided discovery](../learning/guided-discovery.md) · [Design](design.md) · [Security](../quality/security.md)
