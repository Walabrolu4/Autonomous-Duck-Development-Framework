# Sprint 003 - Requirements

**Sprint:** 003  
**Title:** Prompt Catalog  
**Release:** v0.1 Public Proof  
**Mode:** Design Mode  
**Branch:** `sprint/003-prompt-catalog`  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md` section 11

---

## Sprint Goal

Create the v0.1 ADDF prompt catalog as copy-ready Markdown prompts grouped by operating workflow.

The prompt catalog must give operators session-opening and workflow prompts they can copy into any LLM session. Every prompt must be usable without reading the chat history, must declare its mode, must list files to load, and must define expected output.

---

## Context

Sprint 002 produced the starter kit. Sprint 003 produces the prompt catalog that operators will use with that starter kit.

Requirements section 11 defines five prompt categories:

- Research Prompts
- Design Prompts
- Develop Prompts
- Handoff / Resumption Prompts
- Maintenance Prompts

The v0.1 release scope and `PROMPT_CHANGELOG.md` use `prompts/maintain/` as the exact path for maintenance prompts. Sprint 003 follows that existing project memory.

---

## In Scope

Create all 27 required prompt files from requirements section 11:

| Category | Count | Folder |
|---|---:|---|
| Research prompts | 5 | `prompts/research/` |
| Design prompts | 9 | `prompts/design/` |
| Develop prompts | 5 | `prompts/develop/` |
| Handoff prompts | 3 | `prompts/handoff/` |
| Maintenance prompts | 5 | `prompts/maintain/` |

Each prompt file must include these sections exactly:

```md
# Prompt Name

## Purpose

## When to Use

## Mode

## Files to Load First

## Prompt

## Expected Output

## Notes
```

Supporting files are also in scope:

- `prompts/README.md`
- `docs/prompt-catalog.md`
- `README.md`
- `PROMPT_CHANGELOG.md`
- `planning/releases/v0.1/release_plan.md`
- `planning/backlog.md`
- `STATE.md`
- `starter-kit/blank/PROMPTS.md`, only if needed to point operators to the full prompt catalog.

---

## Out of Scope

| Item | Reason |
|---|---|
| Website prompt catalog pages | Website work belongs to v0.2. |
| Prompt catalog ZIP packaging | Release packaging belongs to Sprint 009. |
| Full manual PDF updates | Release packaging belongs to Sprint 009. |
| Source code, scripts, or tests | Sprint 003 is Markdown-only Design Mode work. |
| Changes to the three public ADDF modes | Mode terminology is already settled. |
| New dependencies or external tools | Prompt files require no dependencies. |

---

## Constraints

1. The blueprint must list every prompt file by exact path.
2. Every prompt file must include the required section headings from requirements section 11.4.
3. Prompts must use Research Mode, Design Mode, and Develop Mode only.
4. No prompt may refer to Architect Mode or Builder Mode as public ADDF modes.
5. Develop prompts must enforce dry run before implementation.
6. Prompts must load project files as context, not depend on chat memory.
7. Prompts must not request secrets, credentials, tokens, or private infrastructure details.
8. Prompts must be directly usable by an operator after filling bracketed placeholders.

---

## Success Criteria

See `planning/sprints/sprint_003/acceptance.md`.

Sprint 003 is complete when all 27 prompt files exist at the exact paths listed in `blueprint.md`, support files are updated, and human review confirms the prompt catalog is complete and consistent.

---

*ADDF - `planning/sprints/sprint_003/requirements.md` - Design Mode - 2026-05-31*
