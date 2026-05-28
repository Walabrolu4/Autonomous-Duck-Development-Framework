# Sprint 001 — Blueprint

**Sprint:** 001  
**Title:** Repository skeleton and project brain  
**Mode:** Design Mode  
**Permission Level:** N/A — this sprint contains no Develop Mode work.  
**Primary reference:** `planning/sprints/sprint_001/requirements.md`

This blueprint lists every file to be created or modified in Sprint 001. No file outside this list may be changed during this sprint.

---

## Files to create

### Root project brain files

| File | Purpose |
|---|---|
| `AGENTS.md` | Session operating rules. Defines three modes, dry run approval rule, permission levels, safe-to-load files, session opening protocol. |
| `DOMAIN.md` | Project scope, entities, terminology, v0.1 boundary, core framework concepts, domain rules. |
| `DECISIONS.md` | Durable decisions. Includes Decision 001 (Dogfood ADDF) from requirements §20.3. |
| `COMMANDS.md` | Project commands: setup, documentation, website (v0.2 stubs), CLI (v0.3 stubs), release packaging, git, validation, rollback. |
| `QUESTIONS.md` | All ten open questions from requirements §24. Format: numbered Q001–Q010, each with blocking information. |
| `RISKS.md` | Project-specific risks with severity, probability, status, and mitigation. Minimum 7 risks. |
| `STYLE_GUIDE.md` | Project brain style quick reference. Covers voice, banned words, canonical terminology, file naming, document structure. Points to full brand guide. |
| `GIT_STRATEGY.md` | Branch model, naming conventions, Conventional Commits, PR process, release process, merge strategy. |
| `PROMPT_CHANGELOG.md` | Prompt catalog version history. Lists all 25 prompts planned for v0.1 grouped by five categories. Defines breaking change conventions. |
| `START_HERE.md` | First-session guide. Exactly 15 numbered steps from requirements §3.2 and §8.4. |
| `VERSION.md` | Artifact version registry covering all versioned components. |
| `CHANGELOG.md` | Project changelog in Keep a Changelog format. Contains [Unreleased] and [0.0.1] entries. |

### Planning structure

| File | Purpose |
|---|---|
| `planning/backlog.md` | Complete list of all sprints across all releases. Includes v0.1 sprints (001–009), v0.2 website sprints (004–006), v0.3 CLI sprint (010), v0.4 onboarding sprint (011), and v0.5 expanded examples. |
| `planning/releases/v0.1/release_plan.md` | v0.1 release goal, success criteria, sprint breakdown, unscheduled work, dependencies, release process. |
| `planning/releases/v0.1/scope.md` | Authoritative in-scope and out-of-scope lists for v0.1. |
| `planning/releases/v0.1/release_notes.md` | Placeholder only. Content written at v0.1 release time. |
| `planning/sprints/sprint_001/requirements.md` | Sprint goal, context, in scope, out of scope, constraints, success criteria pointer. |
| `planning/sprints/sprint_001/blueprint.md` | This file. Complete file creation and modification list. |
| `planning/sprints/sprint_001/acceptance.md` | Human-verifiable acceptance checklist. |
| `planning/sprints/sprint_001/consistency_audit.md` | Design Mode audit of the 12 generated project brain files. Produced mid-sprint. |

---

## Files to modify

| File | Section(s) changed | Reason |
|---|---|---|
| `docs/_PDF/style Guide/STYLE_GUIDE.md` | §2.4 (framing), §11.1 (vocabulary table), §11.3 (words to avoid), §12.1 (button examples), §20 (glossary) | Decision 002: Replace Architect Mode / Builder Mode with Research Mode, Design Mode, Develop Mode as canonical public terms. |

---

## Files not in scope

These files exist in the repository but must not be changed during this sprint:

| File | Reason |
|---|---|
| `README.md` | Pre-existing seed. Content review is out of scope. |
| `STATE.md` | Updated when the sprint closes, not during implementation. |
| `SECURITY.md` | Pre-existing seed. Already correct. |
| `docs/` (all other files) | Wiki seed files. Out of scope except for the STYLE_GUIDE correction listed above. |
| `todos/` | Requirements documents. Read-only reference. |

---

## No implementation files

This sprint produces no source code, no website files, no CLI scripts, and no build assets. All outputs are Markdown files. No Develop Mode dry run is required.

---

## Design review note

A consistency audit was produced mid-sprint at `planning/sprints/sprint_001/consistency_audit.md`. It identified 4 issues in `AGENTS.md` (A1–A4), 2 issues in `DOMAIN.md` (D1–D2), 1 warning about the pre-existing brand guide (S1), and 1 warning in `CHANGELOG.md` (C1). All issues were corrected before the sprint was marked ready for acceptance review.

---

*ADDF · `planning/sprints/sprint_001/blueprint.md`*
