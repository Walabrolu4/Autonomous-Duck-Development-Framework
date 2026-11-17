# Guided Discovery: Ask Less, Decide Better

The point of guided discovery is not to make an AI more chatty. It's to help a designer transform uncertainty into **small, informed, human-owned choices** while maintaining a usable project record.

## When to use

Use for new game ideas, an uncertain mechanic, a student who is learning design, or a returning developer unsure how to approach the next playable feature.

## One meaningful question at a time

The default pace is a **single consequential question** per turn. A batch of up to three related questions can be useful if the person opts for faster intake, but avoid demanding ten independent preferences before showing anything useful.

Ask a question *because an immediate decision depends on it*. “Would you prefer direct or inertia-based movement?” is actionable. “What is your favorite color and music genre?” is probably not actionable while movement hasn't been tested.

## The discovery ladder

1. **Player verb:** move, aim, rotate, trade, negotiate, connect, select, build, hide?
2. **System response:** how does the world visibly react to that verb?
3. **Player feedback:** can a novice tell what changed and why?
4. **Smallest experiment:** which five-minute playable slice will test the hypothesis?
5. **Important fork:** which difference might materially change the player's experience?
6. **Human choice:** select, defer, reject or request more evidence.
7. **Durable record:** agent updates `GAME.md`, `DECISIONS.md`, backlog and the active sprint.

Don't march through all seven as a form. Use only what the user's current answer and goal require.

## Option design

When proposing concepts, ensure choices differ **mechanically**. Avoid three identical dodge games wearing different themes. For each option, include one action, one response, one smallest prototype and one uncertain tradeoff.

Recommend an option when helpful, but label it clearly as a recommendation. “I don't know” should lead to a **reversible experiment or focused research**, not forced agreement.

## Example — level design learning

A student wants to teach a player a new jump ability. The agent offers:
- a low-risk introductory gap with safe recovery;
- a timed obstacle requiring the jump immediately.

It explains onboarding, failure cost and feedback tradeoffs, and asks which one the student wants to prototype first. Later the playtest should reveal whether a player notices the jump cue. That's an observable learning checkpoint.

## Recording without bureaucracy

A selected significant choice becomes a `D-###` entry with context, options and actual human response. A minor parameter inside an already approved technical plan may remain a routine T0 detail. The agent shouldn't force the user to hand-write either record.

## Common failures

**AI decides everything:** The agent presents a complete game design and asks for one approval. Break it into material choices.

**Indecision loop:** The assistant asks unlimited open questions. Offer a bounded experiment.

**Learning by lecture:** The agent explains theory without tying it to a gameplay test. Create a prediction and observation instead.

## Related

[Learning checkpoints](checkpoints.md) · [Decision records](decisions.md) · [No-idea start](../guides/from-zero.md)
