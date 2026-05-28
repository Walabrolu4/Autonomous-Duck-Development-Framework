# GIT_STRATEGY.md

**The Autonomous Duck Deployment Framework — git branching, commit, and release strategy.**

Load this file when a session needs to create branches, write commits, open pull requests, or prepare releases.

---

## 1. Branch model

```
main          — stable, always releasable. Protected.
dev           — integration branch. Merges to main when release-ready.
sprint/NNN-*  — one branch per sprint. Merges to dev.
fix/NNN-*     — patch branches. May merge to dev or directly to main.
docs/*        — documentation-only changes. May merge to dev.
```

### Rules

- `main` is never committed to directly.
- `dev` is never committed to directly unless it is a trivial documentation fix.
- Every sprint gets its own branch. The branch name matches the sprint folder.
- Sprint branches are deleted after merging.

---

## 2. Branch naming

| Type | Pattern | Example |
|---|---|---|
| Sprint | `sprint/NNN-short-description` | `sprint/001-repository-skeleton` |
| Fix | `fix/NNN-short-description` | `fix/002-starter-kit-template-error` |
| Documentation | `docs/short-description` | `docs/handoff-protocol-cleanup` |
| Release | `release/vN.N.N` | `release/v0.1.0` |

Use lowercase, hyphens only, no special characters.

---

## 3. Commit message convention

Follow [Conventional Commits](https://www.conventionalcommits.org/).

```
<type>(<scope>): <short description>
```

Types:

| Type | When to use |
|---|---|
| `feat` | New file, new section, new prompt, new template |
| `fix` | Correction to existing content |
| `docs` | Documentation changes |
| `chore` | Project brain file updates, version bumps, tooling |
| `refactor` | Restructuring without behavior change |
| `test` | Test files (CLI tool, future) |
| `release` | Release commit or tag |

Scope examples: `sprint-001`, `agents`, `domain`, `starter-kit`, `prompts`, `examples`, `brain`.

### Examples

```
feat(sprint-001): add project brain files
chore(brain): update STATE.md after Sprint 001 close
fix(domain): correct v0.1 out-of-scope list
docs(handoff): add incoming model resumption protocol
feat(prompts): add sprint pack generation prompt
release(v0.1): prepare release package
```

Rules:
- No emoji in commit messages.
- No exclamation marks.
- No personal pronouns.
- Use imperative or past tense consistently within the repository.
- Keep the subject line under 72 characters.
- Use the body to explain *why*, not *what*, when the diff is not self-evident.

---

## 4. Pull request process

### PR requirements

Every PR must include:

- **Context:** Why this change is needed.
- **What changed:** A brief description of the files and content affected.
- **Verification:** How it was checked (Design Mode review, human review, link check).
- **Out of scope:** What was explicitly not changed and why.
- **Impacted files:** List of files modified.
- **Framework concepts changed:** Yes / No. If yes, reference the `DECISIONS.md` entry.

### PR title format

Follow the same convention as commit messages: `<type>(<scope>): <short description>`.

### Review requirements

- At least one human review before merging to `dev`.
- Changes to framework concepts require a `DECISIONS.md` update.
- Changes to canonical terminology require a `STYLE_GUIDE.md` review.
- Release merges (`dev` → `main`) require the release acceptance criteria to be checked.

---

## 5. Release process

### Step sequence

1. Create a `release/vN.N.N` branch from `dev`.
2. Update `VERSION.md` with the new version numbers.
3. Update `CHANGELOG.md` with the release notes.
4. Run the consistency audit prompt against all documentation.
5. Verify all acceptance criteria for the release are met.
6. Merge `release/vN.N.N` → `main`.
7. Tag the release: `git tag -a vN.N.N -m "vN.N.N [Release name]"`.
8. Push the tag: `git push origin vN.N.N`.
9. Create a GitHub release with the release notes from `CHANGELOG.md`.
10. Attach release package assets (ZIPs, PDFs) to the GitHub release.
11. Update `STATE.md`.

### Tag format

```
vN.N.N
```

Examples: `v0.1.0`, `v0.2.0`, `v1.0.0`.

---

## 6. Merge strategy

- Sprint branches merge to `dev` using **squash merge** when the sprint history is noisy. Use regular merge when the commit history is clean and meaningful.
- `release/*` branches merge to `main` using a **merge commit** (not squash) so the release boundary is clear in history.
- `dev` merges to `main` only at release points.

---

## 7. .gitignore rules

At minimum, `.gitignore` must include:

```
.env
.env.*
*.env
node_modules/
.DS_Store
dist/
build/
*.log
```

Never commit secrets. See `SECURITY.md`.

---

## 8. Repository protection

When the repository is on GitHub:

- Protect `main`: require pull request reviews, no direct pushes, no force pushes.
- Protect `dev`: require pull request reviews.
- Require status checks to pass before merging (when CI is available).

---

*ADDF · `GIT_STRATEGY.md` · maintained as part of the project brain*
