# GIT_STRATEGY.md - Mini Task Tracker

## 1. Branch Model

| Branch | Purpose | Rule |
|---|---|---|
| `main` | Stable release history | Only reviewed release work lands here. |
| `dev` | Integration branch | Sprint branches merge here before release. |
| `sprint/NNN-*` | Sprint work | Use for approved sprint implementation. |
| `fix/NNN-*` | Focused fixes | Use for small approved corrections. |

## 2. Branch Naming

| Type | Pattern | Example |
|---|---|---|
| Sprint | `sprint/NNN-short-name` | `sprint/001-core-task-list` |
| Fix | `fix/NNN-short-name` | `fix/001-localstorage-parse` |
| Docs | `docs/short-name` | `docs/validation` |
| Release | `release/vN.N` | `release/v0.1` |

## 3. Commit Convention

Use Conventional Commits: `type(scope): short description`.

| Type | Use |
|---|---|
| `feat` | Task app feature |
| `fix` | Bug fix |
| `docs` | Documentation-only change |
| `chore` | Maintenance change |
| `refactor` | Internal restructuring without behavior change |
| `test` | Test additions or updates |
| `release` | Release preparation |

## 4. PR Requirements

- [ ] Summary of change is present.
- [ ] Sprint reference is present.
- [ ] Acceptance criteria are linked.
- [ ] Manual verification steps are listed.
- [ ] Framework concepts changed: Yes/No.

## 5. Release Process

1. Create release branch - `release/v0.1`.
2. Update `VERSION.md` with `0.1.0`.
3. Update `CHANGELOG.md` with v0.1 changes.
4. Run consistency audit across project brain and app files.
5. Verify Sprint 001 acceptance criteria.
6. Merge to `main`.
7. Tag release as `v0.1.0`.
8. Publish release notes from `planning/releases/v0.1/release_notes.md`.

## 6. Merge Strategy

1. Squash noisy sprint work.
2. Use merge commits for release branches.
3. Do not merge unreviewed Develop Mode output into `main`.

## 7. .gitignore Minimums

- `.env`
- `.env.*`
- `*.env`
- `*.key`
- `*.pem`
- `secrets/`
- `node_modules/`
- `.DS_Store`
- `dist/`
- `build/`
- `*.log`
