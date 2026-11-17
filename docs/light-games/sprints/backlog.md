# Backlog: Keep Ideas Without Building Them Yet

The backlog collects possible player outcomes, research experiments and deferred work. Its purpose is to **protect focus** while preserving future ideas.

## When to use

Use when a brainstorming session produces too many ideas, when playtesting suggests a new feature, or when a designer asks why a requested system isn't in the active sprint.

## One item = observable outcome

Each candidate uses a stable `B-###` ID and records title, player-facing outcome, priority, status, dependency, linked sprint (if any) and rationale.

For example:

```md
### B-003 — Clear hazard feedback
- id: B-003
- title: Clear hazard feedback
- outcome: A first-time player can identify hazards before colliding.
- priority: next
- status: candidate
- depends_on: B-001
- sprint: none
- reason: Playtest feedback suggests the first obstacle is hard to perceive.
```

Do not interpret the example as a real entry until the human actually requests or confirms it.

## Selecting a first slice

A meaningful `priority: now` candidate should be small enough to answer one question. If “Build enemy AI” contains movement, animation, targeting, health and coordination, split it into separate outcomes. The user chooses consequential priorities; the agent may recommend ordering based on evidence and dependencies.

Only after selection should an item become `status: selected` and link to a real `sprint-NNN`. Backlog inclusion does not authorize implementation.

## Research spikes versus features

A research spike might ask: “Can this browser build reliably access the needed controller inputs?” Its deliverable is sourced evidence or a deliberately authorized experiment, **not** a full input system. Label its outcome explicitly to avoid presenting research progress as shipped gameplay.

## Updates after playtesting

After the human's Gate A verdict, the agent can mark the completed slice, defer new suggestions, preserve discarded ideas with reasons, and recommend the next candidate. “Needs refinement” may stay inside the current sprint if the fix is within scope or requires a revised authorization.

Stable IDs aren't recycled when an idea is rejected. Status values include `candidate`, `selected`, `in-progress`, `completed`, `deferred` and `discarded`.

## Example prioritization

A designer wants enemy waves, new art and more levels. The last test showed movement controls are inconsistent. The agent recommends fixing controls **before** enemy waves because later difficulty feedback will be unreliable otherwise. The user can disagree; the choice and reasoning should be recorded if material.

## Common failures

**Backlog as permission:** The agent implements a “next” idea without a sprint and Gate I. Stop.

**Infinite backlog grooming:** The team spends more time ranking ideas than testing them. Prioritize only enough to select the next slice.

**Deletion without reasoning:** Rejected ideas disappear. Preserve status and reason.

## Related

[Sprint overview](overview.md) · [Decisions](../learning/decisions.md) · [Scope and planning](planning.md)
