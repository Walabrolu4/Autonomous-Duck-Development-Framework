# Sprint 003 - Blueprint

**Sprint:** 003  
**Title:** Prompt Catalog  
**Mode:** Design Mode  
**Primary reference:** `planning/sprints/sprint_003/requirements.md`

This blueprint lists every file to create or modify in Sprint 003. No file outside this list may be changed without updating the sprint pack first.

---

## Order of Operations

1. Create the prompt catalog folder structure.
2. Create `prompts/README.md`.
3. Create prompt files in this order: research, design, develop, handoff, maintain.
4. Update supporting documentation and project memory.
5. Run a consistency audit for prompt paths, prompt sections, mode names, and dry run enforcement.
6. Produce sprint close artifacts after implementation and review.

---

## Files to Create - Catalog Index

| # | File | Purpose |
|---:|---|---|
| 1 | `prompts/README.md` | Prompt catalog index with category descriptions, usage instructions, version 0.1.0, and links to every prompt file. |

## Files to Create - Research Prompts

| # | File | Prompt name |
|---:|---|---|
| 2 | `prompts/research/research-brief.md` | Research Brief |
| 3 | `prompts/research/source-summary.md` | Source Summary |
| 4 | `prompts/research/tool-comparison.md` | Tool Comparison |
| 5 | `prompts/research/open-questions.md` | Open Questions |
| 6 | `prompts/research/risk-discovery.md` | Risk Discovery |

## Files to Create - Design Prompts

| # | File | Prompt name |
|---:|---|---|
| 7 | `prompts/design/project-initialization.md` | Project Initialization |
| 8 | `prompts/design/release-planning.md` | Release Planning |
| 9 | `prompts/design/feature-cycle.md` | Feature Cycle Planning |
| 10 | `prompts/design/sprint-pack-generation.md` | Sprint Pack Generation |
| 11 | `prompts/design/dry-run-review.md` | Dry Run Review |
| 12 | `prompts/design/implementation-review.md` | Implementation Review |
| 13 | `prompts/design/consistency-audit.md` | Consistency Audit |
| 14 | `prompts/design/documentation-drift-audit.md` | Documentation Drift Audit |
| 15 | `prompts/design/resumption.md` | Resumption |

## Files to Create - Develop Prompts

| # | File | Prompt name |
|---:|---|---|
| 16 | `prompts/develop/dry-run.md` | Dry Run |
| 17 | `prompts/develop/authorization.md` | Implementation Authorization |
| 18 | `prompts/develop/verification-run.md` | Verification Run |
| 19 | `prompts/develop/implementation-log-update.md` | Implementation Log Update |
| 20 | `prompts/develop/patch-implementation.md` | Patch Implementation |

## Files to Create - Handoff Prompts

| # | File | Prompt name |
|---:|---|---|
| 21 | `prompts/handoff/session-checkpoint.md` | Session Checkpoint |
| 22 | `prompts/handoff/incoming-model-resumption.md` | Incoming Model Resumption |
| 23 | `prompts/handoff/long-break-resumption.md` | Long-Break Resumption |

## Files to Create - Maintenance Prompts

| # | File | Prompt name |
|---:|---|---|
| 24 | `prompts/maintain/quick-patch.md` | Quick Patch |
| 25 | `prompts/maintain/refactor-planning.md` | Refactor Planning |
| 26 | `prompts/maintain/migration-planning.md` | Migration Planning |
| 27 | `prompts/maintain/dependency-approval.md` | Dependency Approval |
| 28 | `prompts/maintain/rollback-planning.md` | Rollback Planning |

---

## Files to Modify

| File | Change | Reason |
|---|---|---|
| `README.md` | Add or update a link to the prompt catalog. | Requirements section 11 says the prompt catalog must be discoverable. |
| `docs/prompt-catalog.md` | Replace the seed inline catalog with links and summaries for the 27 individual prompt files. | Documentation should point to the canonical prompt files. |
| `PROMPT_CHANGELOG.md` | Mark v0.1.0 prompt catalog as created and list exact prompt paths. | Public prompt version history must match actual files. |
| `planning/releases/v0.1/release_plan.md` | Update Sprint 003 status during closeout. | Release tracking must reflect prompt catalog progress. |
| `planning/backlog.md` | Update Sprint 003 status and branch. | Sprint lifecycle tracking. |
| `STATE.md` | Update current status and next step during sprint work and closeout. | Project memory must remain current. |
| `starter-kit/blank/PROMPTS.md` | Add a pointer to the full `prompts/` catalog if needed after prompt files exist. | The prompt catalog must be available from the starter kit. |

---

## Files Not in Scope

| File or area | Reason |
|---|---|
| `website/` | Website prompt pages are v0.2 work. |
| Release ZIP files | Packaging is Sprint 009 work. |
| `tools/` | CLI work is v0.3. |
| Source code files | Sprint 003 is Markdown-only. |
| `examples/mini-task-tracker/` | Standalone example project is Sprint 007. |

---

## Required Prompt File Rules

Every prompt file must contain:

1. `# Prompt Name`
2. `## Purpose`
3. `## When to Use`
4. `## Mode`
5. `## Files to Load First`
6. `## Prompt`
7. `## Expected Output`
8. `## Notes`

Every prompt must use only these public mode names:

- Research Mode
- Design Mode
- Develop Mode

Develop prompts must include the dry run boundary where relevant. The authorization prompt must include the exact authorization message:

```text
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

---

## Consistency Audit Requirements

The consistency audit must check that all exact paths listed above exist, every prompt contains the required section headings, every prompt declares its mode, no prompt uses deprecated public mode names, and the maintenance folder path is consistently `prompts/maintain/`.

---

*ADDF - `planning/sprints/sprint_003/blueprint.md` - Design Mode - 2026-05-31*
