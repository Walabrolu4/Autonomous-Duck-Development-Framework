# Starting With a One-Sentence Idea

An idea such as “a fishing game where the weather changes the fish” is enough to begin. The agent should **unpack it carefully**, not treat its guesses as settled facts or build an enormous project from it.

## When to use

Use this when the user knows a fantasy, setting, core interaction or desired emotion but has not chosen the engine, control model, scope or technical system.

## Three-column understanding

The first agent response distinguishes:

| Category | Example for a weather-driven fishing game |
| --- | --- |
| **Known** | Fishing is the main activity; weather affects fish in some way |
| **Inferred** | The player may cast a line; fish may have spawn rules; likely needs feedback |
| **Unknown** | What weather changes; platform/input; arcade vs simulation; intended first slice |

Do not convert inferred mechanics into `GAME.md` pillars without user confirmation.

## Narrow to a testable core

Ask: “What should the player be able to do in the first five minutes of testing?” A useful slice could be: **press a button to cast a line; a simple rain toggle changes the visible chance of a fish appearing**. This tests the weather-mechanic relationship with placeholder art and no inventory/economy.

Explain alternatives that actually affect the experience. For example, “weather changes bite probability” versus “weather changes fish movement” asks for a different test and different technical plan.

Put boats, characters, maps, online co-op and nuanced ecosystems into the backlog until relevant.

## Research when needed

If a claim about a target game engine or platform might change feasibility, check current authoritative documentation or perform a small bounded experiment. Record sources and unknowns. Never fabricate an engine feature, benchmark or API call.

If the idea needs expensive hardware, credentials, a data source or paid service, propose an offline substitute for the first slice or request the necessary separate authorization.

## Write the design record

The agent should maintain:
- `GAME.md` — confirmed player action, intended experience, constraints and playable hypothesis;
- `DECISIONS.md` — meaningful human selection among weather-mechanic alternatives;
- `planning/BACKLOG.md` — deferred features;
- `SPRINT.md` — one selected outcome, in/out scope and `AC-##` checks.

Then prepare `PLAN.md` with exact implementation operations and seek Gate I. Do not preinstall dependencies while “doing research.”

## Example acceptance criteria

**AC-01:** The player can initiate a cast with a clearly labeled input; the game shows the action.

**AC-02:** Toggling rain changes the observed in-game indicator and affects one defined fishing rule.

**AC-03:** Reset returns weather and fishing state to the chosen baseline.

The criteria should specify methods, environment and evidence when actual sprint documents are written. A player must test whether the relation is understandable even if deterministic unit checks pass.

## Common failures

**Scope inflation:** AI adds crafting, inventory and fishing economy. Recover by isolating one observable cause/effect.

**False consensus:** It assumes realism, difficulty or graphics without user choice. Mark such matters unknown.

**Early technology lock-in:** “Fishing implies Unity.” The framework is engine-agnostic; choose tools based on the actual slice.

## Related

[Design](../lifecycle/design.md) · [Sprint planning](../sprints/planning.md) · [Backlog](../sprints/backlog.md)
