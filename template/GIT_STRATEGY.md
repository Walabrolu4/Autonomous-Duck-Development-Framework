# GIT_STRATEGY.md

## Branch Model

| Branch                      | Purpose                                        |
|-----------------------------|------------------------------------------------|
| `main`                      | Production-ready code only                     |
| `dev`                       | Integration branch — all sprint branches merge here first |
| `sprint/NNN-short-desc`     | One branch per sprint                          |
| `refactor/short-description`| Used for Mode 3 refactor or migration work     |

## Rules

1. Builder works only on the assigned branch.
2. Sprint branches merge into `dev` only after `human_review.md` passes.
3. `dev` merges into `main` only after Architect approval.
4. Mode 1 quick patches may work directly on `dev` only when under 10 lines and no business logic is introduced.

## Commit Message Format
```
[sprint/NNN] short description of change
```
