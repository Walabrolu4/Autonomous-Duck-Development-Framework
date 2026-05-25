[Home](index.md)

# Complete Example: Mini Task Tracker

This page walks a real project through all 8 lifecycle steps. The project is intentionally small so the entire loop is visible from beginning to end. If you prefer learning by example rather than by reference, start here.

---

## The Project

Mini Task Tracker is a simple local-only web app. A user can add tasks, mark them complete, and have their tasks persist across page refreshes. No user accounts. No cloud sync. No collaboration features.

---

## Step 1 — Research & Architecture

Before any code is written, you write the business rules. The completed `DOMAIN.md` for this project:

```markdown
# DOMAIN.md Business Logic and Definitions

## Project Overview
Mini Task Tracker is a local-only task management app for a single user.
It helps a user record small tasks and mark them complete.

## Core Entities

### Task
Definition: A single item the user wants to complete.
Key fields: id, title, status, createdAt, completedAt.
Business rules:
- A task title cannot be empty. Empty-title submissions must be rejected.
- A completed task can be reopened (status reverts to "active").
- Tasks are stored in browser localStorage.
What it is NOT: A shared task, a cloud record, a calendar event, or a reminder.

## Workflows

### Add a Task
1. User types a title and submits.
2. A new Task is created with status "active" and the current timestamp.
3. Task is saved to localStorage and appears in the list immediately.
Edge case: If the title is empty or whitespace-only, reject the submission
with a visible error message. Do not create the task.

### Complete a Task
1. User clicks a task's complete button.
2. Task status changes to "completed". completedAt is recorded.
3. Task remains visible in the list.
Edge case: Clicking complete on a completed task reopens it
(status → "active", completedAt cleared).

## Out of Scope
- User accounts or authentication
- Multi-device sync
- Email or push notifications
- Team sharing or collaboration
- Cloud storage of any kind
```

You run the [Project Kickoff Interview](prompts.md#kickoff-interview) with this `DOMAIN.md` and your raw notes. The Architect asks clarifying questions — framework choice, persistence approach, browser targets — then produces a draft `STATE.md`, `STYLE_GUIDE.md`, `docs/architecture.md`, and starter ledgers for `DECISIONS.md`, `QUESTIONS.md`, and `RISKS.md`.

---

## Step 2 — Initial Development

You ask the Architect to generate the Sprint 001 pack. Sprint goal: build the core task list — add, display, complete, and persist tasks.

The Architect produces:
- **`requirements.md`** — The user can add a task with a non-empty title. Tasks appear in a list immediately. The user can mark a task complete. Completed tasks can be reopened. Tasks persist after browser refresh. No other features this sprint.
- **`blueprint.md`** — Three components: `TaskForm`, `TaskList`, and a `localStorage` helper module. Files to create: `src/components/TaskForm.tsx`, `src/components/TaskList.tsx`, `src/utils/storage.ts`.
- **`acceptance.md`** — See [Sprint 001 Acceptance Criteria (Full)](#sprint-001-acceptance-criteria-full) below.

You review the blueprint, verify each Architect assumption at the bottom of `blueprint.md`. No blockers. You create the sprint branch: `git checkout -b sprint/001-core-task-list`.

The full 10-step [Sprint Workflow](sprint-workflow.md) runs from here.

---

## Step 3 — Testing

Before the Builder writes any implementation code, `acceptance.md` already defines what done means. The Builder is required to write unit tests before functional code.

Why write tests before code? Because the most common failure in AI-assisted development is building first and checking visually after. If acceptance criteria are not written down, the AI declares success when the UI looks right — even if the underlying logic is broken. The checklist in `acceptance.md` is the actual definition of done, not a visual inspection.

---

## Step 4 — Documentation

After Sprint 001, you record the structural decision in `DECISIONS.md`:

```markdown
## Decision 001: localStorage for persistence
Date: 2026-01-15
Status: Accepted
Type: Data Model
Context: The app needs to persist tasks across browser refreshes without a backend.
Decision: Use browser localStorage for version 1.
Tradeoffs: localStorage is limited to approximately 5MB and is not synced across
devices. This is acceptable because the app is explicitly single-device
(see DOMAIN.md Out of Scope). Cloud sync is deferred to a future version.
```

This entry is permanent. If a future sprint proposes cloud sync, the Architect will find this record and understand the original reasoning. No decision is made in a vacuum — the ADR records why.

---

## Step 5 — Full-Scale Development

Sprint 002 adds task filters (All, Active, Completed). Sprint 003 adds the ability to edit a task title. Each sprint follows the same loop: Architect generates the pack, Builder runs the dry run, you approve, Builder implements, you verify, context resets.

Every third sprint, you run the [Cross-Sprint Consistency Audit](prompts.md#consistency-audit) to check that the codebase still matches what `DOMAIN.md` says. This catches drift early, before it becomes a larger problem.

---

## Step 6 — Reflection Loop

After Sprint 002, the Builder created a task with an empty title when the user triggered form submission via a keyboard shortcut. This was a gap in the acceptance criteria — the check only covered button clicks, not keyboard events.

You record it in `retrospective.md` and add a new constraint to `AGENTS.md`:

```markdown
## Additional Builder Constraints (added Sprint 002 retrospective)
- Always validate non-empty, non-whitespace title before task creation,
  regardless of how form submission was triggered.
```

This constraint is now permanent. Every future Builder session reads it. The lesson converts from a one-time failure into a guardrail.

---

## Step 7 — Deployment

You run `npm run build`. You add the build command and a rollback command to `COMMANDS.md` before pushing to production. Rollback must exist before deployment — not after.

Two weeks later, a user reports a typo in the empty-state message. You fix it as a [Mode 1 Quick Patch](modes/quick-patch.md) — a single-line change, no sprint pack required, Builder works directly on the `dev` branch.

---

## Step 8 — Resumption

Three weeks later, you return to the project. You open a fresh Architect session. You load `STATE.md`, `DOMAIN.md`, and `AGENTS.md`. You run the [Resumption Prompt](prompts.md#resumption):

```
Execute Resumption Protocol.
Loaded: STATE.md, DOMAIN.md, AGENTS.md.
Summarize:
1. Current project goal
2. Active sprint or paused status
3. Known blockers
4. Last completed step
5. Next safest action
6. Files to load before the next Builder session
```

The Architect reads the files and tells you exactly where you left off and what to do next. Because the project memory lives in files — not in AI memory — nothing was lost during the three-week break. The cost of resumption: two minutes.

---

## Sprint 001 Acceptance Criteria (Full)

```markdown
# Sprint 001 Acceptance Criteria
All items must be checked before this sprint is considered complete.

## Functional Criteria
- [ ] User can type a task title and submit it.
- [ ] An empty or whitespace-only title is rejected with a visible error message.
- [ ] Newly added tasks appear in the list immediately.
- [ ] User can mark a task complete. Completed state is visually distinct.
- [ ] A completed task can be reopened.
- [ ] Tasks persist after browser refresh (localStorage).

## Technical Criteria
- [ ] No TypeScript type errors.
- [ ] Build completes successfully.
- [ ] Unit tests written and passing.
- [ ] Test results pasted into implementation_log.md.

## Verification Commands (run in order)
1. npm run test
2. npm run build
3. npm run lint
```

## See Also

- [Getting Started](getting-started.md)
- [The 8-Step Lifecycle](lifecycle/index.md)
- [DOMAIN.md](file-reference/domain.md)
