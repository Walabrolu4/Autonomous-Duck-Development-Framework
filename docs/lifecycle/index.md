# The 8-Step ADDF Lifecycle

The lifecycle is scalable — apply every step to a new project, a single step to a bounded patch, and any slice in between to anything else.

## Table of contents

1. [Introduction](#introduction)
2. [Step 1 — Research](#research)
3. [Step 2 — Design & Feasibility](#design-feasibility)
4. [Step 3 — Validation Gate](#validation-gate)
5. [Step 4 — Architecture](#architecture)
6. [Step 5 — Sprint Planning](#sprint-planning)
7. [Step 6 — Build & Test](#build-test)
8. [Step 7 — Review & Reflection](#review-reflection)
9. [Step 8 — Deploy, Maintain, or Resume](#deploy-maintain-resume)
10. [Mode-to-lifecycle mapping](#mode-to-lifecycle-mapping)
11. [Scale examples](#scale-examples)

---

## Introduction

The lifecycle describes the delivery path. It is not a rigid sequence — it is a reference for choosing which stages apply to a given piece of work.

Apply it deeply to a new project or major release. Apply it lightly to a bounded feature. Skip irrelevant stages for low-risk patches.

The lifecycle does not run in isolation from scale and mode. See [How scale, lifecycle, and modes interlock](#mode-to-lifecycle-mapping) at the bottom of this page, and [Work Scale Model](../work-scale.md) for the full treatment.

![8-Step Lifecycle](_PDF/images/5_8-Step Lifecycle.png)

---

## Step 1 — Research {#research}

**Primary mode:** Research Mode

**Purpose:** Understand the problem space before committing to a direction.

Inputs may include raw notes, business context, user needs, external documentation, technical constraints, and unknowns.

Outputs may include:

```
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
```

Exit criteria: meaningful unknowns are documented, relevant sources are summarized, risks are visible, and the work is ready for design.

**Rule:** Do not design against unknowns you have not named.

---

## Step 2 — Design & Feasibility {#design-feasibility}

**Primary mode:** Design Mode

**Purpose:** Convert research into viable approaches and evaluate constraints.

Outputs may include:

```
design_options.md
feasibility.md
mvp_scope.md
risk_matrix.md
prototype_plan.md
```

Exit criteria: at least one viable approach is documented, MVP boundaries are clear, major tradeoffs are recorded, and high-risk assumptions are identified.

**Rule:** Feasibility work narrows options before architecture hardens them.

---

## Step 3 — Validation Gate {#validation-gate}

**Primary mode:** Design Mode + human review

**Purpose:** Decide whether the work is defined enough to proceed.

The validation gate asks seven questions:

1. Is the goal clear?
2. Is the target user clear?
3. Is scope bounded?
4. Are security boundaries known?
5. Are high-risk assumptions visible?
6. Are open questions acceptable or resolved?
7. Is the preferred approach explicit?

Outputs may include:

```
validation.md
approved_approach.md
updated QUESTIONS.md
updated RISKS.md
```

Exit criteria: human approval exists, blockers are resolved or explicitly deferred, and the work is ready for architecture or sprint planning.

**Rule:** No validation, no architecture.

---

## Step 4 — Architecture {#architecture}

**Primary mode:** Design Mode

**Purpose:** Convert validated intent into durable project memory.

Outputs may include:

```
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

Exit criteria: domain rules are explicit, command paths are documented, security boundaries are known, major decisions are recorded, and current state is accurate.

**Rule:** Architecture lives in files before Develop Mode starts.

---

## Step 5 — Sprint Planning {#sprint-planning}

**Primary mode:** Design Mode

**Purpose:** Convert architecture or feature intent into an implementation-ready Sprint Pack.

Outputs:

```
requirements.md
blueprint.md
acceptance.md
```

Exit criteria: requirements are specific, `blueprint.md` lists exact files and implementation steps, assumptions are explicit, acceptance criteria are checkable, and the human has reviewed scope.

**Rule:** The Sprint Pack is the contract for Develop Mode.

---

## Step 6 — Build & Test {#build-test}

**Primary mode:** Develop Mode

**Purpose:** Implement approved work under controlled permissions.

Develop Mode first produces `dry_run.md` and stops. After human approval, it implements approved changes and produces:

```
source files
tests
implementation_log.md
test output
handoff notes
```

Exit criteria: implementation touched only approved files, verification ran, raw output is logged, failures are documented, and no unapproved dependencies were added.

**Rule:** Develop Mode does not self-authorize.

---

## Step 7 — Review & Reflection {#review-reflection}

**Primary mode:** Design Mode + human review

**Purpose:** Verify output, capture lessons, and update project memory.

Outputs may include:

```
human_review.md
retrospective.md
updated STATE.md
updated DECISIONS.md
updated planning/backlog.md
updated AGENTS.md
```

Exit criteria: work is approved or rejected, known issues are captured, decisions are recorded, state reflects reality, and the next action is clear.

**Rule:** A sprint is not complete until the project brain is current.

---

## Step 8 — Deploy, Maintain, or Resume {#deploy-maintain-resume}

**Primary mode:** Design Mode and/or Develop Mode

**Purpose:** Decide the next operational state after review.

The project may take any of eight paths from here:

1. deploy,
2. start another sprint,
3. start a new feature cycle,
4. start a new release cycle,
5. enter maintenance,
6. pause,
7. resume later,
8. or pivot.

Outputs may include:

```
release_notes.md
rollback_log.md
handoff_summary.md
updated COMMANDS.md
updated RISKS.md
updated STATE.md
```

Exit criteria: deployment or distribution steps are documented, rollback exists when needed, state is current, and handoff notes exist if pausing.

**Rule:** A project can pause only after state is written down.

---

## Mode-to-lifecycle mapping

| Lifecycle step | Primary mode |
|---|---|
| Research | Research Mode |
| Design & Feasibility | Design Mode |
| Validation Gate | Design Mode + human |
| Architecture | Design Mode |
| Sprint Planning | Design Mode |
| Build & Test | Develop Mode |
| Review & Reflection | Design Mode + human |
| Deploy, Maintain, or Resume | Design Mode and/or Develop Mode |

![Scale, Lifecycle, Mode interlock](_PDF/images/4_Scale  Lifecycle  Mode interlock.png)

A lifecycle step may involve more than one mode. A session has one explicit mode.

---

## Scale examples

### New project

```
Scale:     Project
Lifecycle: Full 8 steps
Modes:     Research → Design → Develop → Design review
```

### New feature

```
Scale:     Feature
Lifecycle: Feature-sized path
Modes:     Research if needed → Design → Develop → Design review
```

### Sprint

```
Scale:     Sprint
Lifecycle: Sprint planning → Build & test → Review
Modes:     Design → Develop → Design
```

### Patch

```
Scale:     Patch
Lifecycle: Minimal
Modes:     Human-only or Develop, with Design only if state or docs change
```

**Rule:** Scale chooses the process depth. Lifecycle describes stage. Mode controls model permissions.

---

[← Wiki Home](../index.md) · ADDF v3.5
