# Sprint 003 - Acceptance Criteria

**Sprint:** 003  
**Title:** Prompt Catalog  
**Reviewer:** Human  
**How to use this file:** Check each box only after opening the relevant file or running the stated search. Do not check boxes based only on the model's summary.

---

## 1. Folder and Index Existence

- [ ] `prompts/README.md` exists.
- [ ] `prompts/research/` exists.
- [ ] `prompts/design/` exists.
- [ ] `prompts/develop/` exists.
- [ ] `prompts/handoff/` exists.
- [ ] `prompts/maintain/` exists.

**Issues found:** `[None / list]`

---

## 2. Research Prompt Files

- [ ] `prompts/research/research-brief.md` exists.
- [ ] `prompts/research/source-summary.md` exists.
- [ ] `prompts/research/tool-comparison.md` exists.
- [ ] `prompts/research/open-questions.md` exists.
- [ ] `prompts/research/risk-discovery.md` exists.

**Issues found:** `[None / list]`

---

## 3. Design Prompt Files

- [ ] `prompts/design/project-initialization.md` exists.
- [ ] `prompts/design/release-planning.md` exists.
- [ ] `prompts/design/feature-cycle.md` exists.
- [ ] `prompts/design/sprint-pack-generation.md` exists.
- [ ] `prompts/design/dry-run-review.md` exists.
- [ ] `prompts/design/implementation-review.md` exists.
- [ ] `prompts/design/consistency-audit.md` exists.
- [ ] `prompts/design/documentation-drift-audit.md` exists.
- [ ] `prompts/design/resumption.md` exists.

**Issues found:** `[None / list]`

---

## 4. Develop Prompt Files

- [ ] `prompts/develop/dry-run.md` exists.
- [ ] `prompts/develop/authorization.md` exists.
- [ ] `prompts/develop/verification-run.md` exists.
- [ ] `prompts/develop/implementation-log-update.md` exists.
- [ ] `prompts/develop/patch-implementation.md` exists.

**Issues found:** `[None / list]`

---

## 5. Handoff Prompt Files

- [ ] `prompts/handoff/session-checkpoint.md` exists.
- [ ] `prompts/handoff/incoming-model-resumption.md` exists.
- [ ] `prompts/handoff/long-break-resumption.md` exists.

**Issues found:** `[None / list]`

---

## 6. Maintenance Prompt Files

- [ ] `prompts/maintain/quick-patch.md` exists.
- [ ] `prompts/maintain/refactor-planning.md` exists.
- [ ] `prompts/maintain/migration-planning.md` exists.
- [ ] `prompts/maintain/dependency-approval.md` exists.
- [ ] `prompts/maintain/rollback-planning.md` exists.

**Issues found:** `[None / list]`

---

## 7. Required Prompt Sections

- [ ] Every prompt has `## Purpose`.
- [ ] Every prompt has `## When to Use`.
- [ ] Every prompt has `## Mode`.
- [ ] Every prompt has `## Files to Load First`.
- [ ] Every prompt has `## Prompt`.
- [ ] Every prompt has `## Expected Output`.
- [ ] Every prompt has `## Notes`.

**Issues found:** `[None / list]`

---

## 8. Mode Terminology

- [ ] Prompt files use Research Mode, Design Mode, and Develop Mode as public modes.
- [ ] No prompt file refers to Architect Mode as a public mode.
- [ ] No prompt file refers to Builder Mode as a public mode.

**Issues found:** `[None / list]`

---

## 9. Develop Mode Safety

- [ ] `prompts/develop/dry-run.md` requires Permission Level 0 and says not to implement.
- [ ] `prompts/develop/authorization.md` contains the exact dry run approval message.
- [ ] Develop prompts say to modify only approved files.
- [ ] Develop prompts say to update `implementation_log.md` where relevant.
- [ ] Develop prompts do not authorize new dependencies without approval.

**Issues found:** `[None / list]`

---

## 10. Catalog Discoverability

- [ ] `prompts/README.md` links to all 27 prompt files.
- [ ] `docs/prompt-catalog.md` links to the individual prompt files.
- [ ] `README.md` links to the prompt catalog.
- [ ] `starter-kit/blank/PROMPTS.md` points operators to the full prompt catalog or remains intentionally scoped as starter-kit prompts.
- [ ] `PROMPT_CHANGELOG.md` records v0.1.0 prompt creation.

**Issues found:** `[None / list]`

---

## 11. Consistency Audit

- [ ] `planning/sprints/sprint_003/consistency_audit.md` exists.
- [ ] The audit lists every prompt file path from `blueprint.md`.
- [ ] The audit reports no unresolved FAIL items.
- [ ] The audit confirms the maintenance folder path is `prompts/maintain/`.

**Issues found:** `[None / list]`

---

## Sprint 003 Is Complete When

All boxes above are checked, all 27 prompt files exist, all support files are updated, and human review approves the prompt catalog.

---

*ADDF - `planning/sprints/sprint_003/acceptance.md` - Design Mode - 2026-05-31*
