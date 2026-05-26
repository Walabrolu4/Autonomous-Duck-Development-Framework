# Feature Cycles

A feature cycle adds a capability to an existing project without restarting the full lifecycle.

## Table of contents

1. [Feature flow](#feature-flow)
2. [Feature folder structure](#feature-folder-structure)
3. [Feature brief template](#feature-brief-template)

---

## Feature flow

A feature follows an 8-step flow. Steps 3 and 4 are conditional — skip them if the feature is well-understood and constraints are already clear.

1. Add idea to `planning/backlog.md`.
2. Write the feature brief in `planning/features/[feature-name]/feature_brief.md`.
3. Research if needed — use Research Mode for unknowns.
4. Design feasibility if needed — use Design Mode to evaluate constraints.
5. Validate scope — confirm the feature is bounded, and that security and domain boundaries are respected.
6. Generate the Sprint Pack — Design Mode produces `requirements.md`, `blueprint.md`, `acceptance.md`.
7. Develop with Dry Run — Develop Mode follows the [Sprint Loop](sprint-loop.md).
8. Review and update project memory — Design Mode updates `STATE.md`, `DECISIONS.md`, and relevant docs.

**Rule:** A feature cycle extends the project. It does not erase existing state.

---

## Feature folder structure

Each feature gets its own folder under `planning/features/`:

```
planning/
└── features/
    └── [feature-name]/
        ├── feature_brief.md
        ├── research.md
        ├── feasibility.md
        ├── validation.md
        ├── decisions.md
        └── sprint_map.md
```

Not every file is required for every feature. A simple, low-risk feature may need only `feature_brief.md` and the Sprint Pack. A complex feature may use all of them.

---

## Feature brief template

The feature brief is the first Design Mode output for any new feature. It defines the scope, constraints, and done condition before sprint planning begins.

```md
# Feature Brief: [Feature Name]

## Summary
[What capability is being added?]

## User Value
[Why does this matter?]

## In Scope
- [Item]

## Out of Scope
- [Item]

## Known Constraints
- [Constraint]

## Research Needed
- [Question or "None"]

## Feasibility Risks
- [Risk or "None"]

## Acceptance Summary
- [High-level done condition]

## Related Files
- [Relevant files or folders]

## Release Target
[Version]
```

**Rule:** Templates are starting points, not decoration. Remove sections that do not apply.

---

[← Release Cycles](release-cycles.md) · [← Work Scale Model](work-scale.md) · [← Wiki Home](index.md) · ADDF v3.5
