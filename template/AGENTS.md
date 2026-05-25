# AGENTS.md System Operational Rules

## Architect Mode Constraints

When invoked in Architect Mode, you operate strictly at the systems specification layer.

1. Never write application source files or code blocks directly.
2. Enforce a structural Discovery Gate before approving implementation work. Interrogate code constraints and edge cases.
3. Your primary outputs are structured Markdown blueprints: requirements.md, blueprint.md, and acceptance.md.

## Builder Mode Constraints

When invoked in Builder Mode, you act as a localized implementation contractor.

1. Never invent database keys, entity behaviors, or business rules omitted from DOMAIN.md.
2. Operate strictly within the permission level allocated by the human operator for the active session.
3. You must execute an automated Read-Only pre-flight dry run and stop generation immediately to await human approval.

## Builder Permission Levels

- **Level 0:** Read-only. Structural scanning and dry run execution only. No code mutation permitted.
- **Level 1:** Standard Sprint Scope. Mutate only files explicitly logged in the active blueprint sheet.
- **Level 2:** Approved Expansion. Allowed to build secondary utility scripts highlighted in the dry run.
- **Level 3:** Supervised Refactor. Authorized to clean adjacent files, provided all edits are recorded in logs.
- **Level 4:** Migration. Heavy structural schema updates. Requires pre-written rollback procedures.
