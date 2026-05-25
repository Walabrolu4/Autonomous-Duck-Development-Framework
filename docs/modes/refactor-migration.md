[Home](../index.md) → [Operating Modes](index.md) → Mode 3: Refactor / Migration

# Mode 3: Refactor / Migration

## Use For

Database migrations, major dependency upgrades, architectural restructuring, auth system changes, or anything that could break existing functionality across the codebase.

---

## Workflow / Rule

1. Architect generates a full Sprint Pack with a dedicated `refactor/description` branch
2. Builder operates at **Level 3 or Level 4**, assigned explicitly at session start
3. Builder pre-fills `rollback_log.md` with the current clean commit hash and rollback command before writing any code
4. Builder implements with full logging in `implementation_log.md`
5. Architect reviews `implementation_log.md` before merge to `dev` or `main`
6. Retrospective is mandatory after every Mode 3 sprint

---

## Rollback Requirement

`rollback_log.md` must be pre-filled before the Builder begins — not after. If anything goes wrong in production, you need to be able to revert in seconds, not minutes. The rollback command should be:

```
git checkout [branch] && git revert HEAD~[N] --no-edit
```

Fill in the current clean commit hash with `git log --oneline -1` before starting. If this step is skipped and a migration fails, you may not have a clean revert path.

For Level 4 migrations, this is a hard requirement. For Level 3 refactors, it is strongly recommended.

## See Also

- [Sprint Files — rollback_log.md](../file-reference/sprint-files.md#rollback_logmd)
- [Builder Permission Levels](../orchestration.md#builder-permission-levels)
- [Step 7: Deployment & Maintenance](../lifecycle/07-deployment.md)
