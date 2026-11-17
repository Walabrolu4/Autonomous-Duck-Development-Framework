# Optional OpenClaw Coordination

OpenClaw is an **optional coordinator** for scheduling or routing AI tasks in a trusted workspace. ADDF Light Games does **not** require OpenClaw, and installing a skill does not provision a remote development machine, messaging channel or unattended task.

## When to use

Use when multiple agents or devices need coordinated research, planning, coding and review. Avoid introducing a coordinator for a small single-agent game prototype unless it genuinely reduces friction.

## What a coordinator may do

A properly configured coordinator can read permitted project-brain files, ask human design questions, delegate safe research, prepare scope proposals and aggregate **actual** worker evidence. It must not treat its own assignment as a human approval.

The project's `SECURITY.md`, `AGENTS.md`, current `PLAN.md` and actual human gate responses remain authoritative.

## Installation boundary

The Stage 4 adapter includes `integrations/openclaw/skills/addf-light-games/SKILL.md`. It is intended to be copied deliberately to an OpenClaw workspace skill path, for example:

```text
<workspace>/skills/addf-light-games/SKILL.md
```

Workspace location and tool availability vary. Confirm the installed version, exact paths, permissions and credential isolation. Do not automatically enable remote shell, continuous background tasks, cron, public deployment or messaging channels.

## Safe delegation packet

Before asking a coding worker to act, specify:
- game project and active `sprint-NNN`;
- verified stage/status;
- exact safe read files;
- exact permitted write paths/operations;
- approved commands, directories, dependency list and risk boundaries;
- current Gate I revision **and real human source reference**;
- expected output/test evidence;
- stop conditions for uncertain state or scope changes.

The coding worker must **verify Gate I independently**. If the coordinator requests “finish the game” with no approved plan, the worker refuses implementation.

## Multi-machine caution

A school-browser conversation and a home PC may have different files, repositories, authentication and clocks. A skill does not bridge them automatically. Use explicitly authorized trusted transport, verify the correct branch and exact source state, and avoid sending private code or tokens to an unknown worker.

If a remote command times out, its outcome is **unknown** until checked. Don't blindly rerun a deploy, install or destructive operation.

## Example

The user approves `PLAN.md` r2 for two Phaser source files and a test command. OpenClaw delegates exactly those operations to a coding worker, which reports changed-file diffs and actual test results. The coordinator may summarize them and request a human playtest. It **cannot** grant Gate A. A request for a new library triggers r3 and fresh human Gate I.

## Common failures

**Always-on by default:** Automatically schedule work without an explicit user-controlled scope. Leave it manual until separately authorized.

**Coordinator self-approves:** A model-to-model message substitutes for Gate I. Reject.

**Fabricated remote status:** Worker stops responding, coordinator says success. Verify actual artifact.

## Related

[OpenClaw adapter](../../integrations/openclaw/README.md) · [Coordinator playbook](../../integrations/openclaw/COORDINATOR_PLAYBOOK.md) · [Permissions](permissions.md)
