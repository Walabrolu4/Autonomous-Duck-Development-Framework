# Autonomous Duck Deployment Framework

> **A file-first, AI-assisted project delivery system for research, architecture, implementation, handoff, and long-term iteration.**

**Framework Version:** 4.0 Draft  
**Short Name:** ADDF  
**Core Principle:** Files are permanent. Chats are disposable.  
**Core Methodology:** Context Engineering through Local File Sovereignty  
**Primary Workflow:** Research → Design & Feasibility → Validation → Architecture → Sprint Planning → Build & Test → Review & Reflection → Deploy / Maintain / Resume  
**Primary Modes:** Research Mode, Design / Feasibility Mode, Architect Mode, Builder Mode, Audit / Review Mode  
**Domain Coverage:** Web, Game, Desktop, Mobile, Data / Automation, Documentation, Tooling, Education

---

## Contents

- [1. Why This Framework Exists](#1-why-this-framework-exists)
  - [1.1 The Vibe Coding Problem](#11-the-vibe-coding-problem)
  - [1.2 The Rubber Duck Principle](#12-the-rubber-duck-principle)
  - [1.3 Context Engineering Over Context Windows](#13-context-engineering-over-context-windows)
  - [1.4 The Central Rule](#14-the-central-rule)
- [2. The Framework in One Page](#2-the-framework-in-one-page)
- [3. The Big Mental Model](#3-the-big-mental-model)
  - [3.1 Project Brain](#31-project-brain)
  - [3.2 Project Lifecycle](#32-project-lifecycle)
  - [3.3 Release Cycle](#33-release-cycle)
  - [3.4 Feature Cycle](#34-feature-cycle)
  - [3.5 Sprint Loop](#35-sprint-loop)
  - [3.6 Patch Path](#36-patch-path)
- [4. The ADDF Work Scale Model](#4-the-addf-work-scale-model)
  - [4.1 Project vs Release vs Feature vs Sprint vs Patch](#41-project-vs-release-vs-feature-vs-sprint-vs-patch)
  - [4.2 When to Run the Full Lifecycle](#42-when-to-run-the-full-lifecycle)
  - [4.3 When to Run a Feature Cycle](#43-when-to-run-a-feature-cycle)
  - [4.4 When to Use a Sprint Only](#44-when-to-use-a-sprint-only)
  - [4.5 When to Use a Quick Patch](#45-when-to-use-a-quick-patch)
- [5. The 8-Step ADDF Project Lifecycle](#5-the-8-step-addf-project-lifecycle)
  - [Step 1 — Research](#step-1--research)
  - [Step 2 — Design & Feasibility](#step-2--design--feasibility)
  - [Step 3 — Validation Gate](#step-3--validation-gate)
  - [Step 4 — Architecture](#step-4--architecture)
  - [Step 5 — Sprint Planning](#step-5--sprint-planning)
  - [Step 6 — Build & Test](#step-6--build--test)
  - [Step 7 — Review & Reflection](#step-7--review--reflection)
  - [Step 8 — Deploy, Maintain, or Resume](#step-8--deploy-maintain-or-resume)
- [6. Modes of Operation](#6-modes-of-operation)
  - [6.1 Research Mode](#61-research-mode)
  - [6.2 Design / Feasibility Mode](#62-design--feasibility-mode)
  - [6.3 Architect Mode](#63-architect-mode)
  - [6.4 Builder Mode](#64-builder-mode)
  - [6.5 Audit / Review Mode](#65-audit--review-mode)
  - [6.6 Mode Switching](#66-mode-switching)
- [7. The ADDF Sprint Loop](#7-the-addf-sprint-loop)
- [8. Release Cycles and Version Updates](#8-release-cycles-and-version-updates)
- [9. Adding New Features Without Restarting the Project](#9-adding-new-features-without-restarting-the-project)
- [10. Handoff, Resumption, and Model Switching](#10-handoff-resumption-and-model-switching)
- [11. Agile and Scrum Relationship](#11-agile-and-scrum-relationship)
- [12. Repository and Folder Structure](#12-repository-and-folder-structure)
- [13. Setup and First Session](#13-setup-and-first-session)
- [14. File Templates](#14-file-templates)
- [15. Prompt Catalog](#15-prompt-catalog)
- [16. Domain Adaptations](#16-domain-adaptations)
- [17. Example: Mini Task Tracker](#17-example-mini-task-tracker)
- [18. Example: Building the ADDF Public Website and Starter Kit](#18-example-building-the-addf-public-website-and-starter-kit)
- [19. Quick Reference Checklists](#19-quick-reference-checklists)
- [20. When Things Go Wrong](#20-when-things-go-wrong)
- [21. Glossary](#21-glossary)

---

# 1. Why This Framework Exists

Before any instructions, file names, prompts, commands, or diagrams, here is the problem this framework solves.

AI-assisted development often begins with speed. A developer opens an AI tool, describes an idea, asks for code, reacts to the result, asks for changes, and keeps going in the same conversation until the output looks useful. This can feel productive in the moment. It can also produce fragile projects that are hard to understand, hard to resume, and hard to maintain.

The Autonomous Duck Deployment Framework exists to solve that problem.

ADDF treats AI tools as temporary compute partners. The project memory does not live in the model. It lives in local Markdown files. Those files define the project, capture decisions, preserve state, describe constraints, hold acceptance criteria, record implementation logs, and allow any capable LLM to resume work without needing the previous chat history.

The framework is not meant to make projects slower. It is meant to make AI-assisted work safer, more repeatable, easier to hand off, and easier to continue over time.

## 1.1 The Vibe Coding Problem

Vibe coding is what happens when a developer describes an app idea to an AI tool, hits generate, eyeballs the output, and keeps asking for changes in the same chat thread indefinitely.

It feels productive because output appears immediately.

It fails predictably because of three structural weaknesses.

### Context bleed and memory bloat

A long chat thread fills with old code blocks, abandoned directions, half-correct fixes, speculative ideas, and conversational filler. The AI begins responding to the entire messy history instead of the current truth of the project.

The longer the thread grows, the harder it becomes to know which instructions are still valid.

### Improvisation bias

When an AI builder lacks a strict specification, it invents. It creates fields that do not match your schema, assumes workflows you did not approve, chooses package dependencies without recording why, or takes the path that seems easiest rather than the path that matches the project.

The AI is not being malicious. It is filling gaps.

ADDF reduces those gaps by requiring the human and Architect to write down the project logic before the Builder implements.

### The missing anchor

In vibe coding, the chat history becomes the project memory. That memory is fragile, unsearchable, non-portable, and often lost when the chat gets too long, the model changes, the tool hits a token limit, or the user returns weeks later.

ADDF moves the anchor from the chat to the file system.

## 1.2 The Rubber Duck Principle

The framework's name comes from rubber duck debugging.

Rubber duck debugging works because explaining your code out loud forces you to organize your thinking. A rubber duck cannot invent missing logic for you. It only reflects the clarity of your explanation.

ADDF applies that principle to AI-assisted development.

Before the AI acts, the project must be explained clearly enough in writing that the AI can work from those written instructions. The Markdown files are the explanation. The AI reads what the human has made explicit.

> **A rubber duck cannot invent your business logic. Neither should your AI.**

## 1.3 Context Engineering Over Context Windows

A larger context window does not automatically solve project confusion. It can make the problem larger by allowing more unrelated history, more abandoned ideas, and more stale decisions to influence the model.

ADDF prioritizes **clean context** over **more context**.

Context Engineering is the practice of placing the right project information into the right files and loading only the files needed for the current mode of work.

A Research session needs research questions, constraints, and source notes.

An Architect session needs project rules, state, decisions, questions, and risks.

A Builder session needs the sprint pack, commands, relevant source files, and permission level.

An Audit session needs acceptance criteria, dry run, implementation log, and test output.

The rule is simple:

> Load what the session needs. Do not load everything just because it exists.

## 1.4 The Central Rule

> **The question is never which AI does what. The question is what files must exist before any AI is allowed to act.**

If the required files do not exist, the AI should not proceed.

This rule prevents the framework from becoming tool-dependent. Claude, ChatGPT, Gemini, Codex, Cursor, Cline, or any other capable LLM can participate as long as it reads the same project files and obeys the same mode constraints.

The AI is interchangeable.

The project files are the source of truth.

---

# 2. The Framework in One Page

ADDF is a file-first project delivery system for AI-assisted work.

The project is organized around five layers:

1. **Project Brain** — durable Markdown files that preserve project memory.
2. **Project Lifecycle** — the full 8-step path from research to deployment or resumption.
3. **Release Cycle** — the process for V1, V2, V3, and later updates.
4. **Feature Cycle** — the process for adding new capabilities to an existing project.
5. **Sprint Loop** — the bounded implementation packet used by the AI Builder.

The framework uses multiple AI modes:

- **Research Mode** explores unknowns.
- **Design / Feasibility Mode** turns research into possible approaches.
- **Architect Mode** makes plans, decisions, requirements, blueprints, and acceptance criteria.
- **Builder Mode** implements only approved work after a dry run.
- **Audit / Review Mode** checks whether the output matches the plan.

ADDF is not a one-time waterfall process. It is an iterative, file-backed system.

You use the full lifecycle when starting a new project, planning a major release, changing direction, or making a high-risk architectural decision.

You use a smaller feature cycle when adding a new feature to an existing project.

You use the sprint loop when implementing a bounded unit of work.

You use a quick patch path for tiny fixes.

The key idea is scale.

A full project, a version release, a feature, a sprint, and a typo fix should not all receive the same amount of process. ADDF gives you a way to decide how much structure the work needs.

---

# 3. The Big Mental Model

ADDF becomes easier to understand when separated into five layers.

```txt
Project Brain
└── Project Lifecycle
    └── Release Cycles
        └── Feature Cycles
            └── Sprint Loops
                └── Patches / Tasks
```

Each layer has a different purpose.

## 3.1 Project Brain

The Project Brain is the durable memory of the project.

It lives in local Markdown files such as:

```txt
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
STYLE_GUIDE.md
SECURITY.md
QUESTIONS.md
RISKS.md
GIT_STRATEGY.md
PROMPT_CHANGELOG.md
planning/backlog.md
```

The Project Brain answers:

- What is this project?
- What are the rules?
- What has been decided?
- What is currently happening?
- What is risky?
- What is unresolved?
- What commands run the project?
- What should never be shared with an AI?
- What changed recently?
- What should happen next?

The Project Brain is what allows the project to survive model changes, token limits, long breaks, and handoffs between LLMs.

## 3.2 Project Lifecycle

The Project Lifecycle is the high-level path for starting or significantly rethinking a project.

The ADDF project lifecycle is:

```txt
1. Research
2. Design & Feasibility
3. Validation Gate
4. Architecture
5. Sprint Planning
6. Build & Test
7. Review & Reflection
8. Deploy, Maintain, or Resume
```

Use the full lifecycle when:

- Starting a new project.
- Beginning a major version.
- Changing architecture.
- Pivoting direction.
- Entering a domain you do not understand.
- Making a high-risk technical decision.
- Recovering from a project that has become disorganized.

## 3.3 Release Cycle

A Release Cycle organizes work around a version.

Examples:

```txt
v0.1 Public Proof
v0.2 Website MVP
v0.3 CLI Init Tool
v1.0 Stable Framework Release
v2.0 Major Rewrite
```

A release cycle asks:

- What did the previous version accomplish?
- What should this version accomplish?
- What features are in scope?
- What features are out of scope?
- What research is needed?
- What risks must be resolved?
- What sprints will deliver the release?
- What must be true before release?

Release cycles prevent the framework from feeling like it only works for brand-new projects.

After V1 is complete, you start a new release cycle for V2.

You do not erase the Project Brain.

You build on it.

## 3.4 Feature Cycle

A Feature Cycle is used when adding a new capability to an existing project.

Examples:

```txt
Add prompt catalog page
Add starter kit download
Add CLI init command
Add onboarding app
Add cloud sync to Mini Task Tracker
Add enemy AI to a game prototype
```

A feature cycle asks:

- Does this feature fit the project domain?
- Does it need research?
- Does it require feasibility testing?
- What files will it touch?
- What user outcome defines success?
- What acceptance criteria are required?
- Does it require a new decision record?
- Should it be one sprint or several?

A feature cycle may run a small version of the full lifecycle. It does not restart the whole project.

## 3.5 Sprint Loop

A Sprint Loop is the bounded implementation packet.

A sprint is not necessarily a Scrum sprint. It is an AI-safe unit of work.

A sprint typically includes:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
rollback_log.md when needed
```

The sprint loop is where the Builder operates.

The Architect creates the plan.

The Builder performs a dry run.

The human approves.

The Builder implements.

The work is verified, logged, reviewed, committed, and reflected on.

## 3.6 Patch Path

A Patch Path is for small, low-risk changes.

Examples:

- Fix a typo.
- Update a broken link.
- Rename a label.
- Change a small copy block.
- Adjust a minor style value.
- Update a single documentation sentence.

A patch does not need a full sprint pack unless it touches business logic, architecture, dependencies, data model, or multiple files.

Patch work should still update `STATE.md` when appropriate.

---

# 4. The ADDF Work Scale Model

The framework can feel rigid if every change is treated like a full project. ADDF v4 avoids that by classifying work by scale.

## 4.1 Project vs Release vs Feature vs Sprint vs Patch

| Work Scale | Meaning | Example | Process Needed |
|---|---|---|---|
| Project | A complete product or initiative | Build the ADDF public website and starter kit ecosystem | Full lifecycle |
| Release | A version of the project | ADDF v0.2 Website MVP | Release cycle |
| Feature | A capability added to an existing project | Add prompt catalog page | Feature cycle |
| Sprint | A bounded implementation packet | Build static homepage and download links | Sprint loop |
| Patch | A tiny low-risk change | Fix typo in README | Quick patch path |

ADDF is iterative. A project contains releases. Releases contain features. Features may require one or more sprints. Patches can happen along the way.

## 4.2 When to Run the Full Lifecycle

Run the full lifecycle when the work changes the direction, structure, or foundation of the project.

Examples:

- Starting a new product.
- Planning V1.
- Planning V2 after V1 is complete.
- Changing from static site to dynamic app.
- Adding a backend where none existed before.
- Changing core architecture.
- Moving from prototype to production.
- Entering a new technical domain.
- Recovering a messy project.

The full lifecycle is not meant for every small feature.

## 4.3 When to Run a Feature Cycle

Run a feature cycle when the project already exists and the new work fits inside the existing domain.

Examples:

- Add a new website page.
- Add a starter kit generator.
- Add a search feature.
- Add an export option.
- Add user settings.
- Add a new enemy type to a game.
- Add a data import format.

A feature cycle may include research, feasibility, validation, architecture, build, and review, but only at the scale required by that feature.

## 4.4 When to Use a Sprint Only

Use a sprint when the feature is already understood and needs implementation.

Examples:

- Build the homepage after architecture is approved.
- Create the starter-kit folder after templates are defined.
- Generate prompt catalog files after prompt structure is decided.
- Implement a known component from an approved blueprint.

## 4.5 When to Use a Quick Patch

Use a quick patch when the change is small, obvious, and low-risk.

A quick patch should not introduce new business logic, new dependencies, new data structures, new permissions, or new architectural behavior.

If you are unsure whether something is a patch, treat it as a sprint.

---

# 5. The 8-Step ADDF Project Lifecycle

The ADDF project lifecycle is the big map.

It is not a rigid checklist that must be run fully for every tiny change. It is a scalable pattern.

The lifecycle can be applied at different levels:

- Full project.
- Major release.
- High-risk feature.
- Architectural pivot.

The steps are:

```txt
1. Research
2. Design & Feasibility
3. Validation Gate
4. Architecture
5. Sprint Planning
6. Build & Test
7. Review & Reflection
8. Deploy, Maintain, or Resume
```

## Step 1 — Research

**Purpose:** Understand the problem before deciding what to build.

Research Mode explores the domain, tools, prior art, constraints, user needs, technical unknowns, and risk areas.

Research answers:

- What do we know?
- What do we not know?
- What tools are available?
- What examples exist?
- What constraints matter?
- What risks are visible?
- What questions must be answered before architecture?

Research produces:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
research_risks.md
```

Research does not make final decisions. It gathers evidence.

### Completion criteria

Research is complete enough when:

- The major unknowns are listed.
- The important sources are summarized.
- Tool options and tradeoffs are visible.
- Open questions are captured.
- Risks are documented.
- The project is ready for design and feasibility analysis.

## Step 2 — Design & Feasibility

**Purpose:** Turn research into possible approaches and test whether the work is realistic.

Design / Feasibility Mode explores possible solutions without committing to implementation.

It answers:

- What approaches are possible?
- Which option is simplest?
- Which option is safest?
- What is the MVP?
- What should be out of scope?
- What must be prototyped before committing?
- Which constraints affect architecture?
- What makes the project risky?

Design & Feasibility produces:

```txt
design_options.md
feasibility.md
mvp_scope.md
risk_matrix.md
prototype_plan.md
```

### Completion criteria

Design & Feasibility is complete enough when:

- At least one viable approach is described.
- The MVP scope is clear.
- Key tradeoffs are documented.
- High-risk assumptions are identified.
- The human can choose an approach.
- The project is ready for validation.

## Step 3 — Validation Gate

**Purpose:** Confirm that the work is defined well enough to architect.

The Validation Gate is a human decision checkpoint. It prevents the Architect from planning against vague, unstable, or unvalidated assumptions.

The gate asks:

- Is the goal clear?
- Is the user clear?
- Is the MVP clear?
- Are major unknowns documented?
- Are high-risk assumptions identified?
- Are security boundaries known?
- Is the preferred approach selected?
- Are out-of-scope items explicit?
- Are there any blockers in `QUESTIONS.md`?
- Are unresolved risks acceptable?

Validation produces:

```txt
validation.md
approved_approach.md
updated QUESTIONS.md
updated RISKS.md
```

### Completion criteria

The project may move to Architecture when:

- The human approves the direction.
- Blocking questions are resolved or explicitly deferred.
- Risks are documented.
- Security boundaries are known.
- The scope is clear enough for planning.

## Step 4 — Architecture

**Purpose:** Convert validated intent into durable project rules and architecture.

Architect Mode turns the approved approach into project files.

Architecture produces or updates:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
STYLE_GUIDE.md
SECURITY.md
docs/architecture.md
docs/data_model.md
docs/api.md
QUESTIONS.md
RISKS.md
```

The Architect does not write source code.

The Architect defines the rules that later Builder sessions must follow.

### Completion criteria

Architecture is complete enough when:

- `DOMAIN.md` defines the project clearly.
- `SECURITY.md` defines safe and unsafe files.
- `COMMANDS.md` lists relevant run, test, build, and rollback commands.
- `DECISIONS.md` captures key decisions.
- `STATE.md` names the current status and next step.
- No sprint-blocking questions remain unresolved.

## Step 5 — Sprint Planning

**Purpose:** Convert architecture into a bounded implementation packet.

Sprint Planning produces the Sprint Pack:

```txt
requirements.md
blueprint.md
acceptance.md
```

The Sprint Pack defines:

- What is being built.
- What is not being built.
- What files will be touched.
- What assumptions must be verified.
- What commands must run.
- What counts as done.

### Completion criteria

Sprint Planning is complete when:

- Requirements are specific.
- Blueprint lists files and steps.
- Acceptance criteria are checkable.
- Out-of-scope items are explicit.
- The human has reviewed assumptions.
- A branch has been created if applicable.

## Step 6 — Build & Test

**Purpose:** Implement approved work safely.

Builder Mode begins with Permission Level 0.

The Builder reads:

```txt
AGENTS.md
STATE.md
COMMANDS.md
requirements.md
blueprint.md
acceptance.md
relevant source files
```

The Builder produces:

```txt
dry_run.md
```

Then it stops.

After human approval, the Builder receives a higher permission level and implements.

Build & Test produces:

```txt
source files
implementation_log.md
test output
```

### Completion criteria

Build & Test is complete when:

- Builder modified only approved files.
- Verification commands ran.
- Raw output is logged.
- Failures are documented.
- No unapproved dependencies were added.
- The implementation matches acceptance criteria.

## Step 7 — Review & Reflection

**Purpose:** Verify the work and convert lessons into future constraints.

Review includes:

- Architect implementation review.
- Human approval gate.
- Acceptance criteria check.
- Decision updates.
- Backlog updates.
- Retrospective.
- State update.

Review produces:

```txt
human_review.md
retrospective.md
updated STATE.md
updated DECISIONS.md
updated planning/backlog.md
updated AGENTS.md when constraints change
```

### Completion criteria

Review is complete when:

- The human approves the work.
- Known issues are captured.
- Decisions are recorded.
- `STATE.md` reflects reality.
- The branch is committed.
- The Builder chat is closed or checkpointed.

## Step 8 — Deploy, Maintain, or Resume

**Purpose:** Decide what happens after the work is reviewed.

The project may:

1. Deploy.
2. Continue to another sprint.
3. Enter maintenance.
4. Start a new feature cycle.
5. Start a new release cycle.
6. Pause and resume later.
7. Pivot and rerun the lifecycle at a larger scale.

Deploy / Maintain / Resume produces:

```txt
release_notes.md
rollback_log.md
updated COMMANDS.md
updated RISKS.md
handoff_summary.md
updated STATE.md
```

### Completion criteria

This step is complete when:

- Deployment or release steps are documented.
- Rollback path exists when needed.
- State is updated.
- Handoff notes exist if pausing.
- Next action is clear.

---

# 6. Modes of Operation

Modes describe how the AI should behave.

Lifecycle steps describe where the project is.

Work scale describes how large the change is.

Modes describe the rules for the AI session.

## 6.1 Research Mode

Research Mode explores.

Use Research Mode when:

- You do not know enough to plan.
- You need to compare tools.
- You need to understand a domain.
- You need to gather public information.
- You need to summarize source documents.
- You need to identify risks and unknowns.

Research Mode may produce:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
research_risks.md
```

Research Mode may not:

- Write application source code.
- Make final architecture decisions.
- Add dependencies to the project.
- Mutate project files without human review.
- Convert research into business rules automatically.

### Research Mode prompt pattern

```txt
You are operating in Research Mode.

Explore the following question:
[research question]

Do not write source code.
Do not make final architecture decisions.
Do not mutate project files.

Produce:
1. Research summary
2. Options
3. Tradeoffs
4. Risks
5. Open questions
6. Recommended next step for Design / Feasibility Mode
```

## 6.2 Design / Feasibility Mode

Design / Feasibility Mode turns research into possible approaches.

Use this mode when:

- There are multiple ways to build something.
- You need to define MVP scope.
- You need to test whether an idea is realistic.
- You need to compare architecture options.
- You need to choose what not to build.

Design / Feasibility Mode may produce:

```txt
design_options.md
feasibility.md
mvp_scope.md
risk_matrix.md
prototype_plan.md
```

It may not:

- Write production source code.
- Pretend uncertain assumptions are facts.
- Approve implementation without validation.
- Hide tradeoffs.

### Design / Feasibility Mode prompt pattern

```txt
You are operating in Design / Feasibility Mode.

Use the provided research notes and project constraints.
Do not write implementation code.

Produce:
1. Viable approaches
2. MVP recommendation
3. In-scope and out-of-scope boundaries
4. Technical feasibility notes
5. Risk matrix
6. Prototype or validation plan
7. Recommendation for the Validation Gate
```

## 6.3 Architect Mode

Architect Mode decides and plans.

Use Architect Mode when:

- You need to create foundational project files.
- You need to generate a Sprint Pack.
- You need to turn validated intent into requirements.
- You need to update architecture documentation.
- You need to review a dry run.
- You need to audit implementation logs.

Architect Mode produces:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
requirements.md
blueprint.md
acceptance.md
docs/architecture.md
docs/data_model.md
docs/api.md
```

Architect Mode may not:

- Write application source files directly.
- Modify the codebase.
- Skip unresolved blockers.
- Approve work without acceptance criteria.
- Invent business rules without marking them as assumptions.

### Architect Mode prompt pattern

```txt
You are operating in Architect Mode.

Use the loaded project files as the source of truth.
Do not write application source code.

Produce:
1. Requirements
2. Blueprint
3. Acceptance criteria
4. Assumptions
5. Risks
6. Files to update
7. Questions requiring human review
```

## 6.4 Builder Mode

Builder Mode implements.

Use Builder Mode when:

- There is an approved Sprint Pack.
- The Builder is running in a repo-aware coding environment.
- You are ready to modify source files.
- You have defined permission level.
- You have a verification path.

Builder Mode produces:

```txt
dry_run.md
source files
implementation_log.md
test output
handoff_summary.md when needed
```

Builder Mode must:

- Start with Permission Level 0.
- Produce a dry run.
- Stop after the dry run.
- Wait for explicit approval.
- Modify only approved files.
- Log all changes.
- Run verification commands.
- Stop when ambiguity appears.
- Checkpoint before token/context limits.

Builder Mode may not:

- Invent business rules.
- Add dependencies without approval.
- Modify unrelated files.
- Skip verification.
- Continue after a failed test without logging the failure.
- Continue after context becomes unstable.

## 6.5 Audit / Review Mode

Audit / Review Mode checks outputs against plans.

Use Audit / Review Mode when:

- Reviewing a dry run.
- Reviewing implementation logs.
- Checking acceptance criteria.
- Checking documentation drift.
- Checking cross-sprint consistency.
- Preparing for release.
- Reviewing handoff readiness.

Audit / Review Mode produces:

```txt
audit_report.md
implementation_review.md
cross_sprint_consistency_audit.md
documentation_drift_audit.md
release_readiness_audit.md
```

Audit / Review Mode may not:

- Modify source code.
- Rewrite history.
- Approve missing test output.
- Ignore scope creep.

## 6.6 Mode Switching

Mode switching is explicit.

The human operator declares the mode and loads the correct files.

### Switch to Research Mode

Load:

```txt
raw notes
research question
known constraints
SECURITY.md if relevant
```

Declare:

```txt
You are operating in Research Mode.
Explore only.
Do not make final decisions.
Do not write source code.
```

### Switch to Design / Feasibility Mode

Load:

```txt
research notes
project constraints
open questions
known risks
```

Declare:

```txt
You are operating in Design / Feasibility Mode.
Turn research into options and tradeoffs.
Do not implement.
```

### Switch to Architect Mode

Load:

```txt
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
QUESTIONS.md
RISKS.md
research notes if relevant
feasibility notes if relevant
```

Declare:

```txt
You are operating in Architect Mode.
Do not write application source code.
Generate project files, requirements, blueprints, and acceptance criteria.
```

### Switch to Builder Mode

Load:

```txt
AGENTS.md
STATE.md
COMMANDS.md
requirements.md
blueprint.md
acceptance.md
relevant source files
```

Declare:

```txt
You are operating in Builder Mode.
Permission Level 0.
Perform a read-only dry run and stop.
```

---

# 7. The ADDF Sprint Loop

The Sprint Loop is the daily operating loop for bounded implementation work.

Use it for:

- New features.
- Multi-file changes.
- Refactors.
- Migrations.
- Tooling additions.
- Documentation package changes.
- Website sections.
- Starter kit updates.
- Any change that needs acceptance criteria.

## Sprint Loop Overview

```txt
1. Pre-Flight Gate
2. Prime the Architect
3. Generate Sprint Pack
4. Human Blueprint Review
5. Builder Dry Run
6. Architect Sanity Audit
7. Dependency Approval Gate
8. Authorize and Build
9. Run Verification
10. Architect Implementation Review
11. Human Approval Gate
12. Commit, Update, Reset
```

## 7.1 Pre-Flight Gate

The human checks:

- Are there open blockers in `QUESTIONS.md`?
- Are there high risks in `RISKS.md`?
- Is the scope clear?
- Is the branch created?
- Is the relevant release or feature defined?
- Are needed decisions recorded?

If the project is not ready, return to Research, Design / Feasibility, or Architecture.

## 7.2 Prime the Architect

Load:

```txt
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
QUESTIONS.md
RISKS.md
release_plan.md if relevant
feature_brief.md if relevant
```

Ask the Architect to generate:

```txt
requirements.md
blueprint.md
acceptance.md
```

## 7.3 Generate Sprint Pack

The Sprint Pack must include:

### requirements.md

Defines:

- Sprint goal.
- Functional requirements.
- Non-functional requirements.
- In-scope items.
- Out-of-scope items.
- Constraints.

### blueprint.md

Defines:

- Implementation plan.
- Files to create.
- Files to modify.
- Assumptions.
- Dependencies.
- Risks.
- Rollback considerations.

### acceptance.md

Defines:

- Functional criteria.
- Technical criteria.
- Verification commands.
- Review gates.
- Definition of done.

## 7.4 Human Blueprint Review

The human checks:

- Does this match the desired outcome?
- Does it conflict with `DOMAIN.md`?
- Does it touch too many files?
- Are assumptions clear?
- Are tests or validation commands included?
- Are out-of-scope items explicit?

If rejected, write feedback to `blueprint_feedback.md` and rerun Architect Mode.

## 7.5 Builder Dry Run

The Builder begins at Permission Level 0.

It creates or outputs `dry_run.md` with:

- Files it intends to create.
- Files it intends to modify.
- Folders it intends to move.
- Commands it intends to run.
- Dependencies it thinks are needed.
- Ambiguities.
- Assumptions.

Then it stops.

## 7.6 Architect Sanity Audit

The Architect compares:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
```

It checks:

- Scope creep.
- Missing files.
- Unapproved dependencies.
- Hidden refactors.
- Missing tests.
- Risky assumptions.
- Security issues.

It returns:

```txt
Approved / Not Approved
Required corrections
Recommended permission level
```

## 7.7 Dependency Approval Gate

Any new dependency requires a `DECISIONS.md` entry before implementation.

The decision should document:

- Dependency name.
- Why it is needed.
- Alternatives considered.
- Risks.
- Rollback plan if needed.

## 7.8 Authorize and Build

The human explicitly authorizes the Builder:

```txt
Dry run approved.
Permission Level 1 authorized.
Proceed with implementation according to requirements.md, blueprint.md, and acceptance.md.
Modify only approved files.
Log all changes in implementation_log.md.
Run verification commands and paste raw output.
Stop if ambiguity appears.
```

## 7.9 Run Verification

The Builder or human runs the commands in:

```txt
acceptance.md
COMMANDS.md
```

Raw output must be pasted into:

```txt
implementation_log.md
```

A summary alone is not enough.

## 7.10 Architect Implementation Review

The Architect reviews:

```txt
acceptance.md
dry_run.md
implementation_log.md
test output
```

It answers:

- Was scope followed?
- Did verification pass?
- Were all accepted files logged?
- Are there undocumented changes?
- Are there decisions to record?
- Is the sprint ready for human review?

## 7.11 Human Approval Gate

The human reviews:

- Scope.
- Tests.
- Debt.
- Decisions.
- State.
- Security.
- Handoff readiness if pausing.

## 7.12 Commit, Update, Reset

The human commits the branch, updates project files, and closes or checkpoints the Builder session.

Required updates:

```txt
STATE.md
planning/backlog.md if needed
DECISIONS.md if needed
retrospective.md
implementation_log.md
```

Then the Builder chat is closed to prevent context bleed.

---

# 8. Release Cycles and Version Updates

ADDF explicitly supports V1, V2, V3, and long-term iteration.

A completed V1 does not mean the framework ends. It means the next version begins with the existing Project Brain.

## 8.1 What Is a Release Cycle?

A Release Cycle is a planning and delivery container for a version.

Examples:

```txt
v0.1 Public Proof
v0.2 Website MVP
v0.3 Init Tool Prototype
v1.0 Stable Public Release
v2.0 Major Framework Rewrite
```

A release cycle defines:

- Release goal.
- In-scope features.
- Out-of-scope features.
- Required research.
- Risks.
- Sprint sequence.
- Release criteria.
- Release notes.
- Retrospective.

## 8.2 Release Folder Structure

Recommended:

```txt
planning/
├── backlog.md
└── releases/
    ├── v0.1/
    │   ├── release_plan.md
    │   ├── scope.md
    │   ├── release_notes.md
    │   ├── retrospective.md
    │   └── sprints/
    │       ├── sprint_001/
    │       └── sprint_002/
    └── v0.2/
        ├── release_plan.md
        └── sprints/
            └── sprint_001/
```

This keeps version history clean.

Projects that prefer a flatter structure may keep all sprints in `planning/sprints/` and reference release numbers inside `STATE.md`.

## 8.3 Starting V2 After V1

When V1 is done, do not restart from scratch.

Load:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
RISKS.md
QUESTIONS.md
planning/backlog.md
planning/releases/v1.0/retrospective.md
user feedback
open issues
```

Ask Architect Mode:

```txt
We are beginning V2.

Review the current project state, V1 decisions, backlog, risks, and retrospective.

Generate:
1. V2 release goals
2. V2 in-scope features
3. V2 out-of-scope items
4. Required research
5. Proposed sprint sequence
6. Risks
7. Updates needed to DOMAIN.md, STATE.md, and DECISIONS.md
```

Outputs:

```txt
planning/releases/v2.0/release_plan.md
planning/releases/v2.0/scope.md
planning/releases/v2.0/research_questions.md
updated STATE.md
updated planning/backlog.md
updated RISKS.md
```

## 8.4 Release Completion Criteria

A release is complete when:

- All in-scope features are complete or intentionally deferred.
- Acceptance criteria for the release are met.
- Documentation is updated.
- `CHANGELOG.md` is updated.
- Release notes exist.
- `STATE.md` reflects the release status.
- Known issues are in the backlog.
- Deployment or distribution is complete.
- A release retrospective exists.

---

# 9. Adding New Features Without Restarting the Project

ADDF allows new features to be added continuously.

The key is not to rerun the full project lifecycle every time. Instead, run the appropriate scale of process.

## 9.1 Feature Cycle

Use the Feature Cycle when adding a capability to an existing project.

```txt
1. Add feature idea to backlog
2. Write feature brief
3. Research if needed
4. Design / feasibility if needed
5. Validate scope
6. Architect sprint pack
7. Builder dry run
8. Build and test
9. Review and update project brain
```

## 9.2 Feature Folder Structure

Recommended:

```txt
planning/
└── features/
    └── starter-kit-generator/
        ├── feature_brief.md
        ├── research.md
        ├── feasibility.md
        ├── validation.md
        ├── decisions.md
        └── sprint_map.md
```

For small projects, feature files may live directly in the sprint folder instead.

## 9.3 Feature Brief Template

```md
# Feature Brief: [Feature Name]

## Summary
[What capability are we adding?]

## User Value
[Why does this matter?]

## In Scope
- [Item]

## Out of Scope
- [Item]

## Known Constraints
- [Constraint]

## Research Needed
- [Question or "None"]

## Feasibility Risks
- [Risk or "None"]

## Acceptance Summary
- [High-level done condition]

## Related Files
- [Relevant files or folders]
```

## 9.4 Feature Completion Criteria

A feature is complete when:

- It satisfies its feature brief.
- Required sprints are complete.
- Acceptance criteria pass.
- Docs are updated.
- `STATE.md` is updated.
- Any new decisions are recorded.
- Any unresolved work is moved to backlog.
- The feature is included in the relevant release notes.

---

# 10. Handoff, Resumption, and Model Switching

One of ADDF's strongest use cases is model handoff.

If Codex is working on something, runs out of tokens, and Claude needs to pick up, the framework supports that through local project files.

The outgoing model writes down what happened.

The incoming model reads the files and resumes.

No old chat history is required.

## 10.1 Session Checkpoint Protocol

Before ending a Builder session, switching models, or approaching context/token limits, the active LLM must update:

```txt
STATE.md
implementation_log.md
QUESTIONS.md
RISKS.md
planning/backlog.md
retrospective.md when appropriate
```

It must also produce a handoff summary.

## 10.2 Handoff Summary Template

```md
# Handoff Summary

## Current Goal
[What the session was trying to accomplish]

## Current Mode
[Research / Design / Architect / Builder / Audit]

## Active Project Scale
[Project / Release / Feature / Sprint / Patch]

## Completed Work
[What has been done]

## Files Changed
- [File path]: [What changed]

## Commands Run
- [Command]: [Result]

## Current Problems
[Errors, blockers, failed tests]

## Unfinished Work
[What remains]

## Next Recommended Action
[What the next LLM or human should do first]

## Warnings
[Any risks, assumptions, or caveats]
```

## 10.3 Incoming Model Resumption Protocol

A new model should load:

```txt
AGENTS.md
DOMAIN.md
STATE.md
COMMANDS.md
current requirements.md
current blueprint.md
current acceptance.md
current dry_run.md
current implementation_log.md
QUESTIONS.md
RISKS.md
DECISIONS.md
handoff_summary.md
```

Then run:

```txt
Execute Handoff Resumption Protocol.

Read the loaded files.
Summarize the current project state.
Identify:
1. Current goal
2. Active release / feature / sprint
3. Completed work
4. Unfinished work
5. Blockers
6. Files changed
7. Next safest action

Do not modify files until human authorizes the correct mode.
```

## 10.4 Resumption After a Long Break

When returning after days, weeks, or months, load:

```txt
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
QUESTIONS.md
RISKS.md
planning/backlog.md
```

Then run the Resumption Prompt in Architect Mode.

The goal is not to continue blindly. The goal is to reconstruct the project state from files and identify the safest next action.

## 10.5 Handoff Acceptance Criteria

A handoff is successful when:

- The new LLM can summarize the project without old chat history.
- The active work scale is clear.
- The current mode is clear.
- Changed files are listed.
- Unfinished work is listed.
- Blockers are visible.
- The next safest action is clear.
- No source code is modified before authorization.

---

# 11. Agile and Scrum Relationship

ADDF borrows useful ideas from Agile but is not Scrum.

It uses terms like:

- Sprint
- Backlog
- Acceptance criteria
- Retrospective
- Review
- Iteration

But ADDF does not require:

- Scrum Master
- Product Owner
- Daily standups
- Story points
- Velocity
- Sprint ceremonies
- Two-week cadence
- Formal team roles

## 11.1 How ADDF Sprints Differ from Scrum Sprints

In Scrum, a sprint is a timeboxed team iteration.

In ADDF, a sprint is a bounded AI implementation packet.

An ADDF sprint is defined by:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
```

It is less about calendar time and more about controlled scope.

## 11.2 Agile-ish Mapping

| Agile / Scrum Term | ADDF Equivalent |
|---|---|
| Product | Project |
| Release | Release Cycle |
| Epic | Major Feature Group |
| User Story | Feature Brief / Requirement |
| Sprint | AI Implementation Packet |
| Acceptance Criteria | acceptance.md |
| Backlog | planning/backlog.md |
| Sprint Review | Architect Review + Human Review |
| Retrospective | retrospective.md |
| Definition of Done | acceptance.md + human_review.md |
| Product Owner | Human Operator |
| Development Team | Builder Mode + Human |
| Scrum Master | Not required |

## 11.3 Recommended Language

Use:

```txt
Agile-inspired
Sprint loop
Feature cycle
Release cycle
Backlog
Acceptance criteria
Retrospective
```

Avoid requiring:

```txt
Scrum ceremony
Velocity
Story points
Daily scrum
Formal team roles
```

ADDF should feel lightweight, not corporate.

---

# 12. Repository and Folder Structure

ADDF can be used in any repo, but the following structure is recommended.

## 12.1 Standard Project Structure

```txt
Project-Root/
├── AGENTS.md
├── DOMAIN.md
├── STATE.md
├── DECISIONS.md
├── COMMANDS.md
├── STYLE_GUIDE.md
├── SECURITY.md
├── QUESTIONS.md
├── RISKS.md
├── GIT_STRATEGY.md
├── PROMPT_CHANGELOG.md
├── README.md
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── data_model.md
│   ├── api.md
│   ├── permissions.md
│   └── validation.md
├── research/
│   ├── notes.md
│   ├── sources.md
│   └── open_questions.md
├── planning/
│   ├── backlog.md
│   ├── releases/
│   │   └── v0.1/
│   │       ├── release_plan.md
│   │       ├── scope.md
│   │       ├── release_notes.md
│   │       ├── retrospective.md
│   │       └── sprints/
│   │           └── sprint_001/
│   │               ├── requirements.md
│   │               ├── blueprint.md
│   │               ├── blueprint_feedback.md
│   │               ├── acceptance.md
│   │               ├── dry_run.md
│   │               ├── implementation_log.md
│   │               ├── human_review.md
│   │               ├── retrospective.md
│   │               └── rollback_log.md
│   └── features/
│       └── [feature-name]/
│           ├── feature_brief.md
│           ├── research.md
│           ├── feasibility.md
│           └── validation.md
├── prompts/
│   ├── research/
│   ├── architect/
│   ├── builder/
│   ├── audit/
│   └── handoff/
├── starter-kit/
│   ├── blank/
│   └── example-filled/
└── src/
```

## 12.2 Minimum Viable ADDF Structure

For small projects, start with:

```txt
Project-Root/
├── AGENTS.md
├── DOMAIN.md
├── STATE.md
├── COMMANDS.md
├── SECURITY.md
├── planning/
│   ├── backlog.md
│   └── sprints/
│       └── sprint_001/
│           ├── requirements.md
│           ├── blueprint.md
│           ├── acceptance.md
│           ├── dry_run.md
│           ├── implementation_log.md
│           ├── human_review.md
│           └── retrospective.md
└── src/
```

The full structure can be added later.

## 12.3 ADDF Public Framework Repository Structure

For the public ADDF repo itself:

```txt
autonomous-duck-deployment-framework/
├── README.md
├── START_HERE.md
├── LICENSE
├── CHANGELOG.md
├── VERSION.md
├── CONTRIBUTING.md
├── AGENTS.md
├── DOMAIN.md
├── STATE.md
├── DECISIONS.md
├── COMMANDS.md
├── STYLE_GUIDE.md
├── SECURITY.md
├── QUESTIONS.md
├── RISKS.md
├── docs/
│   ├── full-manual.md
│   ├── getting-started.md
│   ├── lifecycle.md
│   ├── modes.md
│   ├── starter-kit.md
│   ├── prompt-catalog.md
│   ├── examples.md
│   └── glossary.md
├── starter-kit/
│   ├── blank/
│   └── example-filled/
├── prompts/
│   ├── research/
│   ├── architect/
│   ├── builder/
│   ├── audit/
│   └── handoff/
├── examples/
│   └── mini-task-tracker/
├── website/
├── assets/
├── brand/
├── tools/
└── planning/
```

---

# 13. Setup and First Session

This section gives the practical first-use path.

## 13.1 What You Need

You need:

- A text editor or code editor.
- A terminal.
- Git.
- At least one capable LLM.
- Optional repo-aware Builder tool such as Codex, Claude Code, Cursor, or Cline.

## 13.2 Create the Project Folder

```bash
mkdir -p src docs research planning/backlog planning/sprints/sprint_001
touch AGENTS.md DOMAIN.md STATE.md DECISIONS.md COMMANDS.md STYLE_GUIDE.md SECURITY.md QUESTIONS.md RISKS.md GIT_STRATEGY.md PROMPT_CHANGELOG.md
```

For release-aware structure:

```bash
mkdir -p planning/releases/v0.1/sprints/sprint_001
```

## 13.3 Fill SECURITY.md First

Before loading any file into an AI tool, define what is safe and unsafe.

```md
# SECURITY.md

## Never Upload
- API keys
- Tokens
- Database connection strings
- .env files
- Real user PII
- Payment information
- Private keys
- Internal credentials

## Safe to Upload
- Framework Markdown files without secrets
- Redacted source snippets
- Sprint planning files
- Documentation without sensitive data
```

## 13.4 Fill AGENTS.md

Use the template in Section 14.1.

This file defines mode behavior and permission rules.

## 13.5 Draft DOMAIN.md

Write:

- Project overview.
- Core entities.
- Workflows.
- Business rules.
- Out-of-scope items.

## 13.6 Initialize STATE.md

Write:

- Current goal.
- Current scale.
- Current mode.
- Active release.
- Active feature.
- Active sprint.
- Status.
- Blockers.
- Last completed step.
- Next intended step.

## 13.7 Run the Kickoff Flow

If you need research, begin with Research Mode.

If you already understand the project, begin with Architect Mode.

For a new project, the recommended flow is:

```txt
Research Mode if needed
Design / Feasibility Mode if needed
Validation Gate
Architect Mode kickoff
Sprint Planning
Builder Dry Run
Build
Review
Commit
```

---

# 14. File Templates

This section provides baseline templates.

## 14.1 AGENTS.md

```md
# AGENTS.md

## Framework
This project uses the Autonomous Duck Deployment Framework.

## Central Rule
The question is never which AI does what. The question is what files must exist before any AI is allowed to act.

## Modes

### Research Mode
- Explore unknowns.
- Summarize sources.
- Identify options, risks, and open questions.
- Do not make final architecture decisions.
- Do not write application source code.

### Design / Feasibility Mode
- Convert research into viable approaches.
- Define MVP scope.
- Identify tradeoffs and risks.
- Produce feasibility notes.
- Do not implement production code.

### Architect Mode
- Produce requirements, blueprints, acceptance criteria, and architecture documentation.
- Make assumptions explicit.
- Update decision, question, and risk ledgers when needed.
- Never write application source files directly.

### Builder Mode
- Implement only approved plans.
- Begin with Permission Level 0 dry run.
- Stop after dry run.
- Wait for explicit human authorization.
- Modify only approved files.
- Log all changes and verification output.

### Audit / Review Mode
- Compare implementation against requirements, blueprint, acceptance, dry run, and logs.
- Identify drift, scope creep, missing tests, and undocumented decisions.
- Do not modify source code.

## Builder Permission Levels
- Level 0: Read-only dry run. No file mutation.
- Level 1: Sprint scope. Modify only files approved in the blueprint and dry run.
- Level 2: Approved expansion. Add minor helpers only when surfaced in dry run and approved.
- Level 3: Supervised refactor. Mutate adjacent files only with explicit logging and approval.
- Level 4: Migration. High-risk structural change. Requires rollback plan before work begins.

## Session Checkpoint Rule
Before ending a session, switching models, or approaching context limits, update STATE.md and implementation_log.md, then produce a handoff summary.
```

## 14.2 STATE.md

```md
# STATE.md

## Current Goal
[What are we trying to accomplish?]

## Active Scale
[Project / Release / Feature / Sprint / Patch]

## Current Mode
[Research / Design-Feasibility / Architect / Builder / Audit / Human Review]

## Active Release
[Version or "None"]

## Active Feature
[Feature name or "None"]

## Active Sprint
Sprint [NUMBER]: [Brief description]
Branch: [branch name]

## Current Status
[Discovery / Research / Feasibility / Planning / In Progress / Verification / Complete / Blocked / Paused]

## Known Blockers
[Blockers or "None"]

## Last Completed Step
[What was last completed?]

## Next Intended Step
[What should happen next?]

## Files Recently Changed
- [file]: [brief note]

## Handoff Notes
[Anything the next model or human must know]
```

## 14.3 DOMAIN.md

```md
# DOMAIN.md

## Project Overview
[What this project does and why it exists.]

## Target Users
[Who uses this?]

## Core Entities

### [Entity Name]
Definition:
Key fields:
Business rules:
What it is NOT:

## Workflows

### [Workflow Name]
1. [Step]
2. [Step]
Edge cases:

## In Scope
- [Item]

## Out of Scope
- [Item]

## Non-Negotiable Rules
- [Rule]
```

## 14.4 DECISIONS.md

```md
# DECISIONS.md

Decisions are never deleted. They are superseded by later decisions.

## Decision 001: [Short Title]
**Date:** [YYYY-MM-DD]
**Status:** Accepted / Superseded / Proposed
**Type:** Architecture / Dependency / Data Model / Security / Process / Other

### Context
[What situation forced this decision?]

### Decision
[What was decided?]

### Tradeoffs
[Costs, limitations, risks]

### Alternatives Considered
[What else was considered?]
```

## 14.5 COMMANDS.md

```md
# COMMANDS.md

## Development
[command]

## Test
[command]

## Build
[command]

## Lint / Type Check
[command]

## Deploy
[command]

## Rollback
[command]

## Notes
[Any environment or setup notes]
```

## 14.6 Feature Brief

```md
# Feature Brief: [Feature Name]

## Summary

## User Value

## In Scope

## Out of Scope

## Research Needed

## Feasibility Risks

## Acceptance Summary

## Related Files

## Release Target
```

## 14.7 Release Plan

```md
# Release Plan: [Version]

## Release Goal

## In Scope

## Out of Scope

## Features

## Required Research

## Risks

## Sprint Plan

## Release Criteria

## Release Notes Draft
```

## 14.8 Sprint requirements.md

```md
# Sprint [NUMBER] Requirements

## Sprint Goal

## Active Scale
[Release / Feature / Sprint]

## Functional Requirements

## Technical Requirements

## In Scope

## Out of Scope

## Constraints

## Related Decisions

## Open Questions
```

## 14.9 Sprint blueprint.md

```md
# Sprint [NUMBER] Blueprint

## Architect

## Summary

## Files to Create

## Files to Modify

## Implementation Steps

## Assumptions

## Dependencies

## Risks

## Rollback Considerations
```

## 14.10 Sprint acceptance.md

```md
# Sprint [NUMBER] Acceptance Criteria

## Functional Criteria
- [ ] [Criterion]

## Technical Criteria
- [ ] [Criterion]

## Documentation Criteria
- [ ] [Criterion]

## Verification Commands
1. [command]

## Definition of Done
- [ ] Requirements met
- [ ] Tests / checks run
- [ ] implementation_log.md updated
- [ ] human_review.md passed
- [ ] STATE.md updated
```

## 14.11 Sprint dry_run.md

```md
# Sprint [NUMBER] Dry Run

## Builder Tool

## Permission Level
Level 0

## Files I Intend to Create

## Files I Intend to Modify

## Files I Intend to Move or Delete

## Commands I Intend to Run

## Dependencies Requested

## Risks or Ambiguities

## Assumptions

**STOPPED. Awaiting Architect audit and human permission.**
```

## 14.12 implementation_log.md

```md
# Sprint [NUMBER] Implementation Log

## Builder Tool

## Permission Level Used

## Summary

## Files Created

## Files Modified

## Files Moved or Deleted

## Commands Run

## Verification Output

## Errors Encountered

## Unfinished Work

## Handoff Notes
```

## 14.13 human_review.md

```md
# Sprint [NUMBER] Human Review

## Scope Gate
- [ ] implementation_log.md lists only approved files.

## Verification Gate
- [ ] Required commands ran.
- [ ] Raw output is present.

## Documentation Gate
- [ ] STATE.md updated.
- [ ] DECISIONS.md updated if needed.
- [ ] Backlog updated if needed.

## Security Gate
- [ ] No secrets committed.
- [ ] No unsafe files added.

## Handoff Gate
- [ ] Next action is clear.
- [ ] Handoff notes exist if pausing.

## Approved to Commit
Yes / No
```

## 14.14 retrospective.md

```md
# Sprint [NUMBER] Retrospective

## What Went Well

## What Broke or Was Unclear

## Blueprint Quality

## Acceptance Criteria Quality

## Time Estimate vs Actual

## New Risks

## New Backlog Items

## New Constraints Added to AGENTS.md
```

## 14.15 rollback_log.md

```md
# Sprint [NUMBER] Rollback Log

## Pre-Implementation
Current clean commit:
Rollback command:

## Post-Implementation
Was rollback needed?
Root cause:
State after rollback:
```

---

# 15. Prompt Catalog

This section contains core prompts. In a real repo, each prompt should also be stored as an individual file under `prompts/`.

## 15.1 Research Brief Prompt

```txt
You are operating in Research Mode.

Research the following topic:
[topic]

Project context:
[brief context]

Constraints:
[constraints]

Do not write source code.
Do not make final project decisions.

Produce:
1. Summary
2. Key findings
3. Options
4. Tradeoffs
5. Risks
6. Open questions
7. Recommended next step for Design / Feasibility Mode
```

## 15.2 Design / Feasibility Prompt

```txt
You are operating in Design / Feasibility Mode.

Use the provided research notes and constraints.

Do not write production code.

Produce:
1. Possible approaches
2. Recommended MVP scope
3. In-scope items
4. Out-of-scope items
5. Feasibility risks
6. Prototype plan if needed
7. Validation Gate checklist
```

## 15.3 Validation Gate Prompt

```txt
You are operating as a Validation Gate reviewer.

Review:
- Research notes
- Feasibility notes
- MVP scope
- Risks
- Open questions

Decide whether the project is ready for Architect Mode.

Return:
1. Ready / Not Ready
2. Blocking questions
3. Risks requiring mitigation
4. Approved approach
5. Files that should be created or updated next
```

## 15.4 Architect Kickoff Prompt

```txt
You are operating in Architect Mode for [PROJECT_NAME].

Use the provided notes, research, feasibility findings, and validation decision.

Do not write application source code.

Generate:
1. DOMAIN.md
2. STATE.md
3. DECISIONS.md starter entries
4. QUESTIONS.md
5. RISKS.md
6. COMMANDS.md draft
7. STYLE_GUIDE.md draft
8. docs/architecture.md draft

Make all assumptions explicit.
```

## 15.5 Sprint Pack Generation Prompt

```txt
You are operating in Architect Mode.

Generate a Sprint Pack for:

Sprint:
[NUMBER and title]

Goal:
[goal]

Use:
- AGENTS.md
- DOMAIN.md
- STATE.md
- DECISIONS.md
- QUESTIONS.md
- RISKS.md

Do not write source code.

Output:
1. requirements.md
2. blueprint.md
3. acceptance.md

The blueprint must list exact files to create or modify.
The acceptance criteria must be checkable.
```

## 15.6 Builder Dry Run Prompt

```txt
You are operating in Builder Mode.

Permission Level: 0.

Read:
- AGENTS.md
- STATE.md
- COMMANDS.md
- requirements.md
- blueprint.md
- acceptance.md

Perform a read-only dry run.

Produce dry_run.md with:
1. Files to create
2. Files to modify
3. Files to move or delete
4. Commands to run
5. Dependencies requested
6. Risks
7. Ambiguities

Stop after the dry run.
Do not write code.
```

## 15.7 Architect Sanity Audit Prompt

```txt
You are operating in Audit / Review Mode.

Compare:
- requirements.md
- blueprint.md
- acceptance.md
- dry_run.md

Check for:
1. Scope creep
2. Missing acceptance criteria
3. Unapproved dependencies
4. Hidden refactors
5. Security issues
6. Missing rollback needs
7. Ambiguous assumptions

Return:
- Approved / Not Approved
- Required corrections
- Recommended Builder permission level
```

## 15.8 Builder Authorization Prompt

```txt
Dry run approved.

Permission Level [LEVEL] authorized.

Proceed according to:
- requirements.md
- blueprint.md
- acceptance.md
- dry_run.md

Rules:
1. Modify only approved files.
2. Do not invent business rules.
3. Do not add dependencies unless approved.
4. Log all changes in implementation_log.md.
5. Run verification commands.
6. Paste raw output.
7. Stop if ambiguity appears.
8. Produce handoff notes before ending.
```

## 15.9 Implementation Review Prompt

```txt
You are operating in Audit / Review Mode.

Review:
- acceptance.md
- dry_run.md
- implementation_log.md
- test output
- changed file list

Determine:
1. Did implementation match the approved plan?
2. Were all acceptance criteria met?
3. Were unapproved files touched?
4. Were dependencies added?
5. Are decisions or docs missing?
6. Is the sprint ready for human_review.md?

Return:
- Approved / Not Approved
- Required fixes
- Documentation updates
- Backlog items
```

## 15.10 Handoff Checkpoint Prompt

```txt
You are approaching the end of this session or a model handoff.

Update or produce:
1. STATE.md update
2. implementation_log.md update
3. QUESTIONS.md additions
4. RISKS.md additions
5. backlog additions
6. Handoff Summary

The Handoff Summary must include:
- Current goal
- Current mode
- Active scale
- Completed work
- Files changed
- Commands run
- Current problems
- Unfinished work
- Next recommended action
- Warnings
```

## 15.11 Resumption Prompt

```txt
You are operating in Architect Mode for resumption.

Loaded files:
- AGENTS.md
- DOMAIN.md
- STATE.md
- DECISIONS.md
- QUESTIONS.md
- RISKS.md
- backlog
- current sprint or release files if present

Summarize:
1. What this project is
2. Current active scale
3. Current mode
4. Active release / feature / sprint
5. Last completed step
6. Known blockers
7. Next safest action
8. Files to load before Builder Mode
```

## 15.12 Release Planning Prompt

```txt
You are operating in Architect Mode.

We are beginning release [VERSION].

Review:
- DOMAIN.md
- STATE.md
- DECISIONS.md
- backlog
- prior release retrospective
- known risks
- user feedback if available

Generate:
1. release_plan.md
2. scope.md
3. release risks
4. required research
5. proposed features
6. proposed sprint sequence
7. release criteria
```

## 15.13 Feature Cycle Prompt

```txt
You are operating in Architect Mode.

Create a feature cycle plan for:
[Feature Name]

Use:
- DOMAIN.md
- STATE.md
- DECISIONS.md
- backlog
- relevant release plan

Generate:
1. feature_brief.md
2. research questions if needed
3. feasibility notes if needed
4. validation checklist
5. proposed sprint map
6. acceptance summary
```

---

# 16. Domain Adaptations

ADDF is domain-agnostic. The structure remains similar, but the contents of `DOMAIN.md`, `COMMANDS.md`, `STYLE_GUIDE.md`, and acceptance criteria change.

## 16.1 Web Applications

Common entities:

- Routes.
- Pages.
- Components.
- API endpoints.
- Users.
- Sessions.
- Database tables.
- Forms.
- Permissions.

Common commands:

```txt
npm run dev
npm run test
npm run build
npm run lint
```

Common risks:

- Auth complexity.
- API contract drift.
- Database migration risk.
- Styling inconsistency.
- Deployment environment mismatch.

## 16.2 Game Development

Common entities:

- Scenes.
- Levels.
- Player states.
- Enemies.
- Game modes.
- Input actions.
- Assets.
- Save data.
- UI screens.

Common commands may include:

- Engine build command.
- Play mode tests.
- Export command.
- Asset validation.
- Packaging command.

Important note:

For game projects, `DOMAIN.md` functions like a technical game design document. It should define gameplay rules explicitly so the AI does not invent mechanics.

## 16.3 Desktop Applications

Common entities:

- Windows.
- Menus.
- Local files.
- System permissions.
- User settings.
- Background services.

Common risks:

- Local filesystem access.
- Platform differences.
- Auto-update complexity.
- Native permissions.
- Installer behavior.

## 16.4 Data / Automation Projects

Common entities:

- Input files.
- Output files.
- Data rows.
- Transformations.
- Validation rules.
- Error records.
- Schedules.

Common risks:

- PII leakage.
- Dirty input data.
- Schema mismatch.
- Silent failure.
- Incomplete logs.

## 16.5 Documentation and Framework Projects

Common entities:

- Pages.
- Sections.
- Templates.
- Prompts.
- Examples.
- Downloads.
- Versions.
- Release packages.

Common risks:

- Outdated docs.
- Inconsistent terminology.
- Broken links.
- Missing examples.
- Unclear onboarding.

---

# 17. Example: Mini Task Tracker

This example shows how ADDF works for a small project.

## 17.1 Project Summary

Mini Task Tracker is a local-only web app for one user.

The user can:

- Add tasks.
- Mark tasks complete.
- Reopen completed tasks.
- Persist tasks across refresh using localStorage.

Out of scope:

- User accounts.
- Cloud sync.
- Collaboration.
- Notifications.

## 17.2 Work Scale

```txt
Project: Mini Task Tracker
Release: v0.1 Local MVP
Feature: Core task list
Sprint: Sprint 001 — Add, display, complete, and persist tasks
```

## 17.3 Lifecycle Application

### Research

Research browser localStorage behavior and basic task app patterns.

### Design & Feasibility

Choose localStorage for persistence because the app is single-user and local-only.

### Validation Gate

Confirm:

- No accounts.
- No backend.
- No sync.
- localStorage is acceptable.

### Architecture

Create:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
docs/architecture.md
```

### Sprint Planning

Generate:

```txt
requirements.md
blueprint.md
acceptance.md
```

### Build & Test

Builder creates:

```txt
TaskForm
TaskList
storage helper
unit tests
```

### Review & Reflection

Review acceptance criteria and update retrospective.

### Deploy / Resume

Build locally, deploy static app if desired, or resume later through `STATE.md`.

## 17.4 Example DOMAIN.md

```md
# DOMAIN.md

## Project Overview
Mini Task Tracker is a local-only task management app for a single user.

## Core Entities

### Task
Definition: A single item the user wants to complete.
Key fields: id, title, status, createdAt, completedAt.
Business rules:
- A task title cannot be empty.
- A completed task can be reopened.
- Tasks are stored in browser localStorage.
What it is NOT:
- A shared task
- A cloud record
- A calendar event
- A reminder

## Workflows

### Add a Task
1. User types a title.
2. User submits.
3. Task is created with active status.
4. Task is saved to localStorage.

Edge case:
If the title is empty or whitespace-only, reject submission.

## Out of Scope
- User accounts
- Cloud sync
- Notifications
- Collaboration
```

---

# 18. Example: Building the ADDF Public Website and Starter Kit

This example applies ADDF to itself.

## 18.1 Project Summary

The ADDF public project includes:

- Website.
- Documentation.
- Starter kit.
- Prompt catalog.
- Example project.
- Download packages.
- Possible CLI init tool.
- Possible web onboarding app.

## 18.2 Work Scale

```txt
Project: ADDF Public Framework Repository
Release: v0.1 Public Proof
Feature: Starter Kit
Sprint: Sprint 001 — Repo structure and starter kit normalization
```

## 18.3 Recommended Early Release Plan

### v0.1 Public Proof

Deliver:

```txt
README.md
START_HERE.md
Full manual Markdown
Full manual PDF
starter-kit/blank
starter-kit/example-filled
examples/mini-task-tracker
prompts/
assets/logo
assets/lifecycle image
```

### v0.2 Website MVP

Deliver:

```txt
Static website
Homepage
Start Here page
Lifecycle page
Modes page
Downloads page
```

### v0.3 Init Tool Prototype

Deliver:

```txt
addf init
minimal/full setup
project-type presets
generated starter files
```

### v0.4 Web Onboarding App

Deliver:

```txt
Browser questionnaire
Generated file preview
Download starter ZIP
Copy prompt buttons
```

## 18.4 Sprint 001 for ADDF Repo

Goal:

```txt
Normalize the repository structure and starter kit so the repo becomes the official public ADDF project home.
```

In scope:

- Organize docs.
- Create starter-kit folder.
- Create prompt folders.
- Create planning structure.
- Create examples placeholder.
- Create README and START_HERE if missing.
- Do not build the website yet.

Out of scope:

- Website implementation.
- CLI implementation.
- Backend.
- Branding finalization.
- Package publishing.

---

# 19. Quick Reference Checklists

## 19.1 Before the First AI Session

- [ ] `SECURITY.md` exists.
- [ ] Never-share items are defined.
- [ ] Project goal is written.
- [ ] If unknowns exist, use Research Mode first.
- [ ] If multiple approaches exist, use Design / Feasibility Mode.
- [ ] If ready, use Architect Mode.

## 19.2 Before Architect Mode

- [ ] `DOMAIN.md` draft exists or raw notes are available.
- [ ] `STATE.md` is current.
- [ ] `QUESTIONS.md` lists unknowns.
- [ ] `RISKS.md` lists known risks.
- [ ] Research and feasibility notes are available if relevant.

## 19.3 Before Builder Mode

- [ ] Sprint Pack exists.
- [ ] `requirements.md` is clear.
- [ ] `blueprint.md` lists files.
- [ ] `acceptance.md` is checkable.
- [ ] Branch is created.
- [ ] Permission Level 0 is declared.
- [ ] Builder is told to dry run and stop.

## 19.4 Before Authorizing Build

- [ ] `dry_run.md` matches `blueprint.md`.
- [ ] Architect Sanity Audit passed.
- [ ] New dependencies are approved.
- [ ] Risks are acceptable.
- [ ] Rollback exists if needed.
- [ ] Permission level is explicit.

## 19.5 Before Committing

- [ ] Implementation log is complete.
- [ ] Test output is pasted.
- [ ] Human review passed.
- [ ] Decisions updated.
- [ ] Backlog updated.
- [ ] State updated.
- [ ] Retrospective completed.
- [ ] Handoff notes exist if pausing.

## 19.6 Before Starting V2

- [ ] V1 release retrospective exists.
- [ ] Backlog is triaged.
- [ ] User feedback is gathered.
- [ ] Risks are reviewed.
- [ ] Decisions are reviewed.
- [ ] V2 goals are defined.
- [ ] V2 release plan is created.

---

# 20. When Things Go Wrong

## 20.1 Builder Touched Unapproved Files

Stop immediately.

Actions:

1. Do not continue implementation.
2. Record the issue in `implementation_log.md`.
3. Compare changes against `dry_run.md`.
4. Revert unapproved changes if needed.
5. Update `RISKS.md`.
6. Add a constraint to `AGENTS.md`.

## 20.2 The AI Invented Business Logic

Actions:

1. Identify the invented logic.
2. Check whether it exists in `DOMAIN.md`.
3. If not, remove it or mark it for human review.
4. Update `DOMAIN.md` if the logic is actually desired.
5. Add a retrospective note.
6. Add a Builder constraint.

## 20.3 The Project Is Confused After Many Sprints

Run a Cross-Sprint Consistency Audit.

Load:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
recent sprint folders
docs/architecture.md
```

Ask:

```txt
Identify drift between the project files and implemented work.
List contradictions.
Recommend updates to restore consistency.
Do not write source code.
```

## 20.4 The Builder Runs Out of Tokens

Use the Session Checkpoint Protocol.

Require the Builder to produce:

```txt
implementation_log.md update
STATE.md update
handoff_summary.md
```

Then open a new session and run the Resumption Protocol.

## 20.5 V1 Is Done and V2 Feels Unclear

Start a Release Planning Sprint.

Load:

```txt
STATE.md
DECISIONS.md
backlog
V1 retrospective
user feedback
RISKS.md
QUESTIONS.md
```

Ask Architect Mode to generate a V2 release plan.

## 20.6 The Framework Feels Too Heavy

Scale down.

Use Minimum Viable ADDF:

```txt
AGENTS.md
DOMAIN.md
STATE.md
COMMANDS.md
SECURITY.md
planning/sprints/sprint_001/
```

Do not use release folders, feature folders, or full audit files until needed.

---

# 21. Glossary

## Acceptance Criteria

The checklist that defines whether work is complete.

## ADDF

Autonomous Duck Deployment Framework.

## Architect Mode

The AI mode responsible for planning, requirements, blueprints, decisions, and acceptance criteria. It does not write source code.

## Audit / Review Mode

The AI mode responsible for checking output against plans, acceptance criteria, logs, and decisions.

## Builder Mode

The AI mode responsible for implementation. It begins with a dry run and requires explicit permission before changing files.

## Context Engineering

The practice of placing the right information in the right files and loading only the context needed for the current session.

## Design / Feasibility Mode

The AI mode that turns research into possible approaches, MVP scope, feasibility notes, and tradeoff analysis.

## Dry Run

A read-only Builder report describing intended file changes before implementation.

## Feature Cycle

The process for adding a new capability to an existing project.

## Handoff Summary

A written summary that allows another LLM or human to resume work.

## Local File Sovereignty

The principle that project memory lives in local files, not in chat history.

## Patch

A small, low-risk change that does not require a full sprint.

## Project Brain

The collection of Markdown files that preserve project state, decisions, constraints, and workflow.

## Project Lifecycle

The full 8-step lifecycle used for new projects, major releases, or pivots.

## Release Cycle

The process for planning and delivering a project version such as V1 or V2.

## Research Mode

The AI mode that explores unknowns, summarizes sources, compares tools, and identifies risks.

## Resumption

The process of restarting work from project files after a break or handoff.

## Sprint

A bounded AI implementation packet, not necessarily a Scrum sprint.

## Sprint Pack

The set of `requirements.md`, `blueprint.md`, and `acceptance.md`.

## Validation Gate

The human approval checkpoint that determines whether research and feasibility work is ready for architecture.

---

# Closing Principle

ADDF is not a rigid process. It is a scalable structure.

Use the full lifecycle when the work is uncertain, foundational, or high risk.

Use release cycles to move from V1 to V2.

Use feature cycles to add capabilities.

Use sprint loops to implement bounded work.

Use quick patches for tiny fixes.

Keep the project memory in files.

Let the AI think, plan, build, and review — but only from the context you deliberately provide.

> **Files are permanent. Chats are disposable.**
