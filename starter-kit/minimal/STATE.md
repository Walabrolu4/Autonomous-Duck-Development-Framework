# Current Project State

> This is a safe **blank-project initial state**. Do not report code, tests, approvals, active sprints or user playtests that have not actually happened. The agent updates this record whenever verified state changes.

## Identity and state

- project_id: undecided
- active_sprint: none
- lifecycle_stage: research
- sprint_status: discovering
- last_verified_at: unknown

`lifecycle_stage` may be `research`, `design`, `implement`, `refine` or `acceptance`. `sprint_status` may be `discovering`, `designing`, `awaiting_approval`, `implementing`, `refining`, `awaiting_acceptance`, `accepted`, `rejected` or `paused`. Do not advance based only on agent claims.

## Gate evidence

- gate_d: pending
- gate_i: pending
- gate_a: pending

These fields are summaries **only**. A real decision and human approval must be recorded in the appropriate `SPRINT.md`, `PLAN.md` and `REVIEW.md`; a summary value cannot grant permission.

## Active authorization

- plan_revision: none
- scope_reference: none
- authorized: no
- authorized_by: none

`authorized: yes` requires actual human Gate I evidence for the exact current `PLAN.md` revision, operations and commands, with no stale scope or new risk. No code, asset or test writes until then.

## Blockers and unknowns

- Blockers: none.
- Unknowns: game concept, player experience, platform, engine and first milestone.
- Current human commitments: none recorded.
- If paused, record prior safe status and restart preconditions here; never preserve unverified permission.

## Latest verified evidence

- Build/test: not_verified
- Human playtest: not_verified
- Source diff: not_verified
- Deployment: not_verified

Actual command output or human observation belongs in the active sprint's `PLAN.md` or `REVIEW.md` and may be summarized here with a reference.

## Next action

- actor: agent
- action: Ask the human one meaningful question to begin game discovery, or offer two or three buildable game ideas if they have none.

The next action must be a single executable or reviewable step, not a vague “finish game” goal.

## Session handoff

- Mandatory first reads: `SECURITY.md`, `AGENTS.md`, `STATE.md`.
- For project intent: `GAME.md`, `DECISIONS.md`, `planning/BACKLOG.md`.
- Active sprint triplet: none.
- Known safe next action: discovery only; **do not modify game implementation**.
- When resuming: verify branch/worktree, human approval evidence, outstanding commands and blockers. If uncertain, stop or return to `awaiting_approval`.

**Update triggers:** confirmed decision, chosen sprint, lifecycle/status change, authorized plan, actual test evidence, human verdict, blocker or session handoff. No fictional timestamp.
