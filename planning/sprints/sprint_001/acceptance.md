# Sprint 001 — Acceptance Criteria

**Sprint:** 001  
**Title:** Repository skeleton and project brain  
**Reviewer:** Human  
**How to use this file:** Work through each section in order. Check each box only after directly verifying the stated condition — do not check a box based on the AI's description of the file. Open the file and look.

---

## 1. File existence — project brain

Open the repository root directory and confirm each file is present.

- [ ] `AGENTS.md` exists.
- [ ] `DOMAIN.md` exists.
- [ ] `DECISIONS.md` exists.
- [ ] `COMMANDS.md` exists.
- [ ] `QUESTIONS.md` exists.
- [ ] `RISKS.md` exists.
- [ ] `STYLE_GUIDE.md` exists.
- [ ] `GIT_STRATEGY.md` exists.
- [ ] `PROMPT_CHANGELOG.md` exists.
- [ ] `START_HERE.md` exists.
- [ ] `VERSION.md` exists.
- [ ] `CHANGELOG.md` exists.

---

## 2. File existence — planning structure

Open the `planning/` directory and confirm each file and folder is present.

- [ ] `planning/backlog.md` exists.
- [ ] `planning/releases/v0.1/` directory exists.
- [ ] `planning/releases/v0.1/release_plan.md` exists.
- [ ] `planning/releases/v0.1/scope.md` exists.
- [ ] `planning/releases/v0.1/release_notes.md` exists.
- [ ] `planning/sprints/sprint_001/requirements.md` exists.
- [ ] `planning/sprints/sprint_001/blueprint.md` exists.
- [ ] `planning/sprints/sprint_001/acceptance.md` exists (this file).
- [ ] `planning/sprints/sprint_001/consistency_audit.md` exists.

---

## 3. AGENTS.md — mode definitions

Open `AGENTS.md`.

- [ ] The file defines exactly three modes. The mode names are: Research Mode, Design Mode, Develop Mode. No other mode names appear as primary mode definitions.
- [ ] The Research Mode section contains both an **Allowed actions** list and a **Forbidden actions** list.
- [ ] The Design Mode section contains both an **Allowed actions** list and a **Forbidden actions** list.
- [ ] The Develop Mode section contains both an **Allowed actions** list and a **Forbidden actions** list.
- [ ] The Develop Mode **Writes to** line includes all three of: `dry_run.md`, `implementation_log.md`, `handoff_summary.md`.
- [ ] The Research Mode **Must not write to** line references sprint plan files (`requirements.md`, `blueprint.md`, `acceptance.md`) — not a blanket `planning/sprints/` prohibition.

---

## 4. AGENTS.md — dry run approval rule

Open `AGENTS.md` Section 2 (Dry run approval rule).

- [ ] The dry run content definition lists all seven items: files to create; files to modify; files to move or delete; commands to run; dependencies requested; risks; ambiguities.
- [ ] Step 5a (or equivalent) states that a new dependency listed in `dry_run.md` requires a `DECISIONS.md` entry before authorization proceeds.
- [ ] The authorization message is present and reads: `Dry run approved. / Permission Level [LEVEL] authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.`
- [ ] A statement appears confirming the model cannot self-authorize.

---

## 5. AGENTS.md — permission levels

Open `AGENTS.md` Section 3 (Permission levels).

- [ ] The table lists exactly five levels: 0, 1, 2, 3, 4.
- [ ] Level 0 is named "Dry Run Only."
- [ ] Level 4 is named "Migration / High-Risk Change."

---

## 6. DOMAIN.md — scope accuracy

Open `DOMAIN.md` Section 4 (v0.1 scope).

- [ ] The in-scope list says "all five groups" for prompts (not four).
- [ ] The five groups named are: Research, Design, Develop, Handoff/Resumption, Maintenance.
- [ ] The out-of-scope table contains at least 15 rows.
- [ ] The out-of-scope table includes: "Complex SaaS dashboard."
- [ ] The out-of-scope table includes: "Fully automated agent runner."
- [ ] The out-of-scope table includes: "Deep IDE integration."
- [ ] The out-of-scope table includes: "Requirement to use a specific LLM."

---

## 7. DOMAIN.md — mode names

Open `DOMAIN.md` Section 6.2 (Operating modes).

- [ ] The three listed modes are: Research Mode, Design Mode, Develop Mode.
- [ ] A statement is present that says not to refer to Architect Mode or Builder Mode as public ADDF modes.

---

## 8. DECISIONS.md — Decision 001

Open `DECISIONS.md`.

- [ ] Decision 001 is present with the title: "Dogfood ADDF in the public repository."
- [ ] Decision 001 shows **Status: Accepted**.
- [ ] Decision 001 contains a Context section.
- [ ] Decision 001 contains a Decision section.
- [ ] Decision 001 contains a Tradeoffs section. The Tradeoffs section includes the sentence: "This increases repository size but makes the methodology inspectable."
- [ ] At least 5 decisions are listed (001 through at least 005).
- [ ] Decision 006 and Decision 007 are marked **Status: Pending**.

---

## 9. QUESTIONS.md — completeness

Open `QUESTIONS.md`.

- [ ] Count the questions in the Open Questions section. There are exactly 10 questions numbered Q001 through Q010 that were there before any user additions. (Note: the user may have added Q011 or other questions after generation — that is acceptable.)
- [ ] Q001 is about the license.
- [ ] Q002 is about the CLI package name.
- [ ] Q010 is about prompt distribution format.
- [ ] A `## Resolved questions` section exists at the bottom of the file.

---

## 10. RISKS.md — completeness and specificity

Open `RISKS.md`.

- [ ] At least 7 risks are present.
- [ ] Each risk entry includes: Severity, Probability, Status, and a Mitigation section.
- [ ] Risk 001 is about terminology drift.
- [ ] Risk 004 is about secrets committed to a public repository.
- [ ] Risk 008 is about the handoff protocol not being tested before v0.1.
- [ ] No risk entry reads as a generic placeholder (e.g., "a risk may occur" without specifics).

---

## 11. START_HERE.md — first-session steps

Open `START_HERE.md`.

- [ ] Count the numbered steps in the main guide. There are exactly 15 steps.
- [ ] Step 1 instructs the operator to copy the starter kit.
- [ ] Step 2 instructs the operator to fill `SECURITY.md`.
- [ ] Step 6 instructs the operator to run Research Mode if unknowns exist, and states this step may be skipped.
- [ ] Step 9 instructs the operator to run Develop Mode at Permission Level 0.
- [ ] Step 10 instructs the operator to review `dry_run.md`.
- [ ] Step 11 contains the authorization message text.
- [ ] Step 15 instructs the operator to close or checkpoint the AI session.
- [ ] A "Next sessions" section exists explaining that the model has no memory between sessions and the files do.

---

## 12. STYLE_GUIDE.md (root project brain file)

Open the root `STYLE_GUIDE.md`.

- [ ] The canonical terminology table lists Research Mode, Design Mode, and Develop Mode.
- [ ] The canonical terminology table does not list Architect Mode or Builder Mode as primary terms.
- [ ] The banned words list is present.
- [ ] A Quack! usage rule is present and states a one-per-page limit.
- [ ] The file points to the full brand guide at `docs/_PDF/style Guide/STYLE_GUIDE.md`.

---

## 13. Full brand guide — terminology corrections

Open `docs/_PDF/style Guide/STYLE_GUIDE.md`.

- [ ] Section 2.4 does not contain the phrase "The Architect and Builder are roles."
- [ ] Section 11.1 vocabulary table does not list "Architect Mode / Builder Mode" as a canonical term.
- [ ] Section 11.1 vocabulary table lists Research Mode, Design Mode, and Develop Mode as canonical terms.
- [ ] Section 12.1 button examples table does not contain "Close the Builder thread" or "Send back to Architect."
- [ ] Section 20 Glossary does not define Architect or Builder as standalone terms. It defines Research Mode, Design Mode, and Develop Mode.

---

## 14. CHANGELOG.md — project brain files entry

Open `CHANGELOG.md` and find the v0.0.1 entry under `### Added`.

- [ ] `SECURITY.md` appears inside the "Project brain files:" list, not as a standalone bullet.
- [ ] `STATE.md` appears inside the "Project brain files:" list, not as a standalone bullet.
- [ ] The project brain files list contains exactly 11 files: AGENTS.md, DOMAIN.md, STATE.md, DECISIONS.md, COMMANDS.md, STYLE_GUIDE.md, SECURITY.md, QUESTIONS.md, RISKS.md, GIT_STRATEGY.md, PROMPT_CHANGELOG.md.

---

## 15. VERSION.md — artifact registry

Open `VERSION.md`.

- [ ] A version table is present with entries for at least: framework manual, starter kit, prompt catalog, example projects, diagram package, website, CLI init tool, web onboarding app.
- [ ] Framework manual version is listed as 3.5.
- [ ] Starter kit, prompt catalog, and example projects are listed as 0.1.0 with status "In development" or equivalent.

---

## 16. GIT_STRATEGY.md — branch and commit conventions

Open `GIT_STRATEGY.md`.

- [ ] The branch naming pattern for sprint branches is `sprint/NNN-short-description`.
- [ ] Conventional Commits format is described.
- [ ] PR requirements are listed, including a "Framework concepts changed: Yes/No" field.
- [ ] The release process lists a tagging step.

---

## 17. planning/backlog.md — sprint coverage

Open `planning/backlog.md`.

- [ ] Sprint 001 is listed with status `[ACTIVE]`.
- [ ] Sprints 002, 003, 007, 008, 009 are listed under v0.1.
- [ ] Sprint 004, 005, 006 are listed under v0.2 (Website).
- [ ] Sprint 010 is listed under v0.3 (CLI Init Tool).
- [ ] Sprint 011 is listed under v0.4 (Web Onboarding App).
- [ ] Unscheduled v0.1 items are present (full manual, diagrams, LICENSE, etc.).

---

## 18. planning/releases/v0.1/release_plan.md — release goal

Open `planning/releases/v0.1/release_plan.md`.

- [ ] The release goal statement is present.
- [ ] A success criteria checklist is present with at least 15 items.
- [ ] The sprint breakdown table lists Sprints 001, 002, 003, 007, 008, 009.
- [ ] The release process steps are present (minimum: version update, changelog update, tagging, GitHub release).

---

## 19. Security — no secrets

Perform a text search across all newly created files for the following patterns: `api_key`, `api-key`, `password`, `token`, `secret`, `.env`.

- [ ] No results found in any file listed in `planning/sprints/sprint_001/blueprint.md`.
- [ ] No `.env` file is present in the repository.
- [ ] `SECURITY.md` defines at least one category of files that must never be loaded into AI tools.

---

## 20. Consistency audit applied

Open `planning/sprints/sprint_001/consistency_audit.md`.

- [ ] The audit report exists and contains a `## Audit summary` section.
- [ ] The Audit summary section lists the files that needed correction (AGENTS.md, DOMAIN.md) and the warnings (STYLE_GUIDE.md, CHANGELOG.md).
- [ ] Cross-check: Open `AGENTS.md` and verify the dry run definition includes all 7 items (Issue A1 correction applied).
- [ ] Cross-check: Open `AGENTS.md` and verify Develop Mode "Writes to" includes `dry_run.md` and `handoff_summary.md` (Issue A2 correction applied).
- [ ] Cross-check: Open `DOMAIN.md` and verify the prompt count says "five groups" (Issue D1 correction applied).
- [ ] Cross-check: Open `DOMAIN.md` and verify the out-of-scope table includes complex SaaS dashboard, fully automated agent runner, deep IDE integration, and specific LLM requirement (Issue D2 correction applied).

---

## Sprint 001 is complete when

All boxes above are checked. Specifically:
- All files listed in `blueprint.md` exist.
- All AGENTS.md and DOMAIN.md corrections from the audit are present.
- The full brand guide no longer uses Architect Mode or Builder Mode as canonical terms.
- No secrets or private paths are present in any file.
- `STATE.md` is updated to reflect the sprint close and the next step.

---

*ADDF · `planning/sprints/sprint_001/acceptance.md`*
