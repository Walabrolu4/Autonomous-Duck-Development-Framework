# Docs_List.md

> The complete inventory of wiki pages to be created for the ADDF documentation site.
> Every page listed here corresponds to one or more todos in `Docs_Todo.md`.

**Based on:** ADDF v3.5 / v3.6, `STYLE_GUIDE.md`, `README.md`, `todos/ADDF_Full_Project_Requirements.md`  
**Wiki root:** `docs/`  
**Last updated:** 2026-05-25

---

## How to read this list

- **Path** — the file path relative to the repo root.
- **Title** — the H1 heading for the page.
- **Purpose** — one sentence on what it does for the reader.
- **Source** — which section(s) of the source documents to draw from.
- **Links to** — pages this page should link out to.
- **Linked from** — pages that should link in to this page.

---

## Section 1 — Root & Navigation

### 1.1 Wiki Home

| Field | Value |
|---|---|
| **Path** | `docs/index.md` |
| **Title** | ADDF Wiki |
| **Purpose** | The root of the wiki — explains the framework in a sentence and provides a complete navigation table to every section. |
| **Source** | `README.md` documentation table; v3.5 §1 Purpose, §3 Framework summary |
| **Links to** | All pages in this list |
| **Linked from** | `README.md`; every wiki page footer |

---

## Section 2 — Getting Started

### 2.1 Getting Started

| Field | Value |
|---|---|
| **Path** | `docs/getting-started.md` |
| **Title** | Getting Started |
| **Purpose** | Answers "I downloaded this — what do I do in the next 20 minutes?" with a numbered first-session walkthrough. |
| **Source** | v3.5 §17 Initial setup, §23 Operational checklists, §9 Project brain (core files) |
| **Links to** | `docs/core-concepts.md`, `docs/modes/index.md`, `docs/project-brain.md`, `docs/prompt-catalog.md`, `docs/file-reference.md` |
| **Linked from** | `docs/index.md`, `README.md` |

---

## Section 3 — Core Concepts

### 3.1 Core Concepts

| Field | Value |
|---|---|
| **Path** | `docs/core-concepts.md` |
| **Title** | Core Concepts |
| **Purpose** | Defines the four separations ADDF makes (scale, lifecycle, mode, project memory) and the six core principles in plain language. |
| **Source** | v3.5 §3 Framework summary, §4 Core principles |
| **Links to** | `docs/work-scale.md`, `docs/lifecycle/index.md`, `docs/modes/index.md`, `docs/project-brain.md` |
| **Linked from** | `docs/index.md`, `docs/getting-started.md` |

---

## Section 4 — The 8-Step Lifecycle

### 4.1 Lifecycle Overview

| Field | Value |
|---|---|
| **Path** | `docs/lifecycle/index.md` |
| **Title** | The 8-Step ADDF Lifecycle |
| **Purpose** | Explains all eight lifecycle steps — from Research through Deploy/Maintain/Resume — with entry/exit criteria and mode mapping for each. |
| **Source** | v3.5 §7 The 8-step ADDF lifecycle, §8 How scale, lifecycle, and modes interlock |
| **Links to** | `docs/modes/index.md`, `docs/work-scale.md`, `docs/sprint-loop.md`, `docs/project-brain.md` |
| **Linked from** | `docs/index.md`, `docs/core-concepts.md`, `README.md` |
| **Image** | `_PDF/images/5_8-Step Lifecycle.png`, `_PDF/images/4_Scale  Lifecycle  Mode interlock.png` |

---

## Section 5 — Operating Modes

### 5.1 Modes Overview

| Field | Value |
|---|---|
| **Path** | `docs/modes/index.md` |
| **Title** | Operating Modes |
| **Purpose** | Introduces all three modes, explains the mode-boundary table, and links to the deep-dive page for each. |
| **Source** | v3.5 §5 The three operating modes (intro + §5.4 Mode boundaries) |
| **Links to** | `docs/modes/research-mode.md`, `docs/modes/design-mode.md`, `docs/modes/develop-mode.md`, `docs/permission-levels.md` |
| **Linked from** | `docs/index.md`, `docs/core-concepts.md`, `docs/lifecycle/index.md`, `README.md` |
| **Image** | `_PDF/images/2_Three Operating Modes.png` |

### 5.2 Research Mode

| Field | Value |
|---|---|
| **Path** | `docs/modes/research-mode.md` |
| **Title** | Research Mode |
| **Purpose** | Deep-dive on what Research Mode investigates, what it may produce, and what it must never do. Includes the Research Mode prompt. |
| **Source** | v3.5 §5.1 Research Mode, §7.1 Research lifecycle step, §19.1 Research Mode prompt |
| **Links to** | `docs/modes/index.md`, `docs/modes/design-mode.md`, `docs/prompt-catalog.md` |
| **Linked from** | `docs/modes/index.md` |

### 5.3 Design Mode

| Field | Value |
|---|---|
| **Path** | `docs/modes/design-mode.md` |
| **Title** | Design Mode |
| **Purpose** | Deep-dive on Design Mode — what it writes, what it reviews, what it never touches. Includes a note mapping the older "Architect Mode" name. |
| **Source** | v3.5 §5.2 Design Mode, §7.2–7.5 lifecycle steps, §19.2 §19.3 §19.5 §19.7 prompts |
| **Links to** | `docs/modes/index.md`, `docs/modes/research-mode.md`, `docs/modes/develop-mode.md`, `docs/prompt-catalog.md`, `docs/project-brain.md` |
| **Linked from** | `docs/modes/index.md` |

### 5.4 Develop Mode

| Field | Value |
|---|---|
| **Path** | `docs/modes/develop-mode.md` |
| **Title** | Develop Mode |
| **Purpose** | Deep-dive on Develop Mode — implementation constraints, dry run requirement, verification rules, and permission levels. Includes a note mapping the older "Builder Mode" name. |
| **Source** | v3.5 §5.3 Develop Mode, §13 Permission levels, §7.6 Build & test lifecycle step, §19.4 §19.6 prompts |
| **Links to** | `docs/modes/index.md`, `docs/permission-levels.md`, `docs/sprint-loop.md`, `docs/prompt-catalog.md` |
| **Linked from** | `docs/modes/index.md` |
| **Image** | `_PDF/images/8_Dry Run Approval Gate.png` |

---

## Section 6 — Work Scale

### 6.1 Work Scale Model

| Field | Value |
|---|---|
| **Path** | `docs/work-scale.md` |
| **Title** | Work Scale Model |
| **Purpose** | Defines the five work scales (Project → Release → Feature → Sprint → Patch), what each requires in terms of process, and the scale-to-process mapping table. |
| **Source** | v3.5 §6 Work scale model |
| **Links to** | `docs/lifecycle/index.md`, `docs/sprint-loop.md`, `docs/release-cycles.md`, `docs/feature-cycles.md` |
| **Linked from** | `docs/index.md`, `docs/core-concepts.md`, `docs/lifecycle/index.md` |
| **Image** | `_PDF/images/3_Work Scale Model.png` |

---

## Section 7 — Sprint Workflow

### 7.1 Sprint Loop

| Field | Value |
|---|---|
| **Path** | `docs/sprint-loop.md` |
| **Title** | Sprint Loop |
| **Purpose** | The 11-step controlled implementation workflow — from pre-flight gate through commit, update, and reset. Includes the dry run approval gate detail. |
| **Source** | v3.5 §12 Sprint loop |
| **Links to** | `docs/modes/develop-mode.md`, `docs/permission-levels.md`, `docs/project-brain.md`, `docs/checklists.md` |
| **Linked from** | `docs/index.md`, `docs/lifecycle/index.md`, `docs/work-scale.md`, `README.md` (as `sprint-workflow.md`) |
| **Note** | README references this as `docs/sprint-workflow.md` — the file should be named `docs/sprint-loop.md` but an alias or note in `index.md` should bridge the gap. |
| **Image** | `_PDF/images/7_Sprint Loop.png`, `_PDF/images/8_Dry Run Approval Gate.png` |

---

## Section 8 — The Project Brain

### 8.1 Project Brain

| Field | Value |
|---|---|
| **Path** | `docs/project-brain.md` |
| **Title** | The Project Brain |
| **Purpose** | The complete reference for the file-backed memory layer — all core files, sprint files, and release/feature files with their responsibilities. |
| **Source** | v3.5 §9 The project brain (§9.1–9.4) |
| **Links to** | `docs/file-reference.md`, `docs/modes/design-mode.md`, `docs/getting-started.md` |
| **Linked from** | `docs/index.md`, `docs/core-concepts.md`, `docs/getting-started.md` |
| **Image** | `_PDF/images/6_Project Brain file map.png` |

---

## Section 9 — File Reference

### 9.1 File Reference

| Field | Value |
|---|---|
| **Path** | `docs/file-reference.md` |
| **Title** | File Reference |
| **Purpose** | Template and purpose for every project brain file — AGENTS.md, STATE.md, DOMAIN.md, DECISIONS.md, and the full Sprint Pack. |
| **Source** | v3.5 §18 File templates, §9.4 File responsibilities table |
| **Links to** | `docs/project-brain.md`, `docs/sprint-loop.md` |
| **Linked from** | `docs/index.md`, `docs/getting-started.md`, `docs/project-brain.md`, `README.md` (as `docs/file-reference/index.md`) |
| **Note** | README links to `docs/file-reference/index.md` — this single-file approach should redirect or the index note in `docs/index.md` should clarify. |

---

## Section 10 — Prompt Catalog

### 10.1 Prompt Catalog

| Field | Value |
|---|---|
| **Path** | `docs/prompt-catalog.md` |
| **Title** | Prompt Catalog |
| **Purpose** | All copy-paste prompts grouped by mode — Research, Design, Develop, and Resumption — with full prompt text and context for each. |
| **Source** | v3.5 §19 Prompt catalog (§19.1–19.7) |
| **Links to** | `docs/modes/research-mode.md`, `docs/modes/design-mode.md`, `docs/modes/develop-mode.md`, `docs/handoff-protocol.md` |
| **Linked from** | `docs/index.md`, `docs/getting-started.md`, `README.md` (as `docs/prompts.md`) |
| **Note** | README links to `docs/prompts.md` — bridge this in `docs/index.md` navigation. |

---

## Section 11 — Handoff & Resumption

### 11.1 Handoff Protocol

| Field | Value |
|---|---|
| **Path** | `docs/handoff-protocol.md` |
| **Title** | Handoff, Resumption & Model Switching |
| **Purpose** | How to checkpoint a session, produce a handoff summary, and onboard an incoming model from files alone — no prior chat required. |
| **Source** | v3.5 §14 Handoff, resumption, and model switching (§14.1–14.3), §19.7 Resumption prompt |
| **Links to** | `docs/project-brain.md`, `docs/prompt-catalog.md`, `docs/modes/develop-mode.md` |
| **Linked from** | `docs/index.md`, `docs/lifecycle/index.md` |
| **Image** | `_PDF/images/9_Handoff and Resumption.png` |

---

## Section 12 — Repository Structure

### 12.1 Repository Structure

| Field | Value |
|---|---|
| **Path** | `docs/repository-structure.md` |
| **Title** | Repository Structure |
| **Purpose** | Three repo layouts — standard ADDF project, minimum viable ADDF, and the public ADDF repo — with annotated folder trees. |
| **Source** | v3.5 §16 Repository structure |
| **Links to** | `docs/project-brain.md`, `docs/initial-setup.md`, `docs/work-scale.md` |
| **Linked from** | `docs/index.md`, `docs/initial-setup.md` |
| **Image** | `_PDF/images/12_Repository structure.png` |

---

## Section 13 — Initial Setup

### 13.1 Initial Setup

| Field | Value |
|---|---|
| **Path** | `docs/initial-setup.md` |
| **Title** | Initial Setup |
| **Purpose** | Bash commands to create the project scaffold, the correct order to populate files, and how to structure the first AI session. |
| **Source** | v3.5 §17 Initial setup |
| **Links to** | `docs/getting-started.md`, `docs/repository-structure.md`, `docs/file-reference.md`, `docs/prompt-catalog.md` |
| **Linked from** | `docs/index.md`, `docs/getting-started.md`, `docs/repository-structure.md` |
| **Image** | `_PDF/images/10_First-session onboarding flow.png` |

---

## Section 14 — Permission Levels

### 14.1 Permission Levels

| Field | Value |
|---|---|
| **Path** | `docs/permission-levels.md` |
| **Title** | Develop Mode Permission Levels |
| **Purpose** | The 0–4 permission level scale — what each level allows, when to use it, and the rules around escalation. |
| **Source** | v3.5 §13 Develop Mode permission levels |
| **Links to** | `docs/modes/develop-mode.md`, `docs/sprint-loop.md`, `docs/checklists.md` |
| **Linked from** | `docs/modes/develop-mode.md`, `docs/modes/index.md`, `docs/sprint-loop.md` |

---

## Section 15 — Release & Feature Cycles

### 15.1 Release Cycles

| Field | Value |
|---|---|
| **Path** | `docs/release-cycles.md` |
| **Title** | Release Cycles |
| **Purpose** | How to plan, track, and complete a versioned release — the release plan, folder structure, starting a new version, and completion criteria. |
| **Source** | v3.5 §10 Release cycles |
| **Links to** | `docs/work-scale.md`, `docs/feature-cycles.md`, `docs/project-brain.md` |
| **Linked from** | `docs/index.md`, `docs/work-scale.md` |

### 15.2 Feature Cycles

| Field | Value |
|---|---|
| **Path** | `docs/feature-cycles.md` |
| **Title** | Feature Cycles |
| **Purpose** | The feature cycle flow, folder structure, and feature brief template for adding a capability to an existing project. |
| **Source** | v3.5 §11 Feature cycles |
| **Links to** | `docs/work-scale.md`, `docs/release-cycles.md`, `docs/sprint-loop.md` |
| **Linked from** | `docs/index.md`, `docs/work-scale.md`, `docs/release-cycles.md` |

---

## Section 16 — Domain Adaptations

### 16.1 Domain Adaptations

| Field | Value |
|---|---|
| **Path** | `docs/domain-adaptations.md` |
| **Title** | Domain Adaptations |
| **Purpose** | Shows how ADDF adapts to web apps, game development, desktop apps, data/automation, and documentation/framework projects without changing its structure. |
| **Source** | v3.5 §20 Domain adaptations |
| **Links to** | `docs/project-brain.md`, `docs/file-reference.md`, `docs/examples.md` |
| **Linked from** | `docs/index.md` |

---

## Section 17 — Examples

### 17.1 Examples Overview

| Field | Value |
|---|---|
| **Path** | `docs/examples.md` |
| **Title** | Examples |
| **Purpose** | Walkthrough of the Mini Task Tracker and ADDF public repository examples — showing scale, lifecycle, and modes in practice. |
| **Source** | v3.5 §21 Mini Task Tracker, §22 ADDF public repository |
| **Links to** | `docs/lifecycle/index.md`, `docs/work-scale.md`, `docs/modes/index.md`, `docs/sprint-loop.md` |
| **Linked from** | `docs/index.md`, `README.md` (as `docs/example.md`) |
| **Note** | README links to `docs/example.md` (singular). Use `docs/examples.md` and add an alias note in `docs/index.md`. |
| **Image** | `_PDF/images/15_Mini Task Tracker scale example.png`, `_PDF/images/14_Public roadmap.png` |

---

## Section 18 — Operational Reference

### 18.1 Operational Checklists

| Field | Value |
|---|---|
| **Path** | `docs/checklists.md` |
| **Title** | Operational Checklists |
| **Purpose** | The four gate checklists — before first AI session, before Develop Mode, before authorizing development, and before commit. |
| **Source** | v3.5 §23 Operational checklists |
| **Links to** | `docs/sprint-loop.md`, `docs/modes/develop-mode.md`, `docs/permission-levels.md`, `docs/project-brain.md` |
| **Linked from** | `docs/index.md`, `docs/sprint-loop.md`, `docs/getting-started.md` |

### 18.2 Failure Handling

| Field | Value |
|---|---|
| **Path** | `docs/troubleshooting.md` |
| **Title** | Failure Handling & Troubleshooting |
| **Purpose** | Four failure recovery procedures — unapproved file edits, invented business logic, confused project state, and context exhaustion — with step-by-step actions. |
| **Source** | v3.5 §24 Failure handling |
| **Links to** | `docs/project-brain.md`, `docs/modes/develop-mode.md`, `docs/handoff-protocol.md` |
| **Linked from** | `docs/index.md`, `README.md` (as `docs/troubleshooting.md`) |

---

## Section 19 — Reference Pages

### 19.1 Agile Comparison

| Field | Value |
|---|---|
| **Path** | `docs/agile-comparison.md` |
| **Title** | ADDF and Agile |
| **Purpose** | Explains what ADDF borrows from Agile/Scrum and what it deliberately does not require — with the term mapping table. |
| **Source** | v3.5 §15 Relationship to Agile and Scrum |
| **Links to** | `docs/work-scale.md`, `docs/sprint-loop.md` |
| **Linked from** | `docs/index.md`, `docs/core-concepts.md` |

### 19.2 Glossary

| Field | Value |
|---|---|
| **Path** | `docs/glossary.md` |
| **Title** | Glossary |
| **Purpose** | Definitions for all canonical ADDF terms, from ADDF through Validation Gate. |
| **Source** | v3.5 §25 Glossary, `STYLE_GUIDE.md` §11 Vocabulary, §20 Glossary |
| **Links to** | Relevant deep-dive pages for each term |
| **Linked from** | `docs/index.md`, `README.md`, every page footer (optional) |

---

## Summary — Complete Page Count

| # | Path | Section |
|---|---|---|
| 1 | `docs/index.md` | Root & Navigation |
| 2 | `docs/getting-started.md` | Getting Started |
| 3 | `docs/core-concepts.md` | Core Concepts |
| 4 | `docs/lifecycle/index.md` | 8-Step Lifecycle |
| 5 | `docs/modes/index.md` | Modes Overview |
| 6 | `docs/modes/research-mode.md` | Research Mode |
| 7 | `docs/modes/design-mode.md` | Design Mode |
| 8 | `docs/modes/develop-mode.md` | Develop Mode |
| 9 | `docs/work-scale.md` | Work Scale Model |
| 10 | `docs/sprint-loop.md` | Sprint Loop |
| 11 | `docs/project-brain.md` | Project Brain |
| 12 | `docs/file-reference.md` | File Reference |
| 13 | `docs/prompt-catalog.md` | Prompt Catalog |
| 14 | `docs/handoff-protocol.md` | Handoff & Resumption |
| 15 | `docs/repository-structure.md` | Repository Structure |
| 16 | `docs/initial-setup.md` | Initial Setup |
| 17 | `docs/permission-levels.md` | Permission Levels |
| 18 | `docs/release-cycles.md` | Release Cycles |
| 19 | `docs/feature-cycles.md` | Feature Cycles |
| 20 | `docs/domain-adaptations.md` | Domain Adaptations |
| 21 | `docs/examples.md` | Examples |
| 22 | `docs/checklists.md` | Operational Checklists |
| 23 | `docs/troubleshooting.md` | Failure Handling |
| 24 | `docs/agile-comparison.md` | Agile Comparison |
| 25 | `docs/glossary.md` | Glossary |

**Total: 25 pages**

---

*ADDF · `docs/Docs_List.md` · generated 2026-05-25*
