# Stage 2 — Design and Ideation

Design turns possibilities into **one bounded, testable gameplay outcome**. The agent facilitates and documents; the human owns material creative direction.

## When to use

Use once there is enough context to propose an observable action, game-system response and acceptance test—or when a failed prototype reveals that the intended experience needs to change.

## Design brief for one slice

A useful sprint brief answers:
1. **Player verb:** What does a player do?
2. **System response:** What happens in the game?
3. **Feeling or insight:** What should the player perceive or learn?
4. **Scope in/out:** What precisely isn't being built yet?
5. **Learning checkpoint:** Which mechanic/system tradeoff deserves explanation and a prediction?
6. **Acceptance criteria:** Which observable checks will determine whether the slice works?

If no significant design fork exists, document `gate_d_status: not_required` with a specific reason. Do not invent a second option to create artificial approval paperwork.

## Design alternatives and Gate D

A consequential choice deserves two genuine alternatives and tradeoffs. Examples:
- Movement is **instant** or **inertial**;
- Enemy reaction is **line-of-sight chase** or **proximity trigger**;
- Level learning happens in a **safe introduction** or a **high-pressure first encounter**.

Show the recommendation as advice, not a committed decision. Record the user's actual choice in `DECISIONS.md` and `SPRINT.md`, with rationale and conditions. A design approval **does not** permit writing code.

## Create the sprint pack at the right time

Only after a real milestone is selected should the agent copy `SPRINT.md`, `PLAN.md`, and `REVIEW.md` templates into `planning/sprints/sprint-NNN/`. The agent can fill planning documents without user having to type entire schemas.

`SPRINT.md` defines the intended behavior and actual `AC-##` entries **before source implementation**. Each criterion specifies test method, setup/input, observable pass condition, evidence to capture and whether it blocks release.

## Example: a dodge prototype

The human approves a 2D browser slice:
- move a duck in four directions;
- avoid one type of moving obstacle;
- hit ends the attempt, restart begins again.

**Out of scope:** sounds, scoring service, level editor, multiplayer, art generator. **Learning checkpoint:** predicted difference between instantaneous and accelerating movement.

`AC-01` tests input response and arena bounds. `AC-02` tests collision/game-over visibility. `AC-03` tests restart. The person should still judge actual readability and feel during later acceptance.

## Exit criteria

The design stage is ready for technical planning when selected scope, player behavior, significant choices, risk assumptions and criteria are explicit. The agent then drafts `PLAN.md` and seeks **Gate I** separately.

Do not allow “we agree on the game” to stand in for authorization of unreviewed paths or downloads.

## Common failures

**Large invisible requirement:** “Create a fun game.” Specify what the player can do and observe.

**Design by agent default:** Select platform or art style without acknowledging the user didn't choose.

**Acceptance after implementation:** Define `AC-##` only when code is done. Reverse the order and obtain meaningful pre-implementation checks.

## Related

[Sprint planning](../sprints/planning.md) · [Approval gates](../sprints/approvals.md) · [Learning checkpoints](../learning/checkpoints.md)
