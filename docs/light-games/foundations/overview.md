# What Is ADDF Light Games?

ADDF Light Games is a **human-guided, file-first AI game-development methodology**. It helps someone go from “I want to make a game” to a testable playable slice without requiring a complete game design document, a specific game engine, or an autonomous agent platform.

The short loop is **Research → Design / Ideation → Implement → Refine → Acceptance**. It repeats for each bounded sprint. Research reveals uncertainty; Design chooses a viable experience; Implement produces approved changes; Refine responds to evidence; Acceptance belongs to the person playing or evaluating the result.

## When to use

Use Light for solo developers, game-design students, prototypes, interaction designers, small teams, and developers learning from AI assistance. The first supported domain is **games and interactive playable experiences**, not a general replacement for original ADDF's broader software-development governance.

The methodology works through a plain chat assistant and Markdown. A coding agent is optional for early discovery but valuable after you approve a technical plan. Claude Code, Codex and OpenClaw are optional adapters, **not requirements**.

## What “Light” means

Light describes the **user's operational workload**, not less rigorous permissions or shallow explanations. The documentation may be exhaustive while the runtime starts with **six files** and only adds the three-file sprint pack when a milestone exists.

The agent researches, teaches relevant tradeoffs, drafts documentation, proposes actions and records actual results. The person decides consequential design direction, authorizes precise implementation scope and judges the playable outcome.

You should spend your attention on **what the player does and what you learn from testing**, not on manually writing a dozen administrative files.

## The two repositories

The **framework distribution** lives in the `ADDF_light_games` Git branch. It contains specifications, starter templates, prompts, optional integrations, examples, validators and this wiki.

Your **game repository** is separate. The six starter files copied into it refer to that game. Never copy the framework's inherited root `AGENTS.md` into your game: that file belongs to the original full ADDF edition.

## The three non-negotiable gates

| Gate | Human decides | Durable record |
| --- | --- | --- |
| **D — Design** | Meaningful design alternatives and the sprint's intended outcome | `DECISIONS.md` and `SPRINT.md` |
| **I — Implementation** | Exact files, commands, dependencies, side effects and plan revision | `PLAN.md` |
| **A — Acceptance** | Whether first-hand playtesting/review meets the sprint goal | `REVIEW.md` |

A conversational “sounds good” about a concept **is not** permission to change code. A passing test **is not** player acceptance.

## What a first result looks like

A user chooses a tiny dodge game. The agent compares direct versus accelerating movement, the person selects a style, and the agent drafts one sprint: move a placeholder duck in an arena and avoid one repeating obstacle. The agent shows exactly what it plans to change and asks for authorization. After implementation, the person plays, observes a readability problem and requests a small refinement. The sprint ends only with the person's verdict.

This is more useful than generating an entire untested game from one sentence.

## Common failures

**Too much process:** Require the full wiki before starting, or make the user fill every field. Instead, start with one question and let the agent draft files.

**Too little control:** Skip the dry-run approval for “obvious” changes. Instead, use a short exact plan.

**False progress:** Treat an AI's claim that a build works as evidence of gameplay feel. Instead, distinguish verified command output from a human observation.

## Related

[Philosophy](philosophy.md) · [Original ADDF comparison](comparison.md) · [Quick Start guide](../guides/first-session.md) · [Glossary](glossary.md)
