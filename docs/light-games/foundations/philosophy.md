# Philosophy: Deep Reference, Small Runtime

ADDF Light Games retains original ADDF's **file-first memory, bounded roles and human approval** while reducing the number of documents and repetitive prompts needed to run an ordinary game-design sprint.

## When to use

Read this when deciding whether the framework is too heavy, when explaining it to a class or team, or when considering a new rule that would add friction to a beginner's first session.

## Principle 1 — The human designs the experience

The agent can research camera options, prototype a movement controller and summarize playtest comments. It must not silently decide whether the game should be a puzzle or a shooter, whether acceleration is desirable, or whether a playable slice “feels good.” Those are meaningful human choices informed by evidence.

Not every variable name is a vote. **T0 routine** implementation details can be resolved by the agent inside an approved plan. **T1 significant** choices require a design decision. **T2 high-impact** matters—security, costs, destructive actions, public publishing—require stricter review and possibly separate special authorization.

## Principle 2 — Learning is part of making

An agent should explain *why* the first sprint tests movement or feedback, not merely provide code. A learning checkpoint may ask the designer to predict whether instant movement will feel snappy or overly rigid, then compare that hypothesis with actual playtesting.

It must be relevant to the work. No artificial quizzes or compulsory theoretical detours.

## Principle 3 — Evidence beats plausible narration

Each important statement is **verified**, **inferred**, **proposed**, or **unknown**. An installed test script is not a passing test. A green test is not a successful manual playthrough. A model's fabricated “Human approved” field does not authorize anything.

Agent handoffs start from the project's files and check Git/worktree state where possible. Chat history is useful context but insufficient authority for a stale plan.

## Principle 4 — One playable slice at a time

A *slice* is a narrow, observable player experience. A full level, inventory, skill tree and save system in Sprint 001 would hide risks and make evaluation harder. Isolate the smallest experiment that tests the central unknown.

Ideas not needed now stay in `planning/BACKLOG.md`; they are not lost, nor automatically approved.

## Principle 5 — Safety isn't an optional advanced feature

The simple workflow retains three separate human gates: design, exact implementation authorization, and actual acceptance. Permission to run a terminal is not permission to run an arbitrary command. Permission to edit one file does not authorize a new package, API, deletion, deployment or network transfer.

The validator checks **internal file consistency** but cannot authenticate consent. This limitation is intentional and documented.

## Principle 6 — Progressive disclosure

The normal path needs six persistent Markdown files and, when work is chosen, `SPRINT.md`, `PLAN.md`, `REVIEW.md`. Add architecture diagrams, asset licensing inventories, release records or cross-sprint risk logs **only when needed**.

A comprehensive wiki, generated manual and provider-specific skills can exist without burdening the user with all of them during onboarding.

## Example: avoiding false autonomy

A student says: “Make enemy AI.” The agent asks which behavior should be observable in the first playtest, compares patrol-and-chase versus a stationary defender, and asks the student to choose. It writes acceptance criteria, then a narrow implementation plan. When the student says “I choose patrol,” the agent records Gate D **but does not code** until Gate I. Once the code is built, the student tries it and reports whether the chase is legible; the model does not award itself Gate A.

## Common failures

**Process theater:** Files are complete but nobody tested the mechanic. Recover by defining observable acceptance criteria.

**Agent overreach:** An adapter enables shell tools and assumes it may edit anything. Recover by checking the actual `PLAN.md` revision.

**Documentation overload:** A novice gets nine questionnaires. Recover with the first-session script and a default `unknown` value.

## Related

[Overview](overview.md) · [Decision making](../learning/decisions.md) · [Approval gates](../sprints/approvals.md) · [Human playtesting](../quality/playtesting.md)
