# Claude Code Integration

Claude Code is an **optional host** for implementing an approved game sprint. ADDF Light Games stays useful without it; the project-brain files and gates remain authoritative even when a provider skill is installed.

## When to use

Use if you work with Claude Code in a game repository and want the same discovery/planning/review process as the model-neutral prompts.

## Installation

The Stage 4 adapter distributes an Agent Skill at `integrations/claude-code/skills/addf-light-games/SKILL.md`. Copy it deliberately into **the game project** at:

```text
.claude/skills/addf-light-games/SKILL.md
```

Optional `CLAUDE.md.example` contains a pointer to the project's standing `SECURITY.md`, `AGENTS.md` and `STATE.md`. **Never overwrite an existing `CLAUDE.md`**; review and merge its relevant pointer if needed.

The framework's original root `AGENTS.md` belongs to full ADDF and must not be mistaken for the game project's Light instructions.

## Starting a session

Ask Claude to use the ADDF Light Games skill, read only the permitted project-brain files and report the last verified stage/status. If no game idea exists, it should offer small options. If the project is already at `awaiting_approval`, it should show the exact plan revision rather than starting to code.

The host may have its own permission prompts; those are necessary technical controls but **do not replace Gate I**.

## Verifying skill behavior

A useful smoke test asks Claude to:
1. inspect a blank six-file project and **not** write source;
2. propose a one-slice design and record Gate D separately;
3. show `PLAN.md` with exact paths/commands and stop before edits;
4. reject an unapproved new dependency after Gate I;
5. report actual tests without claiming human Gate A.

These are **tests to run**, not claims that Stage 4's skill was installed and exercised in your environment. The documented live Claude runtime pilot remains pending.

## Example

Claude proposes editing a scene and script for a jump mechanic. The user approves only the script. Claude must revise the plan to exclude scene changes or ask for explicit scene approval. A broad skill invocation isn't consent to do both.

## Common failures

**Conflicting CLAUDE.md:** Automatically replace an existing file. Merge deliberately and keep stricter instructions.

**Skill as authority:** Invoke the skill and assume all commands are approved. Read the actual plan.

**Unverified adapter:** A `SKILL.md` exists in GitHub, but no actual host installation was tested. Record pending.

## Related

[Claude adapter guide](../../../integrations/claude-code/README.md) · [Permissions](permissions.md) · [Handoff](handoff.md)
