# Your First ADDF Light Games Session

The first session should feel like a short game-design conversation, **not a form**. A user may start with no idea; the agent must provide useful choices without demanding a novel-length GDD.

## When to use

Use this after copying the six starter files, or when showing a new game-design student how to ask an AI assistant for thoughtful help instead of one-shot generation.

## Before the conversation

The agent reads `SECURITY.md` first, then `AGENTS.md` and `STATE.md`. It may read `GAME.md`, `DECISIONS.md` and the backlog when necessary. If it has no file access, the user can provide safe excerpts, and the agent must label its edits **proposed** instead of claiming it saved them.

Never provide API keys, private accounts or hidden credentials to get the session started.

## The first prompt

> Use ADDF Light Games. Read the project's SECURITY.md, AGENTS.md and STATE.md before exploring other files. Help me find **one small playable outcome** by asking one meaningful question at a time. Explain major design tradeoffs, label assumptions, and maintain the project brain if permitted. Do not edit game code, install packages or publish anything. Stop before implementation and show me an exact plan for my approval.

Then add your idea—or simply say, “I have no idea what to make.”

## Session sequence

1. **Orient:** Establish whether the user has no idea, one sentence or an existing game. Report known versus inferred details.
2. **Discover:** Offer two or three genuinely distinct small ideas when needed. Each should have a player action, a system response and a feasible first slice.
3. **Learn:** Compare one consequential tradeoff such as instant movement versus acceleration, or a fixed obstacle versus a moving one.
4. **Choose:** Let the person select or defer. Record real decisions in `DECISIONS.md`; unanswered questions remain pending.
5. **Propose a sprint:** One observable goal, in/out scope, testing method and minimal risk. Move extra ideas to the backlog.
6. **Gate D:** Obtain an actual human decision on significant game direction and acceptance criteria.
7. **Prepare a dry run:** Draft `PLAN.md` with exact paths, commands, dependencies, risk and rollback.
8. **Gate I:** Stop and ask the human to authorize the actual plan revision. Only after explicit authorization may implementation begin.
9. **Gate A later:** The human plays the resulting game; automated test success is not acceptance.

For most first sessions, stopping after steps 1–6 is perfectly useful.

## What the agent writes

The agent updates `GAME.md` only for actual intended experience or clearly proposed ideas, allocates `D-###` entries for significant choices, and puts future candidates in `planning/BACKLOG.md`.

Only after selecting an actual milestone does it create `planning/sprints/sprint-001/` from the three template files. It can draft technical assumptions and tests, but it cannot invent a past consent record.

## Example conversation

**User:** “I want something about movement.”

**Agent:** “Two small first slices: a duck avoiding horizontal obstacles, or a character jumping between two platforms. The first isolates movement clarity; the second adds timing and gravity. Which interaction do you want to study?”

**User:** “Duck dodge, simple directional controls.”

**Agent:** “We can start with immediate movement or acceleration. Immediate movement makes collision and responsiveness easier to evaluate; acceleration might feel more expressive but needs tuning. Which do you prefer?”

**User:** “Immediate for Sprint 001.”

That is a real design choice in the conversation. It is **not yet Gate I**. The agent should now show the exact first-sprint plan and ask permission before building.

## Closing the session

Summarize last verified status, what documents changed, which gates are pending, and **one next action**. Update `STATE.md` if tools and permission allow. Next session begins with the [resumption protocol](../agents/handoff.md) rather than trusting a model's memory.

## Common failures

**Too many questions:** Ask one impactful question, not ten unrelated preferences.

**Overeager agent:** It generates the game immediately after the user selects a genre. Stop at the dry-run gate.

**Pretend state:** A chat assistant claims it edited files without file tools. Provide a proposed diff instead.

## Related

[No-idea route](from-zero.md) · [One-sentence route](from-idea.md) · [Design stage](../lifecycle/design.md) · [Approval gates](../sprints/approvals.md)
