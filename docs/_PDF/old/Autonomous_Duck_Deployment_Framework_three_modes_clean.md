# Autonomous Duck Deployment Framework

> **A file-first, AI-assisted project delivery system for research, design, development, handoff, and long-term iteration.**

**Framework Version:** 1.0 Draft  
**Short Name:** ADDF  
**Core Principle:** Files are permanent. Chats are disposable.  
**Core Methodology:** Context Engineering through Local File Sovereignty  
**Three Modes:** Research Mode, Design Mode, Develop Mode  
**Work Scale:** Project → Release → Feature → Sprint → Patch  
**Lifecycle:** Research → Design & Feasibility → Validation → Architecture → Sprint Planning → Build & Test → Review & Reflection → Deploy / Maintain / Resume  
**Domain Coverage:** Web, Game, Desktop, Mobile, Data / Automation, Documentation, Tooling, Education

---

## Contents

- [1. Why This Framework Exists](#1-why-this-framework-exists)
  - [1.1 The Vibe Coding Problem](#11-the-vibe-coding-problem)
  - [1.2 The Rubber Duck Principle](#12-the-rubber-duck-principle)
  - [1.3 Context Engineering Over Context Windows](#13-context-engineering-over-context-windows)
  - [1.4 The Central Rule](#14-the-central-rule)
- [2. The Framework in One Page](#2-the-framework-in-one-page)
- [3. The Three ADDF Modes](#3-the-three-addf-modes)
  - [3.1 Research Mode](#31-research-mode)
  - [3.2 Design Mode](#32-design-mode)
  - [3.3 Develop Mode](#33-develop-mode)
  - [3.4 Why Only Three Modes?](#34-why-only-three-modes)
- [4. The Scale Model](#4-the-scale-model)
  - [4.1 Project](#41-project)
  - [4.2 Release](#42-release)
  - [4.3 Feature](#43-feature)
  - [4.4 Sprint](#44-sprint)
  - [4.5 Patch](#45-patch)
  - [4.6 How Scale Controls Process Depth](#46-how-scale-controls-process-depth)
- [5. How the Modes, Scale Model, and 8 Steps Fit Together](#5-how-the-modes-scale-model-and-8-steps-fit-together)
- [6. The 8-Step ADDF Lifecycle](#6-the-8-step-addf-lifecycle)
  - [Step 1 — Research](#step-1--research)
  - [Step 2 — Design & Feasibility](#step-2--design--feasibility)
  - [Step 3 — Validation Gate](#step-3--validation-gate)
  - [Step 4 — Architecture](#step-4--architecture)
  - [Step 5 — Sprint Planning](#step-5--sprint-planning)
  - [Step 6 — Build & Test](#step-6--build--test)
  - [Step 7 — Review & Reflection](#step-7--review--reflection)
  - [Step 8 — Deploy, Maintain, or Resume](#step-8--deploy-maintain-or-resume)
- [7. The Project Brain](#7-the-project-brain)
- [8. Release Cycles and Version Updates](#8-release-cycles-and-version-updates)
- [9. Feature Cycles](#9-feature-cycles)
- [10. The Sprint Loop](#10-the-sprint-loop)
- [11. Develop Mode Permission Levels](#11-develop-mode-permission-levels)
- [12. Handoff, Resumption, and Model Switching](#12-handoff-resumption-and-model-switching)
- [13. Agile and Scrum Relationship](#13-agile-and-scrum-relationship)
- [14. Repository and Folder Structure](#14-repository-and-folder-structure)
- [15. Setup and First Session](#15-setup-and-first-session)
- [16. File Templates](#16-file-templates)
- [17. Prompt Catalog](#17-prompt-catalog)
- [18. Domain Adaptations](#18-domain-adaptations)
- [19. Example: Mini Task Tracker](#19-example-mini-task-tracker)
- [20. Example: Building the ADDF Public Website and Starter Kit](#20-example-building-the-addf-public-website-and-starter-kit)
- [21. Quick Reference Checklists](#21-quick-reference-checklists)
- [22. When Things Go Wrong](#22-when-things-go-wrong)
- [23. Glossary](#23-glossary)
- [Closing Principle](#closing-principle)

---

# 1. Why This Framework Exists

AI-assisted development is powerful, but it can become chaotic when the project memory lives inside a chat thread.

A developer describes an idea, asks an AI to generate code, reacts to the result, asks for changes, pastes errors, accepts fixes, and keeps going. This can feel fast at first. Over time, the conversation fills with outdated decisions, partial fixes, abandoned ideas, and code that no longer matches the project.

The Autonomous Duck Deployment Framework exists to make AI-assisted work more structured, resumable, auditable, and safe.

ADDF treats AI tools as temporary collaborators. The durable memory of the project lives in local Markdown files. The files define the project, record decisions, preserve state, guide implementation, and allow one LLM to hand work off to another.

The framework is not meant to make small work feel heavy. It is meant to help you choose the right amount of structure for the size and risk of the work.

A typo should not need a full lifecycle.

A new product should not be vibe-coded from a single prompt.

ADDF gives you a way to scale the process.

## 1.1 The Vibe Coding Problem

Vibe coding is what happens when the chat becomes the project.

The developer says what they want, the AI generates output, and the developer keeps steering from inside the same conversation. This breaks down in predictable ways.

### Context bleed and memory bloat

Long chats collect old code, outdated decisions, abandoned approaches, and unrelated discussion. The AI may treat all of it as relevant, even when some of it is no longer true.

### Improvisation bias

When the AI does not have a clear written specification, it invents missing logic. It may invent database fields, workflows, permissions, project structure, dependencies, or edge-case behavior.

The AI is not being malicious. It is filling gaps.

ADDF reduces those gaps by requiring key project logic to exist in files before implementation begins.

### The missing anchor

If the chat is the project memory, then the project becomes fragile. It is hard to search, hard to hand off, hard to resume, and easy to lose when the model changes, a session ends, or tokens run out.

ADDF makes the file system the anchor.

## 1.2 The Rubber Duck Principle

The name comes from rubber duck debugging.

A rubber duck does not solve your problem for you. It forces you to explain the problem clearly enough that the solution becomes visible.

ADDF applies that idea to AI-assisted development.

Before the AI builds, the human and AI must explain the project clearly in writing. Those explanations live in Markdown files.

> **A rubber duck cannot invent your business logic. Neither should your AI.**

## 1.3 Context Engineering Over Context Windows

A large context window is not the same as clean context.

If you paste an entire codebase, a long chat history, old notes, and half-finished plans into an AI session, the model has more information, but not necessarily better information.

ADDF uses Context Engineering.

Context Engineering means:

- Put project rules in the right files.
- Keep current state separate from old history.
- Record decisions instead of relying on memory.
- Load only the files needed for the current task.
- Close or checkpoint sessions before they become noisy.
- Treat Markdown files as the durable project brain.

The goal is not to give the AI everything.

The goal is to give the AI the right things.

## 1.4 The Central Rule

> **The question is never which AI does what. The question is what files must exist before any AI is allowed to act.**

This rule makes ADDF model-agnostic.

Claude, ChatGPT, Gemini, Codex, Cursor, Cline, or any other capable LLM can participate if it reads the same files and follows the same mode rules.

The AI is interchangeable.

The files are the source of truth.

---

# 2. The Framework in One Page

ADDF has three main ideas:

```txt
1. Scale Model — How big is the work?
2. 8-Step Lifecycle — Where is the work in the process?
3. Three Modes — What is the AI allowed to do right now?
```

The **Scale Model** classifies the work:

```txt
Project → Release → Feature → Sprint → Patch
```

The **8-Step Lifecycle** describes the journey:

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

The **Three Modes** control AI behavior:

```txt
Research Mode = learn
Design Mode = write Markdown project memory
Develop Mode = write code or implementation files
```

The Project Brain is the set of Markdown files that makes the system work:

```txt
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
SECURITY.md
QUESTIONS.md
RISKS.md
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
```

ADDF is not a rigid waterfall process. It is a scalable workflow.

Use the full lifecycle for new projects, major versions, major pivots, or high-risk features.

Use a feature cycle for new capabilities inside an existing project.

Use the sprint loop for bounded implementation.

Use a quick patch path for tiny low-risk changes.

---

# 3. The Three ADDF Modes

ADDF uses three modes:

```txt
Research Mode
Design Mode
Develop Mode
```

These modes answer one question:

> **What is the AI allowed to do in this session?**

## 3.1 Research Mode

Research Mode is for learning before deciding.

The AI investigates, compares, summarizes, and identifies unknowns.

Use Research Mode when:

- You do not understand the domain yet.
- You need to compare tools.
- You need to review documentation.
- You need to identify risks.
- You need examples or prior art.
- You need to understand feasibility before planning.
- You need to collect information before writing project rules.

Research Mode may produce:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
research_summary.md
```

Research Mode may not:

- Write application source code.
- Modify implementation files.
- Make final project decisions.
- Pretend uncertain information is settled.
- Add dependencies.
- Rewrite the Project Brain without explicit instruction.

### Research Mode rule

> Research Mode explores. It does not decide or build.

## 3.2 Design Mode

Design Mode is for writing the project memory.

Design Mode writes and updates Markdown files.

It turns research, ideas, requirements, feedback, logs, and decisions into durable project context.

Design Mode may produce or update:

```txt
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
research_notes.md
design_options.md
feasibility.md
validation.md
release_plan.md
feature_brief.md
requirements.md
blueprint.md
acceptance.md
dry_run_review.md
human_review.md
retrospective.md
handoff_summary.md
planning/backlog.md
docs/architecture.md
docs/data_model.md
docs/api.md
```

Design Mode is used for:

- Feasibility analysis.
- MVP scope.
- Validation gates.
- Architecture.
- Sprint planning.
- Release planning.
- Feature planning.
- Dry run review.
- Implementation review.
- Retrospectives.
- Resumption summaries.
- Handoff notes.
- Documentation updates.

Design Mode may not:

- Write application source code.
- Modify implementation files.
- Add dependencies to the codebase.
- Run uncontrolled code changes.
- Pretend a plan is implementation.

### Design Mode rule

> Design Mode writes Markdown project memory. It does not write source code.

## 3.3 Develop Mode

Develop Mode is for changing the actual project.

This is the only mode that writes code or implementation files.

Develop Mode may create or modify:

```txt
src/
app/
components/
tests/
scripts/
website files
game project files
config files
package files
build files
tooling files
assets when approved
```

Develop Mode may also write implementation-related Markdown logs:

```txt
dry_run.md
implementation_log.md
handoff_summary.md
```

Develop Mode must start with a dry run.

The default first permission level is:

```txt
Level 0 — Dry Run Only
```

The AI lists what it intends to change and then stops.

After review and approval, the human may authorize a higher permission level.

Develop Mode must:

- Read the approved sprint files.
- Start with a dry run.
- Stop after the dry run.
- Wait for explicit permission.
- Modify only approved files.
- Log every change.
- Run verification commands.
- Paste raw output into `implementation_log.md`.
- Stop if ambiguity appears.
- Checkpoint before token limits or model handoff.

Develop Mode may not:

- Invent business rules.
- Rewrite project planning files unless explicitly approved.
- Add dependencies without a `DECISIONS.md` entry.
- Modify unrelated files.
- Skip the dry run.
- Skip verification.
- Continue blindly after failures.

### Develop Mode rule

> Develop Mode changes implementation files only after a dry run and human approval.

## 3.4 Why Only Three Modes?

The three modes are easier to remember and easier to enforce.

```txt
Research = learn
Design = write Markdown
Develop = write implementation
```

This clean separation removes the clash between modes and lifecycle steps.

The lifecycle describes the process.

The scale model describes how much process is needed.

The mode describes what the AI is allowed to do.

---

# 4. The Scale Model

The Scale Model answers:

> **How big is this work?**

ADDF recognizes five work scales:

```txt
Project
Release
Feature
Sprint
Patch
```

This model prevents over-processing small work and under-processing large work.

## 4.1 Project

A Project is the whole initiative.

Examples:

```txt
Build the ADDF public website and starter kit ecosystem.
Build a task management app.
Build a Unity educational prototype.
Build a data automation tool.
Build a local politics education website.
```

Project-level work usually needs the full lifecycle.

## 4.2 Release

A Release is a version of a project.

Examples:

```txt
v0.1 Public Proof
v0.2 Website MVP
v0.3 CLI Init Tool
v1.0 Stable Release
v2.0 Major Update
```

A release groups multiple features into a version.

A release has its own plan, scope, criteria, notes, and retrospective.

## 4.3 Feature

A Feature is a new capability.

Examples:

```txt
Starter kit download
Prompt catalog page
CLI init command
Web onboarding app
Search page
Export button
New enemy type
CSV import workflow
```

A feature may need research, design, validation, and one or more sprints.

## 4.4 Sprint

A Sprint is a bounded implementation packet.

In ADDF, a sprint is not necessarily a Scrum sprint. It is a controlled unit of AI-assisted implementation.

A sprint has:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
```

Sprints are where Develop Mode usually operates.

## 4.5 Patch

A Patch is a tiny low-risk change.

Examples:

```txt
Fix a typo.
Update a broken link.
Rename a heading.
Change a small copy block.
Adjust one style value.
```

A patch usually does not need a full sprint pack.

It may still need a note in `STATE.md` or a small commit.

## 4.6 How Scale Controls Process Depth

The larger or riskier the work, the more of the lifecycle you use.

| Work Scale | Process Depth | Typical Modes |
|---|---|---|
| Project | Full 8-step lifecycle | Research, Design, Develop |
| Release | Full or partial lifecycle | Research, Design, Develop |
| Feature | Feature cycle | Research if needed, Design, Develop |
| Sprint | Sprint loop | Design, Develop |
| Patch | Minimal path | Develop or human-only |

The scale model does not replace the lifecycle.

It tells you how much of the lifecycle to apply.

---

# 5. How the Modes, Scale Model, and 8 Steps Fit Together

ADDF separates three decisions that are often mixed together.

## Decision 1 — Scale

Ask:

```txt
How big is this work?
```

Answer:

```txt
Project / Release / Feature / Sprint / Patch
```

## Decision 2 — Lifecycle Step

Ask:

```txt
Where is this work in the process?
```

Answer:

```txt
Research / Design & Feasibility / Validation / Architecture / Sprint Planning / Build & Test / Review & Reflection / Deploy-Maintain-Resume
```

## Decision 3 — Mode

Ask:

```txt
What is the AI allowed to do right now?
```

Answer:

```txt
Research / Design / Develop
```

The relationship is:

```txt
Scale tells you how much process you need.
Lifecycle tells you where the work is.
Mode tells the AI what kind of action is allowed.
```

## 5.1 Mode Mapping to the Lifecycle

| Lifecycle Step | Main Mode |
|---|---|
| 1. Research | Research Mode |
| 2. Design & Feasibility | Design Mode |
| 3. Validation Gate | Design Mode + Human |
| 4. Architecture | Design Mode |
| 5. Sprint Planning | Design Mode |
| 6. Build & Test | Develop Mode |
| 7. Review & Reflection | Design Mode + Human |
| 8. Deploy, Maintain, or Resume | Design Mode and/or Develop Mode |

## 5.2 Example: New Project

```txt
Scale: Project
Lifecycle: Full 8 steps
Modes:
- Research Mode for unknowns
- Design Mode for project brain, architecture, sprint packs, reviews
- Develop Mode for implementation
```

## 5.3 Example: New Feature

```txt
Scale: Feature
Lifecycle: Feature-sized version of the 8 steps
Modes:
- Research Mode if the feature has unknowns
- Design Mode for feature brief, feasibility, sprint pack
- Develop Mode for implementation
- Design Mode for review and state updates
```

## 5.4 Example: Sprint

```txt
Scale: Sprint
Lifecycle: Mostly Steps 5–7
Modes:
- Design Mode creates requirements.md, blueprint.md, acceptance.md
- Develop Mode creates dry_run.md, implements after approval, writes implementation_log.md
- Design Mode reviews output and updates state
```

## 5.5 Example: Patch

```txt
Scale: Patch
Lifecycle: Minimal
Modes:
- Human-only or Develop Mode
- Design Mode only if state or documentation needs updating
```

---

# 6. The 8-Step ADDF Lifecycle

The 8-step lifecycle is the project journey.

It is not meant to be run fully for every tiny change. It is a scalable pattern that can apply to a whole project, a release, a high-risk feature, or a major pivot.

## Step 1 — Research

**Mode:** Research Mode  
**Purpose:** Learn before deciding.

Research explores:

- Problem space.
- User needs.
- Existing tools.
- Technical constraints.
- Prior art.
- Risks.
- Unknowns.
- Feasibility questions.

Research produces:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
```

Research is complete enough when the unknowns are visible and the project can move to design thinking.

## Step 2 — Design & Feasibility

**Mode:** Design Mode  
**Purpose:** Turn research into possible approaches.

Design & Feasibility answers:

- What are the possible approaches?
- Which approach is simplest?
- Which approach is safest?
- What is the MVP?
- What is out of scope?
- What should be prototyped?
- What constraints shape the work?

Design & Feasibility produces:

```txt
design_options.md
feasibility.md
mvp_scope.md
risk_matrix.md
prototype_plan.md
```

This step is still not code. It is planning.

## Step 3 — Validation Gate

**Mode:** Design Mode + Human  
**Purpose:** Confirm that the work is defined enough to architect or sprint.

The Validation Gate asks:

- Is the goal clear?
- Is the target user clear?
- Is the MVP clear?
- Are risks visible?
- Are open questions listed?
- Are security boundaries known?
- Is the preferred direction chosen?
- Are out-of-scope items explicit?

Validation produces:

```txt
validation.md
updated QUESTIONS.md
updated RISKS.md
approved_approach.md
```

The human decides whether the work can proceed.

## Step 4 — Architecture

**Mode:** Design Mode  
**Purpose:** Convert validated intent into durable project rules.

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

The AI is writing the project brain, not source code.

## Step 5 — Sprint Planning

**Mode:** Design Mode  
**Purpose:** Convert architecture or feature intent into an implementation-ready sprint pack.

Sprint Planning produces:

```txt
requirements.md
blueprint.md
acceptance.md
```

The sprint pack defines:

- What is being built.
- What is not being built.
- What files may be touched.
- What assumptions must be reviewed.
- What commands must run.
- What counts as done.

## Step 6 — Build & Test

**Mode:** Develop Mode  
**Purpose:** Implement approved work.

Develop Mode begins with a dry run.

It reads:

```txt
AGENTS.md
STATE.md
COMMANDS.md
requirements.md
blueprint.md
acceptance.md
relevant source files
```

It produces:

```txt
dry_run.md
```

Then it stops.

After approval, it implements and logs:

```txt
source files
tests
config changes if approved
implementation_log.md
test output
```

## Step 7 — Review & Reflection

**Mode:** Design Mode + Human  
**Purpose:** Verify the work and update the project brain.

Review & Reflection includes:

- Compare implementation to acceptance criteria.
- Check whether the dry run was followed.
- Confirm verification output.
- Update decisions.
- Update backlog.
- Update state.
- Write retrospective.
- Add new constraints to `AGENTS.md` when needed.

It produces:

```txt
human_review.md
retrospective.md
updated STATE.md
updated DECISIONS.md
updated planning/backlog.md
updated AGENTS.md if needed
```

## Step 8 — Deploy, Maintain, or Resume

**Mode:** Design Mode and/or Develop Mode  
**Purpose:** Decide what happens after review.

The project may:

- Deploy.
- Start another sprint.
- Start a new feature cycle.
- Start a new release cycle.
- Enter maintenance.
- Pause.
- Resume later.
- Pivot and rerun the lifecycle at a larger scale.

This step may produce:

```txt
release_notes.md
rollback_log.md
handoff_summary.md
updated COMMANDS.md
updated RISKS.md
updated STATE.md
```

---

# 7. The Project Brain

The Project Brain is the set of files that makes ADDF work.

It is the durable memory of the project.

## 7.1 Core Brain Files

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
```

## 7.2 Sprint Files

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
rollback_log.md
```

## 7.3 Release and Feature Files

```txt
release_plan.md
scope.md
release_notes.md
feature_brief.md
feasibility.md
validation.md
research.md
sprint_map.md
```

## 7.4 Why the Project Brain Matters

The Project Brain allows:

- One model to hand off to another.
- Work to resume after weeks away.
- Decisions to persist.
- Scope to remain visible.
- Builders to avoid inventing business logic.
- Reviews to compare work against plans.
- Releases and features to evolve without restarting the whole project.

---

# 8. Release Cycles and Version Updates

ADDF explicitly supports V1, V2, V3, and long-term iteration.

A completed V1 does not end the framework. It creates the baseline for V2.

## 8.1 What Is a Release Cycle?

A Release Cycle is a version-level planning container.

Examples:

```txt
v0.1 Public Proof
v0.2 Website MVP
v0.3 Init Tool Prototype
v1.0 Stable Public Release
v2.0 Major Update
```

A release cycle defines:

- Release goal.
- In-scope features.
- Out-of-scope items.
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

## 8.3 Starting V2 After V1

When V1 is done, load:

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

Use Design Mode to generate:

```txt
planning/releases/v2.0/release_plan.md
planning/releases/v2.0/scope.md
planning/releases/v2.0/research_questions.md
updated STATE.md
updated planning/backlog.md
updated RISKS.md
```

V2 may then use Research Mode, Design Mode, and Develop Mode as needed.

You do not restart the Project Brain. You update it.

## 8.4 Release Completion Criteria

A release is complete when:

- All in-scope features are complete or intentionally deferred.
- Release criteria are met.
- Documentation is updated.
- `CHANGELOG.md` is updated.
- Release notes exist.
- `STATE.md` reflects release status.
- Known issues are in the backlog.
- Deployment or distribution is complete.
- Release retrospective exists.

---

# 9. Feature Cycles

A Feature Cycle adds a capability to an existing project.

It does not restart the whole project.

## 9.1 Feature Cycle Flow

```txt
1. Add idea to backlog
2. Write feature brief
3. Research if needed
4. Design / feasibility if needed
5. Validate scope
6. Generate sprint pack
7. Develop with dry run
8. Review and update project brain
```

## 9.2 Feature Folder Structure

```txt
planning/
└── features/
    └── [feature-name]/
        ├── feature_brief.md
        ├── research.md
        ├── feasibility.md
        ├── validation.md
        ├── decisions.md
        └── sprint_map.md
```

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

## Release Target
[Version]
```

## 9.4 Feature Completion Criteria

A feature is complete when:

- Feature brief is satisfied.
- Required sprints are complete.
- Acceptance criteria pass.
- Documentation is updated.
- `STATE.md` is updated.
- New decisions are recorded.
- Deferred work is moved to backlog.
- Feature appears in release notes if relevant.

---

# 10. The Sprint Loop

The Sprint Loop is the implementation workflow for bounded work.

Use it for:

- New features.
- Multi-file changes.
- Refactors.
- Migrations.
- Tooling additions.
- Website sections.
- Starter kit updates.
- Prompt catalog updates.
- Documentation package changes.

## 10.1 Sprint Loop Overview

```txt
1. Pre-Flight Gate
2. Design Sprint Pack
3. Human Blueprint Review
4. Develop Dry Run
5. Design Review of Dry Run
6. Dependency Approval Gate
7. Authorize Development
8. Build & Test
9. Design Review of Output
10. Human Approval Gate
11. Commit, Update, Reset
```

## 10.2 Pre-Flight Gate

The human checks:

- Is the scale correct?
- Is this a sprint, feature, release, or patch?
- Are there blockers in `QUESTIONS.md`?
- Are there high risks in `RISKS.md`?
- Is the relevant branch created?
- Is scope clear enough?

If not, go back to Research Mode or Design Mode.

## 10.3 Design Sprint Pack

Design Mode creates:

```txt
requirements.md
blueprint.md
acceptance.md
```

## 10.4 Human Blueprint Review

The human checks:

- Does the blueprint match the desired result?
- Does it conflict with `DOMAIN.md`?
- Are assumptions clear?
- Are files listed?
- Is scope limited?
- Are out-of-scope items explicit?
- Are acceptance criteria checkable?

If rejected, write `blueprint_feedback.md` and revise.

## 10.5 Develop Dry Run

Develop Mode starts at Permission Level 0.

It creates or outputs:

```txt
dry_run.md
```

The dry run must list:

- Files to create.
- Files to modify.
- Files to move or delete.
- Commands to run.
- Dependencies requested.
- Risks.
- Ambiguities.
- Assumptions.

Then it stops.

## 10.6 Design Review of Dry Run

Design Mode reviews the dry run against:

```txt
requirements.md
blueprint.md
acceptance.md
```

It checks:

- Scope creep.
- Hidden refactors.
- Missing files.
- Unapproved dependencies.
- Missing tests.
- Security concerns.
- Rollback needs.

## 10.7 Dependency Approval Gate

Any new dependency requires a `DECISIONS.md` entry before development continues.

## 10.8 Authorize Development

The human explicitly authorizes Develop Mode:

```txt
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
Modify only approved files.
Log all changes in implementation_log.md.
Run verification commands and paste raw output.
Stop if ambiguity appears.
```

## 10.9 Build & Test

Develop Mode implements approved changes and writes:

```txt
implementation_log.md
test output
handoff notes if needed
```

## 10.10 Design Review of Output

Design Mode reviews:

```txt
acceptance.md
dry_run.md
implementation_log.md
test output
changed files
```

It determines:

- Did implementation match the approved plan?
- Were all acceptance criteria met?
- Were unapproved files touched?
- Were new dependencies added?
- Are docs or decisions missing?
- Is the sprint ready for human review?

## 10.11 Human Approval Gate

The human checks:

- Scope.
- Verification.
- Documentation.
- Decisions.
- Security.
- State.
- Handoff readiness.

## 10.12 Commit, Update, Reset

The human commits the work, updates the Project Brain, and closes or checkpoints the AI session.

---

# 11. Develop Mode Permission Levels

Permission levels apply to Develop Mode.

They control how much the AI can change.

| Level | Name | Meaning |
|---|---|---|
| 0 | Dry Run Only | Read-only planning of intended changes. No implementation. |
| 1 | Approved Sprint Scope | Modify only files explicitly approved in blueprint and dry run. |
| 2 | Approved Expansion | Add minor helper files surfaced during dry run and approved by Design Mode / human. |
| 3 | Supervised Refactor | Modify adjacent files only with explicit approval and detailed logging. |
| 4 | Migration / High-Risk Change | Structural changes, migrations, or architecture-heavy work. Requires rollback plan. |

Most work starts with Level 0 and proceeds to Level 1 after approval.

Levels 2–4 require stronger review.

---

# 12. Handoff, Resumption, and Model Switching

ADDF supports switching between LLMs.

If Codex runs out of tokens and Claude needs to pick up, the outgoing model writes state to files and the incoming model reads those files.

## 12.1 Session Checkpoint Protocol

Before ending a session, switching models, or approaching context limits, the active AI must update or produce:

```txt
STATE.md
implementation_log.md if in Develop Mode
QUESTIONS.md
RISKS.md
planning/backlog.md
retrospective.md if appropriate
handoff_summary.md
```

## 12.2 Handoff Summary Template

```md
# Handoff Summary

## Current Goal
[What the session was trying to accomplish]

## Current Mode
[Research / Design / Develop]

## Active Scale
[Project / Release / Feature / Sprint / Patch]

## Active Release
[Version or "None"]

## Active Feature
[Feature or "None"]

## Active Sprint
[Sprint or "None"]

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
[What the next AI or human should do first]

## Warnings
[Any risks, assumptions, or caveats]
```

## 12.3 Incoming Model Resumption Protocol

A new AI should load:

```txt
AGENTS.md
DOMAIN.md
STATE.md
COMMANDS.md
DECISIONS.md
QUESTIONS.md
RISKS.md
current requirements.md
current blueprint.md
current acceptance.md
current dry_run.md
current implementation_log.md
handoff_summary.md
```

Then it runs:

```txt
Execute Handoff Resumption Protocol.

Read the loaded files.
Summarize:
1. Current project
2. Current mode
3. Active scale
4. Active release / feature / sprint
5. Completed work
6. Unfinished work
7. Blockers
8. Files changed
9. Next safest action

Do not modify files until the human authorizes the correct mode.
```

## 12.4 Resumption After a Long Break

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

Use Design Mode to reconstruct state and decide the next safest action.

---

# 13. Agile and Scrum Relationship

ADDF borrows useful ideas from Agile but is not Scrum.

It uses terms like:

- Sprint
- Backlog
- Acceptance criteria
- Retrospective
- Review
- Iteration

It does not require:

- Scrum Master
- Product Owner
- Daily standups
- Story points
- Velocity tracking
- Formal ceremonies
- Two-week cadence

## 13.1 ADDF Sprint vs Scrum Sprint

A Scrum sprint is a timeboxed team iteration.

An ADDF sprint is a bounded AI implementation packet.

It is defined by:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
```

It is less about time and more about controlled scope.

## 13.2 Agile-ish Mapping

| Agile / Scrum Term | ADDF Equivalent |
|---|---|
| Product | Project |
| Release | Release Cycle |
| Epic | Major Feature Group |
| User Story | Feature Brief / Requirement |
| Sprint | AI Implementation Packet |
| Acceptance Criteria | acceptance.md |
| Backlog | planning/backlog.md |
| Sprint Review | Design Review + Human Review |
| Retrospective | retrospective.md |
| Definition of Done | acceptance.md + human_review.md |
| Product Owner | Human Operator |
| Development Team | Develop Mode + Human |
| Scrum Master | Not required |

---

# 14. Repository and Folder Structure

## 14.1 Standard ADDF Project Structure

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
│   └── features/
│       └── [feature-name]/
│           ├── feature_brief.md
│           ├── research.md
│           ├── feasibility.md
│           └── validation.md
├── prompts/
│   ├── research/
│   ├── design/
│   └── develop/
├── starter-kit/
│   ├── blank/
│   └── example-filled/
└── src/
```

## 14.2 Minimum Viable ADDF Structure

For small projects:

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

## 14.3 ADDF Public Framework Repository Structure

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
│   ├── design/
│   └── develop/
├── examples/
│   └── mini-task-tracker/
├── website/
├── assets/
├── brand/
├── tools/
└── planning/
```

---

# 15. Setup and First Session

## 15.1 What You Need

You need:

- A text editor or code editor.
- A terminal.
- Git.
- At least one capable LLM.
- Optional repo-aware development tool such as Codex, Claude Code, Cursor, or Cline.

## 15.2 Create the Project Folder

```bash
mkdir -p src docs research planning/sprints/sprint_001
touch AGENTS.md DOMAIN.md STATE.md DECISIONS.md COMMANDS.md STYLE_GUIDE.md SECURITY.md QUESTIONS.md RISKS.md GIT_STRATEGY.md PROMPT_CHANGELOG.md
touch planning/backlog.md
touch planning/sprints/sprint_001/requirements.md planning/sprints/sprint_001/blueprint.md planning/sprints/sprint_001/acceptance.md planning/sprints/sprint_001/dry_run.md planning/sprints/sprint_001/implementation_log.md planning/sprints/sprint_001/human_review.md planning/sprints/sprint_001/retrospective.md
```

## 15.3 Fill SECURITY.md First

Before loading anything into an AI tool:

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

## 15.4 Fill AGENTS.md

Use the template in Section 16.1.

This file defines the three modes and Develop Mode permission levels.

## 15.5 Draft DOMAIN.md

Write:

- Project overview.
- Target users.
- Core entities.
- Workflows.
- Business rules.
- Out-of-scope items.

## 15.6 Initialize STATE.md

Write:

- Current goal.
- Active scale.
- Current mode.
- Active release.
- Active feature.
- Active sprint.
- Status.
- Blockers.
- Last completed step.
- Next intended step.

## 15.7 Start the Workflow

For a new project:

```txt
Research Mode if needed
Design Mode for feasibility and project brain
Design Mode for sprint planning
Develop Mode for dry run and implementation
Design Mode for review and state updates
```

---

# 16. File Templates

## 16.1 AGENTS.md

```md
# AGENTS.md

## Framework
This project uses the Autonomous Duck Deployment Framework.

## Central Rule
The question is never which AI does what. The question is what files must exist before any AI is allowed to act.

## Three Modes

### Research Mode
The AI investigates, compares, summarizes, and identifies unknowns.

Allowed:
- Summarize sources
- Compare options
- Identify risks
- Produce research notes
- List open questions

Forbidden:
- Writing source code
- Making final project decisions
- Mutating implementation files

### Design Mode
The AI writes Markdown project memory.

Allowed:
- Create and update Project Brain files
- Write release plans
- Write feature briefs
- Write sprint packs
- Review dry runs
- Review implementation logs
- Write retrospectives
- Write handoff summaries

Forbidden:
- Writing source code
- Mutating implementation files
- Adding dependencies directly

### Develop Mode
The AI writes code and implementation files.

Allowed:
- Produce dry_run.md
- Modify approved implementation files after permission
- Create tests
- Run verification commands
- Update implementation_log.md
- Produce handoff_summary.md

Forbidden:
- Skipping dry run
- Modifying unapproved files
- Inventing business rules
- Adding dependencies without a decision record
- Skipping verification output

## Develop Mode Permission Levels
- Level 0: Dry run only. No implementation.
- Level 1: Approved sprint scope.
- Level 2: Approved expansion.
- Level 3: Supervised refactor.
- Level 4: Migration / high-risk change.

## Session Checkpoint Rule
Before ending a session, switching models, or approaching context limits, update STATE.md and relevant logs, then produce a handoff summary.
```

## 16.2 STATE.md

```md
# STATE.md

## Current Goal
[What are we trying to accomplish?]

## Active Scale
[Project / Release / Feature / Sprint / Patch]

## Current Mode
[Research / Design / Develop / Human Review]

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
[Anything the next AI or human must know]
```

## 16.3 DOMAIN.md

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

## 16.4 DECISIONS.md

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

## 16.5 COMMANDS.md

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

## 16.6 Feature Brief

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

## 16.7 Release Plan

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

## 16.8 Sprint requirements.md

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

## 16.9 Sprint blueprint.md

```md
# Sprint [NUMBER] Blueprint

## Design Mode Author

## Summary

## Files to Create

## Files to Modify

## Implementation Steps

## Assumptions

## Dependencies

## Risks

## Rollback Considerations
```

## 16.10 Sprint acceptance.md

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

## 16.11 Sprint dry_run.md

```md
# Sprint [NUMBER] Dry Run

## Develop Tool

## Permission Level
Level 0

## Files I Intend to Create

## Files I Intend to Modify

## Files I Intend to Move or Delete

## Commands I Intend to Run

## Dependencies Requested

## Risks or Ambiguities

## Assumptions

**STOPPED. Awaiting Design Mode review and human permission.**
```

## 16.12 implementation_log.md

```md
# Sprint [NUMBER] Implementation Log

## Develop Tool

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

## 16.13 human_review.md

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

## 16.14 retrospective.md

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

---

# 17. Prompt Catalog

In a full repo, each prompt should also exist as its own Markdown file under:

```txt
prompts/research/
prompts/design/
prompts/develop/
```

## 17.1 Research Mode Prompt

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
7. Recommended next step for Design Mode
```

## 17.2 Design Mode — Project Kickoff Prompt

```txt
You are operating in Design Mode for [PROJECT_NAME].

Use the provided notes, research, and constraints.

Do not write source code.

Generate:
1. DOMAIN.md
2. STATE.md
3. DECISIONS.md starter entries
4. QUESTIONS.md
5. RISKS.md
6. COMMANDS.md draft
7. STYLE_GUIDE.md draft
8. SECURITY.md draft
9. docs/architecture.md draft

Make all assumptions explicit.
```

## 17.3 Design Mode — Sprint Pack Prompt

```txt
You are operating in Design Mode.

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

## 17.4 Develop Mode — Dry Run Prompt

```txt
You are operating in Develop Mode.

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

## 17.5 Design Mode — Dry Run Review Prompt

```txt
You are operating in Design Mode.

Review:
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
- Recommended Develop Mode permission level
```

## 17.6 Develop Mode — Authorization Prompt

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

## 17.7 Design Mode — Implementation Review Prompt

```txt
You are operating in Design Mode.

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

## 17.8 Handoff Checkpoint Prompt

```txt
You are approaching the end of this session or a model handoff.

Update or produce:
1. STATE.md update
2. implementation_log.md update if in Develop Mode
3. QUESTIONS.md additions
4. RISKS.md additions
5. backlog additions
6. Handoff Summary

The Handoff Summary must include:
- Current goal
- Current mode
- Active scale
- Active release / feature / sprint
- Completed work
- Files changed
- Commands run
- Current problems
- Unfinished work
- Next recommended action
- Warnings
```

## 17.9 Resumption Prompt

```txt
You are operating in Design Mode for resumption.

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
8. Files to load before Develop Mode
```

## 17.10 Release Planning Prompt

```txt
You are operating in Design Mode.

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

## 17.11 Feature Cycle Prompt

```txt
You are operating in Design Mode.

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

# 18. Domain Adaptations

ADDF is domain-agnostic. The structure stays similar, but the files change content based on the domain.

## 18.1 Web Applications

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

## 18.2 Game Development

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

For game projects, `DOMAIN.md` functions like a technical game design document.

## 18.3 Desktop Applications

Common entities:

- Windows.
- Menus.
- Local files.
- System permissions.
- User settings.
- Background services.

## 18.4 Data / Automation Projects

Common entities:

- Input files.
- Output files.
- Data rows.
- Transformations.
- Validation rules.
- Error records.
- Schedules.

## 18.5 Documentation and Framework Projects

Common entities:

- Pages.
- Sections.
- Templates.
- Prompts.
- Examples.
- Downloads.
- Versions.
- Release packages.

---

# 19. Example: Mini Task Tracker

## 19.1 Project Summary

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

## 19.2 Work Scale

```txt
Project: Mini Task Tracker
Release: v0.1 Local MVP
Feature: Core task list
Sprint: Sprint 001 — Add, display, complete, and persist tasks
```

## 19.3 Lifecycle Application

### Research

Research browser localStorage behavior and basic task app patterns.

### Design & Feasibility

Choose localStorage because the app is single-user and local-only.

### Validation Gate

Confirm:

- No accounts.
- No backend.
- No sync.
- localStorage is acceptable.

### Architecture

Design Mode creates:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
docs/architecture.md
```

### Sprint Planning

Design Mode generates:

```txt
requirements.md
blueprint.md
acceptance.md
```

### Build & Test

Develop Mode creates:

```txt
TaskForm
TaskList
storage helper
unit tests
implementation_log.md
```

### Review & Reflection

Design Mode reviews implementation logs, updates state, and writes retrospective notes.

### Deploy / Resume

The project can be deployed as a static app or resumed later through `STATE.md`.

---

# 20. Example: Building the ADDF Public Website and Starter Kit

## 20.1 Project Summary

The ADDF public project includes:

- Website.
- Documentation.
- Starter kit.
- Prompt catalog.
- Example project.
- Download packages.
- Possible CLI init tool.
- Possible web onboarding app.

## 20.2 Work Scale

```txt
Project: ADDF Public Framework Repository
Release: v0.1 Public Proof
Feature: Starter Kit
Sprint: Sprint 001 — Repo structure and starter kit normalization
```

## 20.3 Recommended Early Release Plan

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

## 20.4 Sprint 001 for ADDF Repo

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

# 21. Quick Reference Checklists

## 21.1 Before the First AI Session

- [ ] `SECURITY.md` exists.
- [ ] Never-share items are defined.
- [ ] Project goal is written.
- [ ] Work scale is identified.
- [ ] If unknowns exist, use Research Mode first.
- [ ] If ready to write project files, use Design Mode.

## 21.2 Before Design Mode

- [ ] Research notes are available if needed.
- [ ] `DOMAIN.md` draft exists or raw notes are available.
- [ ] `STATE.md` is current if the project already exists.
- [ ] `QUESTIONS.md` lists unknowns.
- [ ] `RISKS.md` lists known risks.

## 21.3 Before Develop Mode

- [ ] Sprint Pack exists.
- [ ] `requirements.md` is clear.
- [ ] `blueprint.md` lists files.
- [ ] `acceptance.md` is checkable.
- [ ] Branch is created.
- [ ] Permission Level 0 is declared.
- [ ] Develop Mode is instructed to dry run and stop.

## 21.4 Before Authorizing Development

- [ ] `dry_run.md` matches `blueprint.md`.
- [ ] Design Mode review passed.
- [ ] Dependencies are approved.
- [ ] Risks are acceptable.
- [ ] Rollback exists if needed.
- [ ] Permission level is explicit.

## 21.5 Before Committing

- [ ] Implementation log is complete.
- [ ] Test output is pasted.
- [ ] Human review passed.
- [ ] Decisions updated.
- [ ] Backlog updated.
- [ ] State updated.
- [ ] Retrospective completed.
- [ ] Handoff notes exist if pausing.

## 21.6 Before Starting V2

- [ ] V1 release retrospective exists.
- [ ] Backlog is triaged.
- [ ] User feedback is gathered.
- [ ] Risks are reviewed.
- [ ] Decisions are reviewed.
- [ ] V2 goals are defined.
- [ ] V2 release plan is created.

---

# 22. When Things Go Wrong

## 22.1 Develop Mode Touched Unapproved Files

Stop immediately.

Actions:

1. Do not continue implementation.
2. Record the issue in `implementation_log.md`.
3. Compare changes against `dry_run.md`.
4. Revert unapproved changes if needed.
5. Update `RISKS.md`.
6. Add a constraint to `AGENTS.md`.

## 22.2 The AI Invented Business Logic

Actions:

1. Identify the invented logic.
2. Check whether it exists in `DOMAIN.md`.
3. If not, remove it or mark it for human review.
4. Update `DOMAIN.md` if the logic is actually desired.
5. Add a retrospective note.
6. Add a Develop Mode constraint.

## 22.3 The Project Is Confused After Many Sprints

Use Design Mode to run a consistency audit.

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
Identify drift between project files and implemented work.
List contradictions.
Recommend updates to restore consistency.
Do not write source code.
```

## 22.4 The AI Runs Out of Tokens

Use the Session Checkpoint Protocol.

Require the AI to produce:

```txt
implementation_log.md update if in Develop Mode
STATE.md update
handoff_summary.md
```

Then open a new session and run the Resumption Prompt.

## 22.5 V1 Is Done and V2 Feels Unclear

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

Use Design Mode to generate a V2 release plan.

## 22.6 The Framework Feels Too Heavy

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

# 23. Glossary

## Acceptance Criteria

The checklist that defines whether work is complete.

## ADDF

Autonomous Duck Deployment Framework.

## Context Engineering

The practice of placing the right information in the right files and loading only the context needed for the current session.

## Design Mode

The AI mode that writes Markdown project memory, including plans, decisions, sprint packs, reviews, and handoff notes.

## Develop Mode

The AI mode that writes code or modifies implementation files after dry run approval.

## Dry Run

A read-only Develop Mode report describing intended file changes before implementation.

## Feature

A capability added to a project.

## Feature Cycle

The process for adding a capability to an existing project without restarting the whole lifecycle.

## Handoff Summary

A written summary that allows another AI or human to resume work.

## Local File Sovereignty

The principle that project memory lives in local files, not in chat history.

## Patch

A small, low-risk change that does not require a full sprint.

## Project Brain

The collection of Markdown files that preserve project state, decisions, constraints, and workflow.

## Release

A version of a project, such as V1, V2, or v0.3.

## Release Cycle

The process for planning and delivering a project version.

## Research Mode

The AI mode that investigates, compares, summarizes, and identifies unknowns.

## Resumption

The process of restarting work from project files after a break or handoff.

## Scale Model

The ADDF model for classifying work as Project, Release, Feature, Sprint, or Patch.

## Sprint

A bounded AI implementation packet. It is inspired by Agile language but is not necessarily a Scrum sprint.

## Sprint Pack

The set of `requirements.md`, `blueprint.md`, and `acceptance.md`.

## Validation Gate

The checkpoint that determines whether research and design work are ready for architecture or sprint planning.

---

# Closing Principle

ADDF is not a rigid process. It is a scalable structure.

Use the full lifecycle when the work is uncertain, foundational, or high risk.

Use release cycles to move from V1 to V2.

Use feature cycles to add capabilities.

Use sprint loops to implement bounded work.

Use quick patches for tiny fixes.

Use Research Mode to learn.

Use Design Mode to write the project memory.

Use Develop Mode to change the actual project.

Keep the project memory in files.

Let the AI help, but only from the context you deliberately provide.

> **Files are permanent. Chats are disposable.**
