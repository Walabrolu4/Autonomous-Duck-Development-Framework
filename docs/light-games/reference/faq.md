# Frequently Asked Questions

## Do I need an AI coding agent to start?

No. Plain chat and Markdown are enough for ideation, research, planning and producing proposed file edits. A coding agent becomes useful **after Gate I**, when a particular set of implementation operations has been authorized.

## Do I need to know programming?

Not to begin. Light can support learning through relevant tradeoffs and small experiments. A person still needs to evaluate the game's actual behavior and make material design choices.

## Can I start without an idea?

Yes. The agent should offer two or three mechanically distinct options and ask one meaningful question at a time. “I don't know yet” is a valid response.

## Does Light mean weaker safety than original ADDF?

No. It reduces daily file/navigation burden but preserves role boundaries, a dry run, exact implementation authorization, file-backed memory and human acceptance. See the [comparison table](../foundations/comparison.md).

## Is ADDF Light Games a game engine?

No. It can guide a web Canvas/Phaser game, Godot or Unity project, or another playable system. It doesn't automatically install any of them.

## Why six project files and three sprint files?

The six persistent files hold safety, rules, game intent, current status, decisions and backlog. Once a sprint exists, three files separate the **what** (`SPRINT.md`), **how/authorization** (`PLAN.md`) and **results/acceptance** (`REVIEW.md`).

## Why not ask AI to generate my entire game?

Large one-shot outputs hide assumptions and make playtesting difficult. Bounded slices expose the important mechanic early and let a human learn from actual feedback.

## Can the agent make any decisions?

Yes, routine reversible T0 implementation details inside approved scope. It cannot choose significant mechanics, architecture, cost/privacy risks or player acceptance without human authority.

## Is a green GitHub Actions check proof that a game is ready?

No. It can establish specific tested behavior or structural consistency. It cannot prove the player's experience or that a human actually approved the current plan.

## Can the validator verify that I approved something?

It can check whether an approval *record* has consistent fields and a matching revision. It cannot authenticate the actual human or reconstruct the exact historical plan snapshot from Markdown alone. Treat warnings seriously.

## Can I use my existing project?

Yes, through a **read-only audit and reviewed migration**. Don't overwrite existing `AGENTS.md`, source files or GDD. Preserve original ADDF history if the project already uses it.

## What about Claude Code, Codex and OpenClaw?

All are optional integrations. Stage 4 created skill adapters; Stage 5 live host-specific runtime validation remains pending. OpenClaw's coordinator does not automatically provision remote computer access or uninterrupted background jobs.

## Must I use GitHub?

No. Local files are the minimum. Git is helpful for revisions, diffs and provenance, but the methodology is not tied to a specific hosting site.

## What if I reject a sprint?

Preserve the rejection and observations in `REVIEW.md`. The agent proposes refinement or abandonment, seeking fresh Gate D/I as needed. It cannot silently mark the sprint accepted.

## What if I change my mind mid-sprint?

Record the new significant choice, revise affected scope/criteria and invalidate stale technical approval. The agent should explain the smallest safe way forward.

## How is the complete manual maintained?

The wiki pages are canonical, listed in an ordered manifest. `scripts/build_light_manual.py` generates `MANUAL.md` with stable chapter anchors and rewrites internal links. CI checks that the committed manual matches generated content.

## Common failures

**Assuming the FAQ overrides exact contracts:** It doesn't. Follow the approved `spec/` files and current project evidence.

**Assuming a skill is installed because the repo contains it:** Verify actual host discovery.

## Related

[Getting started](../guides/first-session.md) · [Comparison](../foundations/comparison.md) · [Troubleshooting](troubleshooting.md)
