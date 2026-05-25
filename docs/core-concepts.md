[Home](index.md)

# Core Concepts

The ADDF framework uses a small set of terms consistently throughout every section. This page defines the eight most important ones so you can read the rest of the wiki without guessing. Every definition here links to the page where the concept is used in practice.

---

## Architect Mode

Architect Mode is the planning mode. You invoke an LLM in Architect Mode when you want it to produce requirements, blueprints, and acceptance criteria. The Architect asks clarifying questions, identifies risks, and writes Markdown files. It never writes application source code.

Think of the Architect as a senior technical lead who writes the plan but does not touch the keyboard. If the Architect writes code, the planning and execution separation collapses — there is no longer an independent standard against which the Builder's work is measured.

For the full permission model and which tools to use, see [Dual-Mode Orchestration](orchestration.md). For a quick lookup, see [Glossary — Architect Mode](glossary.md#architect-mode).

---

## Builder Mode

Builder Mode is the implementation mode. You invoke an LLM in Builder Mode when you want it to write source code. The Builder reads the sprint blueprint and implements exactly what is specified. It runs a read-only dry run first, stops, waits for your approval, then builds. It never invents business logic that was not in the blueprint.

The dry run pause is the entire safety model of the framework. Without it, there is no window to catch scope creep before the code is written.

For the full permission model, see [Dual-Mode Orchestration](orchestration.md). For a quick lookup, see [Glossary — Builder Mode](glossary.md#builder-mode).

---

## Sprint Pack

The Sprint Pack is the three files that define a sprint: `requirements.md` (what to build and what not to build), `blueprint.md` (the technical plan, step by step), and `acceptance.md` (the checklist that defines done). The Architect generates the Sprint Pack. The Builder consumes it.

No code is written until all three files exist and the human operator has reviewed the blueprint. For templates and full detail on each file, see [Sprint Files](file-reference/sprint-files.md).

---

## Dry Run

A dry run is a read-only report from the Builder listing every file it intends to create or modify, before it changes anything. The Builder produces the dry run and then stops. You review it, confirm it matches the blueprint, and give permission. Only then does the Builder write code.

The dry run gate catches hidden scope creep, accidental refactors, dependency additions, and business-logic invention — before they happen. For the prompt that triggers it, see [Builder Pre-Flight Dry Run](prompts.md#dry-run). For the file it produces, see [Sprint Files — dry_run.md](file-reference/sprint-files.md#dry_runmd).

---

## Permission Level

Permission Level is a number from 0 to 4 that controls how much the Builder can do. You assign it explicitly at the start of each Builder session.

- **Level 0** — Read-only. Dry run only, no code changes.
- **Level 1** — Standard sprint scope. The Builder may only touch files listed in the blueprint.
- **Level 2** — Approved expansion. Minor helper modules surfaced during the dry run and approved by the Architect.
- **Level 3** — Supervised refactor. Adjacent file mutations, fully logged.
- **Level 4** — Migration. Heavy schema changes. Requires pre-written rollback procedures.

Start at Level 1 for almost every sprint. For the full table with operational parameters, see [Builder Permission Levels](orchestration.md#builder-permission-levels).

---

## Local File Sovereignty

Local File Sovereignty is the principle that project memory lives in local Markdown files controlled by the human operator — not in any AI chat session. The files are the project. The AI is the tool.

Because the project brain lives in files, the project survives rate limits, model swaps, lost chats, and long breaks. You can run an Architect session in Claude, hit a rate limit, copy the updated files, and continue in Gemini or ChatGPT without any context degradation. For full detail, see [Dual-Mode Orchestration — The File System](orchestration.md#the-file-system-the-sovereign-brain).

---

## Context Engineering

Context Engineering is the practice of organizing project knowledge into clean, modular Markdown files rather than relying on long chat history. Each AI session receives only the files it needs for the current job — not the entire chat history or codebase.

More context is not better context. Cleaner context is better context. Large context windows do not solve the vibe coding problem; they extend it. For the practical implementation, see [Setup — Context Loading Protocol](setup.md#context-loading-protocol).

---

## State Reset

State Reset is the act of closing the Builder chat at the end of every sprint, after the sprint work has been captured in files. The next sprint then starts from clean, file-based project memory instead of an accumulated conversation thread.

Closing the Builder thread is not optional. A long Builder chat accumulates old sprint decisions, abandoned approaches, and previous implementation details that contaminate future sprints. For the step where this happens, see [Sprint Workflow — Step 10](sprint-workflow.md#step-10--commit-update-reset).

---

> **Tip:** This page covers the eight most critical concepts. The full expanded glossary — including Acceptance Criteria, ADR, Context Bleed, Harness-First Development, Sovereign Brain, and Vibe Coding — is at [Glossary](glossary.md).

## See Also

- [Glossary](glossary.md)
- [Dual-Mode Orchestration](orchestration.md)
- [Sprint Workflow](sprint-workflow.md)
- [File Reference](file-reference/index.md)
