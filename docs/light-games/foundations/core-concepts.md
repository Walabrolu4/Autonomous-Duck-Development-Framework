# Core Concepts and How They Fit Together

ADDF Light Games consists of five interlocking concepts: **the game project**, **persistent project brain**, **bounded sprint**, **write capability**, and **human gate**. Confusing any pair of these is a common source of AI overreach.

## When to use

Use this when an agent seems to conflate an approved design with implementation permission, a branch with a sprint, or a technical test with actual human acceptance.

## Project and framework are different things

The framework distribution supplies rules and starter files. The individual game's project repository contains the actual source, game intent, current state and real approval records. The framework's `spec/` files are authoritative for distribution templates, but a game's current human-approved `GAME.md` and decisions reflect the user's project-specific intentions.

The game engine is not the framework. A browser Canvas prototype, Phaser game, Godot project or Unity game may all follow the same decision and approval process.

## Project brain

Six persistent files exist in a blank project: `SECURITY.md`, `AGENTS.md`, `GAME.md`, `STATE.md`, `DECISIONS.md`, `planning/BACKLOG.md`. They are intentionally small at first. The agent updates them as facts and choices become known.

`STATE.md` is a **summary view**, not independent proof of human permission. The exact consent source and plan revision must be recoverable from the relevant sprint record.

## Sprint pack

One sprint has three files under `planning/sprints/sprint-NNN/`:

| File | Owns | Approval |
| --- | --- | --- |
| `SPRINT.md` | Goal, research, scope, design alternatives, learning checkpoint, `AC-##` criteria | Gate D |
| `PLAN.md` | Exact file operations, dependencies, commands, risks, test plan, implementation record | Gate I |
| `REVIEW.md` | Actual test outcomes, human observations, refinements, final verdict | Gate A |

A sprint represents a bounded, verifiable **learning or playable outcome**. A backlog item is only a candidate, not an approved sprint. Creating a Git branch is not a substitute for creating/approving the sprint documents.

## Stages versus capabilities

**Stages** communicate what work the person and agent are doing: research, design, implement, refine, accept.

**Capabilities** govern file writes:
- Research: safe investigation and notes, no source changes.
- Design: project-brain and plan drafting, no source changes.
- Develop: changes only inside a human-approved exact `PLAN.md`.

An agent in the “Refine” stage may still need Develop capability and a valid Gate I to change code.

## Approval versus evidence

A successful Node test establishes a particular behavior in a known execution environment. It does not show that a person liked the control feel. A line in `PLAN.md` saying `gate_i_status: authorized` must be linked to a real human response; the Python validator can check internal coherence **but cannot authenticate authorship**.

A materially changed plan **invalidates** authorization tied to the older revision. Preserve the historical approval rather than overwriting it.

## Example: moving a duck

The backlog holds “Make movement responsive.” Sprint 001 narrows it to four-direction movement in a small arena. A design choice considers acceleration, Gate D records the selected feel. The plan lists an exact JavaScript file, test command and no dependencies. Gate I permits that revision only. The agent implements, verifies directional movement and presents a runnable game. The human tests and provides Gate A.

If the agent discovers a need for a new input package after starting, it **stops** and revises the plan instead of interpreting the initial authorization broadly.

## Common failures

**Status as authority:** `STATE.md` says authorized but no consent source exists. Fail closed.

**Overgrown sprint:** A sprint bundles several untested systems. Split into testable slices.

**Lost evidence:** The agent stores all choices in chat only. Update `DECISIONS.md` and the sprint pack.

## Related

[Lifecycle overview](../lifecycle/index.md) · [File reference](../reference/file-reference.md) · [Approval gates](../sprints/approvals.md)
