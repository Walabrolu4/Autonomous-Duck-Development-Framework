[Home](../index.md) → [Operating Modes](index.md)

# Operating Modes: Overview

## What a Mode Is

Operating Modes define how to handle individual tasks within the larger lifecycle. The lifecycle tells you which phase of the project you are in. A mode tells you how to approach the specific task in front of you right now.

You can be in Lifecycle Phase 5 (Full-Scale Development) and switch between Mode 1 Quick Patches and Mode 2 Feature Sprints depending on what needs doing. The lifecycle is the map. The mode is the vehicle.

---

## Mode Selection Table

| Situation | Mode | Lifecycle Phase |
|-----------|------|-----------------|
| Starting a brand-new project | Phase 1 Kickoff (pre-mode) | Phase 1 |
| Building the first working feature | Mode 2 — Feature Sprint | Phase 2 |
| Adding a new feature | Mode 2 — Feature Sprint | Phase 5 |
| Fixing a bug or small config change | Mode 1 — Quick Patch | Phase 7 |
| Upgrading a dependency or migrating data | Mode 3 — Refactor/Migration | Phase 7 |
| Parsing raw data files or mapping a new API | Mode 4 — Data Ingestion | Phase 1 or 5 |
| Enforcing code style across new files | Mode 5 — Style Audit | Phase 5 or 7 |
| Running two non-overlapping features at once | Parallel Sprints | Phase 5 |
| Returning to a paused project | Phase 8 Resumption (pre-mode) | Phase 8 |

---

## Mode Pages

- [Mode 1: Quick Patch](quick-patch.md) — Typo fixes, minor UI adjustments, single-function changes
- [Mode 2: Feature Sprint](feature-sprint.md) — New features, new routes, new integrations
- [Mode 3: Refactor / Migration](refactor-migration.md) — Database migrations, major dependency upgrades
- [Mode 4: Data Ingestion / Discovery](data-ingestion.md) — Parsing spreadsheets, mapping APIs, ETL pipelines
- [Mode 5: Style Audit](style-audit.md) — Enforcing STYLE_GUIDE.md conventions across files
- [Parallel Sprints](parallel-sprints.md) — Two non-overlapping feature sprints running simultaneously

## See Also

- [The 8-Step Lifecycle](../lifecycle/index.md)
- [Sprint Workflow](../sprint-workflow.md)
- [Core Concepts](../core-concepts.md)
