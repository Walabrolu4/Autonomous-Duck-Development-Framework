# Install the Minimal Starter Kit

ADDF Light Games has no obligatory CLI installer. Installation means copying **six Markdown files into a new game-project folder**, then using a prompt to begin guided discovery.

## When to use

Use this for a **new** project. If you already have code or a root `AGENTS.md`, follow [existing-project adoption](existing-project.md) instead; do not overwrite it.

## Before you begin

You need a folder where you can create files and an AI assistant. You do **not** need Unity, Godot, Phaser, OpenClaw, a credit card, cloud hosting or a complete concept to start.

Confirm you are viewing the `ADDF_light_games` branch of the framework, not the original `main`. The inherited `starter-kit/blank/` directory belongs to **full ADDF**. Light's six files live under `starter-kit/minimal/`.

## Copy these files

```text
your-game/
├── AGENTS.md
├── SECURITY.md
├── GAME.md
├── STATE.md
├── DECISIONS.md
└── planning/
    └── BACKLOG.md
```

Source: [Light starter kit](../../../starter-kit/LIGHT_GAMES.md) and [minimal folder](../../../starter-kit/minimal/).

The initial `STATE.md` reads `lifecycle_stage: research`, `sprint_status: discovering`, `active_sprint: none`, `authorized: no`. That's correct. The game title, engine and prototype goal may be `unknown`.

**Do not copy the three sprint files yet.** They remain distribution templates under `starter-kit/sprint-template/` until the human chooses the first milestone.

## Initial verification

1. Open `SECURITY.md` and make sure its excluded paths and network restrictions fit your environment. Never add real secret values to the document.
2. Open `AGENTS.md`; it must describe Gate D, Gate I and Gate A and the roles' write boundaries.
3. Open `STATE.md`; confirm no implementation has been authorized.
4. Make sure `GAME.md` still labels unselected ideas as unknown, rather than falsely chosen.
5. Optionally run the Python validator after Stage 6 if you have Python installed:

```bash
python3 /path/to/framework/scripts/validate_light.py /path/to/your-game
```

This is a **read-only** structural check. It is not a permission grant and cannot prove human consent.

## Optional integrations

Claude Code can load a project skill under `.claude/skills/addf-light-games/SKILL.md`; Codex can load one under `.agents/skills/addf-light-games/SKILL.md`; OpenClaw is optional and requires its own deliberately configured workspace. Install these **only if you use that host**. The core six files are sufficient for manual chat workflows.

## Example: first few minutes

The user says, “I want a small browser game but don't know what kind.” The agent reads safe project context and offers a dodge, path-puzzle or tactical encounter concept. The user selects one. The agent drafts a small player-facing goal, not game code. After the human chooses a milestone, it creates the sprint triplet and requests the two appropriate approvals.

## Common failures

**Wrong source:** Copying the framework's root `AGENTS.md` or original full kit. Copy only the six Light `minimal/` files.

**Premature paperwork:** Filling out a future Sprint 001 with fabricated decisions before the user has chosen anything. Leave it absent.

**Unsafe existing repo:** Overwriting another project's instructions. Run the read-only adoption audit first.

## Related

[First session](first-session.md) · [Quick reference](quick-reference.md) · [Existing-project adoption](existing-project.md)
