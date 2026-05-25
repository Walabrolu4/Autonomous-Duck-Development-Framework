[Home](index.md)

# Glossary

All terms used across the ADDF wiki are defined here. Pages that introduce a concept link to this glossary for the formal definition. For the five most important concepts — Architect Mode, Builder Mode, Sprint Pack, Dry Run, and Permission Level — see [Core Concepts](core-concepts.md) for a longer practical explanation.

---

### Acceptance Criteria

The checklist in `acceptance.md` that defines whether a sprint is complete. All items must be checked before the sprint can be committed. Acceptance criteria are written by the Architect before the Builder writes any code.

See also: [Sprint Files — acceptance.md](file-reference/sprint-files.md#acceptancemd)

---

### ADR (Architecture Decision Record)

A permanent entry in `DECISIONS.md` recording why a technical decision was made, what was decided, and what the tradeoffs are. Decisions are never deleted — only superseded by new entries.

See also: [DECISIONS.md](file-reference/decisions.md)

---

### Architect Mode

The planning mode. An LLM invoked in Architect Mode defines requirements, risks, blueprints, and acceptance criteria. It never writes application source code. Any capable LLM can be used in Architect Mode — what matters is the mode, not the model.

See also: [Dual-Mode Orchestration — Architect Mode](orchestration.md#architect-mode), [Core Concepts](core-concepts.md)

---

### Builder Mode

The implementation mode. An LLM invoked in Builder Mode writes source code against an approved blueprint. It always runs a dry run first and stops to await permission before writing anything. It may not invent business logic not present in the blueprint.

See also: [Dual-Mode Orchestration — Builder Mode](orchestration.md#builder-mode), [Core Concepts](core-concepts.md)

---

### Context Bleed

When old or unrelated chat context contaminates the current task. The primary cause of AI regression bugs in vibe coding. Prevented by the [State Reset](#state-reset) at the end of every sprint and by closing the Builder thread between sprints.

See also: [Core Concepts](core-concepts.md)

---

### Context Engineering

The practice of organizing project knowledge into clean, specific Markdown files rather than relying on long chat history. Each AI session receives only the files it needs for the current task. The core methodology of the ADDF framework.

See also: [Core Concepts](core-concepts.md)

---

### Dry Run

A read-only report from the Builder listing every file it intends to create or modify, before any code is written. The Builder stops after the dry run and waits for authorization. The dry run gate is the primary mechanism for catching scope creep before it happens.

See also: [Sprint Files — dry_run.md](file-reference/sprint-files.md#dry_runmd), [Builder Pre-Flight Dry Run prompt](prompts.md#dry-run), [Core Concepts](core-concepts.md)

---

### Harness-First Development

Writing or defining the test harness and acceptance criteria before scaling functional implementation. The Builder writes unit tests before functional code; `acceptance.md` drives what must be proven before the sprint closes.

See also: [Step 3: Testing](lifecycle/03-testing.md)

---

### Local File Sovereignty

The principle that project memory belongs in local Markdown files controlled by the human operator — not in an AI chat session. Because state lives in files, the project survives rate limits, model swaps, lost chats, and long breaks.

See also: [Dual-Mode Orchestration — The File System](orchestration.md#the-file-system-the-sovereign-brain), [Core Concepts](core-concepts.md)

---

### Mode

A task category that defines which workflow to follow. The six modes are: Quick Patch, Feature Sprint, Refactor/Migration, Data Ingestion, Style Audit, and Parallel Sprints. A mode tells you *how* to handle the specific task in front of you; the lifecycle phase tells you *where* you are in the project.

See also: [Operating Modes](modes/index.md)

---

### Permission Level

A number from 0 to 4 that limits what the Builder may do. Always assigned explicitly by the human operator at the start of a Builder session. Level 0 is read-only (dry run only); Level 1 is the standard sprint scope; Levels 2–4 allow progressively more latitude for expansions, refactors, and migrations.

See also: [Dual-Mode Orchestration — Permission Levels](orchestration.md#builder-permission-levels), [Core Concepts](core-concepts.md)

---

### Sprint Pack

The three files that define a sprint: `requirements.md` (what to build and what not to build), `blueprint.md` (the technical plan, step by step), and `acceptance.md` (the checklist that defines done). The Architect generates the Sprint Pack; the Builder consumes it.

See also: [Sprint Files](file-reference/sprint-files.md), [Core Concepts](core-concepts.md)

---

### Sovereign Brain

The local folder containing the Markdown files that define the project's state, rules, and history. Because these files live on the human operator's drive, the project brain survives any model change, rate limit, or session loss.

See also: [Dual-Mode Orchestration](orchestration.md)

---

### State Reset

Closing the active Builder chat after the sprint work is captured in files, so the next sprint begins with clean context. The state reset is non-optional — skipping it allows context bleed to accumulate across sprints.

See also: [Sprint Workflow — Step 10](sprint-workflow.md#step-10--commit-update-reset), [Core Concepts](core-concepts.md)

---

### Vibe Coding

An informal AI coding loop where the developer keeps prompting in one chat session without stable project memory, explicit specifications, or a dry run gate. The improvisation bias and context bleed problems that result from vibe coding are the core problems the ADDF framework solves.

See also: [Home](index.md)

## See Also

- [Core Concepts](core-concepts.md)
- [Dual-Mode Orchestration](orchestration.md)
- [Sprint Workflow](sprint-workflow.md)
