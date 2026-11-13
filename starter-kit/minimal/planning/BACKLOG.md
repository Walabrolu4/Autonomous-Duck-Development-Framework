# Project Backlog

> This is a list of **candidate observable outcomes**, not a promise to implement them. Backlog inclusion and prioritization never constitute Gate I implementation authorization.

## Current direction

- Game direction: unknown.
- Current priority: discovery only.
- Selected sprint: none.
- Selection authority: human for consequential direction; agent may recommend.

## Candidate slices

No candidate slices recorded yet.

When an idea is proposed, create a real, uniquely numbered entry (do not treat the example schema as an actual task):

```md
### B-001 — [short slice title]
- id: B-001
- title: [short slice title]
- outcome: [observable player/user behavior]
- priority: now
- status: candidate
- depends_on: none
- sprint: none
- reason: [why this slice is useful]
```

Actual `priority` values: `now`, `next`, `later`, `unknown`. Actual `status` values: `candidate`, `selected`, `in-progress`, `completed`, `deferred`, `discarded`. IDs `B-001`, `B-002` ... are never reused. Every real item must include `id`, `title`, `outcome`, `priority`, `status`, `depends_on`, `sprint`, and `reason`.

When a candidate is chosen for the next sprint, set `status: selected` and link the actual `sprint-NNN` only after the milestone has been identified. A sprint goal must fit a bounded, testable outcome.

## Research spikes

None selected.

A spike is a focused question with a verifiable evidence deliverable and clear stop condition. Label it as research; **do not** describe a non-playable spike as a finished game feature.

## Deferred and discarded

None.

Retain discarded and deferred items with a reason. Do not hide rejected features or reintroduce them without the user's renewed direction.
