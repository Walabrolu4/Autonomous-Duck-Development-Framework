[Home](../index.md) → [Lifecycle](index.md) → Step 7: Deployment & Maintenance

# Step 7: Deployment & Maintenance

## Goal

Move the product to production and manage it reliably over time.

---

## The Action

Choose the mode that matches the change:

- **Minor fixes** — use [Mode 1: Quick Patch](../modes/quick-patch.md). Single-file changes under 10 lines, no sprint pack required, Builder works directly on `dev`.
- **Heavy migrations or dependency upgrades** — use [Mode 3: Refactor/Migration](../modes/refactor-migration.md). Full sprint pack, dedicated branch, mandatory retrospective.

After deployment, add the build command and rollback command to `COMMANDS.md` if they are not already there. Log fragile production assumptions in `RISKS.md` with specific mitigation plans.

---

## The Rule

Rollback commands must exist in `COMMANDS.md` **before** deployment — not after something breaks. If you need to revert in seconds, you cannot afford to look up the rollback procedure under pressure.

For Mode 3 migrations, `rollback_log.md` must be pre-filled with the current clean commit hash and rollback command before the Builder begins.

## See Also

- [Mode 1: Quick Patch](../modes/quick-patch.md)
- [Mode 3: Refactor / Migration](../modes/refactor-migration.md)
- [COMMANDS.md](../file-reference/commands.md)
- [rollback_log.md](../file-reference/sprint-files.md#rollback_logmd)
