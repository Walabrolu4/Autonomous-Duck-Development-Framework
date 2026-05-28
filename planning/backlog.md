# Backlog

**Project:** Autonomous Duck Deployment Framework — Public Repository  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md`

This file is the single list of all planned, in-progress, and completed sprint work across every release. Update it when a sprint opens, closes, or is re-scoped.

---

## Status key

| Symbol | Meaning |
|---|---|
| `[ACTIVE]` | Currently in progress. |
| `[DONE]` | Sprint closed and accepted. |
| `[READY]` | Sprint pack written, ready to start. |
| `[PLANNED]` | Sequenced and scoped. Sprint pack not yet written. |
| `[FUTURE]` | Assigned to a release but not yet sequenced. |
| `[UNSCHEDULED]` | Identified but release assignment not confirmed. |

---

## v0.1 — Public Proof

**Goal:** A competent operator can understand ADDF, download the starter kit, and run the first session manually.

### Sprint 001 — Repository skeleton and project brain

**Status:** `[ACTIVE]`  
**Branch:** `sprint/001-repository-skeleton`  
**Sprint pack:** `planning/sprints/sprint_001/`

Generate all project brain files, apply terminology corrections, and create the foundational planning structure. This sprint is Design Mode only.

---

### Sprint 002 — Starter kit

**Status:** `[PLANNED]`  
**Sprint pack:** Not yet written.

Create `starter-kit/blank/` and `starter-kit/example-filled/`. The blank kit contains all project brain templates with placeholders. The example-filled variant uses the Mini Task Tracker project. The kit must be downloadable as a ZIP.

Key reference: Requirements §10.

---

### Sprint 003 — Prompt catalog

**Status:** `[PLANNED]`  
**Sprint pack:** Not yet written.

Create all prompt files grouped into five folders: Research, Design, Develop, Handoff/Resumption, Maintenance. Each prompt must declare its mode, list files to load, and define expected output.

Key reference: Requirements §11.

---

### Sprint 007 — Example project (Mini Task Tracker)

**Status:** `[PLANNED]`  
**Sprint pack:** Not yet written.

Create the complete `examples/mini-task-tracker/` directory. The example must demonstrate Project, Release, Feature, and Sprint scale, and include dry run, implementation log, human review, and retrospective files.

Key reference: Requirements §12.

---

### Sprint 008 — Handoff and resumption package

**Status:** `[PLANNED]`  
**Sprint pack:** Not yet written.

Create `docs/handoff-protocol.md` and all prompts in `prompts/handoff/`. The protocol must be copy-ready and model-agnostic. At least one actual handoff scenario must be tested.

Key reference: Requirements §3.5, §11.3 (Handoff prompts).

---

### Sprint 009 — Release package

**Status:** `[PLANNED]`  
**Sprint pack:** Not yet written.

Prepare the v0.1.0 release: update version numbers, finalize CHANGELOG.md, generate release ZIPs (starter kit, prompt catalog, examples), produce the full manual PDF, and write GitHub release notes.

Key reference: Requirements §17.

---

### Unscheduled v0.1 work items

These items are in scope for v0.1 but are not yet assigned to a sprint number. Assign them before Sprint 002 starts.

| Item | Notes |
|---|---|
| Full framework manual Markdown (`docs/full-manual.md`) | Consolidates existing docs/ seed files into one reference document. Assign to Sprint 003 or a new Sprint 003a. |
| Full framework manual PDF | Derived from Markdown. Part of Sprint 009 (release package). |
| 15 core framework diagrams (`assets/diagrams/`) | Requires visual asset production. Assign to a dedicated sprint or sprint 008/009. |
| `assets/logo/` — final files | Duck logo assets. Confirm SVG readiness and assign. |
| `assets/lifecycle/` — lifecycle diagram image | Single image for the lifecycle. Part of diagrams sprint. |
| `LICENSE` | License decision (see `QUESTIONS.md` Q001) must be resolved first. Add to Sprint 001 close or Sprint 002. |
| `CONTRIBUTING.md` | Contribution guidelines. Assign to Sprint 002 or Sprint 009. |
| `CODE_OF_CONDUCT.md` | Standard conduct file. Assign to Sprint 002 or Sprint 009. |

---

## v0.2 — Website

**Goal:** A visitor can learn and download from a clean public site.

### Sprint 004 — Website information architecture

**Status:** `[FUTURE]`

Design the website structure and page content plan. No website implementation. Outputs: `website/README.md`, `docs/site-map.md`, `docs/page-blueprints.md`.

---

### Sprint 005 — Website MVP

**Status:** `[FUTURE]`

Build the first public website: homepage, Start Here page, downloads page, and assets. Static site only.

---

### Sprint 006 — Documentation pages

**Status:** `[FUTURE]`

Build core documentation pages: Framework, Scale Model, Lifecycle, Modes, Project Brain, Starter Kit, Prompt Catalog, Examples.

---

## v0.3 — CLI Init Tool

**Goal:** An operator can generate ADDF starter files from a guided command.

### Sprint 010 — CLI init tool prototype

**Status:** `[FUTURE]`

Build `tools/addf-init/`. Tool must generate minimal and full ADDF structure, support project-type presets, and print the next Design Mode prompt. No LLM calls by default.

Key reference: Requirements §13.

---

## v0.4 — Web Onboarding App

**Goal:** An operator can generate ADDF starter files without using a CLI.

### Sprint 011 — Web onboarding app prototype

**Status:** `[FUTURE]`

Build `website/onboarding/`. Browser-based questionnaire, file preview, ZIP download. No login, no data storage.

Key reference: Requirements §14.

---

## v0.5 — Expanded Examples

**Goal:** Operators from multiple domains can see how ADDF adapts.

| Sprint | Example type | Status |
|---|---|---|
| TBD | Web app example | `[UNSCHEDULED]` |
| TBD | Game project example | `[UNSCHEDULED]` |
| TBD | Data ingestion example | `[UNSCHEDULED]` |
| TBD | Documentation/framework example | `[UNSCHEDULED]` |

---

## Completed sprints

| Sprint | Name | Release | Closed |
|---|---|---|---|
| — | — | — | — |

*(Table will be updated as sprints close.)*

---

*ADDF · `planning/backlog.md` · maintained by Design Mode*
