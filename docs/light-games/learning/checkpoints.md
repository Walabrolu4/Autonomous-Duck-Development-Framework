# Learning Checkpoints Through Playable Evidence

ADDF Light Games includes learning because the human should understand the *design and engineering consequences* of the decisions the AI helps implement.

## When to use

Use when teaching game mechanics, systems or level design, onboarding a nonprogrammer, or deciding which experiment to build next. A checkpoint is especially valuable when two alternatives have different player-facing tradeoffs.

## The six-part pattern

1. **Concept:** One relevant principle in accessible language.
2. **Concrete example:** How this principle appears in this game.
3. **Tradeoff:** Two legitimate approaches, not a false choice.
4. **Prediction:** What the designer expects to notice during play.
5. **Test:** A real playable or observable experiment with relevant acceptance criteria.
6. **Reflection:** Actual observations, uncertainty and any new decision.

No quiz score or compulsory “correct answer” is necessary. If the user wants only the implementation summary, keep the explanation short and provide a deeper link.

## Mechanic design example

**Concept:** Control feel depends on acceleration and stopping behavior.

**Options:** Direct speed gives predictable response; easing/acceleration can feel weightier but needs tuning and can mask collision mistakes.

**Prediction:** “Direct controls will make hazards easier to dodge but may feel abrupt.”

**Test:** Use one obstacle type and inspect input response in a minimal arena. Record both automated movement results and the human's feeling of responsiveness.

**Reflection:** The user may find direct speed too twitchy. That observation supports a revised experiment—not a claim the AI was wrong or that a theory was “failed” definitively.

## System design example

**Concept:** An enemy's state machine makes behavior legible through explicit transitions.

**Options:** Patrol/chase/return states versus a continuously evaluating goal-selection system.

**Test:** Observe whether players can tell when the enemy notices them. The first experiment might use only patrol and chase, with visual cues and one trigger.

**Reflection:** A player who cannot perceive the transition reveals a feedback-design issue; raw AI sophistication is not the only success metric.

## Level design example

**Concept:** Teach an ability with a safe introductory encounter before combining it with pressure.

**Options:** Forgiving first jump versus immediate challenge.

**Test:** New player attempts the first gap with no verbal coaching; observer notes hesitation, errors, retry behavior and cue readability.

**Reflection:** The human designer decides whether the level teaches the intended mechanic.

## Where evidence lives

The checkpoint and prediction belong in `SPRINT.md`; actual automated/manual results and human reflection belong in `REVIEW.md`. A material change in intended player experience goes into `DECISIONS.md`.

The AI may explain a result but must not claim the person learned something without an observation supporting it.

## Common failures

**Performative learning:** Add an unrelated quiz to every sprint. Replace it with a relevant prediction.

**No test:** The agent explains an algorithm but no player behavior is observed. Connect theory to a slice.

**One answer is treated as universal:** One playtest supports a local design choice, not an absolute claim about all players or engines.

## Related

[Guided discovery](guided-discovery.md) · [Human playtesting](../quality/playtesting.md) · [Design stage](../lifecycle/design.md)
