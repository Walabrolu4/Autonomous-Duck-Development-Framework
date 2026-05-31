# Sprint 002 — Blueprint

**Sprint:** 002  
**Title:** Starter Kit  
**Mode:** Design Mode  
**Permission Level:** N/A — this sprint contains no Develop Mode work.  
**Primary reference:** `planning/sprints/sprint_002/requirements.md`

This blueprint lists every file to be created or modified in Sprint 002. No file outside this list may be changed during this sprint.

---

## Order of operations

Sprint 002 proceeds in four phases. Each phase must complete before the next begins.

**Phase 1 — Supporting files**  
Create the starter kit root README and the LICENSE file. These have no dependencies on later files.

**Phase 2 — Blank starter kit**  
Create all 40 files in `starter-kit/blank/`. Generate project brain files first (AGENTS.md through START_HERE.md), then docs/, then research/, then planning/. Start_HERE.md is last because it references all other files.

**Phase 3 — Example-filled starter kit**  
Create all 40 files in `starter-kit/example-filled/mini-task-tracker/`. Mirror the blank kit structure exactly. Files must be internally consistent: project name, version, sprint dates, and mode names must match across all example-filled files.

**Phase 4 — Consistency audit and sprint close**  
Run a consistency audit against all generated files. Resolve any issues. Update `planning/backlog.md` to mark Sprint 002 complete. `STATE.md` is updated at sprint close.

---

## Phase 1 — Supporting files

| # | File | Content specification |
|---|---|---|
| 1 | `starter-kit/README.md` | Title: "ADDF Starter Kit". Sections: (a) What this is — one paragraph explaining the starter kit as the primary ADDF adoption artifact. (b) Two variants — table showing blank/ vs example-filled/ and when to use each. (c) How to use the blank kit — 5-step copy-and-start instructions including the version number (0.1.0). (d) Minimum viable ADDF — the 6-file minimum list from requirements §10.3. (e) Full ADDF additions — the list of additional files from §10.3. (f) License — one sentence stating CC BY 4.0. (g) Further reading — links to START_HERE.md, AGENTS.md, and the ADDF docs/. Footer: version 0.1.0, ADDF framework 3.5. |
| 2 | `LICENSE` | Official Creative Commons Attribution 4.0 International license text. No modifications. Copyright line: "Copyright 2026 Autonomous Duck Deployment Framework Contributors." |

---

## Phase 2 — Blank starter kit (40 files)

### Project brain files

| # | File | Content specification |
|---|---|---|
| 3 | `starter-kit/blank/AGENTS.md` | Header: "AGENTS.md — `[YOUR PROJECT NAME]`". Section 1 (Session contract): one paragraph placeholder explaining what to write. Section 2 (Three modes): full Research Mode, Design Mode, and Develop Mode definitions with Allowed actions, Forbidden actions, Reads from, Writes to, and Must not write to for each — all three mode definitions are complete and correct per the ADDF framework; only `[YOUR PROJECT NAME]` placeholders replace project-specific references. Section 3 (Dry run approval rule): complete 7-item content definition, full 5-step approval sequence including Step 5a (dependency gate), and authorization message verbatim: "Dry run approved. / Permission Level [LEVEL] authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md." Self-authorization prohibition statement. Section 4 (Permission levels): table with all 5 levels (0–4) with names and scope. Section 5 (Safe-to-load files): placeholder list with 5 entries using `[PATH/TO/FILE]` format plus common project brain files pre-listed. Section 6 (Session opening protocol): 5-step checklist. Section 7 (Mode boundaries summary table): table showing which modes read and write which file types. Footer: `[YOUR PROJECT NAME] · AGENTS.md · ADDF 3.5`. |
| 4 | `starter-kit/blank/DOMAIN.md` | Header: "DOMAIN.md — `[YOUR PROJECT NAME]`". Section 1 (Project identity): 6 labelled fields — Full name, Short name, Type, Primary principle, Framework version (pre-filled: 3.5), Requirements document — each with `[placeholder]` value. Section 2 (What this project is): bullet list with 5 `[placeholder]` items. Section 3 (What this project is not): bullet list with 4 `[placeholder]` items. Section 4 (v0.1 scope): In-scope list (5 `[placeholder]` rows), Out-of-scope table (5 rows with Item and Target Release columns, placeholder content). Rule: "Do not automate a structure that has not stabilized." Section 5 (Target operators): table with Operator type and Primary need columns, 3 placeholder rows. Section 6 (Core framework concepts): pre-filled with ADDF standard concepts (Work scale model, 3 modes, 8-step lifecycle, sprint loop, project brain) — these are framework concepts, not project-specific. Section 7 (Key entities and terminology): table with Term and Definition columns, 5 placeholder rows. Section 8 (File naming): conventions pre-filled with ADDF standard rules. Section 9 (Domain rules): numbered list, 5 placeholder rules. Footer: `[YOUR PROJECT NAME] · DOMAIN.md · ADDF 3.5`. |
| 5 | `starter-kit/blank/STATE.md` | Header: "STATE.md". Seven labelled fields, one per line: Active Scale (`[Project / Release / Feature / Sprint / Patch]`), Current Mode (`[Research Mode / Design Mode / Develop Mode — or None between sessions]`), Active Release (`[e.g. v0.1 — Public Proof]`), Active Feature (`[Feature name or None]`), Active Sprint (`[Sprint NNN — Title or None]`), Current Status (placeholder sentence), Next Step (placeholder sentence). Inline comment above each field in HTML comment format (`<!-- Update this field at the start of each session -->`). |
| 6 | `starter-kit/blank/SECURITY.md` | Header: "SECURITY.md — `[YOUR PROJECT NAME]`". Section 1 (Files never to load into AI tools): pre-populated list — `.env`, `.env.*`, `*.env`, `*.key`, `*.pem`, `secrets/`, `credentials.*`, `*.secret`, plus one `[ADD YOUR OWN]` placeholder row. Section 2 (AI tools in use on this project): table with Tool, Provider, and Notes columns, 2 placeholder rows. Section 3 (Session hygiene rules): 5 pre-populated rules covering secrets handling, context sharing, session closure, and credential rotation. |
| 7 | `starter-kit/blank/DECISIONS.md` | Header: "DECISIONS.md — `[YOUR PROJECT NAME]`". Instructions paragraph: "Record every decision that would be costly or confusing to reverse here. Do not record sprint-level choices. When superseded, mark it Superseded and record the new decision." One complete placeholder decision entry: Decision 001 with all fields labelled — Status (`[Accepted / Pending / Superseded]`), Date, Decided by, Context section (placeholder), Decision section (placeholder), Tradeoffs section (placeholder), Consequences section (placeholder). Instructions: "Copy this entry for each new decision." |
| 8 | `starter-kit/blank/QUESTIONS.md` | Header: "QUESTIONS.md — `[YOUR PROJECT NAME]`". Instructions paragraph. Open questions section with one placeholder entry: Q001 with Status, Blocking, Raised, and question body fields all labelled with placeholder text. Resolved questions section (empty, with instructions: "Move resolved questions here with their answer recorded."). |
| 9 | `starter-kit/blank/RISKS.md` | Header: "RISKS.md — `[YOUR PROJECT NAME]`". Instructions paragraph. Three complete placeholder risk entries covering the three most common ADDF risk categories: (a) Risk 001 — Terminology drift (pre-written: "Project-specific terms are used inconsistently across files and AI sessions." Severity: Medium. Mitigation: "Update DOMAIN.md terminology table. Run consistency audit before sprint close.") (b) Risk 002 — Secrets exposure (pre-written: "A secret file is loaded into an AI session accidentally." Severity: High. Mitigation: "Check SECURITY.md before every session. Keep SECURITY.md current.") (c) Risk 003 — Scope creep (pre-written text using `[YOUR PROJECT NAME]` placeholder, Severity and Probability with `[High/Medium/Low]` brackets). |
| 10 | `starter-kit/blank/COMMANDS.md` | Header: "COMMANDS.md — `[YOUR PROJECT NAME]`". Four sections: Setup (1 placeholder command entry), Development (1 placeholder command entry), Testing (1 placeholder command entry), Deployment (1 placeholder command entry). Each entry has: Command label, Shell command field (`[YOUR COMMAND HERE]`), Description field (`[What this command does]`). |
| 11 | `starter-kit/blank/STYLE_GUIDE.md` | Header: "STYLE_GUIDE.md — `[YOUR PROJECT NAME]`". Section 1 (Voice): 3 placeholder rules in imperative form. Section 2 (Banned words): pre-populated list — "just", "simply", "obviously", "easy", "smart" — plus 2 `[ADD YOUR OWN]` placeholder rows. Section 3 (Canonical terminology): table with Term and Use columns, 3 placeholder rows. Section 4 (File naming): pre-populated ADDF standard rules (lowercase, hyphens, no spaces). Section 5 (Document structure): 3 placeholder rules. Section 6 (No emoji rule): pre-populated — "Do not use emoji in project files, commit messages, or AI prompts." Section 7 (Full brand guide): pointer line — "See `docs/brand-guide.md` for visual identity rules." (placeholder path). |
| 12 | `starter-kit/blank/GIT_STRATEGY.md` | Header: "GIT_STRATEGY.md — `[YOUR PROJECT NAME]`". Section 1 (Branch model): pre-populated ADDF standard branch names (main, dev, sprint/NNN-*, fix/NNN-*) with rules. Section 2 (Branch naming): naming pattern table with 4 rows (Sprint, Fix, Docs, Release) — pre-populated. Section 3 (Commit convention): Conventional Commits format explanation with type table (feat, fix, docs, chore, refactor, test, release) — pre-populated. Section 4 (PR requirements): checklist with 5 pre-populated required fields including "Framework concepts changed: Yes/No." Section 5 (Release process): numbered list, 8 steps, step labels pre-populated, content blank with `[YOUR STEP DETAIL]` placeholders. Section 6 (Merge strategy): 3 rules, pre-populated with ADDF standard (squash for noisy sprint history, merge commit for release). Section 7 (.gitignore minimums): pre-populated list — `.env`, `.env.*`, `*.env`, `*.key`, `*.pem`, `secrets/`, `node_modules/`, `.DS_Store`, `dist/`, `build/`, `*.log`. |
| 13 | `starter-kit/blank/PROMPT_CHANGELOG.md` | Header: "PROMPT_CHANGELOG.md — `[YOUR PROJECT NAME]`". Instructions paragraph: "Record every change to the prompts this project uses. Group by version. Mark breaking changes clearly." One placeholder prompt entry: v0.1.0 section with one `[Prompt name] — [What changed]` placeholder row. Breaking change convention: pre-populated — "A breaking change is any modification that requires an operator to update their session-opening procedure." |
| 14 | `starter-kit/blank/START_HERE.md` | Header: "Start Here — `[YOUR PROJECT NAME]`". Version line: "Starter kit version: 0.1.0." Introduction paragraph. Exactly 15 numbered steps: Step 1 (Copy this starter kit), Step 2 (Fill SECURITY.md — list the files that must never be loaded), Step 3 (Fill AGENTS.md — confirm the three modes and add your safe-to-load file list), Step 4 (Draft DOMAIN.md — write your project identity and scope), Step 5 (Initialize STATE.md — set scale and mode), Step 6 (Run Research Mode if unknowns exist — may be skipped), Step 7 (Run Design Mode to complete the project brain), Step 8 (Run Design Mode to generate Sprint 001 sprint pack), Step 9 (Run Develop Mode at Permission Level 0 — dry run only), Step 10 (Review dry_run.md — check every file and command listed), Step 11 (Authorize Develop Mode — use the exact authorization message: "Dry run approved. / Permission Level [LEVEL] authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md."), Step 12 (Verify output against acceptance criteria), Step 13 (Update STATE.md), Step 14 (Commit), Step 15 (Close or checkpoint the AI session). "Next sessions" section: paragraph explaining the model has no memory between sessions — the files are the project memory. Load the project brain files at the start of every session. |

### Documentation templates

| # | File | Content specification |
|---|---|---|
| 15 | `starter-kit/blank/docs/architecture.md` | Header: "Architecture — `[YOUR PROJECT NAME]`". Four sections: Overview (1 sentence of instructional placeholder text: "Describe the overall system shape — what it is, how it runs, and what it connects to."), Components (instructional placeholder: "List each major component, its responsibility, and its boundaries."), Data flow (instructional placeholder: "Describe how data moves through the system from input to output."), Key decisions (instructional placeholder: "Summarize architectural decisions that are not obvious from the code. Link to DECISIONS.md entries."). |
| 16 | `starter-kit/blank/docs/data_model.md` | Header: "Data Model — `[YOUR PROJECT NAME]`". Four sections with instructional placeholder text: Entities, Fields, Relationships, Constraints. |
| 17 | `starter-kit/blank/docs/api.md` | Header: "API Reference — `[YOUR PROJECT NAME]`". Five sections with instructional placeholder text: Endpoints, Authentication, Request format, Response format, Error codes. Note: "Delete this file if your project has no API." |
| 18 | `starter-kit/blank/docs/permissions.md` | Header: "Permissions — `[YOUR PROJECT NAME]`". Three sections with instructional placeholder text: Roles, Access rules, Restrictions. Note: "Delete this file if your project has no permission model." |
| 19 | `starter-kit/blank/docs/validation.md` | Header: "Validation — `[YOUR PROJECT NAME]`". Three sections with instructional placeholder text: Input validation rules, Edge cases, Acceptance tests. |

### Research templates

| # | File | Content specification |
|---|---|---|
| 20 | `starter-kit/blank/research/notes.md` | Header: "Research Notes". Fields: Question being researched (`[YOUR QUESTION]`), Date, Mode (pre-filled: Research Mode). Findings section: 3 placeholder bullet rows. Open items section: 2 placeholder rows. Instruction line: "Create one file per research session or topic. Do not merge unrelated research into one file." |
| 21 | `starter-kit/blank/research/sources.md` | Header: "Sources". Table with columns: Source, URL, Date accessed, Relevance, Key points. Three placeholder rows with `[SOURCE NAME]`, `[URL]`, `[DATE]`, `[High/Medium/Low]`, `[KEY POINT]` in each cell. |
| 22 | `starter-kit/blank/research/open_questions.md` | Header: "Open Research Questions". Table with columns: Question, Blocking what, Raised, Owner. Three placeholder rows. Instruction: "Move answered questions to the relevant QUESTIONS.md entry when resolved." |

### Planning templates

| # | File | Content specification |
|---|---|---|
| 23 | `starter-kit/blank/planning/backlog.md` | Header: "Backlog — `[YOUR PROJECT NAME]`". Status key table (pre-populated with ACTIVE, DONE, READY, PLANNED, FUTURE, UNSCHEDULED and their meanings). Three placeholder sprint entries formatted as: `### Sprint 001 — [Title]` with Status, Branch, Sprint pack pointer, and one sentence description each. Completed sprints table (empty, with instructions). |
| 24 | `starter-kit/blank/planning/releases/v0.1/release_plan.md` | Header: "v0.1 Release Plan — `[YOUR PROJECT NAME]`". Fields: Release goal (placeholder sentence), Target date (`[DATE]`). Success criteria: numbered checklist, 5 `[ ] [placeholder]` items. Sprint breakdown table: columns Sprint, Title, Status, Key output — 3 placeholder rows. Dependency/blocker table: 2 placeholder rows. Release process: numbered list 1–8, step labels present (create release branch, update VERSION.md, update CHANGELOG.md, run consistency audit, verify acceptance criteria, merge to main, tag release, publish release notes), content blank with `[details]` after each. |
| 25 | `starter-kit/blank/planning/releases/v0.1/scope.md` | Header: "v0.1 Scope — `[YOUR PROJECT NAME]`". In-scope table: columns Item, Notes — 5 placeholder rows. Out-of-scope table: columns Item, Target — 5 rows with `[Item]` and `Not planned` as placeholder content. Scope change log section (empty, with instructions: "Record any change to this scope document as a decision in DECISIONS.md."). |
| 26 | `starter-kit/blank/planning/releases/v0.1/release_notes.md` | Header: "v0.1 Release Notes — `[YOUR PROJECT NAME]`". Version field (`0.1.0`). Release name field (`[Name]`). Date field (`[Date]`). Summary section (placeholder). What's new section (placeholder bullet list, 3 items). Known issues section (placeholder). Instruction at top: "Write this file when the release is ready. It is not written during sprint work." |
| 27 | `starter-kit/blank/planning/releases/v0.1/retrospective.md` | Header: "v0.1 Retrospective — `[YOUR PROJECT NAME]`". Date field. Three sections: What worked (2 placeholder bullets), What needs attention (2 placeholder bullets), Rules added (1 placeholder rule). Instruction: "Write this file after v0.1 ships." |
| 28 | `starter-kit/blank/planning/features/_template/feature_brief.md` | Header: "Feature Brief — `[FEATURE NAME]`". Fields: Feature goal (`[one sentence]`), Operator impact (`[who benefits and how]`), Release (`[v0.1 / v0.2 / etc.]`). In-scope list (3 placeholder items). Out-of-scope list (2 placeholder items). Dependencies field (`[None / list]`). Acceptance criteria pointer (`[link to acceptance.md when written]`). |
| 29 | `starter-kit/blank/planning/features/_template/research.md` | Header: "Feature Research — `[FEATURE NAME]`". Fields: Question being answered, Mode (Research Mode). Findings section (3 placeholder bullets). Open items section (2 placeholder items). Recommendation field. |
| 30 | `starter-kit/blank/planning/features/_template/feasibility.md` | Header: "Feature Feasibility — `[FEATURE NAME]`". Approach options table: columns Approach, Pros, Cons — 3 placeholder rows. Risks section (2 placeholder items). Recommendation field (`[Chosen approach and reason]`). Constraints field. |
| 31 | `starter-kit/blank/planning/features/_template/validation.md` | Header: "Feature Validation — `[FEATURE NAME]`". Validation questions: 5-item checklist, each `[ ] [Validation question placeholder]`. Evidence required field. Verdict field (`[ ] Pass  [ ] Fail  [ ] Partial`). Follow-up items section. |
| 32 | `starter-kit/blank/planning/features/_template/sprint_map.md` | Header: "Sprint Map — `[FEATURE NAME]`". Sprint breakdown table: columns Sprint, Goal, Key files — 3 placeholder rows. Dependencies field. Estimated total sprints field. |
| 33 | `starter-kit/blank/planning/sprints/sprint_001/requirements.md` | Header: "Sprint 001 — Requirements". Fields: Sprint number, Title (`[Sprint title]`), Release, Mode, Branch pattern (`sprint/001-[description]`). Sprint goal: placeholder sentence. Context section: placeholder paragraph. In-scope table: columns File, Purpose — 5 placeholder rows. Out-of-scope table: 3 placeholder rows. Constraints: numbered list, 2 placeholder constraints. Success criteria pointer. |
| 34 | `starter-kit/blank/planning/sprints/sprint_001/blueprint.md` | Header: "Sprint 001 — Blueprint". Files-to-create table: columns File, Purpose — 5 placeholder rows. Files-to-modify table: columns File, Section(s) changed, Reason — 2 placeholder rows. Files-not-in-scope table: 2 placeholder rows with reason. |
| 35 | `starter-kit/blank/planning/sprints/sprint_001/blueprint_feedback.md` | Header: "Sprint 001 — Blueprint Feedback". Fields: Reviewer, Date. Section results table: columns Section, Verdict (Approved/Changes needed), Issues — 3 placeholder rows. Overall verdict field (`[ ] Approved  [ ] Changes needed`). Conditions field. Notes field. Instruction: "Fill this file after reviewing blueprint.md. If changes are needed, note them here before authorizing Develop Mode." |
| 36 | `starter-kit/blank/planning/sprints/sprint_001/acceptance.md` | Header: "Sprint 001 — Acceptance Criteria". Instruction line: "Work through each section. Check boxes only after directly verifying the stated condition — do not check based on the AI's description." Three numbered sections, 3 checkboxes each, all human-verifiable. Section 1: File existence checks. Section 2: Content quality checks. Section 3: Security checks. Each section has Issues found field. Sprint-complete statement at the bottom. |
| 37 | `starter-kit/blank/planning/sprints/sprint_001/dry_run.md` | Header: "Sprint 001 — Dry Run". Fields: Mode (Develop Mode), Permission Level (`[0–4]`), Sprint reference. Seven numbered content sections matching the 7-item definition: 1. Files to create (2 placeholder rows with File and Purpose columns), 2. Files to modify (2 placeholder rows with File and Change columns), 3. Files to move or delete (2 placeholder rows or "None"), 4. Commands to run (2 placeholder rows with Command and Purpose columns), 5. Dependencies requested (2 placeholder rows or "None"), 6. Risks (2 placeholder items), 7. Ambiguities (2 placeholder items). Stop instruction: "Dry run complete. Do not proceed. Await human authorization." |
| 38 | `starter-kit/blank/planning/sprints/sprint_001/dry_run_review.md` | Header: "Sprint 001 — Dry Run Review". Fields: Reviewer, Date. Section results for each of the 7 dry run content areas — one row per area with Verdict (Approved/Rejected/Conditional) and Notes. Overall verdict (`[ ] Approved  [ ] Rejected  [ ] Conditional`). Conditions field (for conditional approval). Authorization message field: pre-printed template — "Dry run approved. / Permission Level [LEVEL] authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md." — with instruction to copy and paste to the model only if Approved or Conditional with resolved conditions. |
| 39 | `starter-kit/blank/planning/sprints/sprint_001/implementation_log.md` | Header: "Sprint 001 — Implementation Log". Fields: Mode, Date, Session type. Phase table: columns Phase, Files, Notes — 3 placeholder rows. User actions section: table with Action, File affected, Notes columns — 1 placeholder row. Files not modified section: 2 placeholder rows. Summary table: rows Files created, Files modified, Issues found by audit, Issues resolved, Secrets committed (pre-filled: 0) — all other values placeholder. |
| 40 | `starter-kit/blank/planning/sprints/sprint_001/human_review.md` | Header: "Sprint 001 — Human Review". Fields: Sprint, Title, Reviewer (`[Your name]`), Review date (`[Date]`), Reference (pointer to acceptance.md). Instruction paragraph. Three section result blocks (matching the three sections in acceptance.md) each with Verdict (`[ ] Pass  [ ] Fail  [ ] Partial`) and Issues found field. Additional observations field. Items requiring follow-up table. STATE.md update checklist (3 checkboxes). Overall decision block: three mutually exclusive options (Approved, Approved with conditions, Not approved). Approval signature block. |
| 41 | `starter-kit/blank/planning/sprints/sprint_001/retrospective.md` | Header: "Sprint 001 — Retrospective". Fields: Sprint, Title, Date, Mode at close. What worked section: 2 placeholder items. What needs attention section: 2 placeholder items. Constraints added section: 1 placeholder constraint. Rules section: 1 placeholder rule. Next sprint section: 4 placeholder pre-conditions. |
| 42 | `starter-kit/blank/planning/sprints/sprint_001/rollback_log.md` | Header: "Sprint 001 — Rollback Log". Instructions: "Fill this file only if a rollback was required during this sprint. Leave blank if no rollbacks occurred." Table: columns Date, Change reverted, Reason, Files affected, Status — 2 placeholder rows. |

---

## Phase 3 — Example-filled starter kit (40 files)

All files in `starter-kit/example-filled/mini-task-tracker/` mirror the blank kit structure but are filled with Mini Task Tracker content. Files are created in the same order as Phase 2.

**Consistency requirements across all example-filled files:**
- Project name: "Mini Task Tracker"
- Short name: "MTT"
- Framework version: 3.5
- Starter kit version: 0.1.0
- Sprint dates: Sprint 001 opened 2026-06-01, closed 2026-06-07
- Mode references: Research Mode, Design Mode, Develop Mode only

| # | File | Key content (what makes it different from a placeholder) |
|---|---|---|
| 43 | `example-filled/mini-task-tracker/AGENTS.md` | Same structure as blank. All placeholders replaced: project name is "Mini Task Tracker". Safe-to-load list references MTT project brain files. Session opening protocol refers to MTT STATE.md. |
| 44 | `example-filled/mini-task-tracker/DOMAIN.md` | Project identity: Full name "Mini Task Tracker", Type "Local-only web app", Goal "Single operator task management with localStorage persistence". Scope: in-scope is core task list (add, complete, reopen, persist). Out-of-scope: user accounts, server storage, sharing, notifications, mobile app. Target operators: 1 row — Solo developer. Key entities: Task (id, title, status, created_at), TaskList (array of Tasks). Domain rules: 3 specific rules (tasks persist in localStorage, no backend, completed tasks can be reopened). |
| 45 | `example-filled/mini-task-tracker/STATE.md` | Active Scale: Sprint. Current Mode: None (between sessions). Active Release: v0.1 — Core Task List. Active Feature: Core task list. Active Sprint: Sprint 001 — Core task list (closed). Current Status: Sprint 001 complete. Next Step: Open Sprint 002 or begin handoff to next session. |
| 46 | `example-filled/mini-task-tracker/SECURITY.md` | Files never to load: standard list from blank. AI tools in use: 1 row — Claude (Anthropic), Design and Develop Mode sessions. Session hygiene rules: same as blank (pre-populated rules). |
| 47 | `example-filled/mini-task-tracker/DECISIONS.md` | Decision 001: "Use localStorage for persistence" — Status: Accepted. Decision 002: "Single-file HTML implementation" — Status: Accepted. Decision 003: "No build tool for v0.1" — Status: Accepted. Each with Context, Decision, Tradeoffs, Consequences sections filled with realistic Mini Task Tracker content. |
| 48 | `example-filled/mini-task-tracker/QUESTIONS.md` | Open questions: Q001 "Should completed tasks be archived or permanently deleted?" (Status: Open, Blocking: v0.2 scope, Raised: 2026-06-01). Resolved questions: Q002 "Should we use a framework?" (Resolved: No framework — vanilla JS only. Recorded in DECISIONS.md). |
| 49 | `example-filled/mini-task-tracker/RISKS.md` | Risk 001: localStorage size limit (Severity: Low). Risk 002: Data loss if browser data cleared (Severity: Medium). Risk 003: Scope creep to server-side persistence (Severity: Medium). Each with realistic mitigation text. |
| 50 | `example-filled/mini-task-tracker/COMMANDS.md` | Setup: `open index.html` — "Open the app in a browser. No server required." Development: `open index.html` — "Same as setup." Testing: `open index.html` — "Manual testing only. Check task CRUD and localStorage persistence." Deployment: `[None — local only in v0.1]`. |
| 51 | `example-filled/mini-task-tracker/STYLE_GUIDE.md` | Voice: direct, plain, no jargon. Canonical terminology: Task (not "item" or "todo"), TaskList (not "list"), Complete (not "done" or "finished"). File naming: lowercase, hyphens. |
| 52 | `example-filled/mini-task-tracker/GIT_STRATEGY.md` | Branch model: same as blank template (pre-populated). Commit convention: same. Release process: steps filled with MTT-specific commands (e.g., "Update VERSION.md with 0.1.0", "Tag: v0.1.0"). .gitignore minimums: same as blank. |
| 53 | `example-filled/mini-task-tracker/PROMPT_CHANGELOG.md` | v0.1.0: "All standard ADDF prompts — no project-specific modifications." |
| 54 | `example-filled/mini-task-tracker/START_HERE.md` | Same 15 steps as blank. All placeholders replaced with Mini Task Tracker content. Step 3 says "Fill AGENTS.md for the Mini Task Tracker." Step 9 says "Run Develop Mode at Permission Level 0." Version line: 0.1.0. |
| 55 | `example-filled/mini-task-tracker/docs/architecture.md` | Overview: "Single-page local app. One HTML file, one CSS file, one JS file. Runs in browser. No backend." Components: HTML (structure), CSS (layout and state display), JS module (task CRUD, localStorage). Data flow: User action → JS handler → localStorage update → DOM re-render. Key decisions: localStorage for persistence (see DECISIONS.md 001), no build tool (see DECISIONS.md 003). |
| 56 | `example-filled/mini-task-tracker/docs/data_model.md` | Entities: Task. Fields: id (string, UUID), title (string, 1–200 chars), status (enum: open, complete), created_at (ISO 8601 string). Relationships: none (flat list). Constraints: title required, status default open. |
| 57 | `example-filled/mini-task-tracker/docs/api.md` | Note at top: "Mini Task Tracker has no API. This file is a placeholder. Delete if not needed." All sections empty. |
| 58 | `example-filled/mini-task-tracker/docs/permissions.md` | Note at top: "Mini Task Tracker has no permission model — single operator only. This file is a placeholder. Delete if not needed." All sections empty. |
| 59 | `example-filled/mini-task-tracker/docs/validation.md` | Input validation rules: task title must not be empty, must not exceed 200 characters. Edge cases: whitespace-only title (reject), emoji in title (allow), duplicate title (allow). |
| 60 | `example-filled/mini-task-tracker/research/notes.md` | Research topic: "localStorage limits and browser compatibility". Findings: 5MB limit in most browsers; no cross-tab sync needed for single operator; JSON serialization is sufficient. Open items: confirm Safari behavior. |
| 61 | `example-filled/mini-task-tracker/research/sources.md` | 2 filled rows: MDN Web Docs localStorage article (accessed 2026-06-01, Relevance: High, Key point: 5MB limit), MDN Web Docs JSON.stringify article (accessed 2026-06-01, Relevance: Medium). |
| 62 | `example-filled/mini-task-tracker/research/open_questions.md` | 1 filled row: "What happens to tasks if localStorage is cleared?" (Blocking: v0.1 data loss handling, Raised: 2026-06-01, Owner: Operator). |
| 63 | `example-filled/mini-task-tracker/planning/backlog.md` | Sprint 001 — Core task list (`[DONE]`). Sprint 002 — Task filtering (`[PLANNED]`). Completed sprints table: Sprint 001, closed 2026-06-07. |
| 64 | `example-filled/mini-task-tracker/planning/releases/v0.1/release_plan.md` | Release goal: "A single operator can add, complete, reopen, and persist tasks in a local browser." Success criteria: 5 filled items matching the Mini Task Tracker acceptance criteria. Sprint breakdown: Sprint 001 listed as complete. |
| 65 | `example-filled/mini-task-tracker/planning/releases/v0.1/scope.md` | In-scope: add task, mark complete, reopen task, persist to localStorage, view all tasks. Out-of-scope: user accounts, server storage, sharing, filtering, search. |
| 66 | `example-filled/mini-task-tracker/planning/releases/v0.1/release_notes.md` | Instruction preserved: "Write at release time." Version 0.1.0 placeholder with Mini Task Tracker name. |
| 67 | `example-filled/mini-task-tracker/planning/releases/v0.1/retrospective.md` | Instruction preserved: "Write after v0.1 ships." Date and name placeholders with Mini Task Tracker name. |
| 68 | `example-filled/mini-task-tracker/planning/features/_template/feature_brief.md` | Same as blank template — feature templates are generic by design. Header updated to reflect MTT context. |
| 69 | `example-filled/mini-task-tracker/planning/features/_template/research.md` | Same as blank template. |
| 70 | `example-filled/mini-task-tracker/planning/features/_template/feasibility.md` | Same as blank template. |
| 71 | `example-filled/mini-task-tracker/planning/features/_template/validation.md` | Same as blank template. |
| 72 | `example-filled/mini-task-tracker/planning/features/_template/sprint_map.md` | Same as blank template. |
| 73 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/requirements.md` | Sprint goal: "Build the core task list: add tasks, mark complete, reopen, persist to localStorage." In-scope: index.html, style.css, app.js, AGENTS.md, DOMAIN.md, STATE.md, SECURITY.md, planning/. Out-of-scope: task filtering, task editing, server sync. Constraints: no framework, no build tool, no backend. |
| 74 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/blueprint.md` | Files to create: index.html (task list UI), style.css (layout), app.js (task CRUD + localStorage), planning/sprints/sprint_001/ files. Files to modify: AGENTS.md (session contract for develop mode), STATE.md (sprint active). Note: this is a Develop Mode sprint. Permission Level 1. |
| 75 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/blueprint_feedback.md` | Reviewer: Operator. Date: 2026-06-01. Section 1 (Files to create): Approved. Section 2 (Permission level): Approved. Section 3 (Out of scope): Approved. Overall: Approved. Notes: "Confirm app.js handles localStorage serialization before adding UI." |
| 76 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/acceptance.md` | Section 1 (File existence): index.html, style.css, app.js all exist. Section 2 (Task functionality): add task works, complete works, reopen works, localStorage persists across reload. Section 3 (Security): no API keys, no server paths, no hardcoded credentials. |
| 77 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/dry_run.md` | Files to create: index.html (HTML structure), style.css (layout), app.js (task CRUD + localStorage). Files to modify: STATE.md (active sprint). Files to move or delete: None. Commands to run: `open index.html` (manual browser test). Dependencies: None. Risks: localStorage serialization error if JSON malformed. Ambiguities: whether task IDs should be UUID or sequential integer. |
| 78 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/dry_run_review.md` | All 7 sections: Approved. Overall: Approved. Authorization message filled in: "Dry run approved. / Permission Level 1 authorized. / Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md." |
| 79 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/implementation_log.md` | Phase 1: Create index.html, style.css, app.js. Phase 2: Update STATE.md. Summary: Files created 3, Files modified 1, Issues found 0, Secrets committed 0. |
| 80 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/human_review.md` | All sections: Pass. Overall: Approved. Reviewer: Operator. Date: 2026-06-07. Notes: "All tasks persist correctly. Reopen works. No console errors." |
| 81 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/retrospective.md` | What worked: localStorage approach simple and sufficient; no-framework decision kept implementation fast. What needs attention: task ID strategy (sequential vs UUID) unresolved. Constraints added: None. Rules: "Test localStorage persistence before every sprint close." Next sprint: Sprint 002 — Task filtering. |
| 82 | `example-filled/mini-task-tracker/planning/sprints/sprint_001/rollback_log.md` | Instruction preserved. Table empty (no rollbacks occurred). |

---

## Phase 4 — Consistency audit

| # | File | Content specification |
|---|---|---|
| 83 | `planning/sprints/sprint_002/consistency_audit.md` | Per Constraint 001 (Sprint 001 retrospective): audit all generated files against framework documentation and requirements. Format matches `planning/sprints/sprint_001/consistency_audit.md`. Audit checks: (a) All blank kit mode names use Research Mode, Design Mode, Develop Mode only. (b) AGENTS.md dry run definition lists all 7 items. (c) AGENTS.md authorization message is verbatim correct. (d) Example-filled files are internally consistent (project name, version, dates). (e) No file contains ADDF-repo-specific content in the blank kit. (f) No secrets or machine-specific paths in any file. (g) Version 0.1.0 is visible in starter-kit/README.md and blank/START_HERE.md. Each file receives PASS / FAIL / WARNING verdict. |

---

## Files to modify

| File | Change | Reason |
|---|---|---|
| `planning/backlog.md` | Update Sprint 001 status from `[ACTIVE]` to `[DONE]`. Update Sprint 002 status from `[PLANNED]` to `[ACTIVE]`. Add Sprint 001 to completed sprints table (closed 2026-05-31). Add branch name for Sprint 002. | Sprint lifecycle tracking. |
| `STATE.md` | Update at sprint close: Active Sprint → Sprint 003 (or next sprint). Current Status → Sprint 002 complete. | Standard sprint close. Updated at close, not during implementation. |

---

## Files not in scope

| File | Reason |
|---|---|
| `examples/mini-task-tracker/` | Sprint 007. Separate artifact from the starter kit. |
| `prompts/` | Sprint 003. |
| Any file in `ADDF` project brain | Out of scope unless the consistency audit finds a correction that requires it. |
| Source code files (`.html`, `.css`, `.js`) | Never in Design Mode scope. |

---

## File count summary

| Category | Count |
|---|---|
| Supporting files (README + LICENSE) | 2 |
| Blank kit files | 40 |
| Example-filled kit files | 40 |
| Consistency audit | 1 |
| **Total new files** | **83** |
| Files to modify | 2 |

---

*ADDF · `planning/sprints/sprint_002/blueprint.md` · Design Mode · 2026-05-31*
