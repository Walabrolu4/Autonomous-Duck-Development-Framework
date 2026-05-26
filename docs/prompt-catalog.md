# Prompt Catalog

Copy-paste prompts for every framework mode and workflow — research, planning, implementation, review, and resumption.

## Table of contents

1. [How to use this catalog](#how-to-use-this-catalog)
2. [Research Mode prompt](#research-mode-prompt)
3. [Design Mode — project initialization](#design-mode--project-initialization)
4. [Design Mode — sprint pack generation](#design-mode--sprint-pack-generation)
5. [Develop Mode — dry run](#develop-mode--dry-run)
6. [Design Mode — dry run review](#design-mode--dry-run-review)
7. [Develop Mode — authorization](#develop-mode--authorization)
8. [Resumption prompt](#resumption-prompt)

---

## How to use this catalog

Each prompt is a complete session opener. Copy it, fill in the bracketed placeholders, load the listed files into the session, and send.

Store your project's copies under:

```
prompts/research/
prompts/design/
prompts/develop/
```

**Rule:** Prompts are executable protocol. Keep them terse.

---

## Research Mode prompt

**Purpose:** Open a Research Mode session to investigate a topic before design begins.

**Files to load:** any relevant external context, notes, or constraints.

```
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

---

## Design Mode — project initialization

**Purpose:** Generate the foundational project brain files from initial notes, research, and constraints.

**Files to load:** research notes, business requirements, any prior context.

```
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

---

## Design Mode — sprint pack generation

**Purpose:** Generate `requirements.md`, `blueprint.md`, and `acceptance.md` for an upcoming sprint.

**Files to load:** `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, `QUESTIONS.md`, `RISKS.md`.

```
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

---

## Develop Mode — dry run

**Purpose:** Open Develop Mode at Permission Level 0. The model reads the Sprint Pack and produces `dry_run.md`, then stops.

**Files to load:** `AGENTS.md`, `STATE.md`, `COMMANDS.md`, `requirements.md`, `blueprint.md`, `acceptance.md`.

```
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

---

## Design Mode — dry run review

**Purpose:** Compare the Dry Run against the Sprint Pack and return approval or required corrections.

**Files to load:** `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`.

```
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

---

## Develop Mode — authorization

**Purpose:** Written by the human after the Dry Run review passes. This message authorizes implementation.

**Note:** This is not a session-open prompt — it is the human's authorization message sent to the open Develop Mode session.

```
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

Replace `[LEVEL]` with the Permission Level returned by the Dry Run review. See [Develop Mode Permission Levels](permission-levels.md).

---

## Resumption prompt

**Purpose:** Orient a new model session after a context reset, model switch, or pause. Design Mode reads the current project state and produces a resumption summary.

**Files to load:** `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, `QUESTIONS.md`, `RISKS.md`, `planning/backlog.md`, current sprint or release files if present.

```
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

For the full handoff and resumption protocol, see [Handoff, Resumption & Model Switching](handoff-protocol.md).

---

[← Wiki Home](index.md) · ADDF v3.5
