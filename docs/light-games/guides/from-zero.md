# Starting Without a Game Idea

“No idea yet” is an **acceptable and productive** initial state. Light's discovery protocol exists precisely so the human can learn and choose without having to supply an entire design brief.

## When to use

Use this for new designers, a classroom warm-up, exploratory prototypes and users who know they want to make a game but cannot name a mechanic.

## Discovery procedure

**Step 1 — Ask one preference, not a questionnaire.** For example: “Would you rather make something about movement, solving a puzzle, or tactical decisions—or should I suggest three options?”

**Step 2 — Offer 2–3 differentiated concepts.** Each option should communicate:
- the core player action;
- what the system does in response;
- the feeling or design principle it might explore;
- one minimum playable experiment;
- the main uncertainty.

**Step 3 — Explain one design fork.** If the user chooses movement, compare direct versus momentum-based control. If they choose puzzles, compare open exploration versus a sequence of fixed challenges. The agent recommends a reversible starting experiment and says why.

**Step 4 — Record the actual choice.** Update `GAME.md` and allocate a `D-###` record when the choice is consequential. If the user is unsure, mark the choice deferred and offer a small research spike.

**Step 5 — Select the first slice.** Propose an observable milestone, such as “Move a placeholder in a visible arena and survive one obstacle.” Do not promise a complete scoring system, art style, levels, save system and multiplayer in one step.

**Step 6 — Gate D then Gate I.** Significant design approval is recorded separately from permission to edit exact files.

## Worked example

| Option | Player verb | Smallest playable slice | Primary learning |
| --- | --- | --- | --- |
| Dodge the hazard | Move / avoid | One avatar, one repeating moving obstacle, collision and restart | Control feel and clarity |
| Connect the path | Rotate / connect | Rotate tiles to join start and goal | Local feedback and puzzle legibility |
| Two-unit tactics | Select / choose | Two controllable units and one visible conflict resolution | Rules, state and meaningful choice |

A user picks the puzzle. The agent might ask: “Should a tile snap in quarter turns or rotate freely? Quarter turns are simpler and make valid connections unambiguous. Which first experiment should we build?” The user decides or asks for a side-by-side prototype.

A good first `SPRINT.md` states only the chosen action, measurable outcome, in/out scope, learning objective and acceptance checks. A good `PLAN.md` names the exact files and commands needed to test that outcome.

## If the user cannot choose

Do not force a direction or pretend an AI recommendation is a human decision. Offer a reversible 15-minute **design exercise** or focused no-code research. A formal code-producing prototype still requires an authorized sprint plan.

## What should not happen

- No automatic engine selection based on the AI's comfort.
- No full asset pipeline or monetization strategy before the player verb is known.
- No prefilled “human approved” decision record.
- No multi-page list of aesthetic preferences that delays the first useful test.

## Common failures

**Options differ only in theme:** “Dodge asteroids,” “dodge cars,” “dodge fruit.” Offer different **interaction systems**, not merely art skins.

**Unbounded ideation:** A hundred ideas without choosing. Limit to the smallest decision that unlocks a concrete sprint.

**Agent chooses for the student:** The assistant may recommend, but must record the user's actual preference.

## Related

[Guided discovery](../learning/guided-discovery.md) · [First session](first-session.md) · [Research](../lifecycle/research.md)
