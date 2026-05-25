[Home](index.md)

# Getting Started

A step-by-step script for your first ADDF session. Follow it in order. By the end you will have a project folder with foundational files, a first sprint pack, a reviewed dry run, and a working starting point that any future AI session can resume from.

---

## What You'll Need

- Any capable LLM (Claude, ChatGPT, Gemini) — you need two windows: one for Architect sessions, one for Builder sessions
- A text or code editor (VSCode recommended)
- A terminal
- A repository-aware coding tool for Builder sessions (Cursor, Claude Code, Cline, or similar)

**Time:** approximately 30–45 minutes for your first session.

---

## Step 1 — Create the Project Folder

Open your terminal and run:

```bash
mkdir -p src docs planning/backlog planning/sprints/sprint_001
touch AGENTS.md STATE.md DOMAIN.md DECISIONS.md COMMANDS.md \
      STYLE_GUIDE.md SECURITY.md RISKS.md QUESTIONS.md FILE_INVENTORY.md
```

This creates the skeleton structure. The files are empty for now — you will fill them in over the next steps.

**What these files are for:**
- `DOMAIN.md` — holds your business definitions
- `STATE.md` — holds the current project status
- `AGENTS.md` — tells the AI what rules to follow
- `COMMANDS.md` — holds the commands to run, test, and build the project

For the full annotated directory tree, see [Setup and Scaffolding](setup.md#full-directory-structure).

---

## Step 2 — Fill in SECURITY.md First

Before anything else, open `SECURITY.md` and write two lists: what is safe to upload to an AI session, and what must never be uploaded. This file sets the boundary for everything that follows.

A minimal starting version:

```markdown
# SECURITY.md Data Security Protocol

## Never Upload to an AI Session
- API keys or tokens
- Database connection strings or passwords
- Contents of .env files
- Real user names, emails, phone numbers, or IDs

## Safe to Upload
- All framework Markdown files (AGENTS.md, STATE.md, DOMAIN.md, etc.)
- Source code files that contain no secrets
- Sprint planning files
```

**Why first?** Because every file you create after this may be loaded into an AI session. Setting the boundary before you start means you never accidentally include something you should not. See [SECURITY.md reference](file-reference/security.md) for the full template.

---

## Step 3 — Fill in AGENTS.md

Copy the template from [AGENTS.md reference](file-reference/agents.md#template) into your `AGENTS.md`. This file is the rulebook the AI reads at the start of every session. It defines what Architect Mode and Builder Mode are allowed to do.

The template is ready to use without modification for your first project. As you learn the framework, you will add project-specific constraints here based on what you discover in each sprint's retrospective.

---

## Step 4 — Write Your DOMAIN.md

Open `DOMAIN.md` and describe your project in three parts: what it does, the core entities it works with, and what it explicitly does not handle. Keep it short and honest — you do not need everything figured out yet.

```markdown
# DOMAIN.md Business Logic and Definitions

## Project Overview
[Two to three sentences: what does this project do and why does it exist?]

## Core Entities
### [Entity Name]
Definition: [Exact meaning in this project]
Business rules: [How this entity behaves]
What it is NOT: [Clarify common confusions]

## Out of Scope
This project explicitly does NOT handle:
- [Item 1]
- [Item 2]
```

For a fully completed example showing what this looks like in practice, see [Step 1 in the Mini Task Tracker example](example.md#step-1--research--architecture). For the full template, see [DOMAIN.md reference](file-reference/domain.md).

---

## Step 5 — Run the Project Kickoff Interview

Open a fresh chat window with any capable LLM. Paste the full contents of `AGENTS.md` and your draft `DOMAIN.md`. Then paste this prompt (full version at [Prompts](prompts.md#kickoff-interview)):

```
Execute Project Kickoff Interview Protocol for [YOUR PROJECT NAME].

I will provide raw notes, ideas, rough goals, constraints, and known
unknowns. Your task is to ask up to 10 clarifying questions before
creating any final architecture. Prioritize questions that affect
business logic, data shape, security, user workflows, deployment,
and scope boundaries.

After I answer, generate draft contents for:
1. DOMAIN.md
2. STATE.md
3. STYLE_GUIDE.md
4. docs/architecture.md
5. DECISIONS.md starter ledger
6. QUESTIONS.md starter ledger
7. RISKS.md starter ledger

Do not write application source code. Produce Markdown file blocks only.
```

Answer the AI's questions. Copy the output into the relevant files on your computer. This is Architect Mode — the AI is acting as a technical lead helping you define the project before any code is written.

---

## Step 6 — Generate Your First Sprint Pack

In the same Architect session, paste your current `STATE.md` and run the [Sprint Pack Generation prompt](prompts.md#sprint-pack-generation):

```
Execute Architect Sprint Generation Protocol.
Active Project State: [paste STATE.md contents]
Target Sprint Scope: Sprint 001 — [one sentence describing the first feature]
Structural References: Refer to our active DOMAIN.md parameters.
Generate: requirements.md, blueprint.md, acceptance.md.
Do not output source code.
```

Save the three output files into `planning/sprints/sprint_001/`.

---

## Step 7 — Run the Dry Run

Open a new session in a repository-aware coding tool (Cursor, Claude Code, Cline, or similar). Load the sprint files and paste the [Builder Pre-Flight Dry Run prompt](prompts.md#dry-run):

```
Initialize Pre-Flight Dry Run Protocol.
Permission Level: Level 0 (Read-Only).
Refer to planning/sprints/sprint_001/requirements.md and blueprint.md.
Execute a read-only analysis and produce dry_run.md. Then STOP.
Do not write code until you receive explicit operator clearance.
```

The Builder will produce `dry_run.md` listing every file it intends to create or modify. Review it against `blueprint.md`. If it matches, proceed. If it lists files outside the blueprint, return to the Architect session and resolve the discrepancy first.

---

## Step 8 — Authorize and Build

After confirming the dry run matches the blueprint, type this authorization in the Builder session (full version at [Builder Implementation Authorization](prompts.md#implementation-authorization)):

```
Dry run approved. Permission Level 1 authorized. Proceed with
implementation according to requirements.md, blueprint.md, and
acceptance.md.
Rules:
1. Modify only approved files.
2. Do not invent business rules not in DOMAIN.md.
3. Log every created or modified file in implementation_log.md.
4. Run all verification commands in acceptance.md and COMMANDS.md.
5. Paste raw terminal output into implementation_log.md.
6. Stop if a blocking ambiguity appears.
```

---

## Step 9 — Verify and Close

After the Builder finishes, run the commands in `COMMANDS.md` yourself to verify the work. Work through the five gates in `human_review.md`. Update `STATE.md` to reflect the completed sprint. Close the Builder session.

Your project is now in a state that any future AI session can resume from by loading `STATE.md`, `DOMAIN.md`, and `AGENTS.md`. For full detail on running subsequent sprints, see [Sprint Workflow](sprint-workflow.md).

---

## Next Steps

- [The 8-Step Lifecycle](lifecycle/index.md) — understand the full project arc from research to resumption
- [Operating Modes](modes/index.md) — choose the right mode for each task
- [File Reference](file-reference/index.md) — full templates and guidance for every tracking file

## See Also

- [Complete Example: Mini Task Tracker](example.md)
- [Setup and Scaffolding](setup.md)
- [Core Concepts](core-concepts.md)
