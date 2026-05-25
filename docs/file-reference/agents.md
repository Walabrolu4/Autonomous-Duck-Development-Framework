[Home](../index.md) → [File Reference](index.md) → AGENTS.md

# AGENTS.md

## Purpose

AGENTS.md is the rulebook that every AI session reads first. It defines what Architect Mode and Builder Mode are allowed to do, lists the permission levels, and accumulates project-specific constraints discovered during retrospectives. Loading AGENTS.md is the first action in every session — Architect or Builder — without exception.

---

## Template

Copy this template into your project's `AGENTS.md`:

```markdown
# AGENTS.md System Operational Rules

## Architect Mode Constraints
When invoked in Architect Mode, you operate strictly at the
systems specification layer.
1. Never write application source files or code blocks directly.
2. Enforce a structural Discovery Gate before approving
   implementation work. Interrogate code constraints and edge cases.
3. Your primary outputs are structured Markdown blueprints:
   requirements.md, blueprint.md, and acceptance.md.

## Builder Mode Constraints
When invoked in Builder Mode, you act as a localized
implementation contractor.
1. Never invent database keys, entity behaviors, or business rules
   omitted from DOMAIN.md.
2. Operate strictly within the permission level allocated by the
   human operator for the active session.
3. You must execute an automated Read-Only pre-flight dry run and
   stop generation immediately to await human approval.

## Builder Permission Levels
- Level 0: Read-only. Structural scanning and dry run execution only.
  No code mutation permitted.
- Level 1: Standard Sprint Scope. Mutate only files explicitly logged
  in the active blueprint sheet.
- Level 2: Approved Expansion. Allowed to build secondary utility scripts
  highlighted in the dry run.
- Level 3: Supervised Refactor. Authorized to clean adjacent files,
  provided all edits are recorded in logs.
- Level 4: Migration. Heavy structural schema updates.
  Requires pre-written rollback procedures.
```

---

## How to Customize It

AGENTS.md starts with the generic template above. You add project-specific constraints here as you discover them — typically through the retrospective at the end of each sprint.

For example: after Sprint 002 of the Mini Task Tracker, the Builder created a task with an empty title when the user triggered form submission via a keyboard shortcut. The acceptance criteria had only covered button clicks. The fix was to add this constraint to AGENTS.md:

```markdown
## Additional Builder Constraints (added Sprint 002 retrospective)
- Always validate non-empty, non-whitespace title before task creation,
  regardless of how form submission was triggered.
```

From that point on, every future Builder session reads this constraint. The AI does not learn from mistakes automatically — you must write the lesson down. AGENTS.md is where those lessons live permanently.

---

## When It's Loaded

AGENTS.md is loaded in **every single session**, always first. It is the one file that the AI always reads before anything else, regardless of session type (Architect, Builder, audit, or data ingestion).

## See Also

- [Getting Started](../getting-started.md)
- [Sprint Workflow](../sprint-workflow.md)
- [File Reference Overview](index.md)
