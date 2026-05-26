# Design Mode

Design Mode converts intent into durable project memory — it writes the files that constrain every model session that follows.

> **Note:** Design Mode was called *Architect Mode* in earlier versions of the framework. The two terms refer to the same role.

## Table of contents

1. [What Design Mode covers](#what-design-mode-covers)
2. [What Design Mode may create or update](#what-design-mode-may-create-or-update)
3. [What Design Mode must not do](#what-design-mode-must-not-do)
4. [Design Mode prompts](#design-mode-prompts)

---

## What Design Mode covers

Design Mode handles every planning, specification, review, and memory-writing task:

1. feasibility analysis,
2. MVP definition,
3. validation gates,
4. architecture planning,
5. release planning,
6. feature planning,
7. Sprint Pack generation,
8. Dry Run review,
9. implementation review,
10. retrospective generation,
11. resumption summaries,
12. handoff notes,
13. documentation updates,
14. and decision logging.

If work produces a Markdown file that another session will load, Design Mode wrote it.

---

## What Design Mode may create or update

```
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

---

## What Design Mode must not do

Design Mode must not:

1. write source code,
2. mutate implementation files,
3. add dependencies directly,
4. run uncontrolled repository changes,
5. or treat a plan as implementation.

A blueprint is not code. An acceptance criterion is not a test. Design Mode produces the specification; Develop Mode produces the implementation.

**Rule:** Design Mode writes Markdown project memory. It does not write implementation.

---

## Design Mode prompts

### Project initialization

Use this prompt to generate the foundational project brain files from initial notes, research, and constraints.

Files to load: research notes, any existing context, business requirements.

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

### Sprint Pack generation

Use this prompt to generate `requirements.md`, `blueprint.md`, and `acceptance.md` for an upcoming sprint.

Files to load: `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, `QUESTIONS.md`, `RISKS.md`.

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

### Dry Run review

Use this prompt after Develop Mode produces `dry_run.md`. Design Mode compares the dry run against the Sprint Pack and returns approval or required corrections.

Files to load: `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`.

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

### Resumption

Use this prompt to orient a new model session after a context reset, model switch, or pause.

Files to load: `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, `QUESTIONS.md`, `RISKS.md`, backlog, current sprint or release files if present.

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

The full catalog, including Develop Mode prompts, is at [Prompt Catalog](../prompt-catalog.md).

**Rule:** Design Mode writes Markdown project memory. It does not write implementation.

---

[← Modes Overview](index.md) · [← Wiki Home](../index.md) · ADDF v3.5
