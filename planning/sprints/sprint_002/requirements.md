# Sprint 002 — Requirements

**Sprint:** 002  
**Title:** Starter Kit  
**Release:** v0.1 — Public Proof  
**Mode:** Design Mode  
**Branch:** `sprint/002-starter-kit`  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md` §3.3, §10

---

## Sprint goal

Create the ADDF starter kit: a blank template set an operator can copy into any project and begin using ADDF immediately, and an example-filled version using the Mini Task Tracker project.

The starter kit is the framework's first executable artifact. An operator who downloads the blank kit should be able to open it, read `START_HERE.md`, and begin their first ADDF session without any other reference.

---

## Context

### What preceded this sprint

Sprint 001 produced the public ADDF repository project brain and planning structure. All project brain files exist and are internally consistent. The framework documentation in `docs/` defines how each project brain file is used.

### Decisions that bind this sprint

- **Decision 004:** The starter kit ships before the CLI init tool. The CLI must produce output identical to the starter kit structure.
- **Decision 006:** All starter kit content is licensed CC BY 4.0. The `LICENSE` file is in scope for this sprint.
- **Decision 008:** `DECISIONS.md` and `QUESTIONS.md` are universal — every ADDF project includes both, regardless of scale. The blank starter kit must include both.

### Open question acknowledged

**Q004** — whether the blank kit should include full release folders (`planning/releases/`) — is still open. This sprint follows the canonical structure from requirements §10.2, which includes release folders. If Q004 resolves to exclude release folders from the blank kit, the release folder files may be removed before Sprint 002 closes. This is the only open question that could affect sprint scope.

---

## In scope

### Primary deliverable: blank starter kit

`starter-kit/blank/` — a complete set of ADDF template files with clear placeholders. Every file must be useful on its own. An operator who copies only three files from the blank kit should still get value from each one.

**Project brain files — 12 files:**

| File | Content requirement |
|---|---|
| `AGENTS.md` | Three modes (Research, Design, Develop) with allowed/forbidden actions. Full dry run approval rule with 7-item content definition, Step 5a dependency gate, and authorization message. Permission levels 0–4. Safe-to-load list. Session opening protocol. All ADDF-specific text replaced with `[YOUR PROJECT NAME]` placeholders. |
| `DOMAIN.md` | Project identity, scope, out-of-scope, target users, key entities, and domain rules. All content is placeholders. Includes a worked example row in the out-of-scope table to show format. |
| `STATE.md` | All seven required fields: Active Scale, Current Mode, Active Release, Active Feature, Active Sprint, Current Status, Next Step. Each field contains a placeholder value and an inline comment explaining what to write. |
| `SECURITY.md` | Files-never-to-load list (with common examples pre-populated: `.env`, `*.key`, `*.pem`, `secrets/`). LLM tools in use field. Session hygiene rules. |
| `DECISIONS.md` | Header, instructions, one placeholder decision entry (Decision 001 with all fields blank and labelled). Resolved decisions section. |
| `QUESTIONS.md` | Header, instructions, one placeholder open question (Q001 with all fields blank and labelled). Resolved questions section. |
| `RISKS.md` | Header, instructions, three placeholder risk entries covering the most common risk categories (terminology drift, secrets exposure, scope creep). Each has Severity, Probability, Status, and Mitigation fields with placeholder text. |
| `COMMANDS.md` | Four command sections with placeholder entries: Setup, Development, Testing, Deployment. Each section has one example command entry with `[YOUR COMMAND]` placeholder. |
| `STYLE_GUIDE.md` | Voice rules, banned words list (pre-populated with common AI writing anti-patterns), canonical terminology table with three blank rows, file naming rules, no-emoji rule. Points to ADDF brand guide. |
| `GIT_STRATEGY.md` | Branch model with ADDF-standard patterns (`main`, `dev`, `sprint/NNN-*`, `fix/NNN-*`). Conventional Commits convention. PR template with all required fields. Release process skeleton (numbered steps, content blank). `.gitignore` minimums pre-populated. |
| `PROMPT_CHANGELOG.md` | Header, instructions, one blank prompt entry in the correct format. Breaking change convention. |
| `START_HERE.md` | Exactly 15 numbered steps matching requirements §3.2 and §8.4. Step 11 must include the authorization message text verbatim. A "Next sessions" section explaining the model has no memory between sessions. All project-specific content replaced with `[YOUR PROJECT NAME]` placeholders. |

**Documentation templates — 5 files:**

| File | Content requirement |
|---|---|
| `docs/architecture.md` | Section headers: Overview, Components, Data flow, Key decisions. Each section has one paragraph of placeholder instructional text explaining what to write. |
| `docs/data_model.md` | Section headers: Entities, Fields, Relationships, Constraints. Placeholder instructional text in each section. |
| `docs/api.md` | Section headers: Endpoints, Authentication, Request format, Response format, Error codes. Placeholder instructional text. |
| `docs/permissions.md` | Section headers: Roles, Access rules, Restrictions. Placeholder instructional text. |
| `docs/validation.md` | Section headers: Input validation rules, Edge cases, Acceptance tests. Placeholder instructional text. |

**Research templates — 3 files:**

| File | Content requirement |
|---|---|
| `research/notes.md` | Header, date field, question being researched field, findings section with placeholder rows, open items section. |
| `research/sources.md` | Header, table with columns: Source, URL, Date accessed, Relevance, Key points. Three placeholder rows. |
| `research/open_questions.md` | Header, table with columns: Question, Blocking what, Raised, Owner. Three placeholder rows. |

**Planning templates — 20 files:**

| File | Content requirement |
|---|---|
| `planning/backlog.md` | Status key table. Three placeholder sprint entries (Sprint 001, Sprint 002, Sprint 003) with `[PLANNED]` status. Completed sprints table. |
| `planning/releases/v0.1/release_plan.md` | Release goal field (placeholder). In-scope checklist (5 placeholder items). Sprint breakdown table (3 placeholder rows). Dependency table (2 placeholder rows). Release process numbered list (8 steps, content blank). |
| `planning/releases/v0.1/scope.md` | In-scope table (5 placeholder rows). Out-of-scope table (5 placeholder rows with "Not planned" in Target column). Scope change decision log (empty, with instructions). |
| `planning/releases/v0.1/release_notes.md` | Placeholder header. Version field. Summary section. What changed section. Known issues section. Instructions: "Write this file at release time." |
| `planning/releases/v0.1/retrospective.md` | Section headers: What worked, What needs attention, Rules added. Each section has one placeholder bullet. Retrospective date field. |
| `planning/features/_template/feature_brief.md` | Feature name, goal, operator impact, in-scope list, out-of-scope list, dependencies, acceptance pointer fields. All placeholder content. |
| `planning/features/_template/research.md` | Question being answered, findings, open items, recommendation fields. Placeholder content. |
| `planning/features/_template/feasibility.md` | Approach options table (3 rows), risks, recommendation, constraints. Placeholder content. |
| `planning/features/_template/validation.md` | Validation questions checklist (5 items), evidence required, pass/fail verdict, follow-up items. Placeholder content. |
| `planning/features/_template/sprint_map.md` | Sprint breakdown table (3 placeholder rows), dependencies, estimated total. Placeholder content. |
| `planning/sprints/sprint_001/requirements.md` | Sprint goal field, context section, in-scope table (5 placeholder file rows), out-of-scope table (3 rows), constraints list (2 items), success criteria pointer. |
| `planning/sprints/sprint_001/blueprint.md` | Files-to-create table (5 placeholder rows), files-to-modify table (2 placeholder rows), files-not-in-scope table (2 placeholder rows). No-implementation note if Design Mode only. |
| `planning/sprints/sprint_001/blueprint_feedback.md` | Reviewer field, date field, section results table (columns: Section, Verdict, Issues). Three placeholder rows. Overall verdict field. Notes field. |
| `planning/sprints/sprint_001/acceptance.md` | Three numbered sections with 3 checkboxes each. Every checkbox must be human-verifiable without AI self-assessment. Each section has an "Issues found" field. |
| `planning/sprints/sprint_001/dry_run.md` | Mode field, permission level field. Seven content sections matching the 7-item dry run definition: Files to create, Files to modify, Files to move or delete, Commands to run, Dependencies requested, Risks, Ambiguities. Each section has 2 placeholder entries. |
| `planning/sprints/sprint_001/dry_run_review.md` | Reviewer field, date field, section results for each of the 7 dry run content areas. Verdict per section (Approved / Rejected / Conditional). Overall verdict. Conditions field. Authorization message field (to be filled by human if approved). |
| `planning/sprints/sprint_001/implementation_log.md` | Mode field. Phase table (columns: Phase, Files, Notes). Three placeholder phases. Summary table (rows: Files created, Files modified, Issues found, Secrets committed). |
| `planning/sprints/sprint_001/human_review.md` | Reviewer, date, reference fields. Three acceptance sections with Pass/Fail/Partial verdict. Additional observations. Items requiring follow-up table. Overall decision block (Approved / Approved with conditions / Not approved). Approval signature block. |
| `planning/sprints/sprint_001/retrospective.md` | What worked section (2 placeholder items). What needs attention section (2 placeholder items). Constraints added section. Rules section. Next sprint section. |
| `planning/sprints/sprint_001/rollback_log.md` | Header, instructions. Table with columns: Date, Change reverted, Reason, Files affected, Status. Two placeholder rows with `[DATE]` and `[REASON]` placeholder text. Note: "Fill this file only if a rollback was required. Leave blank if no rollbacks occurred." |

### Secondary deliverable: example-filled starter kit

`starter-kit/example-filled/mini-task-tracker/` — all files from the blank kit, filled with realistic Mini Task Tracker content.

Mini Task Tracker project description (from requirements §12.2):

> A local-only web app where a single operator can add tasks, mark them complete, reopen completed tasks, and persist tasks in localStorage.

The example-filled kit must show what correct, completed ADDF project files look like for a small, well-defined project. Every file that has a placeholder in the blank kit must have real content in the example-filled kit.

The sprint folder (`planning/sprints/sprint_001/`) in the example-filled kit represents a fictional Sprint 001 for the Mini Task Tracker — the sprint that built the core task list feature (add tasks, mark complete, persist to localStorage).

### Supporting file

`starter-kit/README.md` — explains both variants, how to copy, minimum viable ADDF, full ADDF additions, and where to get help.

### License file

`LICENSE` — CC BY 4.0 license text. Required before v0.1 public release. Decision 006 resolved.

---

## Out of scope

| Item | Reason |
|---|---|
| `examples/mini-task-tracker/` | Sprint 007. The standalone example is a separate artifact from the starter kit. |
| Prompt catalog files (`prompts/`) | Sprint 003. |
| Source code for the Mini Task Tracker web app | Never in scope for Design Mode. ADDF files only. |
| ZIP packaging of starter kit | Sprint 009 (release package). |
| Website download links | Sprint 005 (Website MVP). |
| `CONTRIBUTING.md` | Deferred to Sprint 009. |
| `CODE_OF_CONDUCT.md` | Deferred to Sprint 009. |
| Any change to the ADDF repository's own project brain files | Out of scope unless a discrepancy is found during generation that requires a correction. |

---

## Constraints

1. **Placeholder discipline.** Every blank kit file must use `[YOUR PROJECT NAME]`, `[YOUR GOAL]`, or equivalent bracketed uppercase placeholders for project-specific content. Placeholders must never be ADDF-specific content — an operator should never have to delete framework content, only replace placeholders.

2. **No code.** No source code, scripts, HTML, CSS, or JSON in any starter kit file. ADDF files are Markdown only.

3. **No secrets, no machine-specific paths.** No API keys, tokens, environment variable values, local file paths, or usernames in any file.

4. **Version visibility.** `starter-kit/README.md` and `starter-kit/blank/START_HERE.md` must display the current starter kit version (0.1.0).

5. **AGENTS.md must be framework-correct.** The blank `AGENTS.md` must include the complete, correct dry run approval rule and all three mode definitions. It must not omit or abbreviate the authorization message. An operator copying this file into their project must get a fully functional session contract.

6. **Example-filled files must be consistent.** All project name references, version numbers, and sprint dates across the example-filled kit must match each other. Use "Mini Task Tracker" and "0.1.0" throughout.

7. **Consistency audit.** Per Constraint 001 from Sprint 001 retrospective, a consistency audit must be run before the sprint is marked complete.

---

## Success criteria

See `planning/sprints/sprint_002/acceptance.md` for the complete human-verifiable checklist.

The sprint is complete when:
- All files listed in `blueprint.md` exist.
- The blank kit can be copied into a new empty folder and used immediately.
- The example-filled kit shows realistic completed files for the Mini Task Tracker.
- No file contains a secret, a machine-specific path, or ADDF-repo-specific content.
- The `LICENSE` file exists and states CC BY 4.0.
- The consistency audit has been run and all issues resolved.

---

*ADDF · `planning/sprints/sprint_002/requirements.md` · Design Mode · 2026-05-31*
