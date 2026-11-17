# File-First Handoffs and Safe Resumption

The core ADDF promise is that the **project remains understandable after the chat disappears**. Another model should be able to orient itself from durable project files, test evidence and current source state.

## When to use

Use after a long pause, switching from browser chat to a home coding agent, swapping Claude/Codex, delegating work, or recovering from a crashed terminal session.

## The required resumption order

1. Load `SECURITY.md` first.
2. Load `AGENTS.md` and `STATE.md`.
3. Load `GAME.md`, `DECISIONS.md`, and current backlog as relevant.
4. If `active_sprint` exists, read its `SPRINT.md`, `PLAN.md`, and `REVIEW.md`.
5. Verify current branch/worktree and actual changed files where tools permit.
6. Compare Gate D, Gate I and Gate A records with **real human evidence** and relevant plan/review revisions.
7. Report the last verified stage/status, work completed, tests actually run, blockers and one safe next action.

A remembered “we were approved yesterday” is insufficient when the current `PLAN.md` has changed.

## Handoff packet when coordinating multiple agents

A temporary handoff should contain:
- project/sprint identifier and last verified stage/status;
- requested role (research/design/develop/verify);
- exact safe read files and exclusions;
- permitted writes and commands, or explicit **none**;
- plan revision and real Gate I evidence (or no permission);
- expected verifiable output and stop conditions.

An optional coordinator may format this packet, but cannot approve source changes on the human's behalf. A coding worker should independently verify the same source records.

## Handle uncertain command outcomes

If a remote agent timed out after a build/install/write, **do not blindly retry** a potentially non-idempotent command. Check whether its effects already occurred. Record evidence or label outcome unknown.

The same applies to a Git push, deploy or asset export: the agent's final chat message may be missing even though a tool action succeeded.

## Resumption example

A user opens Codex after designing on a phone. `STATE.md` says `awaiting_approval` for Sprint 002; `PLAN.md` r3 lists two C# scripts and one test. The user never approved r3. Correct Codex behavior: summarize the plan and request Gate I. It can discuss the intended mechanic but cannot silently write the scripts.

If the user later approves r3, the coder can implement only that scope and append truthful evidence for the next review.

## Update the project at session end

Record any real decisions, new blockers, actual changed paths/tests, last valid approval reference and one next action. Do not inject a fictional timestamp if no clock is available. Keep secrets out of state and handoff messages.

## Common failures

**Conversation-only continuity:** All decisions disappear when a model context resets. Write them to files.

**Assumed completion:** Worker says “done,” but actual diff/tests aren't inspected. Verify before reporting success.

**Old gate reused:** Plan changed after approval. Degrade to unapproved and ask again.

## Related

[RESUME prompt](../../prompts/RESUME.md) · [Coordinator playbook](../../integrations/openclaw/COORDINATOR_PLAYBOOK.md) · [Current state](../reference/file-reference.md)
