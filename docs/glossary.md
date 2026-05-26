# Glossary

Canonical definitions for all ADDF framework terms.

---

### ADDF

The **Autonomous Duck Deployment Framework**. A file-first coordination methodology for LLM-assisted software delivery. ADDF separates scale, lifecycle stage, operating mode, and project memory into four explicit decisions before any model acts. The name comes from rubber duck debugging — the practice of explaining a problem clearly enough for a silent listener to "understand" it, which forces the developer to find the flaw in their own reasoning.

---

### Context Engineering

**Context Engineering** is the practice of organizing project context into explicit, scoped, durable files rather than relying on chat thread history. In ADDF, context engineering is embodied by the [Project Brain](project-brain.md) — the set of Markdown files loaded into each AI session.

---

### Design Mode

**Design Mode** is the ADDF operating mode that writes project memory. It covers feasibility analysis, architecture planning, Sprint Pack generation, Dry Run review, retrospectives, and handoff notes. Design Mode may not write source code or mutate implementation files.

> Note: Design Mode was called *Architect Mode* in earlier versions of the framework.

See [Design Mode](modes/design-mode.md).

---

### Develop Mode

**Develop Mode** is the ADDF operating mode that writes code and modifies implementation files. It is the only mode with this permission, and it may not exercise it until a Dry Run has been reviewed and the human has provided explicit authorization.

> Note: Develop Mode was called *Builder Mode* in earlier versions of the framework.

See [Develop Mode](modes/develop-mode.md).

---

### Dry Run

A **Dry Run** is the read-only report that Develop Mode produces at Permission Level 0 before touching any file. It lists every file the model intends to create, modify, move, or delete — plus commands, dependencies, risks, and ambiguities. Implementation begins only after the Dry Run is reviewed and approved.

See [Develop Mode](modes/develop-mode.md), [Sprint Loop](sprint-loop.md).

---

### Feature

A **Feature** is a user-visible or system-visible capability added to an existing project. A feature cycle adds the capability without restarting the full project lifecycle.

See [Feature Cycles](feature-cycles.md), [Work Scale Model](work-scale.md).

---

### Handoff Summary

A **Handoff Summary** is a written continuation record produced by the active AI before a session ends, a model switches, or context limits approach. It captures current goal, mode, active sprint, completed work, files changed, and the next recommended action. An incoming model can orient from the handoff summary and the project brain files without needing the previous chat.

See [Handoff, Resumption & Model Switching](handoff-protocol.md).

---

### Local File Sovereignty

**Local File Sovereignty** is the ADDF principle that the authoritative project state lives in local files — not in model memory, not in chat history, not in a cloud session. The repository is the system of record. The model is temporary compute.

See [Core Concepts](core-concepts.md).

---

### Patch

A **Patch** is a small, low-risk change — a typo fix, a broken link update, a single CSS token correction. A patch does not require the full sprint loop unless it touches logic, dependencies, architecture, or multiple files.

See [Work Scale Model](work-scale.md).

---

### Permission Level

A **Permission Level** is the 0–4 scale that controls how far Develop Mode may reach beyond the approved sprint scope. Level 0 is Dry Run Only. Level 1 is Approved Sprint Scope. Levels 2–4 cover progressively wider changes with progressively stronger justification requirements. The model cannot self-authorize an escalation.

See [Develop Mode Permission Levels](permission-levels.md).

---

### Project Brain

The **Project Brain** is the collection of Markdown files that define the current project truth — mode rules, domain logic, state, decisions, commands, security boundaries, sprint scope, and implementation history. It must be current, explicit, scoped, reviewable, searchable, versioned, and safe to load into an LLM session.

See [The Project Brain](project-brain.md).

---

### Release

A **Release** is a versioned delivery target — a bounded set of features grouped into one shippable unit. A completed release becomes the baseline for the next. The project brain persists across release boundaries.

See [Release Cycles](release-cycles.md), [Work Scale Model](work-scale.md).

---

### Research Mode

**Research Mode** is the ADDF operating mode that investigates and synthesizes information. It gathers evidence, compares options, identifies risks, and names unknowns. It does not make final decisions or write code.

See [Research Mode](modes/research-mode.md).

---

### Sprint

A **Sprint** is a bounded AI implementation packet defined by its artifacts: `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`, `implementation_log.md`, `human_review.md`, `retrospective.md`, and `rollback_log.md`. A sprint is complete when state is updated — not when code compiles.

See [Sprint Loop](sprint-loop.md), [Work Scale Model](work-scale.md).

---

### Sprint Pack

A **Sprint Pack** is the three files that define a sprint's scope and contract: `requirements.md`, `blueprint.md`, and `acceptance.md`. Design Mode generates the Sprint Pack. The human reviews and approves it before any Develop Mode session opens.

See [File Reference](file-reference.md), [Sprint Loop](sprint-loop.md).

---

### Validation Gate

A **Validation Gate** is a decision checkpoint before architecture, sprint planning, or implementation. It asks seven questions: Is the goal clear? Is the target user clear? Is scope bounded? Are security boundaries known? Are high-risk assumptions visible? Are open questions acceptable or resolved? Is the preferred approach explicit? Human approval is required to pass the gate.

See [Lifecycle — Validation Gate](lifecycle/index.md#validation-gate).

---

### Work Scale

**Work Scale** is the explicit classification of how large a unit of work is before it runs. The five scales are Project, Release, Feature, Sprint, and Patch. Scale determines process depth — the wrong process for the wrong scale produces either unnecessary overhead or dangerous underprotection.

See [Work Scale Model](work-scale.md).

---

**Rule:** Framework terms use canonical capitalization. Capitalization matters.

---

[← Wiki Home](index.md) · ADDF v3.5

*Quack!*
