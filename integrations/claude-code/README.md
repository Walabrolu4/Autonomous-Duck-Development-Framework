# Claude Code adapter — ADDF Light Games

**Stage 4 candidate: a project-level Agent Skill.** Use it in **your game project**, not the ADDF framework repository.

## Install deliberately

1. Ensure your game project has the six minimal ADDF Light Games files (or a reviewed adoption of an existing repo).
2. Copy **this distribution file**:

   `integrations/claude-code/skills/addf-light-games/SKILL.md`

   into the **game project** at:

   `.claude/skills/addf-light-games/SKILL.md`

3. Optionally copy [`CLAUDE.md.example`](CLAUDE.md.example) to a new game-project `CLAUDE.md` **only if it does not already exist**. If one exists, merge a small pointer manually after review. This bridges automatic project guidance to the `AGENTS.md` policy.
4. Open Claude Code from the game project. Ask it to use **`/addf-light-games`**, or check whether the skill is offered when relevant. If your version has different discovery behavior, follow the vendor documentation.
5. For each stage, explicitly ask for the next action such as “Use ADDF Light Games to discover one small playable sprint.” A skill invocation does **not** grant permission to implement. It must stop for Gate D, Gate I and Gate A.

**Current official reference:** https://code.claude.com/docs/en/skills

No auto-installer, shell command, host-permission change or network access is included. If user project `.claude/` already contains files, copy only the reviewed new skill path, and don't overwrite other skills.

## What the skill actually does

- Reads `SECURITY.md`, then `AGENTS.md`/`STATE.md` and relevant project files.
- Chooses between no-idea, one-sentence idea, and existing-project routes.
- Uses the five-stage loop and three human gates.
- Reports plans and verifiable evidence; cannot self-authorize a source edit, run an unapproved command or self-accept a game.
- Refers back to the [canonical prompts](../../prompts/LIGHT_GAMES.md) for long-form instructions when those are available.

### Recommended request

> “Use ADDF Light Games to assess the current safe project state, propose a single playable milestone and stop at the next human decision. Do not run code or install dependencies until I approve the exact PLAN.md revision.”

For a new chat, use `/addf-light-games` or the above request. After interruption, say “Resume from project files; report whether the current plan revision still has valid human authorization.”

## Smoke checks for Stage 5

- Skill appears in Claude Code and does not override existing `CLAUDE.md` guidance.
- Blank project starts at `discovering`, no code writes.
- A user who approves a design but not a file plan does not trigger source edits.
- A plan scope change pauses and requests new Gate I.
- Build completion doesn't become human Gate A.
- Existing project adoption does not overwrite a different `AGENTS.md`.

**Stage 4 does not claim these smoke tests were executed.**
