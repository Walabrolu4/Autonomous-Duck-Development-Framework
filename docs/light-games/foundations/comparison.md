# ADDF Light Games vs. Original ADDF

This comparison is a **conceptual comparison of the current original ADDF v3.5 framework and the ADDF Light Games branch**, not a suggestion to overwrite or automatically merge them. The original repository's `main` branch remains the canonical full ADDF edition.

## When to use

Consult this before choosing a methodology, explaining the game-focused adaptation, adopting Light in an existing full-ADDF project, or deciding whether to add more governance.

## Side-by-side comparison

| Dimension | Original ADDF (v3.5) | ADDF Light Games |
| --- | --- | --- |
| **Primary domain** | General LLM-assisted software development | Games and interactive playable experiences |
| **Intended user** | Operators comfortable with a detailed, auditable engineering process | Solo makers, students, designers and small game teams seeking low-friction guidance |
| **Design goal** | Formal file-backed control across complex lifecycle and work scale | Preserve control while minimizing the *user's* process burden |
| **Public lifecycle** | Eight steps: Research; Design & Feasibility; Validation Gate; Architecture; Sprint Planning; Build & Test; Review & Reflection; Deploy/Maintain/Resume | Five stages: Research; Design/Ideation; Implement; Refine; Acceptance |
| **Operating boundaries** | Explicit Research Mode, Design Mode, Develop Mode | Same three distinct *capabilities*, with five player-facing lifecycle stages |
| **Sprint workflow** | Eleven-step controlled Sprint Loop, including dry run and several human checks | One bounded iteration with three human gates, plus scope-aware refinement |
| **Default project memory** | `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `COMMANDS.md`, `SECURITY.md` and additional decision/question/risk/style files | Six persistent files: `AGENTS.md`, `SECURITY.md`, `GAME.md`, `STATE.md`, `DECISIONS.md`, `planning/BACKLOG.md` |
| **Game intent** | General domain is documented in `DOMAIN.md` | Player experience, core loop, design pillars and playable hypothesis in `GAME.md` |
| **Sprint documents** | Typically separate `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`, implementation log, human review and retrospective | Three files: `SPRINT.md`, `PLAN.md`, `REVIEW.md` |
| **Research handling** | Dedicated research files, questions and risk tracking | Focused active sprint research; larger studies are optional |
| **Human design control** | Explicit validation/blueprint and design review | **Gate D** for consequential direction and acceptance criteria |
| **Code authorization** | Develop Mode starts with Permission Level 0 dry run and specific human authorization | **Gate I**, tied to exact plan revision, paths, commands, dependencies and side effects |
| **Outcome acceptance** | Human review, approval and retrospective within sprint governance | **Gate A**, requiring actual human gameplay/review; tests alone do not count |
| **Permission detail** | Formal Develop Mode permission levels and scale model | Core safe boundaries plus separate special approvals; advanced controls optional |
| **Onboarding** | Copy full blank starter kit and initialize more project-memory files | Copy six files or adopt an existing repo read-only; choose first sprint later |
| **User questioning** | Formal research/design workflows | Guided discovery: one consequential question at a time by default |
| **Learning focus** | Engineering rigor, repeatability and auditability | Those goals **plus explicit game-design learning and playtest predictions** |
| **Example deliverable** | General mini-task-tracker example and engineering artifacts | Dependency-free browser Duck Dodge pilot with real tests, plus onboarding/adoption exercises |
| **Model integrations** | Model-agnostic prompt catalog | Nine lifecycle prompts and optional Claude Code, Codex, OpenClaw skill adapters |
| **Automated validation** | Full-ADDF checklists and governance procedures | Python structural validator and branch-only CI; warns that human consent cannot be authenticated |
| **Documentation depth** | Extensive wiki and long consolidated reference | Extensive dedicated wiki and generated single-document manual, **without forcing every chapter into normal workflow** |
| **Suitable scale** | Broad work, multi-team delivery, governance-heavy/high-risk projects | Prototypes, learning, smaller game projects and bounded playable feature increments |
| **Relationship** | Independent canonical edition on `main` | Separate branch `ADDF_light_games`; **not** an automatic merge or replacement |

Original ADDF itself is adaptable to work scale. It is inaccurate to say it *always* requires every optional file for the smallest patch. The distinction here is that Light **codifies** a tiny default runtime around game-playable evidence.

## What is deliberately preserved?

Both editions require durable project memory, role-aware write boundaries, a dry-run before changing implementation, explicit human authorization, honest test evidence and resumable handoffs. Light is **not a permissionless mode**.

## What is deliberately reduced?

Light consolidates sprint artifacts and keeps optional risk, architecture, asset, feature and release records out of the first-time template. Rather than a complete project brief, it can start from one sentence and expand only after decisions are made.

That consolidation is a *navigation decision*, not permission to omit scope, source provenance, rollback, review history or security constraints.

## Choosing an edition

Use **Light Games** if the immediate goal is to explore and validate playable behavior with a small team, to teach game mechanic/system/level design, or to build an incremental game prototype. Choose **original ADDF** when delivery requires detailed formal architecture, richer cross-team release governance, multiple risk tracks, or explicitly managed permission tiers.

A real existing project can migrate only via an **audited, human-approved mapping**; do not blindly rename its `DOMAIN.md` to `GAME.md` or delete historic sprint records.

## References and verification

Original ADDF evidence: [main README](https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/blob/main/README.md), [original lifecycle](https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/blob/main/docs/lifecycle/index.md), [original sprint loop](https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/blob/main/docs/sprint-loop.md), [original starter kit](https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/blob/main/starter-kit/README.md). Light contracts: [framework specification](../../../spec/FRAMEWORK_SPEC.md), [architecture](../../../spec/REPOSITORY_ARCHITECTURE.md), [sprint file contracts](../../../spec/SPRINT_FILE_CONTRACTS.md).

## Related

[File reference](../reference/file-reference.md) · [Existing-project adoption](../guides/existing-project.md) · [Philosophy](philosophy.md)
