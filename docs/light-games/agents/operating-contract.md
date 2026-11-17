# The Agent Operating Contract

`AGENTS.md` is the standing instruction file for **the individual game project**. It defines how an assistant should read context, write project records, protect permissions and hand off work. Tool access alone never overrides it.

## When to use

Read before allowing any agent to work in a game repository, when a provider adapter conflicts with local instructions, or when an agent has lost context.

## Session startup

An agent should:
1. read `SECURITY.md` **before** arbitrary file discovery;
2. read `AGENTS.md` and `STATE.md`;
3. load only relevant `GAME.md`, `DECISIONS.md`, backlog and active sprint files;
4. verify actual worktree/branch and last known gate evidence where tools permit;
5. state the current **verified** status, uncertainties and one safe next action.

A prior model's summary is a clue, not permission to resume an unapproved command.

## Research, Design, Develop capabilities

Research gathers evidence and may prepare research notes in allowed documentation. It does not change game code, scenes, tests or assets.

Design drafts game intent, decision options, `SPRINT.md`, `PLAN.md` and relevant project memory. It does not change implementation files.

Develop is the only capability that may modify game implementation, and **only** within a human-approved Gate I revision/scope. This applies even when the user-facing stage is “Refine.”

One model may move between capabilities, but it must respect their boundaries.

## One-model versus many-agent setup

A solo coding agent can perform all planning and authorized implementation with the same files. A coordinator plus specialist workers can divide research, design, coding and verification, but **delegation does not convey approval**. A worker must verify Gate I itself before writing.

Provider-specific skills are thin adapters. They should not become separate competing sources of project authority.

## Required output behavior

An agent should distinguish:
- what it actually observed or executed;
- what it inferred or proposes;
- which files it changed and which approval allows them;
- which tests ran and which remain unverified;
- what requires the next human decision.

It should not claim a GitHub commit, playable build or passing test absent tool evidence.

## Example

A Codex agent is told, “Continue the duck game.” It opens `STATE.md` and finds `awaiting_approval`, `PLAN.md` r2, but the only human consent points to r1. Correct behavior: report the stale plan and ask for renewed Gate I, **not** start implementing r2 because the user's broad message said continue.

## Common failures

**Provider priority confusion:** A tool's instruction suggests broad edits that conflict with project security. Stop and reconcile.

**Chat as memory:** The agent never updates `STATE.md`. Record durable facts before handoff.

**Self-assigned authority:** A coordinator claims it approved a worker. Only actual human Gate D/I/A applies.

## Related

[Permissions](permissions.md) · [Handoffs](handoff.md) · [File reference](../reference/file-reference.md)
