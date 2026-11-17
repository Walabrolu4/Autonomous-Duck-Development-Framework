# Quick Reference: One Sprint at a Glance

This is the **one-page operational companion** to the full manual. Use it during a work session instead of reading the entire wiki repeatedly.

## When to use

Use it when deciding what prompt to run next, which file the agent should update, what you must personally approve and when to stop.

## Current state → next action

| Status in `STATE.md` | Agent action | Human action |
| --- | --- | --- |
| `discovering` | Summarize known/unknown; ask one question | Choose concept or request options |
| `designing` | Propose one slice, research, tradeoffs and `AC-##` | Decide meaningful direction (Gate D) |
| `awaiting_approval` | Show exact `PLAN.md` revision, paths, commands and risks | Explicitly authorize or revise (Gate I) |
| `implementing` | Change **only** approved source and log evidence | Review deviations if any |
| `refining` | Diagnose observed defect; check existing authorization | Choose correction or approve revised scope |
| `awaiting_acceptance` | Provide tested artifact, limitations and playtest steps | Play/review and provide Gate A |
| `accepted` | Preserve verdict, retro and backlog handoff | Choose next sprint if desired |
| `rejected` | Preserve rejection; propose safe direction | Decide revise/abandon |
| `paused` | Record blocker, last safe state and resume requirements | Supply needed authorization or context |

**The stage** is a separate field: research/design/implement/refine/acceptance. Status and stage must agree with the workflow contract.

## Files you will see

```text
AGENTS.md         agent conduct / role boundaries
SECURITY.md       prohibited reads, tools, external effects
GAME.md           chosen player experience and constraints
STATE.md          current verified status, next action, gates
DECISIONS.md      actual material human choices
planning/BACKLOG.md candidates and deferred ideas
planning/sprints/sprint-NNN/
  SPRINT.md       goal, tradeoffs, acceptance criteria, Gate D
  PLAN.md         dry run, operations, commands, Gate I
  REVIEW.md       real results, playtest and Gate A
```

## The three questions to ask before authorizing work

**Design:** Is the player action/outcome clear, and do I actually choose this approach?

**Implementation:** Have I seen *exactly* which files/commands/dependencies/side effects this plan revision permits?

**Acceptance:** Have I actually played or inspected the result and reported my verdict, rather than trusting a green test?

## A quick “stop” checklist

Stop before edits if:
- the current plan revision isn't explicitly authorized by you;
- a new path, dependency, command, paid service, privacy risk or deployment is needed;
- the worktree/source state conflicts with the plan;
- the assistant claims an approval you cannot verify;
- a human review has not occurred but status says `accepted`.

## Commands

To check your own project file structure from the Light framework repository:

```bash
python3 scripts/validate_light.py /path/to/your-game
```

To check the distributed unstarted starter kit:

```bash
python3 scripts/validate_light.py starter-kit/minimal --mode template --sprint-template starter-kit/sprint-template
```

A PASS means **structural consistency only**, not authenticated human consent.

## Common failures

**Blind prompt chaining:** Automatically run START→IMPLEMENT. Pick prompt based on verified state and stop at each human gate.

**Routine overload:** Require permission for trivial variable names. Let agents choose T0 details within scope.

## Related

[Quick Start in repo](../../QUICK_START.md) · [Prompt catalog](../reference/prompt-catalog.md) · [Approval gates](../sprints/approvals.md)
