# Sprint 002 — Acceptance Criteria

**Sprint:** 002  
**Title:** Starter Kit  
**Reviewer:** Human  
**How to use this file:** Work through each section in order. Check each box only after directly verifying the stated condition — do not check a box based on the AI's description of the file. Open the file and look.

---

## 1. File existence — supporting files

Open the repository root and `starter-kit/` directory.

- [ ] `LICENSE` exists at the repository root.
- [ ] `starter-kit/README.md` exists.
- [ ] `starter-kit/blank/` directory exists.
- [ ] `starter-kit/example-filled/mini-task-tracker/` directory exists.

---

## 2. File existence — blank kit project brain files

Open `starter-kit/blank/` and confirm each file is present.

- [ ] `starter-kit/blank/START_HERE.md` exists.
- [ ] `starter-kit/blank/AGENTS.md` exists.
- [ ] `starter-kit/blank/DOMAIN.md` exists.
- [ ] `starter-kit/blank/STATE.md` exists.
- [ ] `starter-kit/blank/DECISIONS.md` exists.
- [ ] `starter-kit/blank/COMMANDS.md` exists.
- [ ] `starter-kit/blank/STYLE_GUIDE.md` exists.
- [ ] `starter-kit/blank/SECURITY.md` exists.
- [ ] `starter-kit/blank/QUESTIONS.md` exists.
- [ ] `starter-kit/blank/RISKS.md` exists.
- [ ] `starter-kit/blank/GIT_STRATEGY.md` exists.
- [ ] `starter-kit/blank/PROMPT_CHANGELOG.md` exists.

---

## 3. File existence — blank kit docs/, research/, planning/

- [ ] `starter-kit/blank/docs/architecture.md` exists.
- [ ] `starter-kit/blank/docs/data_model.md` exists.
- [ ] `starter-kit/blank/docs/api.md` exists.
- [ ] `starter-kit/blank/docs/permissions.md` exists.
- [ ] `starter-kit/blank/docs/validation.md` exists.
- [ ] `starter-kit/blank/research/notes.md` exists.
- [ ] `starter-kit/blank/research/sources.md` exists.
- [ ] `starter-kit/blank/research/open_questions.md` exists.
- [ ] `starter-kit/blank/planning/backlog.md` exists.
- [ ] `starter-kit/blank/planning/releases/v0.1/release_plan.md` exists.
- [ ] `starter-kit/blank/planning/releases/v0.1/scope.md` exists.
- [ ] `starter-kit/blank/planning/releases/v0.1/release_notes.md` exists.
- [ ] `starter-kit/blank/planning/releases/v0.1/retrospective.md` exists.
- [ ] `starter-kit/blank/planning/features/_template/feature_brief.md` exists.
- [ ] `starter-kit/blank/planning/features/_template/research.md` exists.
- [ ] `starter-kit/blank/planning/features/_template/feasibility.md` exists.
- [ ] `starter-kit/blank/planning/features/_template/validation.md` exists.
- [ ] `starter-kit/blank/planning/features/_template/sprint_map.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/requirements.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/blueprint.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/blueprint_feedback.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/acceptance.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/dry_run.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/dry_run_review.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/implementation_log.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/human_review.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/retrospective.md` exists.
- [ ] `starter-kit/blank/planning/sprints/sprint_001/rollback_log.md` exists.

---

## 4. File existence — example-filled kit

Open `starter-kit/example-filled/mini-task-tracker/` and confirm each file is present. The structure must parallel `starter-kit/blank/`.

- [ ] `START_HERE.md` exists.
- [ ] `AGENTS.md` exists.
- [ ] `DOMAIN.md` exists.
- [ ] `STATE.md` exists.
- [ ] `DECISIONS.md` exists.
- [ ] `COMMANDS.md` exists.
- [ ] `STYLE_GUIDE.md` exists.
- [ ] `SECURITY.md` exists.
- [ ] `QUESTIONS.md` exists.
- [ ] `RISKS.md` exists.
- [ ] `GIT_STRATEGY.md` exists.
- [ ] `PROMPT_CHANGELOG.md` exists.
- [ ] `docs/architecture.md` exists.
- [ ] `docs/data_model.md` exists.
- [ ] `docs/api.md` exists.
- [ ] `docs/permissions.md` exists.
- [ ] `docs/validation.md` exists.
- [ ] `research/notes.md` exists.
- [ ] `research/sources.md` exists.
- [ ] `research/open_questions.md` exists.
- [ ] `planning/backlog.md` exists.
- [ ] `planning/releases/v0.1/release_plan.md` exists.
- [ ] `planning/releases/v0.1/scope.md` exists.
- [ ] `planning/releases/v0.1/release_notes.md` exists.
- [ ] `planning/releases/v0.1/retrospective.md` exists.
- [ ] `planning/features/_template/feature_brief.md` exists.
- [ ] `planning/features/_template/research.md` exists.
- [ ] `planning/features/_template/feasibility.md` exists.
- [ ] `planning/features/_template/validation.md` exists.
- [ ] `planning/features/_template/sprint_map.md` exists.
- [ ] `planning/sprints/sprint_001/requirements.md` exists.
- [ ] `planning/sprints/sprint_001/blueprint.md` exists.
- [ ] `planning/sprints/sprint_001/blueprint_feedback.md` exists.
- [ ] `planning/sprints/sprint_001/acceptance.md` exists.
- [ ] `planning/sprints/sprint_001/dry_run.md` exists.
- [ ] `planning/sprints/sprint_001/dry_run_review.md` exists.
- [ ] `planning/sprints/sprint_001/implementation_log.md` exists.
- [ ] `planning/sprints/sprint_001/human_review.md` exists.
- [ ] `planning/sprints/sprint_001/retrospective.md` exists.
- [ ] `planning/sprints/sprint_001/rollback_log.md` exists.

---

## 5. blank/AGENTS.md — framework correctness

Open `starter-kit/blank/AGENTS.md`.

- [ ] The file defines exactly three modes. The mode names are: Research Mode, Design Mode, Develop Mode. No other mode names appear.
- [ ] The dry run content definition lists all seven items: files to create; files to modify; files to move or delete; commands to run; dependencies requested; risks; ambiguities.
- [ ] A Step 5a (or equivalent) states that a new dependency listed in `dry_run.md` requires a `DECISIONS.md` entry before authorization proceeds.
- [ ] The authorization message is present and reads: `Dry run approved. / Permission Level [LEVEL] authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.`
- [ ] A statement appears confirming the model cannot self-authorize.
- [ ] The permission levels table lists exactly five levels: 0, 1, 2, 3, 4. Level 0 is "Dry Run Only." Level 4 is "Migration / High-Risk Change."

---

## 6. blank/AGENTS.md — placeholder discipline

Open `starter-kit/blank/AGENTS.md`.

- [ ] The file contains at least one `[YOUR PROJECT NAME]` or equivalent bracketed placeholder.
- [ ] The file does not reference the ADDF public repository by name or path.
- [ ] The file does not list ADDF project brain files as the safe-to-load list (the list must be generic placeholders or clearly labelled as examples to replace).

---

## 7. blank/STATE.md — required fields

Open `starter-kit/blank/STATE.md`.

- [ ] Count the labelled fields. There are exactly seven: Active Scale, Current Mode, Active Release, Active Feature, Active Sprint, Current Status, Next Step.
- [ ] Each field contains a placeholder value (not an empty line).

---

## 8. blank/START_HERE.md — content and version

Open `starter-kit/blank/START_HERE.md`.

- [ ] Count the numbered steps. There are exactly 15.
- [ ] Step 9 instructs the operator to run Develop Mode at Permission Level 0.
- [ ] Step 11 contains the authorization message text verbatim.
- [ ] Step 15 instructs the operator to close or checkpoint the AI session.
- [ ] A "Next sessions" section exists explaining that the model has no memory between sessions.
- [ ] The version number 0.1.0 appears in the file.

---

## 9. blank/SECURITY.md — pre-populated dangerous file list

Open `starter-kit/blank/SECURITY.md`.

- [ ] The files-never-to-load list contains at least four pre-populated entries (`.env`, `*.key`, `*.pem`, `secrets/` or equivalent).
- [ ] There is at least one placeholder row inviting the operator to add their own entries.

---

## 10. blank/dry_run.md — all seven sections present

Open `starter-kit/blank/planning/sprints/sprint_001/dry_run.md`.

- [ ] The file contains exactly seven numbered content sections matching the 7-item dry run definition: Files to create, Files to modify, Files to move or delete, Commands to run, Dependencies requested, Risks, Ambiguities.
- [ ] A stop instruction appears at the bottom: "Dry run complete. Do not proceed. Await human authorization." or equivalent.

---

## 11. Blank kit usability — can be copied and used immediately

This check requires you to consider the blank kit as an operator would on day one.

- [ ] Open `starter-kit/blank/START_HERE.md`. The first step instructs the operator to copy the starter kit. This makes sense as a first action.
- [ ] Open `starter-kit/blank/AGENTS.md`. A new operator can read this file and understand what modes exist and how to use the dry run rule, without any other reference material.
- [ ] Open `starter-kit/blank/STATE.md`. Every field has a placeholder — no field is blank or empty.
- [ ] Open `starter-kit/blank/planning/sprints/sprint_001/requirements.md`. An operator can see the structure and understand what to fill in.
- [ ] No blank kit file requires knowledge of the ADDF public repository's internal structure to understand or complete.

---

## 12. Example-filled kit — Mini Task Tracker identity

Open files in `starter-kit/example-filled/mini-task-tracker/`.

- [ ] Open `DOMAIN.md`. The project name is "Mini Task Tracker." The scope describes a local-only web app for task management with localStorage persistence.
- [ ] Open `DECISIONS.md`. At least two decisions are present and filled with Mini Task Tracker-specific content (not placeholders).
- [ ] Open `planning/sprints/sprint_001/dry_run.md`. The files listed under "Files to create" are application files (e.g., index.html, app.js, style.css) — not ADDF project brain files.
- [ ] Open `planning/sprints/sprint_001/human_review.md`. The overall decision is marked Approved (not blank).
- [ ] Open `planning/backlog.md`. Sprint 001 status is `[DONE]`.

---

## 13. Example-filled kit — internal consistency

Verify that the example-filled files reference the same project identity throughout.

- [ ] Open `AGENTS.md` and `DOMAIN.md`. Both refer to the same project name (Mini Task Tracker or MTT).
- [ ] Open `STATE.md`. The Active Release field matches the release described in `planning/releases/v0.1/release_plan.md`.
- [ ] Open `planning/sprints/sprint_001/dry_run_review.md`. The authorization message is filled in (not a template placeholder).
- [ ] Open `planning/sprints/sprint_001/implementation_log.md`. The files listed as created match the files listed in `dry_run.md` under "Files to create."
- [ ] The mode names Research Mode, Design Mode, Develop Mode are used consistently. No file in the example-filled kit uses Architect Mode or Builder Mode.

---

## 14. Security — no secrets, no machine-specific paths

Perform a text search across all files in `starter-kit/` for the following patterns: `api_key`, `api-key`, `password`, `token`, `secret`, `C:\Users`, `C:\`, `/home/`, `/Users/`, `localhost:`.

- [ ] No results found in any file in `starter-kit/blank/`.
- [ ] No results found in any file in `starter-kit/example-filled/`.
- [ ] No file in `starter-kit/blank/` contains a hard-coded local file path.
- [ ] No file in `starter-kit/example-filled/` contains a hard-coded local file path, API key, or credential.

---

## 15. Version visibility

- [ ] Open `starter-kit/README.md`. The version 0.1.0 is visible.
- [ ] Open `starter-kit/blank/START_HERE.md`. The version 0.1.0 is visible.

---

## 16. LICENSE file

Open `LICENSE` at the repository root.

- [ ] The file exists.
- [ ] The text identifies the license as Creative Commons Attribution 4.0 International.
- [ ] A copyright line is present naming ADDF contributors.

---

## 17. starter-kit/README.md — content completeness

Open `starter-kit/README.md`.

- [ ] The file explains what the blank kit is and what it is for.
- [ ] The file explains what the example-filled kit is and what it is for.
- [ ] The file lists the minimum viable ADDF file set (at least: AGENTS.md, DOMAIN.md, STATE.md, COMMANDS.md, SECURITY.md, and a sprint folder).
- [ ] The file lists the full ADDF additions (at least: DECISIONS.md, QUESTIONS.md, RISKS.md, GIT_STRATEGY.md).
- [ ] The file states the license (CC BY 4.0).

---

## 18. Consistency audit applied

Open `planning/sprints/sprint_002/consistency_audit.md`.

- [ ] The audit report exists and contains a `## Audit summary` section.
- [ ] Every file in `starter-kit/blank/` is listed with a PASS, FAIL, or WARNING verdict.
- [ ] The blank kit AGENTS.md receives a PASS for the dry run definition check.
- [ ] No file is listed with an unresolved FAIL at the time the sprint is marked complete.

---

## 19. Backlog and state updated

- [ ] Open `planning/backlog.md`. Sprint 001 status is `[DONE]`. Sprint 002 status is `[ACTIVE]` (or `[DONE]` if the sprint is closing).
- [ ] Sprint 001 appears in the completed sprints table with a closed date.

---

## Sprint 002 is complete when

All boxes above are checked. Specifically:
- All 83 files listed in `blueprint.md` exist.
- The blank kit can be copied into a new empty folder and used without modification.
- The example-filled kit contains consistent, realistic Mini Task Tracker content throughout.
- No file in either kit contains a secret, machine-specific path, or ADDF-repo-specific content.
- `LICENSE` exists and states CC BY 4.0.
- The consistency audit has been run and all issues resolved.
- `STATE.md` is updated to reflect sprint closure.

---

*ADDF · `planning/sprints/sprint_002/acceptance.md`*
