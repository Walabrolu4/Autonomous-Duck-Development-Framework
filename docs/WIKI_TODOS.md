# WIKI_TODOS.md — Temporary Task List

Tracks every action needed to go from the current state to a fully documented, cross-linked wiki inside `docs/`. Delete this file when all tasks are complete.

**Source of truth for all content:** `docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md`
**Authoring instructions for each page:** `docs/WIKI_GUIDE.md`
**Authoring style rules:** See the "Authoring Notes" section at the bottom of `WIKI_GUIDE.md`

---

## Current State

- [x] `docs/PDF/` — source document, PDF, and poster are here
- [x] `docs/old/` — old versions, ignore
- [x] `docs/WIKI_GUIDE.md` — page map and authoring instructions
- [x] `template/` — complete file template scaffold
- [x] `README.md` — root GitHub readme

---

## Phase 1 — Create the Folder and File Structure

> Goal: get every file created as an empty stub so links between pages can be written without breaking. Populate content later.

- [ ] Create folder `docs/lifecycle/`
- [ ] Create folder `docs/modes/`
- [ ] Create folder `docs/file-reference/`
- [ ] Create empty file `docs/index.md`
- [ ] Create empty file `docs/core-concepts.md`
- [ ] Create empty file `docs/getting-started.md`
- [ ] Create empty file `docs/example.md`
- [ ] Create empty file `docs/sprint-workflow.md`
- [ ] Create empty file `docs/orchestration.md`
- [ ] Create empty file `docs/setup.md`
- [ ] Create empty file `docs/prompts.md`
- [ ] Create empty file `docs/domain-adaptations.md`
- [ ] Create empty file `docs/troubleshooting.md`
- [ ] Create empty file `docs/quick-reference.md`
- [ ] Create empty file `docs/glossary.md`
- [ ] Create empty file `docs/lifecycle/index.md`
- [ ] Create empty file `docs/lifecycle/01-research.md`
- [ ] Create empty file `docs/lifecycle/02-initial-development.md`
- [ ] Create empty file `docs/lifecycle/03-testing.md`
- [ ] Create empty file `docs/lifecycle/04-documentation.md`
- [ ] Create empty file `docs/lifecycle/05-full-scale-development.md`
- [ ] Create empty file `docs/lifecycle/06-reflection-loop.md`
- [ ] Create empty file `docs/lifecycle/07-deployment.md`
- [ ] Create empty file `docs/lifecycle/08-resumption.md`
- [ ] Create empty file `docs/modes/index.md`
- [ ] Create empty file `docs/modes/quick-patch.md`
- [ ] Create empty file `docs/modes/feature-sprint.md`
- [ ] Create empty file `docs/modes/refactor-migration.md`
- [ ] Create empty file `docs/modes/data-ingestion.md`
- [ ] Create empty file `docs/modes/style-audit.md`
- [ ] Create empty file `docs/modes/parallel-sprints.md`
- [ ] Create empty file `docs/file-reference/index.md`
- [ ] Create empty file `docs/file-reference/agents.md`
- [ ] Create empty file `docs/file-reference/state.md`
- [ ] Create empty file `docs/file-reference/domain.md`
- [ ] Create empty file `docs/file-reference/decisions.md`
- [ ] Create empty file `docs/file-reference/commands.md`
- [ ] Create empty file `docs/file-reference/style-guide.md`
- [ ] Create empty file `docs/file-reference/security.md`
- [ ] Create empty file `docs/file-reference/git-strategy.md`
- [ ] Create empty file `docs/file-reference/prompt-changelog.md`
- [ ] Create empty file `docs/file-reference/sprint-files.md`
- [ ] Create empty file `docs/file-reference/planning-files.md`

---

## Phase 2 — Add Breadcrumb + See Also Stubs to Every File

> Before writing any real content, add the navigation skeleton to every file so the structure is visible. This also makes it easy to spot missing links later.

For every file in Phase 1, add:
- A breadcrumb line at the top (e.g. `[Home](../index.md) → [Lifecycle](index.md) → Step 1`)
- An `## See Also` section at the bottom with placeholder links

Specific breadcrumbs to write for each folder:

**Root pages** (`docs/*.md`): breadcrumb is simply `[Home](index.md)` except on `index.md` itself.

**Lifecycle pages** (`docs/lifecycle/*.md`): `[Home](../index.md) → [Lifecycle](index.md) → [Step Name]`

**Mode pages** (`docs/modes/*.md`): `[Home](../index.md) → [Operating Modes](index.md) → [Mode Name]`

**File reference pages** (`docs/file-reference/*.md`): `[Home](../index.md) → [File Reference](index.md) → [File Name]`

---

## Phase 3 — Populate: Glossary

> Populate first. All other pages link here for term definitions.
> Source: Section 16 of the framework doc.

- [ ] Write definition for **Acceptance Criteria** — include a link to `sprint-files.md#acceptance`
- [ ] Write definition for **ADR (Architecture Decision Record)** — include a link to `file-reference/decisions.md`
- [ ] Write definition for **Architect Mode** — include a link to `orchestration.md#architect-mode`
- [ ] Write definition for **Builder Mode** — include a link to `orchestration.md#builder-mode`
- [ ] Write definition for **Context Bleed** — include a link to `core-concepts.md`
- [ ] Write definition for **Context Engineering** — include a link to `core-concepts.md`
- [ ] Write definition for **Dry Run** — include a link to `file-reference/sprint-files.md#dry-run` and `prompts.md#dry-run`
- [ ] Write definition for **Harness-First Development** — include a link to `lifecycle/03-testing.md`
- [ ] Write definition for **Local File Sovereignty** — include a link to `orchestration.md#the-file-system`
- [ ] Write definition for **Mode** — include a link to `modes/index.md`
- [ ] Write definition for **Permission Level** — include a link to `orchestration.md#permission-levels`
- [ ] Write definition for **Sprint Pack** — include a link to `file-reference/sprint-files.md`
- [ ] Write definition for **Sovereign Brain** — include a link to `orchestration.md`
- [ ] Write definition for **State Reset** — include a link to `sprint-workflow.md#step-10`
- [ ] Write definition for **Vibe Coding** — include a link to `index.md`
- [ ] Verify all terms are in alphabetical order
- [ ] Verify every term links to at least one related page

---

## Phase 4 — Populate: Core Concepts

> Source: Section 3 of the framework doc.
> These are the 5 definitions every reader must understand before reading anything else.

- [ ] Write **Architect Mode** section — use Section 3's definition, link to `orchestration.md` for full detail, link to `glossary.md#architect-mode` for quick lookup
- [ ] Write **Builder Mode** section — use Section 3's definition, link to `orchestration.md`, link to `glossary.md#builder-mode`
- [ ] Write **Sprint Pack** section — name all three files (requirements.md, blueprint.md, acceptance.md), link to `file-reference/sprint-files.md`
- [ ] Write **Dry Run** section — explain the stop-and-wait mechanic, link to `sprint-workflow.md#step-3` and `prompts.md#dry-run`
- [ ] Write **Permission Level** section — list all 5 levels briefly, link to `orchestration.md#permission-levels` for the full table
- [ ] Write **Local File Sovereignty** section — explain what files survive (rate limits, model swaps, lost chats), link to `orchestration.md#the-file-system`
- [ ] Write **Context Engineering** section — distinguish it from "more context = better", link to `setup.md#context-loading`
- [ ] Write **State Reset** section — explain why closing the Builder thread matters, link to `sprint-workflow.md#step-10`
- [ ] Add footer tip directing readers to `glossary.md` for less-common terms

---

## Phase 5 — Populate: File Reference Pages

> Source: Section 11 of the framework doc for all templates.
> Populate these before lifecycle, modes, and sprint-workflow pages, since those pages link into file-reference.

### `docs/file-reference/index.md`
- [ ] Write "The Project Brain Files" intro paragraph
- [ ] Reproduce the Context Loading Protocol table from Section 10.5 (which files to load per session type)
- [ ] Add links to all 12 file pages

### `docs/file-reference/agents.md`
- [ ] Write **Purpose** section — one paragraph on what AGENTS.md does in every session
- [ ] Write **Template** section — reproduce the full template from Section 11.1 in a fenced code block
- [ ] Write **How to Customize It** section — explain that constraints from retrospectives are added here; use the empty-title example from Section 5, Step 6 as a concrete illustration
- [ ] Write **When It's Loaded** section — every single session, always first
- [ ] Add See Also: `getting-started.md`, `sprint-workflow.md`, `file-reference/index.md`

### `docs/file-reference/state.md`
- [ ] Write **Purpose** section — the living status board
- [ ] Write **Template** section — reproduce from Section 11.2 in a fenced code block
- [ ] Write **Completed Example** section — reproduce the initialized STATE.md from Section 10.4
- [ ] Write **The One Non-Negotiable Rule** section — quote "STATE.md must be updated at the close of every session without exception" and explain why
- [ ] Add See Also: `lifecycle/08-resumption.md`, `sprint-workflow.md#step-10`, `troubleshooting.md#state-out-of-date`

### `docs/file-reference/domain.md`
- [ ] Write **Purpose** section — what DOMAIN.md is and what the AI uses it for
- [ ] Write **Template** section — reproduce from Section 11.3 in a fenced code block
- [ ] Write **What Happens If You Skip It** section — explain improvisation bias; the AI fills gaps with plausible guesses that compound over time
- [ ] Write **Completed Example** link/section — reproduce or link to the Mini Task Tracker DOMAIN.md from Section 5, Step 1 (also in `example.md`)
- [ ] Add See Also: `example.md`, `getting-started.md#step-4`, `core-concepts.md`

### `docs/file-reference/decisions.md`
- [ ] Write **Purpose** section — the immutable ADR ledger
- [ ] Write **The Immutability Rule** section — decisions are never deleted, only superseded; explain why this matters for future AI sessions
- [ ] Write **Template (ADR Format)** section — reproduce from Section 11.4 in a fenced code block
- [ ] Write **Completed Example** section — reproduce the localStorage ADR from Section 5, Step 4
- [ ] Write **When a New Entry Is Required** section — list the triggers: new dependency, schema change, auth change, scope change
- [ ] Add See Also: `sprint-workflow.md#step-5`, `file-reference/index.md`

### `docs/file-reference/commands.md`
- [ ] Write **Purpose** section — every command the Builder needs to run, test, build, deploy, and roll back
- [ ] Write **Template** section — reproduce from Section 11.5 in a fenced code block
- [ ] Write **When to Fill It In** section — before writing any code; the Builder runs these for verification
- [ ] Write **Rollback Rule** callout — "rollback command must be documented before deployment, not after"
- [ ] Add See Also: `modes/refactor-migration.md`, `lifecycle/07-deployment.md`

### `docs/file-reference/style-guide.md`
- [ ] Write **Purpose** section
- [ ] Write **Template** section — reproduce from Section 11.6 in a fenced code block
- [ ] Write **What Requires Architect Approval** section — list the three triggers (schema changes, new dependencies, auth changes)
- [ ] Add See Also: `modes/style-audit.md`

### `docs/file-reference/security.md`
- [ ] Write **Purpose** section — highest-priority file; filled in before any other file
- [ ] Write **The Absolute Rule** section — reproduce the never-upload list verbatim; format as a clear callout block
- [ ] Write **Template** section — reproduce from Section 11.7 in a fenced code block
- [ ] Write **Redaction Protocol** section — the three-step process for Mode 4 files
- [ ] Add See Also: `modes/data-ingestion.md`, `getting-started.md#step-2`, `setup.md#security-protocol`

### `docs/file-reference/git-strategy.md`
- [ ] Write **Purpose** section
- [ ] Write **Template** section — reproduce from Section 11.8 in a fenced code block
- [ ] Write **Branch Rules** section — who commits to which branch and when
- [ ] Add See Also: `setup.md#git-branching`, `modes/quick-patch.md`

### `docs/file-reference/prompt-changelog.md`
- [ ] Write **Purpose** section — version history of all prompts used with the framework
- [ ] Write **Template** section — reproduce from Section 11.9 in a fenced code block
- [ ] Write **When to Add an Entry** section — any time a prompt in `prompts.md` is modified, deprecated, or added
- [ ] Add See Also: `prompts.md`

### `docs/file-reference/sprint-files.md`
- [ ] Write **The Sprint Folder Sequence** intro — explain how the 9 files map to the 10 steps of the sprint workflow; reference `sprint-workflow.md`
- [ ] Write **requirements.md** section — purpose + template from Section 11.10
- [ ] Write **blueprint.md** section — purpose + template from Section 11.11; note on the Architect Assumptions checklist
- [ ] Write **blueprint_feedback.md** section — purpose + template; when to use it (Step 2B)
- [ ] Write **acceptance.md** section — purpose + template from Section 11.12; link to completed example in `example.md`
- [ ] Write **dry_run.md** section — purpose + template from Section 11.13; emphasize the "STOPPED" line and why it must be there
- [ ] Write **implementation_log.md** section — purpose + template from Section 11.14; explain why raw terminal output must be pasted verbatim, not summarized
- [ ] Write **human_review.md** section — purpose + the five gates from Section 11.15 in full; all five must pass before committing
- [ ] Write **retrospective.md** section — purpose + template from Section 11.16; explain the feedback loop back to AGENTS.md
- [ ] Write **rollback_log.md** section — purpose + template from Section 11.17; note that Level 4 requires it, all others should use it
- [ ] Add See Also: `sprint-workflow.md`, `modes/feature-sprint.md`, `modes/refactor-migration.md`

### `docs/file-reference/planning-files.md`
- [ ] Write **backlog.md** section — purpose + template from Section 11.18; when items get added (retrospectives, mid-sprint discoveries)
- [ ] Write **FILE_INVENTORY.md** section — purpose + template; when to update it (after any sprint that creates or significantly modifies files)
- [ ] Add See Also: `lifecycle/06-reflection-loop.md`, `file-reference/index.md`

---

## Phase 6 — Populate: Prompt Catalog

> Source: Section 13 of the framework doc. Prompts are reproduced verbatim — no paraphrasing.
> Add a named anchor to each prompt heading so other pages can deep-link to individual prompts.

### `docs/prompts.md`
- [ ] Write **How to Use These Prompts** intro — distinguish Architect prompts vs Builder prompts; what to paste before each; what to do if no files exist yet
- [ ] Write **Persona Injector** section with anchor `{#persona-injector}` — full prompt block; note: paste at the start of any Architect session
- [ ] Write **Project Kickoff Interview** section with anchor `{#kickoff-interview}` — full prompt block; note: only prompt designed for use before any files exist
- [ ] Write **Resumption Prompt** section with anchor `{#resumption}` — full prompt block; list the three files to load before running it
- [ ] Write **Sprint Pack Generation** section with anchor `{#sprint-pack-generation}` — full prompt block; list files to load; note it outputs three files
- [ ] Write **Builder Pre-Flight Dry Run** section with anchor `{#dry-run}` — full prompt block; the "STOP" instruction must be bolded or called out
- [ ] Write **Architect Sanity Audit** section with anchor `{#sanity-audit}` — full prompt block; list the four files to paste in before running it
- [ ] Write **Builder Implementation Authorization** section with anchor `{#implementation-authorization}` — full prompt block; note it is used only after dry run approval
- [ ] Write **Architect Implementation Review** section with anchor `{#implementation-review}` — full prompt block; list the inputs
- [ ] Write **Cross-Sprint Consistency Audit** section with anchor `{#consistency-audit}` — full prompt block; note the every-third-sprint cadence
- [ ] Add See Also: `sprint-workflow.md`, `getting-started.md`, `orchestration.md`

---

## Phase 7 — Populate: Orchestration and Setup

### `docs/orchestration.md`
- [ ] Write **The Two Modes** intro paragraph — any LLM can play either role; mode not model is what matters
- [ ] Write **Architect Mode** section — what it runs in, what it produces, the "no source code" constraint, and the "why" explanation (collapsing planning/execution separation)
- [ ] Write **Builder Mode** section — what it runs in, what it produces, the "no invented logic" constraint, and the "why" (dry run pause = the entire safety model)
- [ ] Write **The File System: The Sovereign Brain** section — why models are interchangeable; "the files are the project, the AI is the tool"
- [ ] Write **Builder Permission Levels** section — reproduce the full 5-row table (Level 0–4); add guidance on when to use each level
- [ ] Write **Multi-CLI Protocol** section — models as interchangeable compute engines; Claude/Gemini/GPT CLI examples; note these are recommendations not requirements
- [ ] Write **Token Economics** section — compact payloads, splitting large lists, routing simple tasks to smaller models
- [ ] Add See Also: `core-concepts.md`, `sprint-workflow.md`, `file-reference/agents.md`

### `docs/setup.md`
- [ ] Write **Recommended Tooling** section — list Obsidian, VSCode, WSL, Git, Claude CLI, Gemini CLI, GPT CLI with one sentence each; include the "you don't need all of these on day one" note
- [ ] Write **Initializing the Directory** section — reproduce the full bash scaffold command block from Section 10.2; explain what each folder is for
- [ ] Write **Full Directory Structure** section — reproduce the annotated directory tree from Section 10.3
- [ ] Write **Populating Files in Order** section — reproduce the 8-file sequence and explain why the order matters (each file builds on the previous)
- [ ] Write **Context Loading Protocol** section — reproduce the session-type table from Section 10.5 exactly
- [ ] Write **Security and Secrets Protocol** section — reproduce the absolute rule as a callout block; include the .gitignore must-haves
- [ ] Write **Git Branching Protocol** section — reproduce the branch table (main/dev/sprint/refactor) and the four rules
- [ ] Add See Also: `file-reference/security.md`, `getting-started.md`, `file-reference/index.md`

---

## Phase 8 — Populate: Lifecycle Pages

> Source: Section 6 of the framework doc for all lifecycle content.
> Each step page follows the same heading pattern: Goal · Why This Phase Exists · The Tool · The Action · Output Files · The Rule.

### `docs/lifecycle/index.md`
- [ ] Write **What the Lifecycle Is** section — how the 8 steps relate to modes (lifecycle = map, mode = vehicle)
- [ ] Write **The 8 Steps at a Glance** section — describe or recreate the circular diagram; then list all 8 steps with one-line descriptions and the files each step produces or consumes
- [ ] Write **Lifecycle × Mode Mapping** table — reproduce the situation/mode/lifecycle phase table from Section 7
- [ ] Add links to all 8 step pages

### `docs/lifecycle/01-research.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Exists** section — every failure mode of AI-assisted development traces back to skipping this step
- [ ] Write **The Tool** section — Architect LLM; why Claude CLI is preferred for structured planning
- [ ] Write **The Action** section — feed raw ideas + run Project Kickoff Interview; link to `prompts.md#kickoff-interview`
- [ ] Write **Output Files Produced** section — list all 7 files
- [ ] Write **The Rule** section — do not proceed to Step 2 until DOMAIN.md has real business definitions and QUESTIONS.md has no sprint blockers
- [ ] Add See Also: `prompts.md#kickoff-interview`, `file-reference/domain.md`, `lifecycle/index.md`

### `docs/lifecycle/02-initial-development.md`
- [ ] Write **Goal** section
- [ ] Write **The Tools** section — Architect for blueprint, Builder for execution
- [ ] Write **The Action** section — the sequence: review ledger → generate sprint pack → blueprint review gate → Level 0 dry run → Architect audit → Level 1 build
- [ ] Write **The Rule** section — Builder generates only files in the blueprint, on the designated branch, no invented logic
- [ ] Write **Why the Builder Cannot Invent Business Logic** section — explain compounding invention; the dry run gate catches this before it happens
- [ ] Add See Also: `sprint-workflow.md`, `modes/feature-sprint.md`, `prompts.md#dry-run`

### `docs/lifecycle/03-testing.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Matters** section — most effective AI teams invert the testing habit; acceptance criteria before code
- [ ] Write **The Action** section — Builder writes unit tests before functional code; acceptance.md drives what must be proven
- [ ] Write **The Rule** section — Builder must run all COMMANDS.md commands and paste output into implementation_log.md; visual inspection is not acceptance
- [ ] Add See Also: `file-reference/sprint-files.md#acceptance`, `file-reference/sprint-files.md#implementation-log`, `file-reference/commands.md`

### `docs/lifecycle/04-documentation.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Matters** section — documentation debt; if context files fall out of sync, the AI improvises again
- [ ] Write **The Action** section — after every structural sprint, Architect updates docs/data_model.md and docs/api.md
- [ ] Write **The Rule** section — any change to data model, API contract, auth system, or external dependencies requires a new DECISIONS.md entry before the next sprint
- [ ] Add See Also: `file-reference/decisions.md`, `file-reference/index.md`

### `docs/lifecycle/05-full-scale-development.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Matters** section — improvisation bias compounds; Cross-Sprint Consistency Audit catches drift early
- [ ] Write **The Action** section — Mode 2 Feature Sprints in sequence; close Builder chat between sprints; consistency audit every third sprint
- [ ] Write **The Rule** section — each new Builder session loads only freshly updated STATE.md and current sprint folder; context reset is non-negotiable
- [ ] Write **Why Close the Builder Chat Between Sprints** section — explain context bleed accumulation; what "carryover noise" does to the next sprint
- [ ] Add See Also: `modes/feature-sprint.md`, `prompts.md#consistency-audit`, `sprint-workflow.md`

### `docs/lifecycle/06-reflection-loop.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Matters** section — AI tools repeat mistakes unless explicitly told not to; retrospective converts experience into guardrails
- [ ] Write **The Action** section — Architect reviews log loops; human fills retrospective metrics; constraints added to AGENTS.md; backlog triage; Builder thread closed
- [ ] Add See Also: `file-reference/sprint-files.md#retrospective`, `file-reference/agents.md#how-to-customize`, `file-reference/planning-files.md`

### `docs/lifecycle/07-deployment.md`
- [ ] Write **Goal** section
- [ ] Write **The Action** section — minor fixes = Mode 1; heavy migrations = Mode 3
- [ ] Write **The Rule** section — rollback commands must exist before deployment; RISKS.md mitigation plans must be specific
- [ ] Add See Also: `modes/quick-patch.md`, `modes/refactor-migration.md`, `file-reference/commands.md`, `file-reference/sprint-files.md#rollback-log`

### `docs/lifecycle/08-resumption.md`
- [ ] Write **Goal** section
- [ ] Write **Why This Phase Matters** section — project intelligence lives in files, not AI memory; nothing is reconstructed on return
- [ ] Write **The Action** section — update STATE.md before session close; load STATE.md + DOMAIN.md + AGENTS.md on return; run Resumption Prompt; link to `prompts.md#resumption`
- [ ] Write **The Rule** section — STATE.md must be updated at the close of every session without exception; quote it and explain this is the single most important habit
- [ ] Add See Also: `file-reference/state.md`, `prompts.md#resumption`, `troubleshooting.md#state-out-of-date`

---

## Phase 9 — Populate: Mode Pages

> Source: Section 7 of the framework doc.

### `docs/modes/index.md`
- [ ] Write **What a Mode Is** section — how modes differ from lifecycle phases
- [ ] Write **Mode Selection Table** — reproduce the full situation/mode/lifecycle phase table from Section 7
- [ ] Add links to all 6 mode pages

### `docs/modes/quick-patch.md`
- [ ] Write **Use For** section
- [ ] Write **Workflow / Rule** section — the 5-step sequence (open Builder → state change → mutate → verify → update STATE.md)
- [ ] Write **When NOT to Use This Mode** section — reproduce the "does this change require a blueprint?" boundary test in full; this is the most important part of this page
- [ ] Add See Also: `lifecycle/07-deployment.md`, `modes/feature-sprint.md`, `file-reference/commands.md`

### `docs/modes/feature-sprint.md`
- [ ] Write **Use For** section
- [ ] Write **Pre-Flight Checklist** section — list the five pre-flight conditions (no open blockers, Architect loaded, branch created, etc.)
- [ ] Write **Workflow** section — link to `sprint-workflow.md` as the authoritative step-by-step reference
- [ ] Add See Also: `sprint-workflow.md`, `lifecycle/05-full-scale-development.md`, `prompts.md#sprint-pack-generation`

### `docs/modes/refactor-migration.md`
- [ ] Write **Use For** section
- [ ] Write **Workflow / Rule** section — Builder at Level 3 or 4; Architect reviews implementation_log.md before merge; retrospective mandatory
- [ ] Write **Rollback Requirement** section — rollback_log.md must be pre-filled with current clean commit hash and rollback command before Builder begins; explain why (seconds not minutes)
- [ ] Add See Also: `file-reference/sprint-files.md#rollback-log`, `orchestration.md#permission-levels`, `lifecycle/07-deployment.md`

### `docs/modes/data-ingestion.md`
- [ ] Write **Use For** section
- [ ] Write **Security Gate** section — this comes first, always; PII replaced with synthetic placeholders, API keys replaced with [REDACTED], SECURITY.md never-share list checked
- [ ] Write **Workflow / Rule** section
- [ ] Add See Also: `file-reference/security.md`, `file-reference/agents.md`, `lifecycle/01-research.md`

### `docs/modes/style-audit.md`
- [ ] Write **Use For** section
- [ ] Write **Workflow / Rule** section
- [ ] Write **When It's Mandatory** section — before any production deployment
- [ ] Add See Also: `file-reference/style-guide.md`, `lifecycle/07-deployment.md`

### `docs/modes/parallel-sprints.md`
- [ ] Write **Use For** section
- [ ] Write **Conditions Required** section — reproduce the three conditions: zero overlapping files in blueprints, each has its own branch/folder/Builder session, Architect Sanity Audit confirms no overlap
- [ ] Write **Warning** section — reproduce the overlap consequence verbatim: "a single overlapping file in two blueprints can cause a merge conflict that invalidates both sprints. Use conservatively."
- [ ] Add See Also: `prompts.md#sanity-audit`, `modes/feature-sprint.md`, `sprint-workflow.md`

---

## Phase 10 — Populate: Sprint Workflow

### `docs/sprint-workflow.md`
- [ ] Write **Overview** section — what the sprint workflow is, which modes use it (2, 3, 4), what it produces; link to `modes/index.md`
- [ ] Write **Step 1 — Pre-Flight Gate** — what the human checks; the gate question; link to `file-reference/sprint-files.md` for the files being checked
- [ ] Write **Step 2 — Prime the Architect** — files to load; which prompt to run; link to `prompts.md#sprint-pack-generation`
- [ ] Write **Step 2B — Human Blueprint Review Gate** — the four questions to ask; what to do if an assumption is wrong; link to `file-reference/sprint-files.md#blueprint-feedback`
- [ ] Write **Step 3 — Pre-Flight Dry Run** — what the Builder produces; why it stops; the gate question; link to `prompts.md#dry-run`
- [ ] Write **Step 4 — Architect Sanity Audit** — what gets pasted in; what the Architect checks for; link to `prompts.md#sanity-audit`
- [ ] Write **Step 5 — Dependency Approval Gate** — why new dependencies need DECISIONS.md entries before the build; link to `file-reference/decisions.md`
- [ ] Write **Step 6 — Authorize and Build** — the authorization message; what the Builder produces; link to `prompts.md#implementation-authorization`
- [ ] Write **Step 7 — Run Verification** — why the human reads raw terminal output; "tests passed" can mean 1 test ran; link to `file-reference/sprint-files.md#implementation-log`
- [ ] Write **Step 8 — Architect Reviews Output** — what gets pasted in; link to `prompts.md#implementation-review`
- [ ] Write **Step 9 — Human Approval Gate** — the five gates from human_review.md; all five must pass; link to `file-reference/sprint-files.md#human-review`
- [ ] Write **Step 10 — Commit, Update, Reset** — the reset as non-optional; why closing the Builder thread matters; link to `file-reference/state.md`
- [ ] Add See Also: `modes/feature-sprint.md`, `file-reference/sprint-files.md`, `prompts.md`

---

## Phase 11 — Populate: Getting Started and Example

### `docs/getting-started.md`
- [ ] Write **What You'll Need** section — prerequisites and time estimate
- [ ] Write **Step 1 — Create the Project Folder** — show terminal command; explain each folder's purpose
- [ ] Write **Step 2 — Fill in SECURITY.md First** — explain why security comes first; show minimal starter content; link to `file-reference/security.md`
- [ ] Write **Step 3 — Fill in AGENTS.md** — direct to copy from `template/AGENTS.md`; one sentence on what it does; link to `file-reference/agents.md`
- [ ] Write **Step 4 — Write Your DOMAIN.md** — three-part structure; link to `example.md` as model; link to `file-reference/domain.md`
- [ ] Write **Step 5 — Run the Project Kickoff Interview** — show the short-form prompt; link to `prompts.md#kickoff-interview` for full version
- [ ] Write **Step 6 — Generate Your First Sprint Pack** — show the prompt; link to `prompts.md#sprint-pack-generation`
- [ ] Write **Step 7 — Run the Dry Run** — explain what it is and why; show prompt; link to `prompts.md#dry-run`
- [ ] Write **Step 8 — Authorize and Build** — show authorization message; link to `prompts.md#implementation-authorization`
- [ ] Write **Step 9 — Verify and Close** — human review gate and state reset; link to `sprint-workflow.md` for full future sprint detail
- [ ] Write **Next Steps** section — links to `lifecycle/index.md`, `modes/index.md`, `file-reference/index.md`
- [ ] Add See Also: `example.md`, `setup.md`, `core-concepts.md`

### `docs/example.md`
- [ ] Write **The Project** section — Mini Task Tracker description in 2–3 sentences
- [ ] Write **Step 1 — Research & Architecture** section — reproduce the completed DOMAIN.md; explain what the Architect produced
- [ ] Write **Step 2 — Initial Development** section — describe the Sprint 001 pack; link to `sprint-workflow.md`
- [ ] Write **Step 3 — Testing** section — the harness-first principle demonstrated
- [ ] Write **Step 4 — Documentation** section — reproduce the localStorage ADR; link to `file-reference/decisions.md`
- [ ] Write **Step 5 — Full-Scale Development** section — Sprint 002 and 003; consistency audit cadence
- [ ] Write **Step 6 — Reflection Loop** section — the empty-title bug; reproduce the exact constraint added to AGENTS.md
- [ ] Write **Step 7 — Deployment** section — build + rollback; Mode 1 Quick Patch example
- [ ] Write **Step 8 — Resumption** section — 3-week break scenario; Resumption Prompt result; link to `prompts.md#resumption`
- [ ] Write **Sprint 001 Acceptance Criteria (Full)** section — reproduce the complete acceptance.md from Section 5.2
- [ ] Add See Also: `getting-started.md`, `lifecycle/index.md`, `file-reference/domain.md`

---

## Phase 12 — Populate: Troubleshooting and Quick Reference

### `docs/troubleshooting.md`
- [ ] Write **The Builder Touches Files Outside the Blueprint** section — 5-step recovery; AGENTS.md constraint to add; link to `file-reference/agents.md`
- [ ] Write **You Realize Mid-Sprint the Blueprint Is Wrong** section — stop, revert, blueprint_feedback.md, re-run; link to `file-reference/sprint-files.md#blueprint-feedback`
- [ ] Write **You Hit a Rate Limit or Token Limit Mid-Session** section — save partial output, update STATE.md, open new session; why this is trivial to recover from
- [ ] Write **The Sprint Fails Acceptance Criteria** section — do not commit; return to Builder with failing output; when to return to Architect instead
- [ ] Write **The Blueprint Conflicts with DOMAIN.md** section — do not use the blueprint; when to update DOMAIN.md itself; link to `file-reference/domain.md`
- [ ] Write **STATE.md Is Out of Date When You Return** section — load existing files, run Resumption Prompt, update STATE.md manually; the prevention note; link to `prompts.md#resumption`
- [ ] Add See Also: `sprint-workflow.md`, `quick-reference.md`, `file-reference/state.md`

### `docs/quick-reference.md`
- [ ] Write **Before the First AI Session** checklist — reproduce the 5-item list from Section 14.1
- [ ] Write **Before Builder Writes Code** checklist — reproduce the 6-item list from Section 14.2
- [ ] Write **Before Committing a Sprint** checklist — reproduce the 6-item list from Section 14.3
- [ ] Add note: "For full detail on any item, see [Sprint Workflow](sprint-workflow.md)"
- [ ] Add See Also: `sprint-workflow.md`, `troubleshooting.md`, `file-reference/sprint-files.md`

---

## Phase 13 — Populate: Domain Adaptations

### `docs/domain-adaptations.md`
- [ ] Write **How the Framework Adapts** intro paragraph
- [ ] Write **Web Application (Next.js / React)** section — DOMAIN.md entity mapping, COMMANDS.md npm scripts, Architect treating each route as a domain boundary
- [ ] Write **Game Development (Unity / Godot)** section — DOMAIN.md as technical GDD, COMMANDS.md build/export commands per engine
- [ ] Write **Desktop Applications (Electron / Tauri)** section — local filesystem config in DOMAIN.md, SECURITY.md filesystem access definition requirement
- [ ] Write **Data Ingestion & Automation (Python ETL)** section — Mode 4 dependency, DOMAIN.md data shapes and rejection criteria, SECURITY.md upload constraints
- [ ] Write **Starter Template Library** section — `_templates/` folder convention; note that these are populated by you from completed projects, not pre-installed
- [ ] Add See Also: `modes/data-ingestion.md`, `setup.md`, `file-reference/security.md`

---

## Phase 14 — Populate: Home Page

> Write this last. All links must already exist before writing this page.

### `docs/index.md`
- [ ] Write **What Is the Autonomous Duck Deployment Framework?** section — 2–3 sentences; name the two core mechanisms
- [ ] Write **The Problem It Solves** section — the three failure modes; keep each to 1–2 sentences
- [ ] Write **The Central Rule** section — quote verbatim; one sentence of explanation
- [ ] Write **How to Navigate This Wiki** section — four suggested reader paths (new / starting project / mid-sprint / looking up a reference)
- [ ] Write **Quick Links** section — table or list of 6–8 most-used pages
- [ ] Add See Also: not applicable on the home page; instead link to all major sections in the Quick Links

---

## Phase 15 — Cross-Link Audit

> Once all pages are written, audit every page for missing or broken links.

- [ ] Read every page in `docs/lifecycle/` and verify every referenced file, mode, and prompt has a working link
- [ ] Read every page in `docs/modes/` and verify every referenced file, lifecycle step, and sprint file has a working link
- [ ] Read every page in `docs/file-reference/` and verify cross-references to other files are linked
- [ ] Read `docs/sprint-workflow.md` and verify all 10 steps link to the correct prompt and file reference
- [ ] Read `docs/prompts.md` and verify all named anchors (`{#...}`) are present and that other pages linking to them use the correct anchor
- [ ] Read `docs/getting-started.md` and verify every step links to the correct prompt and file reference page
- [ ] Read `docs/troubleshooting.md` and verify each scenario links to the relevant corrective pages
- [ ] Run a search for `](` across all docs files and manually check that no link points to a file that doesn't exist

---

## Phase 16 — Navigation and README Updates

- [ ] Update `README.md` at the project root — change the documentation link from pointing to `docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md` to pointing to `docs/index.md`
- [ ] Add a "Documentation" section to `README.md` with a brief description of the wiki structure and a link to `docs/index.md`
- [ ] Consider adding a `_sidebar.md` to `docs/` if the repo will use GitHub Wiki mode — this file controls the sidebar navigation panel that GitHub renders automatically
- [ ] If not using GitHub Wiki mode (i.e. docs live in the main repo), verify that GitHub renders `docs/index.md` correctly by checking relative links render as clickable in the GitHub file browser

---

## Phase 17 — Final Review

- [ ] Read `docs/index.md` as a first-time visitor — does it clearly explain what ADDF is and where to go?
- [ ] Read `docs/getting-started.md` end to end — can someone follow it without reading anything else first?
- [ ] Read `docs/quick-reference.md` — are all three checklists accurate against the current sprint workflow steps?
- [ ] Read `docs/glossary.md` — is every term used across the wiki defined here?
- [ ] Spot-check 3 file-reference pages — do the templates match what is in `template/`?
- [ ] Delete this file (`WIKI_TODOS.md`) once all tasks are complete

---

## Summary Count

| Phase | Tasks |
|-------|-------|
| 1 — Create folder and file structure | 43 tasks |
| 2 — Breadcrumb + See Also stubs | 35 files to touch |
| 3 — Glossary | 17 tasks |
| 4 — Core Concepts | 9 tasks |
| 5 — File Reference pages | 42 tasks |
| 6 — Prompt Catalog | 11 tasks |
| 7 — Orchestration + Setup | 15 tasks |
| 8 — Lifecycle pages | 36 tasks |
| 9 — Mode pages | 21 tasks |
| 10 — Sprint Workflow | 12 tasks |
| 11 — Getting Started + Example | 22 tasks |
| 12 — Troubleshooting + Quick Reference | 12 tasks |
| 13 — Domain Adaptations | 7 tasks |
| 14 — Home Page | 5 tasks |
| 15 — Cross-Link Audit | 8 tasks |
| 16 — Navigation + README | 4 tasks |
| 17 — Final Review | 6 tasks |
| **Total** | **~305 tasks** |
