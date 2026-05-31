# Sprint 002 — Dry Run

**Mode:** Develop Mode  
**Permission Level:** 0 — Dry Run Only  
**Sprint:** 002 — Starter Kit  
**Sprint pack reference:** `planning/sprints/sprint_002/requirements.md`, `blueprint.md`, `acceptance.md`  
**Date:** 2026-05-31

---

## 1. Files to create

83 new files across four phases. Listed in creation order per `blueprint.md`.

### Phase 1 — Supporting files

| # | File | Purpose |
|---|---|---|
| 1 | `starter-kit/README.md` | Root readme explaining both kit variants, how to use, minimum viable ADDF, license statement, version 0.1.0. |
| 2 | `LICENSE` | Official CC BY 4.0 license text. Required before v0.1 public release. |

### Phase 2 — Blank starter kit

| # | File | Purpose |
|---|---|---|
| 3 | `starter-kit/blank/AGENTS.md` | Complete session contract template: three modes, dry run rule (7-item), Step 5a dependency gate, authorization message, permission levels 0–4. All project-specific content uses `[YOUR PROJECT NAME]` placeholders. |
| 4 | `starter-kit/blank/DOMAIN.md` | Project scope template: identity, what-is/is-not, v0.1 scope, target users, key entities, domain rules. All placeholder content. Framework concepts pre-filled. |
| 5 | `starter-kit/blank/STATE.md` | Seven required fields with placeholder values and inline comments: Active Scale, Current Mode, Active Release, Active Feature, Active Sprint, Current Status, Next Step. |
| 6 | `starter-kit/blank/SECURITY.md` | Files-never-to-load list pre-populated with common secrets patterns. AI tools table. Session hygiene rules. |
| 7 | `starter-kit/blank/DECISIONS.md` | Template with instructions and one complete placeholder Decision 001 entry (all fields labelled). |
| 8 | `starter-kit/blank/QUESTIONS.md` | Template with instructions, one placeholder Q001 entry, and empty resolved questions section. |
| 9 | `starter-kit/blank/RISKS.md` | Three pre-written risk entries for terminology drift, secrets exposure, and scope creep. Third risk uses project name placeholder. |
| 10 | `starter-kit/blank/COMMANDS.md` | Four command sections (Setup, Development, Testing, Deployment), one placeholder entry each. |
| 11 | `starter-kit/blank/STYLE_GUIDE.md` | Voice rules, pre-populated banned words, canonical terminology table, file naming, no-emoji rule, brand guide pointer. |
| 12 | `starter-kit/blank/GIT_STRATEGY.md` | Pre-populated ADDF-standard branch model, naming patterns, Conventional Commits, PR checklist, release process skeleton, .gitignore minimums. |
| 13 | `starter-kit/blank/PROMPT_CHANGELOG.md` | Template with instructions, one placeholder prompt entry, breaking change convention. |
| 14 | `starter-kit/blank/START_HERE.md` | Exactly 15 numbered steps. Step 11 includes the authorization message verbatim. Version 0.1.0 visible. "Next sessions" section. |
| 15 | `starter-kit/blank/docs/architecture.md` | Four section headers with instructional placeholder text: Overview, Components, Data flow, Key decisions. |
| 16 | `starter-kit/blank/docs/data_model.md` | Four section headers with instructional placeholder text: Entities, Fields, Relationships, Constraints. |
| 17 | `starter-kit/blank/docs/api.md` | Five section headers with instructional placeholder text. Delete-if-no-API note. |
| 18 | `starter-kit/blank/docs/permissions.md` | Three section headers with instructional placeholder text. Delete-if-no-permissions note. |
| 19 | `starter-kit/blank/docs/validation.md` | Three section headers with instructional placeholder text: Input validation rules, Edge cases, Acceptance tests. |
| 20 | `starter-kit/blank/research/notes.md` | Research session template: question, date, mode, findings, open items. |
| 21 | `starter-kit/blank/research/sources.md` | Sources table with three placeholder rows (Source, URL, Date, Relevance, Key points). |
| 22 | `starter-kit/blank/research/open_questions.md` | Open questions table with three placeholder rows. Move-to-QUESTIONS.md instruction. |
| 23 | `starter-kit/blank/planning/backlog.md` | Status key table, three placeholder sprint entries, empty completed sprints table. |
| 24 | `starter-kit/blank/planning/releases/v0.1/release_plan.md` | Release goal, success criteria (5 items), sprint breakdown table, dependency table, release process (8 steps). |
| 25 | `starter-kit/blank/planning/releases/v0.1/scope.md` | In-scope table (5 rows), out-of-scope table (5 rows), scope change log with instructions. |
| 26 | `starter-kit/blank/planning/releases/v0.1/release_notes.md` | Placeholder with write-at-release-time instruction. Version and date fields. |
| 27 | `starter-kit/blank/planning/releases/v0.1/retrospective.md` | What worked, What needs attention, Rules added sections. Write-after-release instruction. |
| 28 | `starter-kit/blank/planning/features/_template/feature_brief.md` | Feature goal, impact, release, in/out-of-scope, dependencies, acceptance pointer. |
| 29 | `starter-kit/blank/planning/features/_template/research.md` | Research question, findings, open items, recommendation template. |
| 30 | `starter-kit/blank/planning/features/_template/feasibility.md` | Approach options table (3 rows), risks, recommendation, constraints. |
| 31 | `starter-kit/blank/planning/features/_template/validation.md` | Validation checklist (5 items), evidence required, verdict, follow-up items. |
| 32 | `starter-kit/blank/planning/features/_template/sprint_map.md` | Sprint breakdown table (3 rows), dependencies, estimated total sprints. |
| 33 | `starter-kit/blank/planning/sprints/sprint_001/requirements.md` | Sprint goal, context, in-scope table (5 rows), out-of-scope table (3 rows), constraints (2 items). |
| 34 | `starter-kit/blank/planning/sprints/sprint_001/blueprint.md` | Files-to-create (5 rows), files-to-modify (2 rows), files-not-in-scope (2 rows). |
| 35 | `starter-kit/blank/planning/sprints/sprint_001/blueprint_feedback.md` | Reviewer, date, section results table, overall verdict, conditions, notes. |
| 36 | `starter-kit/blank/planning/sprints/sprint_001/acceptance.md` | Three sections, 3 checkboxes each, all human-verifiable. Sprint-complete statement. |
| 37 | `starter-kit/blank/planning/sprints/sprint_001/dry_run.md` | Seven numbered sections matching 7-item definition. Stop instruction at bottom. |
| 38 | `starter-kit/blank/planning/sprints/sprint_001/dry_run_review.md` | Seven section verdicts, overall verdict, conditions, authorization message template. |
| 39 | `starter-kit/blank/planning/sprints/sprint_001/implementation_log.md` | Phase table, user actions section, files-not-modified section, summary table. |
| 40 | `starter-kit/blank/planning/sprints/sprint_001/human_review.md` | Three section results, additional observations, follow-up table, overall decision block, signature. |
| 41 | `starter-kit/blank/planning/sprints/sprint_001/retrospective.md` | What worked, what needs attention, constraints added, rules, next sprint. |
| 42 | `starter-kit/blank/planning/sprints/sprint_001/rollback_log.md` | Instructions, table with placeholder rows, fill-only-if-rollback-occurred note. |

### Phase 3 — Example-filled starter kit

| # | File | Purpose |
|---|---|---|
| 43 | `starter-kit/example-filled/mini-task-tracker/AGENTS.md` | Blank AGENTS.md with all placeholders replaced for Mini Task Tracker. |
| 44 | `starter-kit/example-filled/mini-task-tracker/DOMAIN.md` | Filled: local-only web app, localStorage persistence, single operator, task CRUD scope. |
| 45 | `starter-kit/example-filled/mini-task-tracker/STATE.md` | Filled: Sprint scale, Sprint 001 closed, next step defined. |
| 46 | `starter-kit/example-filled/mini-task-tracker/SECURITY.md` | Standard pre-populated rules. One AI tools row: Claude (Anthropic). |
| 47 | `starter-kit/example-filled/mini-task-tracker/DECISIONS.md` | Three filled decisions: localStorage persistence, single-file HTML, no build tool. |
| 48 | `starter-kit/example-filled/mini-task-tracker/QUESTIONS.md` | One open question (archive vs delete for completed tasks). One resolved question (use a framework: No). |
| 49 | `starter-kit/example-filled/mini-task-tracker/RISKS.md` | Three filled risks: localStorage size limit, data loss on clear, scope creep to server. |
| 50 | `starter-kit/example-filled/mini-task-tracker/COMMANDS.md` | Setup: `open index.html`. Dev: `open index.html`. Test: `open index.html`. Deploy: None — local only. |
| 51 | `starter-kit/example-filled/mini-task-tracker/STYLE_GUIDE.md` | Filled terminology: Task, TaskList, Complete. File naming and voice rules filled. |
| 52 | `starter-kit/example-filled/mini-task-tracker/GIT_STRATEGY.md` | Pre-populated template with MTT-specific release steps. |
| 53 | `starter-kit/example-filled/mini-task-tracker/PROMPT_CHANGELOG.md` | One entry: v0.1.0, standard ADDF prompts, no modifications. |
| 54 | `starter-kit/example-filled/mini-task-tracker/START_HERE.md` | 15 steps with Mini Task Tracker placeholders replaced. Version 0.1.0 visible. |
| 55 | `starter-kit/example-filled/mini-task-tracker/docs/architecture.md` | Filled: single-page app, HTML/CSS/JS, localStorage, no backend. |
| 56 | `starter-kit/example-filled/mini-task-tracker/docs/data_model.md` | Filled: Task entity with id, title, status, created_at fields. |
| 57 | `starter-kit/example-filled/mini-task-tracker/docs/api.md` | No-API note. Sections empty. |
| 58 | `starter-kit/example-filled/mini-task-tracker/docs/permissions.md` | Single-operator note. Sections empty. |
| 59 | `starter-kit/example-filled/mini-task-tracker/docs/validation.md` | Filled: title required, max 200 chars, whitespace-only rejected. |
| 60 | `starter-kit/example-filled/mini-task-tracker/research/notes.md` | Filled: localStorage limits research, 5MB limit finding, Safari note. |
| 61 | `starter-kit/example-filled/mini-task-tracker/research/sources.md` | Two rows: MDN localStorage, MDN JSON.stringify. |
| 62 | `starter-kit/example-filled/mini-task-tracker/research/open_questions.md` | One row: localStorage clear data loss question. |
| 63 | `starter-kit/example-filled/mini-task-tracker/planning/backlog.md` | Sprint 001 DONE, Sprint 002 PLANNED. Completed sprints table: Sprint 001 closed 2026-06-07. |
| 64 | `starter-kit/example-filled/mini-task-tracker/planning/releases/v0.1/release_plan.md` | Filled: task CRUD release goal, 5 success criteria, Sprint 001 listed. |
| 65 | `starter-kit/example-filled/mini-task-tracker/planning/releases/v0.1/scope.md` | In-scope: add, complete, reopen, persist, view. Out-of-scope: accounts, server, sharing, filter, search. |
| 66 | `starter-kit/example-filled/mini-task-tracker/planning/releases/v0.1/release_notes.md` | Write-at-release instruction preserved. MTT name in header. |
| 67 | `starter-kit/example-filled/mini-task-tracker/planning/releases/v0.1/retrospective.md` | Write-after-release instruction preserved. MTT name in header. |
| 68 | `starter-kit/example-filled/mini-task-tracker/planning/features/_template/feature_brief.md` | Generic template (feature templates are project-agnostic by design). |
| 69 | `starter-kit/example-filled/mini-task-tracker/planning/features/_template/research.md` | Generic template. |
| 70 | `starter-kit/example-filled/mini-task-tracker/planning/features/_template/feasibility.md` | Generic template. |
| 71 | `starter-kit/example-filled/mini-task-tracker/planning/features/_template/validation.md` | Generic template. |
| 72 | `starter-kit/example-filled/mini-task-tracker/planning/features/_template/sprint_map.md` | Generic template. |
| 73 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/requirements.md` | Filled: core task list sprint goal, in-scope app files, no-framework constraint. |
| 74 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/blueprint.md` | Filled: index.html, style.css, app.js. Permission Level 1. Develop Mode sprint. |
| 75 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/blueprint_feedback.md` | Filled: Operator reviewer, all sections Approved, localStorage serialization note. |
| 76 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/acceptance.md` | Filled: file existence, task CRUD functionality, no-secrets checks. |
| 77 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/dry_run.md` | Filled: index.html/style.css/app.js to create, STATE.md to modify, open index.html command, JSON serialization risk, task ID type ambiguity. |
| 78 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/dry_run_review.md` | All 7 sections Approved. Authorization message filled in. |
| 79 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/implementation_log.md` | Filled: 2 phases, 3 created, 1 modified, 0 issues, 0 secrets. |
| 80 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/human_review.md` | All sections Pass. Approved. Date 2026-06-07. Reviewer: Operator. |
| 81 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/retrospective.md` | Filled: localStorage approach worked; task ID question unresolved; test persistence rule added. |
| 82 | `starter-kit/example-filled/mini-task-tracker/planning/sprints/sprint_001/rollback_log.md` | Instruction preserved. Table empty (no rollbacks). |

### Phase 4 — Consistency audit

| # | File | Purpose |
|---|---|---|
| 83 | `planning/sprints/sprint_002/consistency_audit.md` | Audit report for all generated files. PASS/FAIL/WARNING per file. Required before sprint close. |

---

## 2. Files to modify

| File | Change | Reason |
|---|---|---|
| `planning/backlog.md` | Update Sprint 001 from `[ACTIVE]` to `[DONE]`. Update Sprint 002 from `[PLANNED]` to `[ACTIVE]`. Add Sprint 001 to completed sprints table. | Sprint lifecycle tracking. Already partially done in Design Mode — verify current state at implementation time. |
| `STATE.md` | Update at sprint close: Active Sprint → Sprint 003 (or next sprint). Current Status → Sprint 002 complete. Next Step → Begin Sprint 003. | Standard sprint close. Updated at close, not during implementation. |

---

## 3. Files to move or delete

None.

---

## 4. Commands to run

None. This sprint produces Markdown files only. No build step, no tooling, no install required.

---

## 5. Dependencies requested

None. All files are Markdown. No new libraries, packages, APIs, or external tools are required.

---

## 6. Risks

**Risk 1 — Internal consistency across 80 example-filled files.**  
The example-filled kit has 40 files that must use identical project name, version, sprint dates, and mode names. A single inconsistent reference (e.g., "Task Tracker" instead of "Mini Task Tracker", or a wrong sprint date) will fail the acceptance check in Section 13. Mitigation: the consistency audit in Phase 4 must explicitly check cross-file consistency for the example-filled kit.

**Risk 2 — AGENTS.md dry run rule completeness.**  
The blank AGENTS.md is the most critical file in the kit. If the dry run rule omits any of the 7 required items, or the authorization message is paraphrased rather than verbatim, the acceptance check in Section 5 will fail. Mitigation: generate AGENTS.md first, verify it against AGENTS.md in the ADDF project brain before continuing to other files.

**Risk 3 — Q004 scope ambiguity.**  
Q004 (release folders in blank kit) is unresolved. This sprint follows §10.2 which includes release folders. If Q004 is resolved to exclude them before the sprint closes, 5 files must be removed from the blank kit and 5 from the example-filled kit. This would not fail the sprint but would require a scope amendment. Mitigation: raise Q004 with the human before implementation begins.

**Risk 4 — License text accuracy.**  
The LICENSE file must contain the official CC BY 4.0 text unmodified. A paraphrased or abbreviated license is not legally equivalent. Mitigation: use the official Creative Commons legal code text exactly as published at creativecommons.org/licenses/by/4.0/legalcode.

---

## 7. Ambiguities

**Ambiguity 1 — Q004: release folders in blank kit.**  
The blueprint includes `planning/releases/v0.1/` files in the blank kit, following §10.2. Q004 is still open. If the human resolves Q004 to exclude release folders before authorizing implementation, the scope changes. **Requires human decision before implementation begins.**

**Ambiguity 2 — Example-filled sprint dates.**  
The blueprint specifies Sprint 001 dates as opened 2026-06-01, closed 2026-06-07 for the Mini Task Tracker example. These are fictional dates for a fictional project. Confirm these are acceptable as illustrative dates, or provide preferred dates.

**Ambiguity 3 — Feature templates in example-filled kit.**  
The blueprint specifies that the 5 `planning/features/_template/` files in the example-filled kit are the same generic templates as the blank kit (feature templates are project-agnostic by design). Confirm this is the intended approach, or specify whether the example-filled feature templates should also be filled with Mini Task Tracker content.

---

Dry run complete. Do not proceed.

Await human review of this dry run and authorization to implement.

---

*ADDF · `planning/sprints/sprint_002/dry_run.md` · Develop Mode · Permission Level 0 · 2026-05-31*
