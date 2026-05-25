# WIKI_GUIDE.md — Documentation Authoring Guide

This file is the blueprint for the ADDF wiki. It lists every page that needs to be written, every heading on that page, and instructions on what to write under each heading. The source of truth for all content is `docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md`.

**Do not write content in this file.** Write it in the target files listed below.

---

## Wiki Structure at a Glance

```
docs/
├── index.md                        # Home — entry point for the wiki
├── core-concepts.md                # Key terms every reader must understand first
├── getting-started.md              # Step-by-step first session walkthrough
├── example.md                      # Complete worked example (Mini Task Tracker)
├── sprint-workflow.md              # The daily operating loop (10 steps)
├── orchestration.md                # Architect vs Builder + permission levels
├── setup.md                        # Tooling, directory init, file population
├── prompts.md                      # All 9 copy-paste prompts
├── domain-adaptations.md           # Web app, game, desktop, data ingestion variants
├── troubleshooting.md              # When things go wrong (6 failure scenarios)
├── quick-reference.md              # The 3 checklists
├── glossary.md                     # Full definitions of all framework terms
├── lifecycle/
│   ├── index.md                    # The 8-step overview + diagram + mode mapping
│   ├── 01-research.md
│   ├── 02-initial-development.md
│   ├── 03-testing.md
│   ├── 04-documentation.md
│   ├── 05-full-scale-development.md
│   ├── 06-reflection-loop.md
│   ├── 07-deployment.md
│   └── 08-resumption.md
├── modes/
│   ├── index.md                    # Mode selection table + when to use which
│   ├── quick-patch.md
│   ├── feature-sprint.md
│   ├── refactor-migration.md
│   ├── data-ingestion.md
│   ├── style-audit.md
│   └── parallel-sprints.md
└── file-reference/
    ├── index.md                    # All files, their roles, context loading table
    ├── agents.md
    ├── state.md
    ├── domain.md
    ├── decisions.md
    ├── commands.md
    ├── style-guide.md
    ├── security.md
    ├── git-strategy.md
    ├── prompt-changelog.md
    ├── sprint-files.md             # All 9 sprint folder files on one page
    └── planning-files.md           # backlog.md and FILE_INVENTORY.md
```

**Total pages to write: 35**

---

## Linking Convention

Use relative links between pages. Examples:

- From `docs/index.md` to a lifecycle step: `[Step 1](lifecycle/01-research.md)`
- From `docs/lifecycle/01-research.md` back to home: `[Home](../index.md)`
- From `docs/modes/quick-patch.md` to a file reference: `[STATE.md](../file-reference/state.md)`

Every page should have a **breadcrumb line** at the top and a **"See also"** section at the bottom linking to closely related pages.

---

---

# ROOT PAGES

---

## `docs/index.md` — Home

The entry point. A reader landing here from GitHub should immediately understand what ADDF is, why it exists, and where to go next.

### Headings

**What Is the Autonomous Duck Deployment Framework?**
> Write 2–3 sentences: a system for AI-assisted development built around local Markdown files. Name the two core mechanisms (Local File Sovereignty + Dual-Mode Orchestration). Source: Section 2 of the framework doc ("The Framework in One Page").

**The Problem It Solves**
> Name the three failure modes of vibe coding: context bleed, improvisation bias, and the missing anchor. Keep each to 1–2 sentences. Source: Section 1.1.

**The Central Rule**
> Quote the central rule verbatim, then one sentence of explanation. Source: Section 1.4.

**How to Navigate This Wiki**
> A short paragraph directing readers to the right starting point depending on their goal. Suggested paths: "New to ADDF → [Getting Started](getting-started.md)", "Starting a project → [Setup](setup.md)", "Mid-sprint → [Sprint Workflow](sprint-workflow.md)", "Looking up a file → [File Reference](file-reference/index.md)", "Looking up a prompt → [Prompts](prompts.md)".

**Quick Links**
> A simple table or list of the most-used pages. Not a duplicate of the sidebar — just the 6–8 pages people reach for most often.

---

## `docs/core-concepts.md` — Core Concepts

Every framework term used across all other pages is defined here first. Other pages should link here rather than re-defining terms inline.

### Headings

**Architect Mode**
> Define it: the planning mode. An LLM invoked to produce requirements, blueprints, and acceptance criteria. It never writes source code. Source: Section 3 and Section 9.

**Builder Mode**
> Define it: the implementation mode. Writes source code against an approved blueprint. Always runs a dry run first and stops. Source: Section 3 and Section 9.

**Sprint Pack**
> Define it: the three files that define a sprint — requirements.md, blueprint.md, acceptance.md. Source: Section 3.

**Dry Run**
> Define it: a read-only report from the Builder listing every file it intends to touch, before touching anything. Source: Section 3.

**Permission Level**
> Define it: a number 0–4 assigned by the human operator that limits what the Builder may do. Source: Section 3 and Section 9.2.

**Local File Sovereignty**
> Define it: the principle that project memory lives in local Markdown files controlled by the human operator, not in any AI chat session. Source: Section 1.3 and Section 9.1.

**Context Engineering**
> Define it: the practice of organizing project knowledge into clean, modular files rather than relying on long chat history. Source: Section 1.3.

**State Reset**
> Define it: closing the Builder chat after a sprint so the next sprint starts from clean file-based context, not accumulated conversation noise. Source: Section 16.

> *Tip: This page doubles as a lightweight glossary for quick lookups. The full expanded glossary with all terms is at [Glossary](glossary.md).*

---

## `docs/getting-started.md` — Getting Started

A concrete, step-by-step script for a reader's very first ADDF session. Should feel like a tutorial, not a reference page.

### Headings

**What You'll Need**
> List prerequisites: any capable LLM, a text/code editor, a terminal. Mention time estimate (~30–45 minutes). Source: Section 4 intro.

**Step 1 — Create the Project Folder**
> Show the terminal command from Section 4, Step 1. Explain what each folder is for in plain language.

**Step 2 — Fill in SECURITY.md First**
> Explain why security comes first (every file created after this may be uploaded to an AI). Show the minimal starter content. Source: Section 4, Step 2.

**Step 3 — Fill in AGENTS.md**
> Direct the reader to copy the template from [AGENTS.md reference](file-reference/agents.md). Explain what the file does in one sentence. Source: Section 4, Step 3.

**Step 4 — Write Your DOMAIN.md**
> Explain the three-part structure (what it does, core entities, out of scope). Link to the [Mini Task Tracker example](example.md) as a model. Source: Section 4, Step 4.

**Step 5 — Run the Project Kickoff Interview**
> Show the prompt to paste (short version with a link to the full prompt at [Prompts](prompts.md#kickoff-interview)). Explain what Architect Mode is doing here. Source: Section 4, Step 5.

**Step 6 — Generate Your First Sprint Pack**
> Show the sprint generation prompt. Link to [Sprint Pack Generation](prompts.md#sprint-pack-generation). Source: Section 4, Step 6.

**Step 7 — Run the Dry Run**
> Explain what the dry run is and why it exists. Show the dry run prompt. Link to [Dry Run](prompts.md#dry-run). Source: Section 4, Step 7.

**Step 8 — Authorize and Build**
> Show the authorization message. Link to [Builder Implementation Authorization](prompts.md#implementation-authorization). Source: Section 4, Step 8.

**Step 9 — Verify and Close**
> Explain the human review gate and state reset. Link to [Sprint Workflow](sprint-workflow.md) for full detail on future sprints. Source: Section 4, Step 9.

**Next Steps**
> Link to [The Lifecycle](lifecycle/index.md) and [Operating Modes](modes/index.md).

---

## `docs/example.md` — Complete Example: Mini Task Tracker

A worked example showing the entire framework applied to a small real project. Readers who prefer learning by example should be directed here early.

### Headings

**The Project**
> Describe the Mini Task Tracker in 2–3 sentences: what it is, what it does, what it deliberately doesn't do. Source: Section 5 intro.

**Step 1 — Research & Architecture**
> Show the completed DOMAIN.md for the Mini Task Tracker. Explain what the Architect produced from it. Source: Section 5, Step 1.

**Step 2 — Initial Development**
> Describe the Sprint 001 pack the Architect generated: requirements, blueprint summary, acceptance criteria reference. Source: Section 5, Step 2.

**Step 3 — Testing**
> Explain the harness-first principle as demonstrated in this example. Source: Section 5, Step 3.

**Step 4 — Documentation**
> Show the completed DECISIONS.md entry (localStorage decision). Explain why it's recorded this way. Source: Section 5, Step 4.

**Step 5 — Full-Scale Development**
> Describe Sprint 002 (filters) and Sprint 003 (edit title). Mention the Cross-Sprint Consistency Audit cadence. Source: Section 5, Step 5.

**Step 6 — Reflection Loop**
> Show the empty-title bug found in Sprint 002 and the exact constraint added to AGENTS.md as a result. Source: Section 5, Step 6.

**Step 7 — Deployment**
> Describe the build + rollback command addition and the Mode 1 Quick Patch example. Source: Section 5, Step 7.

**Step 8 — Resumption**
> Show the resumption scenario (3-week break) and the Resumption Prompt result. Source: Section 5, Step 8.

**Sprint 001 Acceptance Criteria (Full)**
> Reproduce the complete acceptance.md from Section 5.2.

---

## `docs/sprint-workflow.md` — Sprint Workflow

The daily operating loop. Every sprint (Mode 2, 3, and 4) follows these 10 steps. This page is the one practitioners will return to most often mid-sprint.

### Headings

**Overview**
> One paragraph: what the sprint workflow is, which modes use it, and what it produces. Link to [Operating Modes](modes/index.md).

**Step 1 — Pre-Flight Gate**
> What the human checks before calling the Architect. The gate question to ask yourself. Source: Section 8, Step 1.

**Step 2 — Prime the Architect**
> What files to load, which prompt to run. Link to [Sprint Pack Generation prompt](prompts.md#sprint-pack-generation). Source: Section 8, Step 2.

**Step 2B — Human Blueprint Review Gate**
> The four questions to ask before approving a blueprint. What to do if an assumption is wrong. Source: Section 8, Step 2B.

**Step 3 — Pre-Flight Dry Run**
> What the Builder produces, why it stops. The gate question. Link to [Dry Run prompt](prompts.md#dry-run). Source: Section 8, Step 3.

**Step 4 — Architect Sanity Audit**
> What gets pasted in, what the Architect checks for. Link to [Sanity Audit prompt](prompts.md#sanity-audit). Source: Section 8, Step 4.

**Step 5 — Dependency Approval Gate**
> Why new dependencies need DECISIONS.md entries before the build. Source: Section 8, Step 5.

**Step 6 — Authorize and Build**
> The authorization message and what the Builder produces. Link to [Authorization prompt](prompts.md#implementation-authorization). Source: Section 8, Step 6.

**Step 7 — Run Verification**
> Why the human reads raw terminal output, not summaries. Source: Section 8, Step 7.

**Step 8 — Architect Reviews Output**
> What gets pasted in, what the Architect returns. Link to [Implementation Review prompt](prompts.md#implementation-review). Source: Section 8, Step 8.

**Step 9 — Human Approval Gate**
> The five gates from human_review.md. All five must pass. Source: Section 8, Step 9.

**Step 10 — Commit, Update, Reset**
> The reset as a non-optional step. Why closing the Builder thread matters. Source: Section 8, Step 10.

---

## `docs/orchestration.md` — Dual-Mode Orchestration

How Architect Mode and Builder Mode work together, why they're separate, and what the file system's role is in keeping them coordinated.

### Headings

**The Two Modes**
> Short intro: any LLM can play either role — what matters is mode, not model. Source: Section 9 intro.

**Architect Mode**
> What it runs in, what it produces, its strict constraint (no source code). The "why" — if the Architect writes code, the planning/execution separation collapses. Source: Section 9, Architect Mode.

**Builder Mode**
> What it runs in, what it produces, its strict constraint (no invented business logic, must stop after dry run). The "why" — the dry run pause is the entire safety model. Source: Section 9, Builder Mode.

**The File System: The Sovereign Brain**
> Why Local File Sovereignty makes models interchangeable. The key implication: the files are the project, the AI is the tool. Source: Section 9.1.

**Builder Permission Levels**
> Reproduce the permission level table (0–4). When to use each level. Source: Section 9.2.

**Multi-CLI Protocol and Compute Agnosticism**
> Explain that different models can be used for different tasks because the same local files feed all of them. The Claude/Gemini/GPT CLI examples. Source: Section 9.3.

**Token Economics**
> Short section: compact payloads, splitting large lists, routing simple tasks to smaller models. Source: Section 9.4.

---

## `docs/setup.md` — Setup and Scaffolding

Everything needed to initialize a new project directory from scratch.

### Headings

**Recommended Tooling**
> List the tools (Obsidian, VSCode, WSL, Git, CLIs) with a sentence on each. The "you don't need all of these on day one" note. Source: Section 10.1.

**Initializing the Directory**
> The full bash scaffold command block. Explain what each folder is for. Source: Section 10.2.

**Full Directory Structure**
> Reproduce the annotated directory tree. Source: Section 10.3.

**Populating Files in Order**
> The 8-file sequence and why order matters. Each file builds on the previous. Source: Section 10.4.

**Context Loading Protocol**
> The table: which files to load for each session type (Architect Planning, Builder Implementation, Audit Verification, Data Ingestion, Style Check). Source: Section 10.5.

**Security and Secrets Protocol**
> The absolute rule and the redaction protocol for Mode 4. Source: Section 10.6.

**Git Branching Protocol**
> The branch table (main / dev / sprint / refactor) and the rules. Source: Section 10.7.

---

## `docs/prompts.md` — Prompt Catalog

All 9 copy-paste prompts. Each prompt gets its own named anchor so other pages can link directly to it (e.g., `prompts.md#kickoff-interview`).

### Headings

**How to Use These Prompts**
> Short intro: which prompts are for Architect sessions, which are for Builder sessions, what to paste before each. Source: Section 13 intro.

**Persona Injector** `{#persona-injector}`
> The prompt block. When to use it (start of any Architect session). Source: Section 13.1.

**Project Kickoff Interview** `{#kickoff-interview}`
> The prompt block. When to use it (first session only, before any files exist). Source: Section 13.2.

**Resumption Prompt** `{#resumption}`
> The prompt block. Files to load before using it. Source: Section 13.3.

**Sprint Pack Generation** `{#sprint-pack-generation}`
> The prompt block. Files to load before using it. Source: Section 13.4.

**Builder Pre-Flight Dry Run** `{#dry-run}`
> The prompt block. The critical instruction: Builder must stop after producing dry_run.md. Source: Section 13.5.

**Architect Sanity Audit** `{#sanity-audit}`
> The prompt block. Files to paste in before running it. Source: Section 13.6.

**Builder Implementation Authorization** `{#implementation-authorization}`
> The prompt block. Used after dry run is approved. Source: Section 13.7.

**Architect Implementation Review** `{#implementation-review}`
> The prompt block. Used after Builder completes, before human gate. Source: Section 13.8.

**Cross-Sprint Consistency Audit** `{#consistency-audit}`
> The prompt block. Cadence: every third sprint. Source: Section 13.9.

---

## `docs/domain-adaptations.md` — Domain Adaptations

How to adjust DOMAIN.md, COMMANDS.md, and STYLE_GUIDE.md content for different project types.

### Headings

**How the Framework Adapts**
> One paragraph: the structure is identical across all project types — only the content of the key files changes. Source: Section 12.1 intro.

**Web Application (Next.js / React)**
> What changes in DOMAIN.md (routes, API endpoints, context components), COMMANDS.md (npm scripts), and how the Architect treats each route. Source: Section 12.1.

**Game Development (Unity / Godot)**
> DOMAIN.md as a technical Game Design Document. What COMMANDS.md includes for each engine. Source: Section 12.1.

**Desktop Applications (Electron / Tauri)**
> The local filesystem configuration requirement in DOMAIN.md. The SECURITY.md filesystem access definition. Source: Section 12.1.

**Data Ingestion & Automation (Python ETL)**
> Mode 4 dependency. DOMAIN.md data shapes and rejection criteria. SECURITY.md upload constraints. Source: Section 12.1.

**Starter Template Library**
> The `_templates/` folder structure and the convention for populating it from completed projects. Source: Section 12.2.

---

## `docs/troubleshooting.md` — Troubleshooting

What to do when something goes wrong. Each scenario is self-contained so readers can jump directly to the one they need.

### Headings

**The Builder Touches Files Outside the Blueprint**
> The 5-step recovery. The constraint to add to AGENTS.md. Source: Section 15.1.

**You Realize Mid-Sprint the Blueprint Is Wrong**
> Stop immediately, revert, use blueprint_feedback.md, re-run. Why catching it early saves time. Source: Section 15.2.

**You Hit a Rate Limit or Token Limit Mid-Session**
> Save partial output, update STATE.md, open a new session with any model. Why this is trivial to recover from. Source: Section 15.3.

**The Sprint Fails Acceptance Criteria**
> Do not commit. Record failure in implementation_log.md. Return to Builder with constraints. When to return to Architect instead. Source: Section 15.4.

**The Blueprint Conflicts with DOMAIN.md**
> Do not use the blueprint. Quote the conflicting rule in blueprint_feedback.md. When to update DOMAIN.md itself. Source: Section 15.5.

**STATE.md Is Out of Date When You Return**
> Load what exists, run Resumption Prompt to reconstruct, update STATE.md manually. The prevention note. Source: Section 15.6.

---

## `docs/quick-reference.md` — Quick Reference

Three short checklists for the three most critical moments. Should be printable.

### Headings

**Before the First AI Session**
> The 5-item checklist. Source: Section 14.1.

**Before Builder Writes Code**
> The 6-item checklist. Source: Section 14.2.

**Before Committing a Sprint**
> The 6-item checklist. Source: Section 14.3.

---

## `docs/glossary.md` — Glossary

Full definitions for all framework terms. Pages across the wiki link here for term definitions.

### Headings

Use one `###` heading per term, listed alphabetically. Terms to cover (at minimum):

- Acceptance Criteria
- ADR (Architecture Decision Record)
- Architect Mode
- Builder Mode
- Context Bleed
- Context Engineering
- Dry Run
- Harness-First Development
- Local File Sovereignty
- Mode
- Permission Level
- Sprint Pack
- Sovereign Brain
- State Reset
- Vibe Coding

> Source: Section 16 of the framework doc. Expand each definition with a "See also" link to the relevant page where the concept is used in practice.

---

---

# LIFECYCLE PAGES

---

## `docs/lifecycle/index.md` — The 8-Step Lifecycle: Overview

### Headings

**What the Lifecycle Is**
> How the 8 steps relate to Operating Modes. The lifecycle is the map; the mode is the vehicle. Source: Section 6 intro.

**The 8 Steps at a Glance**
> Reproduce or describe the circular diagram. Then list all 8 steps with a one-line description and the key files each step produces or consumes. Source: Section 6, bullet list.

**Lifecycle × Mode Mapping**
> A table showing which lifecycle phase typically uses which operating mode. Source: Section 7 table (Situation / Mode / Lifecycle Phase).

**Step Pages**
> Links to all 8 step pages.

---

## `docs/lifecycle/01-research.md` — Step 1: Research & Global Architecture

### Headings

**Goal** · **Why This Phase Exists** · **The Tool** · **The Action** · **Output Files Produced** · **The Rule**

> Source: Section 6, Step 1. Each heading gets the corresponding paragraph from the doc.

---

## `docs/lifecycle/02-initial-development.md` — Step 2: Initial Development

### Headings

**Goal** · **The Tools** · **The Action** · **The Rule** · **Why the Builder Cannot Invent Business Logic**

> Source: Section 6, Step 2.

---

## `docs/lifecycle/03-testing.md` — Step 3: Testing

### Headings

**Goal** · **Why This Phase Matters** · **The Action** · **The Rule**

> Source: Section 6, Step 3.

---

## `docs/lifecycle/04-documentation.md` — Step 4: Documentation

### Headings

**Goal** · **Why This Phase Matters** · **The Action** · **The Rule**

> Source: Section 6, Step 4.

---

## `docs/lifecycle/05-full-scale-development.md` — Step 5: Full-Scale Development

### Headings

**Goal** · **Why This Phase Matters** · **The Action** · **The Rule** · **Why Close the Builder Chat Between Sprints**

> Source: Section 6, Step 5.

---

## `docs/lifecycle/06-reflection-loop.md` — Step 6: The Reflection Loop

### Headings

**Goal** · **Why This Phase Matters** · **The Action**

> Source: Section 6, Step 6.

---

## `docs/lifecycle/07-deployment.md` — Step 7: Deployment & Maintenance

### Headings

**Goal** · **The Action** · **The Rule**

> Source: Section 6, Step 7.

---

## `docs/lifecycle/08-resumption.md` — Step 8: Resumption

### Headings

**Goal** · **Why This Phase Matters** · **The Action** · **The Rule**

> Source: Section 6, Step 8.

---

---

# MODE PAGES

---

## `docs/modes/index.md` — Operating Modes: Overview

### Headings

**What a Mode Is**
> How modes differ from lifecycle phases. One describes where you are in the project; the other describes how you handle the task in front of you. Source: Section 7 intro.

**Mode Selection Table**
> Reproduce the situation/mode/lifecycle phase table. Source: Section 7 table.

**Mode Pages**
> Links to all mode pages.

---

## `docs/modes/quick-patch.md` — Mode 1: Quick Patch

### Headings

**Use For** · **Workflow / Rule** · **When NOT to Use This Mode**

> Source: Section 7.1. The "when not to use" paragraph is important — reproduce it in full.

---

## `docs/modes/feature-sprint.md` — Mode 2: Feature Sprint

### Headings

**Use For** · **Pre-Flight Checklist** · **Workflow**

> Source: Section 7.2. Link to [Sprint Workflow](../sprint-workflow.md) for the full 10-step loop.

---

## `docs/modes/refactor-migration.md` — Mode 3: Refactor / Migration

### Headings

**Use For** · **Workflow / Rule** · **Rollback Requirement**

> Source: Section 7.3. Emphasize the rollback_log.md requirement before the Builder begins.

---

## `docs/modes/data-ingestion.md` — Mode 4: Data Ingestion / Discovery

### Headings

**Use For** · **Workflow / Rule** · **Security Gate**

> Source: Section 7.4. The security gate (PII redaction, SECURITY.md check) must come first.

---

## `docs/modes/style-audit.md` — Mode 5: Style Audit

### Headings

**Use For** · **Workflow / Rule** · **When It's Mandatory**

> Source: Section 7.5.

---

## `docs/modes/parallel-sprints.md` — Parallel Sprints

### Headings

**Use For** · **Conditions Required** · **Warning**

> Source: Section 7.6. The overlap warning is important — reproduce the consequence of a single overlapping file.

---

---

# FILE REFERENCE PAGES

---

## `docs/file-reference/index.md` — File Reference: Overview

### Headings

**The Project Brain Files**
> Brief description of the root tracking files and their collective role. 2–3 sentences.

**Context Loading Table**
> Reproduce the table from Section 10.5: which files to load per session type. This is the most useful single reference for practitioners.

**File Pages**
> Links to all individual file pages.

---

## `docs/file-reference/agents.md` — AGENTS.md

### Headings

**Purpose** · **Template** · **How to Customize It** · **When It's Loaded**

> Source: Section 11.1. "How to customize" should explain that constraints discovered in retrospectives get added here — reference the Mini Task Tracker empty-title example from Section 5, Step 6.

---

## `docs/file-reference/state.md` — STATE.md

### Headings

**Purpose** · **Template** · **The One Non-Negotiable Rule**

> Source: Section 11.2. The rule: STATE.md must be updated at the close of every session without exception. Quote Section 6, Step 8's rule verbatim.

---

## `docs/file-reference/domain.md` — DOMAIN.md

### Headings

**Purpose** · **Template** · **What Happens If You Skip It** · **Completed Example**

> Source: Section 11.3. "What happens if you skip it" = the AI invents. Link to [example.md](../example.md) for the full Mini Task Tracker DOMAIN.md.

---

## `docs/file-reference/decisions.md` — DECISIONS.md

### Headings

**Purpose** · **Template (ADR Format)** · **The Immutability Rule** · **Completed Example**

> Source: Section 11.4. The immutability rule: decisions are never deleted, only superseded. Show the localStorage ADR from Section 5, Step 4.

---

## `docs/file-reference/commands.md` — COMMANDS.md

### Headings

**Purpose** · **Template** · **When to Fill It In**

> Source: Section 11.5. Emphasize: rollback command must exist before deployment, not after.

---

## `docs/file-reference/style-guide.md` — STYLE_GUIDE.md

### Headings

**Purpose** · **Template** · **What Requires Architect Approval**

> Source: Section 11.6.

---

## `docs/file-reference/security.md` — SECURITY.md

### Headings

**Purpose** · **The Absolute Rule** · **Template** · **Redaction Protocol**

> Source: Section 11.7 and Section 10.6. This is the highest-priority file — fill it in before any other file.

---

## `docs/file-reference/git-strategy.md` — GIT_STRATEGY.md

### Headings

**Purpose** · **Template** · **Branch Rules**

> Source: Section 11.8.

---

## `docs/file-reference/prompt-changelog.md` — PROMPT_CHANGELOG.md

### Headings

**Purpose** · **Template** · **When to Add an Entry**

> Source: Section 11.9.

---

## `docs/file-reference/sprint-files.md` — Sprint Files

All 9 files that live inside a `planning/sprints/sprint_NNN/` folder. One page covers all of them so readers see how they fit together as a sequence.

### Headings

**The Sprint Folder Sequence**
> A short paragraph explaining how the 9 files relate to the 10-step Sprint Workflow. Each file is a stage in the loop.

**requirements.md**
> Purpose + template. Source: Section 11.10.

**blueprint.md**
> Purpose + template + note on the Architect Assumptions section. Source: Section 11.11.

**blueprint_feedback.md**
> Purpose + template. When to use it (Step 2B of the Sprint Workflow). Source: template file we created.

**acceptance.md**
> Purpose + template + completed example link. Source: Section 11.12 and Section 5.2.

**dry_run.md**
> Purpose + template + the critical "STOPPED" instruction. Source: Section 11.13.

**implementation_log.md**
> Purpose + template + why raw terminal output must be pasted verbatim. Source: Section 11.14.

**human_review.md**
> Purpose + the five gates in full. Source: Section 11.15.

**retrospective.md**
> Purpose + template + how findings feed back into AGENTS.md. Source: Section 11.16.

**rollback_log.md**
> Purpose + template + when it's required (Level 4) vs recommended (all others). Source: Section 11.17.

---

## `docs/file-reference/planning-files.md` — Planning Files

### Headings

**backlog.md**
> Purpose + template. When items get added (retrospectives, mid-sprint discoveries). Source: Section 11.18.

**FILE_INVENTORY.md**
> Purpose + template. When to update it. Source: Section 10.3 description.

---

---

# AUTHORING NOTES

---

## Style Guidelines for Wiki Pages

- **Tone:** Direct and practical. No preamble. Get to the point by the second sentence.
- **Tense:** Present tense for rules ("The Builder stops after the dry run"). Past tense only for examples.
- **Voice:** Second person ("you") for instructions. Third person for describing what Architect/Builder does.
- **Length:** Each page should be readable in 3–5 minutes. If it's getting longer, check whether content belongs on a sub-page instead.
- **Code blocks:** Use fenced code blocks for all file content, commands, and prompt text.
- **Breadcrumbs:** Every page opens with a single breadcrumb line, e.g., `[Home](../index.md) → [Lifecycle](index.md) → Step 1`.
- **See Also:** Every page ends with a "See Also" section linking to 2–4 closely related pages.
- **Do not duplicate content:** If a section already exists on another page, link to it rather than repeating it.

## Populating Order

Fill pages in this order to avoid broken links:

1. `glossary.md` and `core-concepts.md` (no dependencies)
2. `file-reference/` pages (referenced by everything else)
3. `prompts.md` (referenced by sprint workflow and lifecycle)
4. `orchestration.md` and `setup.md`
5. `lifecycle/` pages
6. `modes/` pages
7. `sprint-workflow.md`
8. `getting-started.md` and `example.md`
9. `troubleshooting.md` and `quick-reference.md`
10. `index.md` last (links to everything)
