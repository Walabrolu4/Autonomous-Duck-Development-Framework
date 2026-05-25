# 🦆 Autonomous Duck Deployment Framework

> *A deterministic, end-to-end system for AI-assisted software development.*

**Version 1.2** · Context Engineering via Local File Sovereignty · Dual-Mode Orchestration (Architect & Builder)

---

## The Problem

Vibe coding — describing an idea to an AI, hitting generate, and iterating indefinitely in the same chat thread — fails in three predictable ways:

1. **Context bleed.** Long threads fill with old code, abandoned directions, and conversational filler. The AI loses track of decisions made earlier, and regression bugs appear that can't be explained.
2. **Improvisation bias.** Without a strict specification, the AI invents. It creates database keys that don't match your schema, assumes permission levels that clash with your business logic, and takes the path of least resistance — not the path that matches your intent.
3. **No anchor.** Conversation history is fragile, unsearchable, non-portable, and eventually destroyed by token limits or session loss. When you close the tab, your project context is gone.

The Autonomous Duck Deployment Framework solves all three.

---

## The Core Idea

The framework's name comes from **rubber duck debugging**: explaining code out loud to an inanimate object forces the developer to structure thinking clearly enough to find the problem.

This framework applies that principle to AI-assisted development. Before the AI acts, the human operator structures the problem clearly enough to explain it in writing. The Markdown files are that explanation. **The AI only reads what you have written down.**

> A rubber duck cannot invent your business logic. Neither should your AI.

---

## How It Works

### Local File Sovereignty

The project brain lives in a small set of local Markdown files — `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, and sprint folders. These files survive rate limits, model swaps, lost chats, and long breaks. Load them into any AI session and you restore full project context instantly.

### Dual-Mode Orchestration

| Mode | Role | What It Does | What It Never Does |
|------|------|-------------|-------------------|
| **Architect** | Plans | Generates requirements, blueprints, and acceptance criteria | Writes source code |
| **Builder** | Builds | Implements the approved blueprint | Invents business logic |

Any capable LLM can play either role. What matters is which mode you invoke — not which model you use.

### The Dry Run Gate

Before the Builder writes a single line of code, it produces a read-only report listing every file it intends to create or modify. It then stops and waits. You review the report, confirm it matches the blueprint, and give explicit permission. Only then does code get written.

This one pause is how the framework catches scope creep, accidental refactors, dependency additions, and business-logic invention — before they happen.

### The Central Rule

> The question is never which AI does what.  
> The question is **what files must exist before any AI is allowed to act.**

---

## Repo Contents

```
/
├── README.md                          ← You are here
├── docs/
│   ├── Autonomous_Duck_Deployment_Framework_v3.md   ← Full framework document
│   ├── Autonomous_Duck_Deployment_Framework_v3.pdf  ← Printable version
│   └── ADDF_Poster_V2.png                           ← Visual overview
└── template/                          ← Ready-to-copy project scaffold
    ├── AGENTS.md
    ├── STATE.md
    ├── DOMAIN.md
    ├── DECISIONS.md
    ├── COMMANDS.md
    ├── STYLE_GUIDE.md
    ├── SECURITY.md
    ├── GIT_STRATEGY.md
    ├── PROMPT_CHANGELOG.md
    ├── RISKS.md
    ├── QUESTIONS.md
    ├── FILE_INVENTORY.md
    ├── README.md
    ├── .gitignore
    ├── docs/
    │   ├── architecture.md
    │   ├── data_model.md
    │   ├── api.md
    │   ├── permissions.md
    │   └── validation.md
    ├── planning/
    │   ├── backlog.md
    │   └── sprints/
    │       └── sprint_001/
    │           ├── requirements.md
    │           ├── blueprint.md
    │           ├── blueprint_feedback.md
    │           ├── acceptance.md
    │           ├── dry_run.md
    │           ├── implementation_log.md
    │           ├── human_review.md
    │           ├── retrospective.md
    │           └── rollback_log.md
    ├── _templates/                    ← Domain-specific scaffolds (populate as you build)
    │   ├── web-app/
    │   ├── game-unity/
    │   ├── game-godot/
    │   ├── desktop-electron/
    │   └── data-parser/
    └── src/                           ← Builder writes code here
```

---

## Getting Started

### 1. Copy the template into your new project

```bash
cp -r template/ /path/to/your-project
cd /path/to/your-project
git init && git checkout -b main && git checkout -b dev
```

### 2. Fill in SECURITY.md first

Before anything else, define what is and isn't safe to upload to an AI session. Every file you create after this may be loaded into a model. Set the boundary first.

### 3. Fill in AGENTS.md, DOMAIN.md, and STATE.md

These three files are loaded into every AI session. `AGENTS.md` is the rulebook. `DOMAIN.md` is your business logic. `STATE.md` is your living status board.

### 4. Run the Project Kickoff Interview

Open any capable LLM (Claude, ChatGPT, Gemini). Paste your `AGENTS.md` and draft `DOMAIN.md`, then paste the Project Kickoff Interview Prompt from the full document. The Architect will ask clarifying questions and generate your foundational files.

### 5. Follow the 8-Step Lifecycle

```
Research & Architecture → Initial Development → Testing →
Documentation → Full-Scale Development → Reflection Loop →
Deployment & Maintenance → Resumption (repeat)
```

The full lifecycle, all operating modes, prompt catalog, file templates, and troubleshooting guide are in [`docs/Autonomous_Duck_Deployment_Framework_v3.md`](docs/Autonomous_Duck_Deployment_Framework_v3.md).

---

## The 5 Operating Modes

| Mode | Use For |
|------|---------|
| **1 — Quick Patch** | Typo fixes, single-function changes, minor config edits under ~10 lines |
| **2 — Feature Sprint** | New features, new routes, new components, any multi-file change |
| **3 — Refactor / Migration** | Database migrations, dependency upgrades, architectural restructuring |
| **4 — Data Ingestion** | Parsing spreadsheets or PDFs, mapping external APIs, building ETL pipelines |
| **5 — Style Audit** | Enforcing `STYLE_GUIDE.md` conventions across new or modified files |

---

## Builder Permission Levels

The human operator assigns a permission level at the start of every Builder session. The Builder cannot escalate its own level.

| Level | Name | What the Builder Can Do |
|-------|------|------------------------|
| 0 | Read-Only | Dry run analysis only — no file changes |
| 1 | Sprint Scope | Modify only files listed in the active blueprint |
| 2 | Approved Expansion | Also create minor helper modules surfaced in the dry run |
| 3 | Supervised Refactor | Mutate adjacent files with full change logging |
| 4 | Migration | Heavy schema changes — requires pre-written rollback procedures |

Start at Level 1 for almost every sprint.

---

## Why "Duck"?

Rubber duck debugging is the practice of explaining your code, out loud, to a rubber duck. The act of articulating the problem clearly enough for a silent listener to "understand" it forces the developer to find the flaw in their own reasoning.

This framework applies that discipline at scale. The Markdown files are the duck. The AI is the assistant that reads what the duck heard. The human operator is the one who has to be clear enough to write it down.

---

## Full Documentation

📄 [`docs/Autonomous_Duck_Deployment_Framework_v3.md`](docs/Autonomous_Duck_Deployment_Framework_v3.md) — Complete framework with all prompts, templates, lifecycle steps, operating modes, troubleshooting, and glossary.

---

*Framework Version 1.2 — Flow & Readability Edition*
