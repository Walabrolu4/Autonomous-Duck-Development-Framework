# Codex adapter — ADDF Light Games

**Stage 4 candidate:** A repository-level Agent Skill. Codex already uses the game project's `AGENTS.md` as persistent project guidance; the skill adds a reusable five-stage procedure.

## Install deliberately

1. For a **new game**, copy the six Stage 3 `minimal/` files into its root; do not copy the framework's original full-ADDF root instructions.
2. Copy `integrations/codex/skills/addf-light-games/SKILL.md` into the game project at:

   `.agents/skills/addf-light-games/SKILL.md`

3. For an **existing game**, review any existing `AGENTS.md`, `.agents/skills` directory and security policies first. Never overwrite a same-name skill or instructions silently.
4. Open Codex from the game's repository. Invoke the installed skill explicitly (for example by mentioning **`$addf-light-games`** where supported), or ask “Use the ADDF Light Games skill to resume this project and stop at the next approval gate.”
5. Confirm its response references the correct `SECURITY.md`, `AGENTS.md`, `STATE.md`, sprint and plan revision. The tool still needs ordinary host permissions **and** specific human Gate I for implementation.

**Current official reference:** https://learn.chatgpt.com/docs/build-skills

## Safety and working practice

- Codex permissions/sandbox settings are a **technical ceiling**, not evidence of a user approving edits.
- A valid `PLAN.md` must list operations, paths, working directories, allowed commands, packages, external side effects, risks and rollback.
- Do not weaken sandbox settings, preapprove network/tool permissions, or use unrestricted execution solely to make a skill work.
- Do not create `.codex/config.toml` automatically; that would change local tool behavior and needs a separate reviewed decision.
- Do not merge, push, deploy or publish without explicit, distinct authority.
- After a model/session switch, reconcile actual file state and approval records, not only remembered chat context.

## Suggested first request

> “Use `$addf-light-games`. Read only the allowed project files, summarize my last verified stage, choose the smallest next playable milestone, and stop before implementation. Ask one consequential question at a time.”

## Smoke checks for Stage 5

- Codex discovers the copied skill.
- Repo `AGENTS.md` is not overwritten and remains authoritative.
- Gate D is not interpreted as Gate I; no source write before exact authorization.
- New dependency/command/path triggers revised `PLAN.md` and renewed Gate I.
- A passing test remains unaccepted until a human Gate A.
- Resumption from a different agent fails closed when evidence is missing.

**Not yet tested against a running Codex installation in Stage 4.**
