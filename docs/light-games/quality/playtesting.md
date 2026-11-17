# Human Playtesting and Design Validation

Game development cannot be evaluated entirely from code structure or generated screenshots. A person must interact with the game and report what actually happens and how it feels.

## When to use

Use after an authorized playable slice, when a designer needs to validate a mechanic/system/level, and before assigning a final Gate A verdict.

## Design the playtest around a question

A good playtest asks “Does the first-time player understand that the red square is dangerous?” rather than “Is the game fun?” The latter is too broad for an early slice and difficult to diagnose.

Choose a narrow objective:
- **Mechanic:** Is the movement or jump response predictable?
- **System:** Can players infer how an enemy chooses its target?
- **Level:** Does the first encounter teach the required action?
- **Feedback:** Can players see and understand a collision or success event?
- **Accessibility:** Can relevant players perceive and operate the test in the intended environment?

## Prepare a short protocol

1. Specify the exact build, device and controls.
2. Tie tasks to the original `AC-##` criteria.
3. Let the player attempt the task before explaining it away.
4. Record actual observations, surprises, frustration and helpful recovery behavior.
5. Distinguish the player's actions from the designer's interpretation.
6. Capture the human's Gate A verdict separately from automated evidence.

In a classroom, another student can be a playtester, but the project owner still decides what to accept. Preserve which person actually observed which result.

## Example: testing a level's first jump

The designer predicts the player will notice a safe jump cue and cross a short gap without verbal instructions. During the test, the observer notes hesitation, camera angle, failed attempts and whether the player retries. The feedback may suggest changing geometry or introducing a clearer visual cue.

If the change needs a new asset/path outside the approved plan, return to Gate I rather than treating feedback as blanket permission.

## What to record

`REVIEW.md` can use a simple table:

| Criterion | Human action | Actual observation | Outcome |
| --- | --- | --- | --- |
| AC-01 | Attempts jump | Character responds, lands on platform | Pass for observed player/device |
| AC-02 | Reads hazard cue | Player walks into hazard without noticing | Fail/needs refinement |
| AC-03 | Retries | Player finds restart prompt | Pass |

One individual's report is **local evidence**, not proof all players will respond the same way. Record device, experience level and accessibility constraints if relevant and known.

## Feedback to refinement

State the concrete defect, propose a minimal correction and decide whether it fits current authorization. Retest only after a real build and capture the new round without erasing prior feedback.

The human may accept, accept with conditions, request refinement, reject or pause.

## Common failures

**Designer coaches every action:** A novice never reveals what instructions are unclear. Observe first.

**Tests become a survey only:** Aesthetic opinions replace observable tasks. Mix questions with real actions.

**AI invents observations:** A model estimates how a player would feel. Mark it a hypothesis, never a playtest result.

## Related

[Acceptance stage](../lifecycle/acceptance.md) · [Refinement](../lifecycle/refine.md) · [Learning checkpoints](../learning/checkpoints.md)
