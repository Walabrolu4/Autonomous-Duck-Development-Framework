# Sprint [NUMBER] Rollback Log

Required for Level 4 (Migration) sprints. Recommended for all others.

---

## Pre-Implementation (fill in BEFORE Builder begins)

**Current clean commit hash:**
```
[git log --oneline -1]
```

**Rollback command:**
```
git checkout [branch] && git revert HEAD~[N] --no-edit
```

---

## Post-Implementation (fill in ONLY if recovery was needed)

**Date of rollback:** [YYYY-MM-DD]
**Root cause identified:** [What went wrong]
**State after revert:** Clean / Partial — [describe]
**Follow-up action:** [What will be done differently next sprint]
