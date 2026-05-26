# ADDF and Agile

ADDF borrows useful language from Agile. It is not Scrum.

## Table of contents

1. [What ADDF uses from Agile](#what-addf-uses-from-agile)
2. [What ADDF does not require](#what-addf-does-not-require)
3. [Sprint definition in ADDF](#sprint-definition-in-addf)
4. [Term mapping](#term-mapping)

---

## What ADDF uses from Agile

ADDF uses these Agile concepts without modification:

- **Backlog** — a `planning/backlog.md` file that holds work items not yet assigned to a sprint or feature cycle.
- **Sprint** — a bounded implementation unit (though defined differently — see below).
- **Acceptance criteria** — `acceptance.md` defines what counts as done for each sprint.
- **Review** — Design Mode and human review happen after every sprint.
- **Retrospective** — `retrospective.md` captures lessons and constraints from every sprint.
- **Release** — a versioned delivery target, tracked in `planning/releases/`.
- **Iteration** — the framework is explicitly recursive; the lifecycle repeats at every scale.

**Rule:** Use Agile language where it clarifies. Do not import Scrum ceremony.

---

## What ADDF does not require

ADDF deliberately omits these Scrum requirements:

- Scrum Master — there is no required facilitator role.
- Product Owner — the human operator fills this function informally.
- Daily standups — ADDF has no time-based ceremonies.
- Story points — work is scoped by artifacts, not by estimation units.
- Velocity tracking — ADDF does not measure throughput.
- Ceremony cadence — no required meetings, no sprint planning sessions, no sprint reviews on a calendar.
- Two-week sprint duration — a sprint ends when the work is done and state is updated, not when a timer expires.

---

## Sprint definition in ADDF

In Scrum, a sprint is a fixed-length timebox — typically two weeks.

In ADDF, a sprint is a **bounded AI implementation packet** defined by its artifacts:

```
requirements.md
blueprint.md
acceptance.md
dry_run.md
implementation_log.md
human_review.md
retrospective.md
rollback_log.md
```

A sprint is complete when all eight files exist, the implementation has passed human review, and `STATE.md` reflects the current state. Duration is irrelevant.

---

## Term mapping

| Agile / Scrum term | ADDF equivalent |
|---|---|
| Product | Project |
| Release | Release Cycle |
| Epic | Major Feature Group |
| User Story | Feature Brief / `requirements.md` entry |
| Sprint | AI Implementation Packet |
| Acceptance Criteria | `acceptance.md` |
| Backlog | `planning/backlog.md` |
| Sprint Review | Design Review + Human Review |
| Retrospective | `retrospective.md` |
| Definition of Done | `acceptance.md` + `human_review.md` |
| Product Owner | Human Operator |
| Development Team | Develop Mode + Human |
| Scrum Master | Not required |

**Rule:** Use Agile language where it clarifies. Do not import Scrum ceremony.

---

[← Wiki Home](index.md) · ADDF v3.5
