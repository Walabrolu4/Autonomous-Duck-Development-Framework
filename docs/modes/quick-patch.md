[Home](../index.md) → [Operating Modes](index.md) → Mode 1: Quick Patch

# Mode 1: Quick Patch

## Use For

Typo fixes, minor UI adjustments, single-function changes, renaming, or small config edits. Any change under approximately 10 lines that introduces no new business logic.

---

## Workflow / Rule

1. Open Builder at Level 1 permission on `dev` branch
2. State the specific file and the exact change needed
3. Builder mutates only that file
4. Run verification commands from `COMMANDS.md`
5. Commit and update `STATE.md`

No sprint pack required. No dry run required — but the scope constraint is strict: one file, one change, no new logic.

---

## When NOT to Use This Mode

If the fix requires understanding how multiple files interact, introduces any new logic, or touches a database schema — use Mode 2 or Mode 3.

**The boundary test:** Does this change require a blueprint? If yes, it is not a Quick Patch. Blueprint requirement is the signal that the change has outgrown Mode 1.

Concrete examples that are NOT Quick Patches:
- A bug fix that requires changing how two components share state
- A "small" config change that affects multiple environments
- Updating a function that is imported by more than one file
- Any change that adds a new parameter to an existing API

When in doubt, use Mode 2.

## See Also

- [Step 7: Deployment & Maintenance](../lifecycle/07-deployment.md)
- [Mode 2: Feature Sprint](feature-sprint.md)
- [COMMANDS.md](../file-reference/commands.md)
