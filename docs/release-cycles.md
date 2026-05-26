# Release Cycles

A release groups features into a bounded delivery target — a completed release becomes the baseline for the next.

## Table of contents

1. [Release plan](#release-plan)
2. [Release folder structure](#release-folder-structure)
3. [Starting a new version](#starting-a-new-version)
4. [Release completion criteria](#release-completion-criteria)

---

## Release plan

A release plan defines the scope and delivery terms for one version of the project. It contains:

- release goal,
- in-scope features,
- out-of-scope items,
- required research,
- risks,
- sprint sequence,
- release criteria,
- release notes,
- and retrospective criteria.

Design Mode generates the release plan. The human reviews and approves it before sprint work begins.

**Rule:** A new release updates the project brain. It does not restart the project from zero.

---

## Release folder structure

Each release gets its own folder under `planning/releases/`. Sprint folders live inside the release folder.

```
planning/
├── backlog.md
└── releases/
    ├── v0.1/
    │   ├── release_plan.md
    │   ├── scope.md
    │   ├── release_notes.md
    │   ├── retrospective.md
    │   └── sprints/
    │       ├── sprint_001/
    │       └── sprint_002/
    └── v0.2/
        ├── release_plan.md
        └── sprints/
            └── sprint_001/
```

---

## Starting a new version

To begin v2.0 after v1.0, load the following files into a Design Mode session:

```
DOMAIN.md
STATE.md
DECISIONS.md
RISKS.md
QUESTIONS.md
planning/backlog.md
planning/releases/v1.0/retrospective.md
user feedback
open issues
```

Design Mode generates:

```
planning/releases/v2.0/release_plan.md
planning/releases/v2.0/scope.md
planning/releases/v2.0/research_questions.md
updated STATE.md
updated planning/backlog.md
updated RISKS.md
```

The project brain files — `DOMAIN.md`, `DECISIONS.md`, `AGENTS.md` — carry forward from v1.0 unchanged, unless the new release requires updates to domain logic or operating rules.

---

## Release completion criteria

A release is complete when all eight conditions are met:

1. in-scope features are complete or intentionally deferred with a backlog entry,
2. release criteria defined in `release_plan.md` are met,
3. docs are updated to reflect the release,
4. changelog is updated,
5. release notes exist,
6. known issues are recorded in the backlog,
7. deployment or distribution is complete,
8. and the release retrospective exists.

**Rule:** A new release updates the project brain. It does not restart the project from zero.

---

[← Work Scale Model](work-scale.md) · [← Wiki Home](index.md) · ADDF v3.5
