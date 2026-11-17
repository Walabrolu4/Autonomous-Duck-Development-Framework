# Stage 3 — Implement

Implementation is the **only stage that may actually change game source, tests, scenes, assets or dependencies**, and only while a specific **Gate I** authorization is valid.

## When to use

Use when the human has reviewed the exact current `PLAN.md` revision and expressly permitted its operations. Do not invoke implementation simply because design looks ready, the shell works or a previous chat says “continue.”

## Preconditions

Read `SECURITY.md`, `AGENTS.md`, `STATE.md`, the active `SPRINT.md`, `PLAN.md`, and relevant decisions. Verify:
- active `sprint-NNN` and selected `AC-##`;
- Gate D for meaningful design (or justified not-required);
- plan file revision, exact operations, dependencies and commands;
- **real human approval** of that same revision and scope, with conditions;
- current worktree/source baseline and conflicting human changes;
- special approval for destructive, paid, sensitive, public or other external effects.

Missing proof means **stop**, not reinterpret the plan as authorized.

## Execution sequence

1. Inspect only the approved files and environment; check whether original assumptions still hold.
2. Implement the **smallest change** supporting one acceptance criterion.
3. Execute only approved test/build commands in their specified working directories.
4. Log actual changed paths, command outcomes, failures, versions when known and unexpected behavior.
5. Compare the diff with the approved operation list. Do not assume a green build implies no unauthorized change.
6. Fill the technical sections of `REVIEW.md`; keep human-playtest items `not_tested`.
7. Set an accurate status such as `refining` (defect) or `awaiting_acceptance` (ready for human), consistent with the state machine.

## Scope change = new approval

A newly needed input package, extra script, third-party asset, credential, command, release endpoint or significantly changed gameplay behavior **invalidates** the old Gate I. Stop and present:
- what changed and why;
- exact new paths/commands/dependencies and risks;
- revised `PLAN.md` `rN+1`;
- rollback/protective handling of partial work;
- explicit new authorization question.

Old approval evidence remains in history; it must not be silently rewritten to cover the new scope. Minor fixes **within** the exact approved envelope need not generate repeated gates.

## Example: a fourth source file

Gate I permitted `game.js`, `index.html`, `style.css` and one test file. The agent discovers it needs `audio.js` to add collision feedback. If the agreed outcome can be met with visual feedback in the approved files, use that within scope. If not, stop, explain why `audio.js` is necessary, update the plan and ask for new Gate I. Never quietly create it because it's a “small file.”

## If execution tools are unavailable

Produce proposed edits/commands clearly marked as **not run** and ask the user to perform the verified steps or connect appropriate tooling. Do not claim to have executed a build, produced a local binary or inspected a browser when no such tool result exists.

## Common failures

**Tool permission as consent:** The coding agent has write access to the repository, so it thinks it may modify all files. Gate I is narrower.

**Silent dependency change:** A package manager upgrades versions while installing. Stop and reconcile any material difference.

**Self-acceptance:** Implementation records tests as passed and closes the sprint. Gate A remains human.

## Related

[Technical plan](../sprints/planning.md) · [Approval gates](../sprints/approvals.md) · [Testing](../quality/testing.md)
