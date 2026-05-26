# Core Concepts

ADDF works by separating four decisions that unstructured AI-assisted workflows collapse into one — scale, lifecycle stage, operating mode, and project memory.

## Table of contents

1. [The four separations](#the-four-separations)
2. [The six core principles](#the-six-core-principles)
3. [Why it works](#why-it-works)

---

## The four separations

ADDF separates four decisions before any model acts:

```
1. Work scale      — How large is the change?
2. Lifecycle stage — Where is the work in the delivery process?
3. Operating mode  — What is the model allowed to do?
4. Project memory  — Which files define the current truth?
```

These four questions are related but distinct. Collapsing them produces the failure modes that ADDF is designed to prevent: scope creep without approval, invented business logic, context decay, and sessions that cannot be resumed by a new model.

**Rule:** Choose the scale before choosing the process.

---

## The six core principles

### 4.1 Local File Sovereignty

The authoritative project state lives in local files. LLM sessions can read, summarize, modify, or produce those files according to mode constraints — but the model is not the system of record. The repository is.

Canonical project memory belongs in Markdown files that can be reviewed, diffed, committed, searched, and loaded into any capable LLM session.

**Rule:** The files are the project.

---

### 4.2 Explicit work scale

Every unit of work receives a scale before execution. The five scales are Project, Release, Feature, Sprint, and Patch.

Scale determines process depth. A Project requires research, design, validation, architecture, implementation, review, and release planning. A Patch may require one edit and one commit.

**Rule:** Do not run a project process for a patch. Do not run a patch process for a project.

---

### 4.3 Mode-constrained LLM sessions

Every AI session runs in one explicit mode. Research Mode investigates. Design Mode writes project memory. Develop Mode changes implementation.

Each mode has different write permissions. A session declared as Research Mode cannot write source code. A session declared as Develop Mode cannot invent business rules.

**Rule:** Declare the mode before the model acts.

---

### 4.4 Dry run before mutation

Develop Mode begins with a Dry Run. The model lists every file it intends to create or modify, every command it plans to run, every dependency it needs, and every assumption it is making. Then it stops.

Implementation begins only after the human reviews the Dry Run and gives explicit authorization. This one pause is how the framework catches scope creep, accidental refactors, and unapproved dependency additions — before they happen.

**Rule:** No dry run, no implementation.

---

### 4.5 Reviewable project memory

Significant work produces artifacts that survive the session. These include `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`, `implementation_log.md`, `human_review.md`, `retrospective.md`, `DECISIONS.md`, and `STATE.md`.

These artifacts let the human inspect scope, verify output, recover from failure, and hand work to another model without losing context.

**Rule:** If the work matters, it leaves a file trail.

---

### 4.6 Handoff by file, not by chat

Model handoff uses files, not prior conversation. If one model reaches a context limit and another takes over, the incoming model receives the project files, sprint files, implementation log, and handoff summary. The previous chat is not required.

**Rule:** A valid handoff survives without the old thread.

---

## Why it works

Unstructured AI-assisted development fails in three predictable ways. Long chat threads accumulate stale context — old code, abandoned decisions, superseded requirements — and the model treats all of it as relevant. Without a specification with real teeth, the model fills gaps with plausible but incorrect output: invented schema fields, unapproved dependencies, wrong permission assumptions. And conversation history is fragile: close the tab and context is gone.

The four separations address each failure directly. Explicit scale prevents the wrong process from running. Mode constraints prevent the model from acting outside its lane. Reviewable project memory prevents context decay and makes every decision auditable. File-based handoff makes the project resumable by any model at any time.

See [Work Scale Model](work-scale.md), [Lifecycle](lifecycle/index.md), [Operating Modes](modes/index.md), and [The Project Brain](project-brain.md) for the full detail on each separation.

**Rule:** Cleaner context beats more context.

---

[← Wiki Home](index.md) · ADDF v3.5
