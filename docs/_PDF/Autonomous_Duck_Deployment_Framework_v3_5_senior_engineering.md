# Autonomous Duck Deployment Framework

> **A file-first delivery framework for coordinating LLM-assisted research, design, implementation, review, handoff, and long-term project evolution.**

**Framework Version:** 3.5 Draft  
**Short Name:** ADDF  
**Primary Principle:** Files are permanent. Chats are disposable.  
**Core Methodology:** Context Engineering through Local File Sovereignty  
**Operating Modes:** Research Mode, Design Mode, Develop Mode  
**Work Scale:** Project → Release → Feature → Sprint → Patch  
**Lifecycle:** Research → Design & Feasibility → Validation → Architecture → Sprint Planning → Build & Test → Review & Reflection → Deploy / Maintain / Resume  
**Intended Audience:** Senior engineers, technical leads, AI-assisted development practitioners, tool builders, and teams adopting LLM-driven workflows.

---

## Contents

- [1. Purpose](#1-purpose)
- [2. Problem Statement](#2-problem-statement)
  - [2.1 Chat-Thread Project Memory Does Not Scale](#21-chat-thread-project-memory-does-not-scale)
  - [2.2 LLMs Optimize Toward Plausibility Without Explicit Constraints](#22-llms-optimize-toward-plausibility-without-explicit-constraints)
  - [2.3 Context Size Is Not Context Quality](#23-context-size-is-not-context-quality)
- [3. Framework Summary](#3-framework-summary)
- [4. Core Principles](#4-core-principles)
  - [4.1 Local File Sovereignty](#41-local-file-sovereignty)
  - [4.2 Explicit Work Scale](#42-explicit-work-scale)
  - [4.3 Mode-Constrained LLM Sessions](#43-mode-constrained-llm-sessions)
  - [4.4 Dry Run Before Mutation](#44-dry-run-before-mutation)
  - [4.5 Reviewable Project Memory](#45-reviewable-project-memory)
  - [4.6 Handoff by File, Not by Chat](#46-handoff-by-file-not-by-chat)
- [5. The Three Operating Modes](#5-the-three-operating-modes)
  - [5.1 Research Mode](#51-research-mode)
  - [5.2 Design Mode](#52-design-mode)
  - [5.3 Develop Mode](#53-develop-mode)
  - [5.4 Mode Boundaries](#54-mode-boundaries)
- [6. Work Scale Model](#6-work-scale-model)
  - [6.1 Project](#61-project)
  - [6.2 Release](#62-release)
  - [6.3 Feature](#63-feature)
  - [6.4 Sprint](#64-sprint)
  - [6.5 Patch](#65-patch)
  - [6.6 Scale-to-Process Mapping](#66-scale-to-process-mapping)
- [7. The 8-Step ADDF Lifecycle](#7-the-8-step-addf-lifecycle)
  - [7.1 Research](#71-research)
  - [7.2 Design & Feasibility](#72-design--feasibility)
  - [7.3 Validation Gate](#73-validation-gate)
  - [7.4 Architecture](#74-architecture)
  - [7.5 Sprint Planning](#75-sprint-planning)
  - [7.6 Build & Test](#76-build--test)
  - [7.7 Review & Reflection](#77-review--reflection)
  - [7.8 Deploy, Maintain, or Resume](#78-deploy-maintain-or-resume)
- [8. How Scale, Lifecycle, and Modes Interlock](#8-how-scale-lifecycle-and-modes-interlock)
- [9. Project Brain](#9-project-brain)
- [10. Release Cycles](#10-release-cycles)
- [11. Feature Cycles](#11-feature-cycles)
- [12. Sprint Loop](#12-sprint-loop)
- [13. Develop Mode Permission Levels](#13-develop-mode-permission-levels)
- [14. Handoff, Resumption, and Model Switching](#14-handoff-resumption-and-model-switching)
- [15. Relationship to Agile and Scrum](#15-relationship-to-agile-and-scrum)
- [16. Repository Structure](#16-repository-structure)
- [17. Initial Setup](#17-initial-setup)
- [18. File Templates](#18-file-templates)
- [19. Prompt Catalog](#19-prompt-catalog)
- [20. Domain Adaptations](#20-domain-adaptations)
- [21. Worked Example: Mini Task Tracker](#21-worked-example-mini-task-tracker)
- [22. Worked Example: ADDF Public Repository](#22-worked-example-addf-public-repository)
- [23. Operational Checklists](#23-operational-checklists)
- [24. Failure Handling](#24-failure-handling)
- [25. Glossary](#25-glossary)

---

# 1. Purpose

The Autonomous Duck Deployment Framework (ADDF) is a structured operating model for LLM-assisted software delivery.

Its purpose is to make AI-assisted engineering work:

- explicit,
- reviewable,
- resumable,
- model-agnostic,
- auditable,
- and resistant to context drift.

ADDF assumes that LLMs are useful execution and reasoning engines, but poor long-term custodians of project memory. The framework therefore moves durable memory out of chat threads and into local Markdown files.

The framework does not prescribe a specific LLM, editor, CLI, IDE, language, framework, or deployment platform. It prescribes a coordination model: how project state is represented, how LLM sessions are constrained, how work is scoped, how implementation is approved, and how handoff occurs when tools or models change.

---

# 2. Problem Statement

## 2.1 Chat-Thread Project Memory Does Not Scale

Unstructured AI-assisted development often treats a chat thread as the project memory. This works briefly, then degrades.

A long thread accumulates:

- superseded requirements,
- abandoned implementation paths,
- stale code blocks,
- tool-specific assumptions,
- partial bug fixes,
- context from unrelated work,
- and undocumented decisions.

The model may continue to use that stale context even when it no longer represents the current system. The developer then has to restate constraints, correct regressions, and manually reconstruct intent.

ADDF replaces chat-thread memory with file-backed project memory.

## 2.2 LLMs Optimize Toward Plausibility Without Explicit Constraints

When required behavior is not written down, an LLM will often infer it. That inference may be plausible, but still incorrect.

Common failure modes include:

- invented schema fields,
- invented API routes,
- mismatched permission assumptions,
- unnecessary dependency additions,
- hidden refactors,
- unrequested feature expansion,
- inconsistent naming,
- and business logic that was never approved.

ADDF addresses this by requiring explicit domain files, sprint requirements, blueprints, acceptance criteria, dry runs, and implementation logs.

## 2.3 Context Size Is Not Context Quality

Larger context windows reduce some friction, but they do not eliminate the need for clean context.

A large context window filled with stale or contradictory information can make the model less reliable. ADDF prioritizes context selection over context volume.

A session should load the files required for its current mode and scale of work. It should not ingest the entire repository or prior conversation history unless that is explicitly necessary.

---

# 3. Framework Summary

ADDF separates four concerns that are often conflated in AI-assisted workflows:

```txt
1. Work scale — How large is the change?
2. Lifecycle stage — Where is the work in the delivery process?
3. Operating mode — What is the AI allowed to do?
4. Project memory — Which files define the current truth?
```

The scale model is:

```txt
Project → Release → Feature → Sprint → Patch
```

The lifecycle is:

```txt
Research
→ Design & Feasibility
→ Validation
→ Architecture
→ Sprint Planning
→ Build & Test
→ Review & Reflection
→ Deploy / Maintain / Resume
```

The operating modes are:

```txt
Research Mode
Design Mode
Develop Mode
```

The core memory layer is the Project Brain:

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

The framework is intentionally recursive. The full lifecycle can be applied to a complete project, a major release, a high-risk feature, or a major pivot. Smaller work uses a smaller subset of the lifecycle.

---

# 4. Core Principles

## 4.1 Local File Sovereignty

The authoritative state of the project lives in local files, not in a chat transcript.

The LLM may assist with research, planning, implementation, review, and handoff, but it is not the canonical memory store.

The file system is the durable control plane.

## 4.2 Explicit Work Scale

Every unit of work should be classified before execution.

The available scales are:

```txt
Project
Release
Feature
Sprint
Patch
```

Scale determines how much process is appropriate. A new project and a typo fix should not have the same workflow.

## 4.3 Mode-Constrained LLM Sessions

Each AI session must operate in one of three modes:

```txt
Research Mode
Design Mode
Develop Mode
```

Modes define write permissions and expected outputs.

A session that is researching should not mutate code. A session that is designing should not write implementation. A session that is developing should not invent product rules.

## 4.4 Dry Run Before Mutation

Develop Mode must begin with a dry run.

The dry run lists intended file changes, commands, dependencies, risks, and assumptions. The session stops after the dry run until human approval is granted.

This creates an explicit review boundary before implementation.

## 4.5 Reviewable Project Memory

Significant work must produce artifacts that can be reviewed independently of the AI session.

Examples:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
DECISIONS.md
STATE.md
```

Reviewable memory is what makes the process auditable and resumable.

## 4.6 Handoff by File, Not by Chat

A model handoff should not require the previous conversation.

If Codex runs out of context and Claude must continue, Claude should resume from:

```txt
STATE.md
DOMAIN.md
DECISIONS.md
current sprint files
implementation_log.md
handoff_summary.md
QUESTIONS.md
RISKS.md
```

The handoff object is the file set, not the prior chat.

---

# 5. The Three Operating Modes

ADDF defines three operating modes.

```txt
Research Mode
Design Mode
Develop Mode
```

The modes answer:

> What is the AI allowed to do in this session?

## 5.1 Research Mode

Research Mode investigates and synthesizes information. It is used before committing to a design, architecture, release plan, or implementation approach.

Research Mode is appropriate when the team needs to:

- understand a domain,
- compare tools,
- summarize documentation,
- inspect prior art,
- evaluate constraints,
- identify risks,
- list unknowns,
- or produce research notes for later planning.

Research Mode may produce:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
research_summary.md
```

Research Mode must not:

- write source code,
- mutate implementation files,
- make final architecture decisions,
- add dependencies,
- or convert uncertain findings into binding project rules without Design Mode review.

Research Mode rule:

> Research Mode gathers evidence. It does not decide or build.

## 5.2 Design Mode

Design Mode writes the project memory.

It converts research, intent, requirements, feedback, implementation logs, and decisions into Markdown artifacts.

Design Mode is appropriate for:

- feasibility analysis,
- MVP definition,
- validation gates,
- architecture planning,
- release planning,
- feature planning,
- sprint pack generation,
- dry run review,
- implementation review,
- retrospective generation,
- resumption summaries,
- handoff notes,
- documentation updates,
- and decision logging.

Design Mode may create or update:

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

Design Mode must not:

- write source code,
- mutate implementation files,
- add dependencies directly,
- run uncontrolled repository changes,
- or confuse a plan with an implementation.

Design Mode rule:

> Design Mode writes Markdown project memory. It does not write implementation.

## 5.3 Develop Mode

Develop Mode changes the actual project.

It is the only mode allowed to write code or modify implementation assets.

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
approved assets
```

Develop Mode may also update implementation-related Markdown:

```txt
dry_run.md
implementation_log.md
handoff_summary.md
```

Develop Mode must:

- start at Permission Level 0,
- produce a dry run,
- stop after the dry run,
- wait for explicit approval,
- modify only approved files,
- log every change,
- run verification commands,
- paste raw output into `implementation_log.md`,
- stop when ambiguity appears,
- and checkpoint before context limits or model handoff.

Develop Mode must not:

- invent business rules,
- rewrite planning files unless explicitly authorized,
- add dependencies without a recorded decision,
- touch unrelated files,
- skip dry run,
- skip verification,
- or continue after failures without logging them.

Develop Mode rule:

> Develop Mode changes implementation files only after dry run approval.

## 5.4 Mode Boundaries

The three modes define write boundaries.

| Mode | Primary Action | Writes | Must Not Write |
|---|---|---|---|
| Research | Investigate | Research notes, summaries, open questions | Code, final decisions |
| Design | Specify | Markdown project memory | Source code, implementation files |
| Develop | Implement | Approved code, tests, logs | Unapproved files, invented rules |

A single lifecycle step may use more than one mode, but each session should have one explicit mode.

---

# 6. Work Scale Model

The Work Scale Model answers:

> How large is this unit of work?

Scale determines process depth.

## 6.1 Project

A Project is the full product or initiative.

Examples:

```txt
ADDF public website and starter kit ecosystem
Mini Task Tracker
A Unity training simulation
A local politics education site
A data ingestion pipeline
```

Project-level work generally requires the full lifecycle.

## 6.2 Release

A Release is a version of a project.

Examples:

```txt
v0.1 Public Proof
v0.2 Website MVP
v0.3 CLI Init Tool
v1.0 Stable Release
v2.0 Major Update
```

A release groups features into a bounded delivery target.

## 6.3 Feature

A Feature is a user-visible or system-visible capability.

Examples:

```txt
Starter kit download
Prompt catalog page
CLI init command
Web onboarding app
Search
CSV import
Enemy AI behavior
```

A feature may require research, design, validation, and one or more sprints.

## 6.4 Sprint

A Sprint is a bounded implementation packet.

In ADDF, a sprint is not defined by duration. It is defined by scope and artifacts.

A sprint typically contains:

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

## 6.5 Patch

A Patch is a small, low-risk change.

Examples:

```txt
Fix a typo
Update a broken link
Rename one heading
Adjust one CSS token
Correct one command in documentation
```

A patch does not require the full sprint loop unless it touches logic, dependencies, architecture, data, or multiple files.

## 6.6 Scale-to-Process Mapping

| Work Scale | Process Depth | Typical Modes |
|---|---|---|
| Project | Full lifecycle | Research, Design, Develop |
| Release | Full or partial lifecycle | Research, Design, Develop |
| Feature | Feature cycle | Research if needed, Design, Develop |
| Sprint | Sprint loop | Design, Develop |
| Patch | Minimal path | Human-only or Develop, Design if state changes |

---

# 7. The 8-Step ADDF Lifecycle

The lifecycle describes the delivery path.

It is scalable. It can be applied deeply to a new project or lightly to a feature.

## 7.1 Research

**Primary Mode:** Research Mode  
**Purpose:** Understand the problem space before committing to a direction.

Inputs may include:

```txt
raw notes
business context
user needs
external documentation
technical constraints
unknowns
```

Outputs may include:

```txt
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
```

Exit criteria:

- meaningful unknowns are documented,
- relevant sources are summarized,
- risks are visible,
- and the work is ready for design.

## 7.2 Design & Feasibility

**Primary Mode:** Design Mode  
**Purpose:** Convert research into possible approaches and evaluate feasibility.

Outputs may include:

```txt
design_options.md
feasibility.md
mvp_scope.md
risk_matrix.md
prototype_plan.md
```

Exit criteria:

- at least one viable approach is documented,
- MVP boundaries are clear,
- major tradeoffs are recorded,
- and high-risk assumptions are identified.

## 7.3 Validation Gate

**Primary Mode:** Design Mode + Human Review  
**Purpose:** Decide whether the work is defined enough to proceed.

The validation gate asks:

- Is the goal clear?
- Is the target user clear?
- Is scope bounded?
- Are security boundaries known?
- Are high-risk assumptions visible?
- Are open questions acceptable or resolved?
- Is the preferred approach explicit?

Outputs may include:

```txt
validation.md
approved_approach.md
updated QUESTIONS.md
updated RISKS.md
```

Exit criteria:

- human approval exists,
- blockers are resolved or explicitly deferred,
- and the work is ready for architecture or sprint planning.

## 7.4 Architecture

**Primary Mode:** Design Mode  
**Purpose:** Convert validated intent into durable project memory.

Outputs may include:

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

Exit criteria:

- domain rules are explicit,
- command paths are documented,
- security boundaries are known,
- major decisions are recorded,
- and current state is accurate.

## 7.5 Sprint Planning

**Primary Mode:** Design Mode  
**Purpose:** Convert architecture or feature intent into an implementation-ready sprint pack.

Outputs:

```txt
requirements.md
blueprint.md
acceptance.md
```

Exit criteria:

- requirements are specific,
- blueprint lists files and implementation steps,
- assumptions are explicit,
- acceptance criteria are checkable,
- and the human has reviewed scope.

## 7.6 Build & Test

**Primary Mode:** Develop Mode  
**Purpose:** Implement approved work under controlled permissions.

Develop Mode first produces:

```txt
dry_run.md
```

Then stops.

After approval, Develop Mode implements approved changes and produces:

```txt
source files
tests
implementation_log.md
test output
handoff notes if needed
```

Exit criteria:

- implementation touched only approved files,
- verification ran,
- raw output is logged,
- failures are documented,
- and no unapproved dependencies were added.

## 7.7 Review & Reflection

**Primary Mode:** Design Mode + Human Review  
**Purpose:** Verify output, capture lessons, and update project memory.

Outputs may include:

```txt
human_review.md
retrospective.md
updated STATE.md
updated DECISIONS.md
updated planning/backlog.md
updated AGENTS.md when constraints change
```

Exit criteria:

- work is approved or rejected,
- known issues are captured,
- decisions are recorded,
- state reflects reality,
- and the next action is clear.

## 7.8 Deploy, Maintain, or Resume

**Primary Mode:** Design Mode and/or Develop Mode  
**Purpose:** Decide the next operational state after review.

The project may:

- deploy,
- start another sprint,
- start a new feature cycle,
- start a new release cycle,
- enter maintenance,
- pause,
- resume later,
- or pivot.

Outputs may include:

```txt
release_notes.md
rollback_log.md
handoff_summary.md
updated COMMANDS.md
updated RISKS.md
updated STATE.md
```

Exit criteria:

- deployment or distribution steps are documented,
- rollback exists when needed,
- state is current,
- and handoff notes exist if pausing.

---

# 8. How Scale, Lifecycle, and Modes Interlock

ADDF separates three decisions.

## 8.1 Scale

```txt
How large is this work?
```

Possible answers:

```txt
Project / Release / Feature / Sprint / Patch
```

## 8.2 Lifecycle Stage

```txt
Where is the work in the delivery process?
```

Possible answers:

```txt
Research / Design & Feasibility / Validation / Architecture / Sprint Planning / Build & Test / Review & Reflection / Deploy-Maintain-Resume
```

## 8.3 Mode

```txt
What is the AI allowed to do?
```

Possible answers:

```txt
Research / Design / Develop
```

## 8.4 Mapping

| Lifecycle Step | Primary Mode |
|---|---|
| Research | Research |
| Design & Feasibility | Design |
| Validation Gate | Design + Human |
| Architecture | Design |
| Sprint Planning | Design |
| Build & Test | Develop |
| Review & Reflection | Design + Human |
| Deploy, Maintain, or Resume | Design and/or Develop |

## 8.5 Examples

### New project

```txt
Scale: Project
Lifecycle: Full 8 steps
Modes: Research → Design → Develop → Design review
```

### New feature

```txt
Scale: Feature
Lifecycle: Feature-sized path
Modes: Research if needed → Design → Develop → Design review
```

### Sprint

```txt
Scale: Sprint
Lifecycle: Mostly Sprint Planning → Build & Test → Review
Modes: Design → Develop → Design
```

### Patch

```txt
Scale: Patch
Lifecycle: Minimal
Modes: Human-only or Develop, with Design only if state/docs need updating
```

---

# 9. Project Brain

The Project Brain is the file-backed memory layer.

## 9.1 Core Files

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

## 9.2 Sprint Files

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

## 9.3 Release and Feature Files

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

## 9.4 Properties of Good Project Memory

Good project memory is:

- current,
- explicit,
- scoped,
- reviewable,
- searchable,
- versioned,
- and safe to load into an LLM session.

---

# 10. Release Cycles

ADDF supports versioned delivery.

A completed V1 becomes the baseline for V2. The Project Brain persists across versions.

## 10.1 Release Plan

A release plan defines:

- release goal,
- in-scope features,
- out-of-scope items,
- required research,
- risks,
- sprint sequence,
- release criteria,
- release notes,
- and retrospective criteria.

## 10.2 Release Folder Structure

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

## 10.3 Starting a New Version

To begin V2 after V1, load:

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

## 10.4 Release Completion Criteria

A release is complete when:

- in-scope features are complete or intentionally deferred,
- release criteria are met,
- docs are updated,
- changelog is updated,
- release notes exist,
- known issues are in the backlog,
- deployment or distribution is complete,
- and release retrospective exists.

---

# 11. Feature Cycles

A feature cycle adds a capability to an existing project.

It does not restart the full project lifecycle unless the feature is foundational, high-risk, or changes project direction.

## 11.1 Feature Flow

```txt
1. Add idea to backlog
2. Write feature brief
3. Research if needed
4. Design feasibility if needed
5. Validate scope
6. Generate sprint pack
7. Develop with dry run
8. Review and update project memory
```

## 11.2 Feature Folder Structure

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

## 11.3 Feature Brief Template

```md
# Feature Brief: [Feature Name]

## Summary
[What capability is being added?]

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

---

# 12. Sprint Loop

The Sprint Loop is the controlled implementation workflow.

## 12.1 Overview

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

## 12.2 Pre-Flight Gate

Check:

- scale,
- blockers,
- risks,
- branch,
- relevant release or feature,
- and scope clarity.

## 12.3 Design Sprint Pack

Design Mode creates:

```txt
requirements.md
blueprint.md
acceptance.md
```

## 12.4 Human Blueprint Review

The human validates:

- desired outcome,
- domain alignment,
- file scope,
- assumptions,
- testability,
- and out-of-scope boundaries.

## 12.5 Develop Dry Run

Develop Mode starts at Level 0 and produces:

```txt
dry_run.md
```

The dry run lists intended changes, commands, dependencies, risks, and assumptions.

## 12.6 Design Review of Dry Run

Design Mode compares:

```txt
requirements.md
blueprint.md
acceptance.md
dry_run.md
```

It returns approval, required corrections, or revised permission level.

## 12.7 Dependency Approval Gate

Any new dependency requires a `DECISIONS.md` entry before implementation.

## 12.8 Authorize Development

The human authorizes Develop Mode explicitly.

```txt
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

## 12.9 Build & Test

Develop Mode implements approved work and logs:

```txt
implementation_log.md
test output
errors
handoff notes
```

## 12.10 Design Review of Output

Design Mode reviews implementation against plan, acceptance criteria, logs, and changed files.

## 12.11 Human Approval Gate

The human checks scope, verification, documentation, security, state, decisions, and handoff readiness.

## 12.12 Commit, Update, Reset

The human commits the work, updates Project Brain files, and closes or checkpoints the active AI session.

---

# 13. Develop Mode Permission Levels

Permission levels apply only to Develop Mode.

| Level | Name | Meaning |
|---|---|---|
| 0 | Dry Run Only | Read-only analysis of intended changes. No implementation. |
| 1 | Approved Sprint Scope | Modify only files approved in blueprint and dry run. |
| 2 | Approved Expansion | Add minor helper files surfaced in dry run and explicitly approved. |
| 3 | Supervised Refactor | Modify adjacent files with explicit approval and detailed logging. |
| 4 | Migration / High-Risk Change | Structural changes, migrations, or architecture-heavy work. Requires rollback plan. |

Most work starts at Level 0 and proceeds to Level 1.

Levels 2–4 require stronger justification and review.

---

# 14. Handoff, Resumption, and Model Switching

ADDF supports model handoff as a first-class workflow.

## 14.1 Session Checkpoint Protocol

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

## 14.2 Handoff Summary

```md
# Handoff Summary

## Current Goal
[Current objective]

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
[Completed items]

## Files Changed
- [File path]: [Change summary]

## Commands Run
- [Command]: [Result]

## Current Problems
[Errors, blockers, failed checks]

## Unfinished Work
[Remaining work]

## Next Recommended Action
[Next safest action]

## Warnings
[Risks, assumptions, caveats]
```

## 14.3 Incoming Model Protocol

The incoming model should load:

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

Then it should summarize current state and wait for explicit mode authorization before changing files.

---

# 15. Relationship to Agile and Scrum

ADDF is Agile-inspired but not Scrum.

It uses:

- backlog,
- sprint,
- acceptance criteria,
- review,
- retrospective,
- release,
- iteration.

It does not require:

- Scrum Master,
- Product Owner,
- daily standups,
- story points,
- velocity tracking,
- ceremony cadence,
- or two-week sprint duration.

## 15.1 Sprint Definition

In ADDF, a sprint is a bounded AI implementation packet, not a timeboxed team ceremony.

## 15.2 Mapping

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

# 16. Repository Structure

## 16.1 Standard ADDF Project

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
│   ├── features/
│   └── sprints/
├── prompts/
│   ├── research/
│   ├── design/
│   └── develop/
└── src/
```

## 16.2 Minimum Viable ADDF

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

## 16.3 Public ADDF Repository

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
├── starter-kit/
│   ├── blank/
│   └── example-filled/
├── prompts/
│   ├── research/
│   ├── design/
│   └── develop/
├── examples/
├── website/
├── assets/
├── brand/
├── tools/
└── planning/
```

---

# 17. Initial Setup

## 17.1 Create the Project

```bash
mkdir -p src docs research planning/sprints/sprint_001
touch AGENTS.md DOMAIN.md STATE.md DECISIONS.md COMMANDS.md STYLE_GUIDE.md SECURITY.md QUESTIONS.md RISKS.md GIT_STRATEGY.md PROMPT_CHANGELOG.md
touch planning/backlog.md
touch planning/sprints/sprint_001/requirements.md planning/sprints/sprint_001/blueprint.md planning/sprints/sprint_001/acceptance.md planning/sprints/sprint_001/dry_run.md planning/sprints/sprint_001/implementation_log.md planning/sprints/sprint_001/human_review.md planning/sprints/sprint_001/retrospective.md
```

## 17.2 Populate Files in Order

1. `SECURITY.md`
2. `AGENTS.md`
3. `DOMAIN.md`
4. `STATE.md`
5. `COMMANDS.md`
6. `DECISIONS.md`
7. `QUESTIONS.md`
8. `RISKS.md`

## 17.3 First Session

A new project should begin with:

```txt
Research Mode if needed
Design Mode for project memory
Design Mode for sprint planning
Develop Mode for dry run
Develop Mode for approved implementation
Design Mode for review and state update
```

---

# 18. File Templates

## 18.1 AGENTS.md

```md
# AGENTS.md

## Framework
This project uses the Autonomous Duck Deployment Framework.

## Central Rule
The question is never which AI does what. The question is what files must exist before any AI is allowed to act.

## Modes

### Research Mode
Allowed:
- Summarize sources
- Compare options
- Identify risks
- Produce research notes
- List open questions

Forbidden:
- Source code
- Final decisions
- Implementation changes

### Design Mode
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
- Source code
- Implementation file mutation
- Direct dependency addition

### Develop Mode
Allowed:
- Produce dry_run.md
- Modify approved files after permission
- Create tests
- Run verification commands
- Update implementation_log.md
- Produce handoff_summary.md

Forbidden:
- Skipping dry run
- Touching unapproved files
- Inventing business rules
- Adding dependencies without a decision record
- Skipping verification

## Develop Mode Permission Levels
- Level 0: Dry run only. No implementation.
- Level 1: Approved sprint scope.
- Level 2: Approved expansion.
- Level 3: Supervised refactor.
- Level 4: Migration / high-risk change.

## Session Checkpoint Rule
Before ending a session, switching models, or approaching context limits, update STATE.md and relevant logs, then produce a handoff summary.
```

## 18.2 STATE.md

```md
# STATE.md

## Current Goal
[Current objective]

## Active Scale
[Project / Release / Feature / Sprint / Patch]

## Current Mode
[Research / Design / Develop / Human Review]

## Active Release
[Version or "None"]

## Active Feature
[Feature or "None"]

## Active Sprint
[Sprint or "None"]

## Current Status
[Research / Planning / In Progress / Verification / Complete / Blocked / Paused]

## Known Blockers
[Blockers or "None"]

## Last Completed Step
[Last completed action]

## Next Intended Step
[Next action]

## Files Recently Changed
- [file]: [summary]

## Handoff Notes
[Important continuation context]
```

## 18.3 DOMAIN.md

```md
# DOMAIN.md

## Project Overview
[What this project does and why it exists.]

## Target Users
[Primary users]

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

## 18.4 DECISIONS.md

```md
# DECISIONS.md

Decisions are never deleted. They are superseded by later decisions.

## Decision 001: [Short Title]
**Date:** [YYYY-MM-DD]
**Status:** Accepted / Superseded / Proposed
**Type:** Architecture / Dependency / Data Model / Security / Process / Other

### Context
[Why this decision is needed]

### Decision
[Decision made]

### Tradeoffs
[Costs, limitations, risks]

### Alternatives Considered
[Options rejected or deferred]
```

## 18.5 Sprint Pack

```md
# requirements.md

## Sprint Goal

## Functional Requirements

## Technical Requirements

## In Scope

## Out of Scope

## Constraints

## Related Decisions

## Open Questions
```

```md
# blueprint.md

## Summary

## Files to Create

## Files to Modify

## Implementation Steps

## Assumptions

## Dependencies

## Risks

## Rollback Considerations
```

```md
# acceptance.md

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
- [ ] Verification complete
- [ ] implementation_log.md updated
- [ ] human_review.md passed
- [ ] STATE.md updated
```

---

# 19. Prompt Catalog

## 19.1 Research Mode Prompt

```txt
You are operating in Research Mode.

Research:
[topic]

Context:
[context]

Constraints:
[constraints]

Do not write code.
Do not make final project decisions.

Produce:
1. Summary
2. Findings
3. Options
4. Tradeoffs
5. Risks
6. Open questions
7. Recommended next step for Design Mode
```

## 19.2 Design Mode — Project Initialization Prompt

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

Make assumptions explicit.
```

## 19.3 Design Mode — Sprint Pack Prompt

```txt
You are operating in Design Mode.

Generate a Sprint Pack for:
[Sprint title]

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
Acceptance criteria must be checkable.
```

## 19.4 Develop Mode — Dry Run Prompt

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

## 19.5 Design Mode — Dry Run Review Prompt

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

## 19.6 Develop Mode — Authorization Prompt

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

## 19.7 Resumption Prompt

```txt
You are operating in Design Mode for resumption.

Loaded:
- AGENTS.md
- DOMAIN.md
- STATE.md
- DECISIONS.md
- QUESTIONS.md
- RISKS.md
- backlog
- current sprint or release files if present

Summarize:
1. Project purpose
2. Active scale
3. Current mode
4. Active release / feature / sprint
5. Last completed step
6. Known blockers
7. Next safest action
8. Files to load before Develop Mode
```

---

# 20. Domain Adaptations

ADDF is domain-agnostic. The structure remains stable; file contents adapt to the domain.

## 20.1 Web Applications

Typical entities:

- routes,
- pages,
- components,
- API endpoints,
- sessions,
- database tables,
- forms,
- permissions.

Typical commands:

```txt
npm run dev
npm run test
npm run build
npm run lint
```

## 20.2 Game Development

Typical entities:

- scenes,
- levels,
- game states,
- player states,
- input actions,
- assets,
- UI screens,
- save data.

For games, `DOMAIN.md` should function as a technical game design document.

## 20.3 Desktop Applications

Typical entities:

- windows,
- menus,
- local files,
- system permissions,
- user settings,
- native services.

## 20.4 Data / Automation

Typical entities:

- input files,
- output files,
- rows,
- transformations,
- validations,
- schedules,
- error records.

## 20.5 Documentation / Framework Projects

Typical entities:

- pages,
- sections,
- templates,
- prompts,
- examples,
- downloads,
- versions,
- release packages.

---

# 21. Worked Example: Mini Task Tracker

## 21.1 Work Scale

```txt
Project: Mini Task Tracker
Release: v0.1 Local MVP
Feature: Core task list
Sprint: Sprint 001 — Add, display, complete, and persist tasks
```

## 21.2 Lifecycle Use

Research Mode:

```txt
Investigate localStorage and simple task app persistence.
```

Design Mode:

```txt
Create DOMAIN.md, STATE.md, DECISIONS.md, requirements.md, blueprint.md, and acceptance.md.
```

Develop Mode:

```txt
Dry run, implement TaskForm, TaskList, storage helper, tests, and implementation_log.md.
```

Design Mode:

```txt
Review implementation output, update STATE.md, record retrospective.
```

---

# 22. Worked Example: ADDF Public Repository

## 22.1 Project Scope

The public ADDF repository includes:

- documentation,
- website,
- starter kit,
- prompt catalog,
- example project,
- download packages,
- optional CLI init tool,
- optional web onboarding app.

## 22.2 Release Plan

### v0.1 Public Proof

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

```txt
Static website
Homepage
Start Here page
Lifecycle page
Modes page
Downloads page
```

### v0.3 Init Tool Prototype

```txt
addf init
minimal/full setup
project-type presets
generated starter files
```

### v0.4 Web Onboarding App

```txt
Browser questionnaire
Generated file preview
Download starter ZIP
Copy prompt buttons
```

## 22.3 Sprint 001

Goal:

```txt
Normalize repository structure and starter kit so the repo becomes the official ADDF project home.
```

In scope:

- organize docs,
- create starter-kit folders,
- create prompt folders,
- create planning structure,
- create example placeholders,
- create README and START_HERE if missing.

Out of scope:

- website implementation,
- CLI implementation,
- backend,
- package publishing,
- final branding.

---

# 23. Operational Checklists

## 23.1 Before First AI Session

- [ ] `SECURITY.md` exists.
- [ ] Never-share items are defined.
- [ ] Work scale is identified.
- [ ] Project goal is written.
- [ ] Research Mode is used if unknowns exist.
- [ ] Design Mode is used before Develop Mode.

## 23.2 Before Develop Mode

- [ ] Sprint Pack exists.
- [ ] `requirements.md` is clear.
- [ ] `blueprint.md` lists files.
- [ ] `acceptance.md` is checkable.
- [ ] Branch is created.
- [ ] Permission Level 0 is declared.
- [ ] Develop Mode is instructed to dry run and stop.

## 23.3 Before Authorizing Development

- [ ] `dry_run.md` matches `blueprint.md`.
- [ ] Design Mode review passed.
- [ ] Dependencies are approved.
- [ ] Risks are acceptable.
- [ ] Rollback exists if needed.
- [ ] Permission level is explicit.

## 23.4 Before Commit

- [ ] Implementation log is complete.
- [ ] Verification output is pasted.
- [ ] Human review passed.
- [ ] Decisions updated.
- [ ] Backlog updated.
- [ ] State updated.
- [ ] Retrospective completed.
- [ ] Handoff notes exist if pausing.

---

# 24. Failure Handling

## 24.1 Develop Mode Touched Unapproved Files

Stop implementation.

Actions:

1. Record the issue in `implementation_log.md`.
2. Compare changes against `dry_run.md`.
3. Revert unapproved changes if needed.
4. Update `RISKS.md`.
5. Add a constraint to `AGENTS.md`.

## 24.2 AI Invented Business Logic

Actions:

1. Identify the invented logic.
2. Check `DOMAIN.md`.
3. Remove the logic or mark it for review.
4. Update `DOMAIN.md` only if the logic is approved.
5. Record the issue in `retrospective.md`.
6. Add a Develop Mode constraint.

## 24.3 Project State Is Confused

Use Design Mode for a consistency audit.

Load:

```txt
DOMAIN.md
STATE.md
DECISIONS.md
recent sprint folders
docs/architecture.md
```

Ask Design Mode to identify drift and recommend updates.

## 24.4 Model Runs Out of Context

Use Session Checkpoint Protocol.

Require:

```txt
STATE.md update
implementation_log.md update if applicable
handoff_summary.md
```

Open a new session and run the Resumption Prompt.

---

# 25. Glossary

## ADDF

Autonomous Duck Deployment Framework.

## Context Engineering

The practice of organizing project context into explicit, scoped, durable files.

## Design Mode

The AI operating mode that writes Markdown project memory.

## Develop Mode

The AI operating mode that writes code or implementation files after approval.

## Dry Run

A Develop Mode report describing intended changes before implementation.

## Feature

A capability added to an existing project.

## Handoff Summary

A written continuation record for another AI or human.

## Local File Sovereignty

The principle that project memory lives in local files, not model memory.

## Patch

A tiny low-risk change.

## Project Brain

The collection of Markdown files that define current project truth.

## Release

A versioned delivery target.

## Research Mode

The AI operating mode that investigates and synthesizes information.

## Sprint

A bounded AI implementation packet.

## Sprint Pack

`requirements.md`, `blueprint.md`, and `acceptance.md`.

## Validation Gate

A decision checkpoint before architecture, sprint planning, or implementation.

---

# Closing Principle

ADDF is a coordination framework, not a coding trick.

Use Research Mode to establish evidence.

Use Design Mode to make project memory explicit.

Use Develop Mode to modify implementation under reviewable constraints.

Choose the scale before choosing the process.

Run only as much lifecycle as the work requires.

Keep the source of truth in files.

Let the AI assist, but do not let the AI become the memory of the project.

> **Files are permanent. Chats are disposable.**
