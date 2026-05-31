# Sprint 003 - Dry Run

**Mode:** Develop Mode  
**Permission Level:** 0 - Dry Run Only  
**Sprint:** 003 - Prompt Catalog  
**Sprint pack reference:** `planning/sprints/sprint_003/requirements.md`, `blueprint.md`, `acceptance.md`  
**Date:** 2026-05-31

---

## 1. Files to Create

### Catalog index

| # | File | Purpose |
|---:|---|---|
| 1 | `prompts/README.md` | Prompt catalog index with category descriptions, usage instructions, version 0.1.0, and links to every prompt file. |

### Research prompts

| # | File | Purpose |
|---:|---|---|
| 2 | `prompts/research/research-brief.md` | Copy-ready Research Mode prompt for a bounded research question. |
| 3 | `prompts/research/source-summary.md` | Copy-ready Research Mode prompt for summarizing sources. |
| 4 | `prompts/research/tool-comparison.md` | Copy-ready Research Mode prompt for comparing tools or approaches. |
| 5 | `prompts/research/open-questions.md` | Copy-ready Research Mode prompt for identifying and recording open questions. |
| 6 | `prompts/research/risk-discovery.md` | Copy-ready Research Mode prompt for surfacing and recording risks. |

### Design prompts

| # | File | Purpose |
|---:|---|---|
| 7 | `prompts/design/project-initialization.md` | Copy-ready Design Mode prompt for creating or completing the project brain. |
| 8 | `prompts/design/release-planning.md` | Copy-ready Design Mode prompt for release planning. |
| 9 | `prompts/design/feature-cycle.md` | Copy-ready Design Mode prompt for feature planning. |
| 10 | `prompts/design/sprint-pack-generation.md` | Copy-ready Design Mode prompt for generating sprint packs. |
| 11 | `prompts/design/dry-run-review.md` | Copy-ready Design Mode prompt for reviewing a dry run. |
| 12 | `prompts/design/implementation-review.md` | Copy-ready Design Mode prompt for implementation review. |
| 13 | `prompts/design/consistency-audit.md` | Copy-ready Design Mode prompt for consistency audits. |
| 14 | `prompts/design/documentation-drift-audit.md` | Copy-ready Design Mode prompt for documentation drift audits. |
| 15 | `prompts/design/resumption.md` | Copy-ready Design Mode prompt for project resumption. |

### Develop prompts

| # | File | Purpose |
|---:|---|---|
| 16 | `prompts/develop/dry-run.md` | Copy-ready Develop Mode prompt for Permission Level 0 dry runs. |
| 17 | `prompts/develop/authorization.md` | Human authorization prompt with the exact dry run approval message. |
| 18 | `prompts/develop/verification-run.md` | Copy-ready Develop Mode prompt for approved verification runs. |
| 19 | `prompts/develop/implementation-log-update.md` | Copy-ready Develop Mode prompt for updating implementation logs. |
| 20 | `prompts/develop/patch-implementation.md` | Copy-ready Develop Mode prompt for small approved patches. |

### Handoff prompts

| # | File | Purpose |
|---:|---|---|
| 21 | `prompts/handoff/session-checkpoint.md` | Copy-ready prompt for ending a session with a durable checkpoint. |
| 22 | `prompts/handoff/incoming-model-resumption.md` | Copy-ready prompt for a new model resuming from files. |
| 23 | `prompts/handoff/long-break-resumption.md` | Copy-ready prompt for resuming after a long break. |

### Maintenance prompts

| # | File | Purpose |
|---:|---|---|
| 24 | `prompts/maintain/quick-patch.md` | Copy-ready maintenance prompt for a very small correction. |
| 25 | `prompts/maintain/refactor-planning.md` | Copy-ready maintenance prompt for supervised refactor planning. |
| 26 | `prompts/maintain/migration-planning.md` | Copy-ready maintenance prompt for high-risk migration planning. |
| 27 | `prompts/maintain/dependency-approval.md` | Copy-ready maintenance prompt for dependency approval. |
| 28 | `prompts/maintain/rollback-planning.md` | Copy-ready maintenance prompt for rollback planning. |

### Sprint verification artifact

| # | File | Purpose |
|---:|---|---|
| 29 | `planning/sprints/sprint_003/consistency_audit.md` | Audit report checking prompt paths, required sections, mode names, dry run enforcement, and documentation consistency. |

---

## 2. Files to Modify

| File | Planned change | Reason |
|---|---|---|
| `README.md` | Add or update a link to the prompt catalog. | Make the prompt catalog discoverable from the repository entry point. |
| `docs/prompt-catalog.md` | Replace or update seed inline prompt content with links and summaries for the 27 individual prompt files. | Make individual prompt files canonical while preserving documentation navigation. |
| `PROMPT_CHANGELOG.md` | Mark v0.1.0 prompt catalog as created and list exact prompt paths. | Keep public prompt version history aligned with created files. |
| `planning/releases/v0.1/release_plan.md` | Update Sprint 003 status during closeout. | Keep release tracking current. |
| `planning/backlog.md` | Update Sprint 003 lifecycle status as work progresses or closes. | Keep sprint tracking current. |
| `STATE.md` | Update current status and next step during implementation and closeout. | Keep project memory current. |
| `starter-kit/blank/PROMPTS.md` | Add a pointer to the full prompt catalog only if needed after prompt files exist. | Make the prompt catalog available from the starter kit without duplicating the full catalog. |

---

## 3. Files to Move or Delete

None.

No existing prompt files are present under `prompts/`, so no move or deletion is planned.

---

## 4. Commands to Run

| Command | Purpose |
|---|---|
| `rg --files prompts` | Verify all prompt catalog files exist after creation. |
| `rg "Architect Mode|Builder Mode" prompts docs/prompt-catalog.md README.md PROMPT_CHANGELOG.md` | Confirm deprecated public mode names are not present in prompt catalog surfaces. |
| `rg "## Purpose|## When to Use|## Mode|## Files to Load First|## Prompt|## Expected Output|## Notes" prompts` | Inspect required prompt section headings across prompt files. |
| `rg "Dry run approved.|Permission Level \\[LEVEL\\] authorized.|Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md." prompts/develop/authorization.md` | Confirm the authorization prompt contains the exact approval message. |
| `git status --short` | Confirm the final working tree state before handoff or review. |

---

## 5. Dependencies Requested

None.

Sprint 003 creates and updates Markdown files only. No libraries, packages, external APIs, build tools, or network access are required.

---

## 6. Risks

1. **Prompt path drift.** The requirements text says Maintenance Prompts, while existing project memory uses `prompts/maintain/`. Mitigation: use `prompts/maintain/` consistently because `PROMPT_CHANGELOG.md`, v0.1 scope, and the Sprint 003 sprint pack use that path.
2. **Required section omissions.** With 27 prompt files, one file could miss a required heading. Mitigation: use a consistent prompt template and audit all files.
3. **Develop Mode safety regression.** Develop prompts could accidentally imply implementation before dry run authorization. Mitigation: explicitly include Permission Level 0 and dry run boundaries in Develop prompts.
4. **Documentation duplication drift.** `docs/prompt-catalog.md`, `prompts/README.md`, and `PROMPT_CHANGELOG.md` could disagree on the prompt list. Mitigation: make `prompts/README.md` the catalog index and update supporting docs from the same exact path list.
5. **Starter kit duplication.** `starter-kit/blank/PROMPTS.md` already contains starter prompts; duplicating the full prompt catalog there may create two sources of truth. Mitigation: add a pointer to the full catalog only if needed, rather than copying all prompts into the starter kit file.

---

## 7. Ambiguities

1. **Whether `starter-kit/blank/PROMPTS.md` should be modified.** The blueprint says to modify it only if needed. Recommended handling: add a short pointer to `prompts/README.md` after the prompt catalog exists; do not duplicate all 27 prompts.
2. **Whether `docs/prompt-catalog.md` should retain inline prompt text.** Current docs contain seed inline prompts. Recommended handling: convert this page into a catalog overview that links to the canonical individual files, with brief summaries.
3. **Whether maintenance folder should be `maintain` or `maintenance`.** Existing project memory and sprint pack use `prompts/maintain/`; requirements use the category name "Maintenance Prompts." Recommended handling: keep exact folder `prompts/maintain/` and document the choice in the audit.
4. **Whether to update release package references now.** The prompt catalog ZIP is Sprint 009 scope, so Sprint 003 should not create package artifacts. It may leave release package checklist items for Sprint 009.

---

Dry run complete. Do not proceed.

Await human review of this dry run and authorization before creating or modifying any prompt catalog files.

---

*ADDF - `planning/sprints/sprint_003/dry_run.md` - Develop Mode - Permission Level 0 - 2026-05-31*
