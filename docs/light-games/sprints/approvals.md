# Human Approval Gates: D, I and A

Light's three gates intentionally distribute authority across **experience**, **execution**, and **evaluation**. Skipping one cannot be compensated for by extra technical tests.

## When to use

Use when the user asks “Can the agent just continue?”, when scope changes, or when an AI marks work complete without first-hand verification.

## Gate D — Significant design choices

Gate D settles consequential player experience, scope, architecture or technology direction. The agent offers genuine alternatives, tradeoffs, evidence and a recommendation, then asks one direct question. Record actual choice in `DECISIONS.md` and the sprint's `SPRINT.md`.

No material design fork? A justified `not_required` may be acceptable. A trivial variable name inside existing approved behavior need not trigger a full design vote.

**Gate D never authorizes code edits.**

## Gate I — Exact implementation authorization

The agent presents `PLAN.md` before code changes. The reviewer sees:
- current revision and linked sprint;
- exact create/modify/move/delete paths;
- shell commands, directories, side effects and external service access;
- dependency versions, downloads/asset provenance;
- security, destructive or paid actions;
- test strategy, risks, rollback and exclusions.

Only clear permission for this **exact** scope allows Develop to act. Ambiguous “go ahead” about a concept is insufficient if the file/command plan wasn't shown.

**Gate I becomes stale** when files, commands, dependency/version, material behavior, risk or external effects change. The agent stops, documents the difference and requests a new gate for the revised plan.

## Gate A — Human acceptance

The agent presents the runnable artifact, actual tests, failing/untested checks and short playtest steps. The human evaluates and provides a verdict: `accepted`, `accepted_with_conditions`, `needs_refinement`, `rejected`, or `paused`.

Automated tests can establish logical behavior but cannot decide whether the mechanic feels responsive, a level is readable or an onboarding interaction makes sense.

A condition that blocks release must remain a blocker even if the human conditionally approves the sprint.

## Approval records

Each gate has a source/revision reference and recorded human wording or durable review link. Agents may transcribe actual approvals, **never invent them**. A model's memory or generated checkbox does not independently prove consent.

Gate location:
- D: `SPRINT.md`, cross-linked to `D-###`;
- I: `PLAN.md`, reflected in `STATE.md`;
- A: `REVIEW.md`, reflected in `STATE.md`.

## A common ambiguity

The human says, “Yes, I like the dodge game.” This may settle a concept preference, not authorization to create files or install Phaser. The agent should acknowledge the selected direction, show the technical plan, and ask: “Do you authorize r1's exact operations?”

After implementation, “The tests all pass” isn't an acceptance verdict. Ask the human to try the game and describe whether the agreed experience works.

## Stop conditions

When an approval can't be verified, degrade to a **safe non-implementation state**. Do not forge the missing record or proceed because a previous agent claimed it was approved.

## Common failures

**Gate bundling by inference:** Treat enthusiasm as all three gates. Split the records.

**Retroactive consent:** Add new paths to r1 after its approval. Create r2 and ask again.

**AI self-acceptance:** The agent fills “human verdict: accepted.” Keep pending until real review.

## Related

[Normative approval policy](../../spec/APPROVAL_POLICY.md) · [Plan](planning.md) · [Review](review.md)
