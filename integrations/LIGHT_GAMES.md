# ADDF Light Games — Optional Agent Integrations

**Stage 4 candidate · pending human verification.**

The canonical workflow is **provider-neutral**: [9 lifecycle prompts](../prompts/LIGHT_GAMES.md), [six initial game-project files](../starter-kit/LIGHT_GAMES.md), and the sprint `SPRINT.md` / `PLAN.md` / `REVIEW.md` pack.

The following adapters are **opt-in**. They make the method discoverable inside an AI coding/coordination environment; they do **not** add new project permissions, auto-approve changes, run an engine, host the project or provide a functioning remote-agent setup by themselves.

| Environment | What Stage 4 includes | Destination in **game project** | What remains manual |
| --- | --- | --- | --- |
| [Claude Code](claude-code/README.md) | Agent Skill + optional CLAUDE.md bridge | `.claude/skills/addf-light-games/SKILL.md` | Install/copy, review instructions, invocation, actual tests |
| [Codex](codex/README.md) | Agent Skill | `.agents/skills/addf-light-games/SKILL.md` | Install/copy, invoke/confirm skill, permission prompts |
| [OpenClaw](openclaw/README.md) | Workspace Skill + guarded coordinator playbook | `<workspace>/skills/addf-light-games/SKILL.md` | Configure trusted workspace, tool access, remote delegation |
| No integration | Plain text Markdown prompts and project brain | Only the six minimal files | Paste prompts, apply proposed file edits |

**Important:** `AGENTS.md` inside a user's game project has the core policy. Provider skills are thin **bridges**, not a competing authority or a way to circumvent Gate I. If an assistant has persistent memory, ignore stale remembered approvals when repository evidence disagrees.

## Security and permissions

1. Read `SECURITY.md` before loading additional game files; never ingest `.env`, private keys, secrets, unrelated home directories or user-specific credentials.
2. Before source edits, verify active sprint ID, `PLAN.md` revision, exact allowed operations/commands and an **actual human Gate I** response.
3. For special operations (public deploy, network transfer, purchases, credential handling, destructive commands or branch merges), require explicit **additional** authorization.
4. Treat subagents as delegates, not approvers. The coordinator cannot approve on the user's behalf; each worker receives a bounded, already-authorized task.
5. If adapters or permissions conflict with the project `SECURITY.md`/`AGENTS.md`, stop and request human resolution. Tool availability ≠ consent.

## Compatibility and validation

The vendor skill formats are based on currently documented project/workspace skill directories and `SKILL.md` with YAML `name`/`description` metadata. Sources:

- Claude Code: https://code.claude.com/docs/en/skills
- Codex/ChatGPT skills: https://learn.chatgpt.com/docs/build-skills
- OpenClaw skills: https://docs.openclaw.ai/tools/skills
- OpenClaw skill authoring: https://docs.openclaw.ai/tools/creating-skills

Versions/settings may vary. **These are authored files, not installation success reports.** Stage 5 must test actual discovery/invocation, safe role transitions, handoff and permission-denial behavior on supported local installations.

## Avoid multiple copies of the truth

The full method lives in `spec/` and the game project's brain, not inside vendor-specific preferences. Change core rules in the project `AGENTS.md` only with review. When framework rules evolve, explicitly migrate the installed skills and project contract; do not let an auto-updater rewrite human decisions.

**Next review:** [Stage 4 manual review checklist](STAGE_04_REVIEW.md).
