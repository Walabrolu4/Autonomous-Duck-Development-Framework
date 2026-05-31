# DOMAIN.md - Mini Task Tracker

## 1. Project Identity

| Field | Value |
|---|---|
| Full name | Mini Task Tracker |
| Short name | MTT |
| Type | Local-only web app |
| Primary principle | Single operator task management with localStorage persistence |
| Framework version | 3.5 |
| Requirements document | `planning/sprints/sprint_001/requirements.md` |

## 2. What This Project Is

- A browser-based task list for one operator.
- A local-only app with no backend.
- A small v0.1 app for adding, completing, reopening, and persisting tasks.
- A project that stores tasks in `localStorage`.
- A practical example of ADDF on a small implementation sprint.

## 3. What This Project Is Not

- A multi-user task manager.
- A server-backed application.
- A shared team workspace.
- A mobile app.

## 4. v0.1 Scope

### In Scope

- Add a task.
- Mark a task complete.
- Reopen a completed task.
- Persist tasks to `localStorage`.
- View all tasks.

### Out of Scope

| Item | Target Release |
|---|---|
| User accounts | Not planned |
| Server storage | Not planned |
| Sharing | Not planned |
| Notifications | Not planned |
| Mobile app | Not planned |

**Rule:** Do not automate a structure that has not stabilized.

## 5. Target Operators

| Operator type | Primary need |
|---|---|
| Solo developer | Track a small personal task list in one browser. |

## 6. Core Framework Concepts

| Concept | Meaning |
|---|---|
| Work scale model | Project -> Release -> Feature -> Sprint -> Patch. |
| 3 modes | Research Mode investigates, Design Mode writes project memory, Develop Mode modifies implementation files after dry run approval. |
| 8-step lifecycle | Research; design and feasibility; validation; architecture; sprint planning; build and test; review and reflection; deploy, maintain, or resume. |
| Sprint loop | Plan, review, dry run, approve, build, test, review, close. |
| Project brain | The Markdown files that hold project truth between AI sessions. |

## 7. Key Entities and Terminology

| Term | Definition |
|---|---|
| Task | A single work item with id, title, status, and created_at fields. |
| TaskList | The array of Task records stored in `localStorage`. |
| Complete | The status used when a task is finished. |
| Reopen | The action that returns a completed task to open status. |
| Operator | The single person using the app. |

## 8. File Naming

Use lowercase file names for app files, `UPPER_SNAKE_CASE.md` for project brain files, `sprint_NNN` for sprint folders, and `lowercase_snake.md` for sprint files.

## 9. Domain Rules

1. Tasks persist in `localStorage`.
2. Mini Task Tracker has no backend in v0.1.
3. Completed tasks can be reopened.
4. Task titles are required.
5. v0.1 serves one operator only.

---

Mini Task Tracker - DOMAIN.md - ADDF 3.5
