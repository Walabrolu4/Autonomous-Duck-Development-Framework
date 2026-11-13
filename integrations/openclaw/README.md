# OpenClaw adapter — optional ADDF Light Games coordinator

**Stage 4 candidate · opt-in only.** OpenClaw is useful for coordinating project updates across sessions or machines. It is **not required** for ADDF Light Games and is **not itself** an implementation permission source.

## What this adapter contains

- [Workspace skill](skills/addf-light-games/SKILL.md): `SKILL.md` following OpenClaw's workspace-skill format.
- [Coordinator playbook](COORDINATOR_PLAYBOOK.md): separation between facilitator, research, coding, human review and optional remote handoffs.
- Canonical game-project contract remains `SECURITY.md`, `AGENTS.md`, `STATE.md`, and active sprint files, as described in [the prompt catalog](../../prompts/LIGHT_GAMES.md).

## Installation — intentional and reviewable

1. Establish a **trusted OpenClaw workspace** and confirm which folders/tools the agent can access. Do not automatically grant broad filesystem or shell access.
2. For a **new game**, install the six [minimal](../../starter-kit/LIGHT_GAMES.md) project files in the game's repository. For an existing game, use the [read-only adoption guide](../../starter-kit/EXISTING_PROJECTS.md).
3. Copy `integrations/openclaw/skills/addf-light-games/SKILL.md` from this framework distribution into **your OpenClaw workspace** under:

   `<workspace>/skills/addf-light-games/SKILL.md`

4. Verify OpenClaw discovers the named skill (the exact UI/command may vary by version). Ask it to **read only** the safe game project's `SECURITY.md`, `AGENTS.md`, `STATE.md` first.
5. Do not configure unattended cron tasks, auto-launch, background file edits, remote shell, repo write scopes, messaging channels, publishing or API credentials as part of this copy step. Those require separate user-approved setup.
6. For multi-agent use, follow [COORDINATOR_PLAYBOOK.md](COORDINATOR_PLAYBOOK.md) and use an explicit **handoff packet** that contains the *approved* bounded scope and a pointer to its source records; a coordinator cannot supply Gate I or Gate A on behalf of the human.

**Official format and loading locations** (check against installed version):
- https://docs.openclaw.ai/tools/skills
- https://docs.openclaw.ai/tools/creating-skills

## Coordination boundary

The agent may assist with:
- turning a game idea into small options, research questions and testable sprint proposals;
- summarizing verified project status and preparing documents;
- notifying a human that a design choice, plan authorization or playtest verdict is needed **only if the delivery channel has been expressly configured/authorized**;
- delegating **read-only** analysis to a suitable worker where tools/permissions allow;
- delegating **implementation** only after a real human Gate I and only the exact approved operations.

The agent must **not** turn “please keep this project moving” into continuous autonomous coding, publish a build or approve its own changes.

## Example safe user instruction

> “Use the ADDF Light Games skill as a coordinator for this project. Read the permitted project brain, summarize the last verified stage, identify exactly one next safe action, and stop if a human design or implementation approval is missing. Do not initiate background work, contact third parties or change source code.”

For remote school/browser to home-machine workflows, the developer must first configure trusted transport, credential isolation and machine execution boundaries. **No transport, remote command runner or message delivery is installed by Stage 4.**

## Stage 5 smoke checks

- Workspace skill is visible and reads from the intended game repo.
- Gate D, Gate I and Gate A remain human, even when multiple workers are available.
- Orchestrator reports the worker's actual diff/build/test evidence without fabricating completion.
- Agent stops on missing/expired authorization and during model/session handoff.
- No auto-generated background schedule or public deployment occurs.

**Status:** Skill and instructions authored; OpenClaw runtime behavior not yet exercised. No claim of a configured home/school remote-control channel.
