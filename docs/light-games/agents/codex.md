# Codex Integration

Codex can work with a game repository's `AGENTS.md` and an optional project-level ADDF Light Games skill. The **methodology is the project files and human gates**, not a model menu or a sandbox toggle.

## When to use

Use when working on local Git-controlled game code with Codex, especially for small bounded mechanics, testable fixes and cross-session continuation.

## Installation

Copy the Stage 4 Codex skill from `integrations/codex/skills/addf-light-games/SKILL.md` to your **game repository** at:

```text
.agents/skills/addf-light-games/SKILL.md
```

Do not overwrite an existing skill or root `AGENTS.md` without a reviewed merge. Avoid creating tool configuration or loosening sandbox/network settings merely to make the skill work.

## Expected session behavior

1. Read `SECURITY.md`, `AGENTS.md`, `STATE.md` and the active sprint as necessary.
2. Identify the current approved plan revision, actual human Gate I and permitted operations/commands.
3. If coding is authorized, work on only those files; run only approved commands.
4. If a new dependency, file or risk appears, **stop and re-plan**.
5. Log actual tests and leave human playtesting/Gate A pending.
6. On resumption, verify worktree and approvals rather than blindly continuing an interrupted tool call.

## Example: a Godot fix

The user approved one script to fix camera movement plus a known test command. Codex notices an imported asset needs reconfiguration. That asset isn't in the plan. Correct behavior: present the exact asset and reason, revise `PLAN.md`, and ask for renewed Gate I before editing it.

The coder can still choose ordinary T0 variable names inside the approved script.

## Smoke test checklist

- Installed skill discovered in actual Codex version.
- Blank-project discovery does not create source files.
- Design-only approval does not trigger code writes.
- Plan scope change produces a stop/re-approval.
- Test output is real and human acceptance remains pending.
- New model resumes from durable state.

Stage 4 created the skill file; live Codex host validation remains a **separate outstanding test**.

## Common failures

**Sandbox means approval:** Technical tools being available doesn't authorize unplanned file edits.

**No Git baseline:** The agent overwrites unrelated changes. Inspect current state before source work.

**Chat-only approval:** An old assistant says permission exists but no current source confirms it. Fail closed.

## Related

[Codex adapter guide](../../integrations/codex/README.md) · [File-first resumption](handoff.md) · [Approval gates](../sprints/approvals.md)
