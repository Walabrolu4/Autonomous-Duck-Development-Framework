# Agent Permissions and Special Operations

ADDF Light Games separates **technical capability** from **human authorization**. An installed agent may have filesystem or terminal access, but that does not automatically permit source edits, installing packages or publishing a game.

## When to use

Use when assigning tools to a coding agent, when a plan includes a package install or risky command, or when handling a request involving remote machines and connected services.

## Default permissions

| Capability | May do | Must not do |
| --- | --- | --- |
| Research | Inspect allowed sources, gather facts, propose options | Modify game code or decide material user intent |
| Design | Draft the project brain and sprint plan, record actual human choices | Edit game scenes/assets/tests or run unapproved implementation commands |
| Develop | Make exact approved file operations and run approved commands | Expand scope or self-authorize |
| Coordinator | Route permitted tasks and summarize evidence | Grant Gate D/I/A, assume worker result or background permission |

**Planning Markdown** may be drafted within the user's requested task, subject to `SECURITY.md`. Changes to safety policy that weaken restrictions need explicit human review.

## What Gate I must specify

The plan lists exact paths and operations, shell commands with working directories, expected files, dependency versions/sources, network effects, risks, rollback and tests. A broad “make any necessary changes” scope is invalid.

A **material change** to those elements requires a new plan revision and renewed Gate I.

## Separate high-impact permissions

Require specially explicit approval for:
- deleting substantial data, reset/rebase that might erase unrelated work;
- reading secrets or transferring private code/data externally;
- installing an unknown dependency or downloaded script;
- publishing a game, deployment, branch merge or access-control change;
- purchases, paid APIs, third-party messages, unattended jobs and remote shell tasks.

Even an ordinary authorized `PLAN.md` does not imply these special effects unless they were specifically reviewed.

## Existing-project protections

For existing repositories, inventory instructions and worktree state **read-only** before migration. An install command may change lockfiles or engine project settings. A “helpful cleanup” may delete another person's work. Don't perform either without a reviewed scope and recovery plan.

## Permission check example

A student permits edits to `PlayerController.cs` and the movement test, with a Unity build command. The coding agent discovers it needs a new package or wants to modify the input-actions asset. Those paths and dependencies weren't authorized. It stops, discloses the actual reason, updates the plan and asks again.

Routine variable naming inside an approved C# file does **not** require a separate human decision unless it changes the intended behavior or risk.

## If the agent cannot verify approval

Return to `awaiting_approval` or `paused`, preserving safe work. Do not fabricate a source reference, replay a destructive command, or infer that yesterday's model had valid permission.

## Common failures

**Sandbox = authorization:** It isn't; host permissions are a ceiling, not consent.

**Special effects hidden in build step:** `npm install` or cloud deployment can have network/data side effects. Show them.

**Unattended autonomy by default:** A scheduler or coordinator exists, so the agent keeps working. Require explicit user-controlled schedule/scope first.

## Related

[Security](../quality/security.md) · [Approval gates](../sprints/approvals.md) · [OpenClaw coordination](openclaw.md)
