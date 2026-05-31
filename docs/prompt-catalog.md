# Prompt Catalog

The prompt catalog provides copy-ready operating protocol for each ADDF mode and workflow.

The canonical prompt files live in [`../prompts/`](../prompts/README.md). Each prompt file includes:

- Purpose
- When to use
- Mode
- Files to load first
- Prompt text
- Expected output
- Notes

## Research Prompts

| Prompt | Use |
|---|---|
| [Research Brief](../prompts/research/research-brief.md) | Investigate a bounded research question. |
| [Source Summary](../prompts/research/source-summary.md) | Summarize a source for project relevance. |
| [Tool Comparison](../prompts/research/tool-comparison.md) | Compare tools or approaches before decisions. |
| [Open Questions](../prompts/research/open-questions.md) | Identify unknowns that need tracking. |
| [Risk Discovery](../prompts/research/risk-discovery.md) | Surface project, security, scope, and handoff risks. |

## Design Prompts

| Prompt | Use |
|---|---|
| [Project Initialization](../prompts/design/project-initialization.md) | Create or complete the project brain. |
| [Release Planning](../prompts/design/release-planning.md) | Plan release goals, scope, and sprint breakdown. |
| [Feature Cycle Planning](../prompts/design/feature-cycle.md) | Plan feature research, feasibility, validation, and sprint mapping. |
| [Sprint Pack Generation](../prompts/design/sprint-pack-generation.md) | Generate requirements, blueprint, and acceptance files. |
| [Dry Run Review](../prompts/design/dry-run-review.md) | Review Develop Mode dry runs. |
| [Implementation Review](../prompts/design/implementation-review.md) | Review completed implementation against the sprint pack. |
| [Consistency Audit](../prompts/design/consistency-audit.md) | Audit generated files for consistency. |
| [Documentation Drift Audit](../prompts/design/documentation-drift-audit.md) | Find drift between docs and project memory. |
| [Resumption](../prompts/design/resumption.md) | Resume from files after a session break. |

## Develop Prompts

| Prompt | Use |
|---|---|
| [Dry Run](../prompts/develop/dry-run.md) | Produce `dry_run.md` at Permission Level 0. |
| [Implementation Authorization](../prompts/develop/authorization.md) | Send the exact human authorization message. |
| [Verification Run](../prompts/develop/verification-run.md) | Run approved verification commands. |
| [Implementation Log Update](../prompts/develop/implementation-log-update.md) | Update `implementation_log.md` after approved changes. |
| [Patch Implementation](../prompts/develop/patch-implementation.md) | Apply a small approved patch. |

## Handoff Prompts

| Prompt | Use |
|---|---|
| [Session Checkpoint](../prompts/handoff/session-checkpoint.md) | End a session with durable handoff notes. |
| [Incoming Model Resumption](../prompts/handoff/incoming-model-resumption.md) | Resume as a new model from files. |
| [Long-Break Resumption](../prompts/handoff/long-break-resumption.md) | Resume after a long project break. |

## Maintenance Prompts

| Prompt | Use |
|---|---|
| [Quick Patch](../prompts/maintain/quick-patch.md) | Plan and execute a very small correction. |
| [Refactor Planning](../prompts/maintain/refactor-planning.md) | Plan a supervised refactor. |
| [Migration Planning](../prompts/maintain/migration-planning.md) | Plan a high-risk migration. |
| [Dependency Approval](../prompts/maintain/dependency-approval.md) | Review a dependency before approval. |
| [Rollback Planning](../prompts/maintain/rollback-planning.md) | Plan how to revert risky work. |

## Notes

The maintenance folder is named `prompts/maintain/` to match the v0.1 release scope and `PROMPT_CHANGELOG.md`.

---

[Wiki Home](index.md) - ADDF v3.5
