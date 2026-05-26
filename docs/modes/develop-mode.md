# Develop Mode

Develop Mode is the only mode that writes code — and it does not write a single line until a Dry Run has been reviewed and the human has given explicit authorization.

> **Note:** Develop Mode was called *Builder Mode* in earlier versions of the framework.

## Table of contents

1. [What Develop Mode may create or modify](#what-develop-mode-may-create-or-modify)
2. [What Develop Mode must do](#what-develop-mode-must-do)
3. [What Develop Mode must not do](#what-develop-mode-must-not-do)
4. [The dry run requirement](#the-dry-run-requirement)
5. [Develop Mode prompts](#develop-mode-prompts)

---

## What Develop Mode may create or modify

Implementation assets:

```
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

Implementation-related Markdown (only these three):

```
dry_run.md
implementation_log.md
handoff_summary.md
```

Develop Mode may not write or modify any other Markdown files. Planning files, project brain files, and sprint pack files belong to Design Mode.

---

## What Develop Mode must do

Develop Mode must, in every session:

1. start at Permission Level 0,
2. produce a Dry Run (`dry_run.md`),
3. stop after the Dry Run,
4. wait for explicit human authorization,
5. modify only the files listed in `blueprint.md` and `dry_run.md`,
6. log every change in `implementation_log.md`,
7. run verification commands,
8. paste raw output into `implementation_log.md`,
9. stop when ambiguity appears,
10. and produce a checkpoint before context limits or model handoff.

---

## What Develop Mode must not do

Develop Mode must not:

1. invent business rules,
2. rewrite planning files unless explicitly authorized,
3. add dependencies without a recorded decision in `DECISIONS.md`,
4. touch files not listed in `blueprint.md` or `dry_run.md`,
5. skip the Dry Run,
6. skip verification,
7. continue after failures without logging them,
8. or self-authorize a higher Permission Level.

**Rule:** Develop Mode changes implementation files only after Dry Run approval.

---

## The dry run requirement

Every Develop Mode session begins at Permission Level 0 — Dry Run Only. At this level the model reads the Sprint Pack and produces `dry_run.md` listing everything it intends to change. Then it stops.

The Dry Run lists:

- files to create,
- files to modify,
- files to move or delete,
- commands to run,
- dependencies requested,
- risks,
- and ambiguities.

A human reviews the Dry Run — or Design Mode performs a structured review — before authorization is given. Implementation starts only after explicit approval.

![Dry Run Approval Gate](_PDF/images/8_Dry Run Approval Gate.png)

This gate catches scope creep, accidental refactors, unapproved dependency additions, and business-logic invention before they happen.

**Rule:** No Dry Run, no implementation.

---

## Develop Mode prompts

### Dry Run

Use this prompt at the start of every Develop Mode session. The model reads the Sprint Pack and produces `dry_run.md`, then stops.

Files to load: `AGENTS.md`, `STATE.md`, `COMMANDS.md`, `requirements.md`, `blueprint.md`, `acceptance.md`.

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

### Authorization

Use this prompt — written by the human — to authorize implementation after the Dry Run has been reviewed and approved.

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

Replace `[LEVEL]` with the appropriate Permission Level. Most sprints use Level 1. See [Develop Mode Permission Levels](../permission-levels.md) for the full 0–4 scale.

---

[← Modes Overview](index.md) · [← Wiki Home](../index.md) · ADDF v3.5
