[Home](../index.md) → [File Reference](index.md) → GIT_STRATEGY.md

# GIT_STRATEGY.md

## Purpose

GIT_STRATEGY.md defines the branching model and commit rules for the project. The Builder reads it to know which branch to work on and when it may commit. Without a clear branching strategy, sprints can land on the wrong branch, merge conflicts become unpredictable, and the audit trail breaks.

---

## Template

```markdown
# GIT_STRATEGY.md

## Branch Model
- main: production-ready only
- dev: integration branch
- sprint/NNN-short-description: one branch per sprint
- refactor/short-description: used for Mode 3 refactor or migration work

## Rules
1. Builder works only on the assigned branch.
2. Sprint branches merge into dev only after human_review.md passes.
3. dev merges into main only after Architect approval.
4. Mode 1 quick patches may work directly on dev only when under 10 lines
   and no business logic is introduced.
```

---

## Branch Rules

| Branch | Purpose | Who Commits |
|--------|---------|-------------|
| `main` | Production-ready code only | Human operator, after Architect approval |
| `dev` | Integration branch — all sprint branches merge here first | Human operator, after `human_review.md` passes |
| `sprint/NNN-short-description` | One branch per sprint | Builder agent |
| `refactor/short-description` | Mode 3 refactor or migration work | Builder agent, at Level 3 or 4 |

The four rules to follow on every project:

1. The Builder always works on the named sprint branch — never directly on `dev` or `main`.
2. Sprint branches merge into `dev` only after all five gates in `human_review.md` pass.
3. `dev` merges into `main` only after Architect approval.
4. [Mode 1: Quick Patch](../modes/quick-patch.md) is the only mode that may work directly on `dev`, given its scope constraint of under 10 lines with no new business logic.

## See Also

- [Setup — Git Branching Protocol](../setup.md#git-branching-protocol)
- [Mode 1: Quick Patch](../modes/quick-patch.md)
