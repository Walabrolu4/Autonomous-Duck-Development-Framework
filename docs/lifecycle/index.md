[Home](../index.md) → [Lifecycle](index.md)

# The 8-Step Lifecycle: Overview

## What the Lifecycle Is

The 8-step lifecycle is the central organizing spine of the framework. It describes the phases of a project from idea to production. For a new project, the steps are sequential. After Step 7, loop back to Step 2 for the next feature cycle. Step 8 can happen at any point when returning to a paused project.

**The lifecycle is the map. The mode is the vehicle.** The lifecycle tells you which phase of the project you are in. An [Operating Mode](../modes/index.md) tells you how to approach the specific task in front of you right now. A project in Phase 5 (Full-Scale Development) typically runs Mode 2 Feature Sprints. A project in Phase 7 (Deployment) might run Mode 1 Quick Patches.

---

## The 8 Steps at a Glance

The lifecycle moves from idea to architecture, then prototype, testing, documentation, feature expansion, reflection, deployment, and later resumption.

| Step | Name | Key Files Produced or Consumed |
|------|------|-------------------------------|
| 1 | [Research & Global Architecture](01-research.md) | DOMAIN.md, AGENTS.md, STATE.md, DECISIONS.md, QUESTIONS.md, RISKS.md, docs/architecture.md |
| 2 | [Initial Development](02-initial-development.md) | requirements.md, blueprint.md, acceptance.md, source files |
| 3 | [Testing](03-testing.md) | acceptance.md, implementation_log.md, test output |
| 4 | [Documentation](04-documentation.md) | docs/data_model.md, docs/api.md, DECISIONS.md |
| 5 | [Full-Scale Development](05-full-scale-development.md) | STATE.md, sprint folders (repeating) |
| 6 | [Reflection Loop](06-reflection-loop.md) | retrospective.md, AGENTS.md, planning/backlog.md |
| 7 | [Deployment & Maintenance](07-deployment.md) | COMMANDS.md, RISKS.md, rollback_log.md |
| 8 | [Resumption](08-resumption.md) | STATE.md, DOMAIN.md, AGENTS.md |

---

## Lifecycle × Mode Mapping

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

## Step Pages

- [Step 1: Research & Global Architecture](01-research.md)
- [Step 2: Initial Development](02-initial-development.md)
- [Step 3: Testing](03-testing.md)
- [Step 4: Documentation](04-documentation.md)
- [Step 5: Full-Scale Development](05-full-scale-development.md)
- [Step 6: The Reflection Loop](06-reflection-loop.md)
- [Step 7: Deployment & Maintenance](07-deployment.md)
- [Step 8: Resumption](08-resumption.md)

## See Also

- [Operating Modes](../modes/index.md)
- [Sprint Workflow](../sprint-workflow.md)
- [Core Concepts](../core-concepts.md)
