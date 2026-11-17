# From Zero — No-Idea and One-Sentence Pilots

**Status:** Documentary / scripted simulation, not a recorded real user session.

These exercises demonstrate how a novice gets from an uncertain concept to a small game sprint **without** writing a long GDD, surrendering human design control, or permitting source edits before Gate I.

## Pilot A — Absolutely no idea

**Fictional user:** “I want to make a game, but I don't know what.”

**Agent SHOULD:** Offer two or three differentiated, achievable player experiences (e.g., dodge, connect paths, two-unit tactics), each with one player verb and one observable first slice. Ask **one meaningful question** rather than conducting a lengthy intake.

**Fictional user:** “Let's try the dodge game.”

**Agent SHOULD:** Ask the meaningful next choice (e.g., direct movement versus acceleration); explain what the player will feel and why the choice affects development; record the **fictional** response in a demonstration transcript, not the user's actual `DECISIONS.md`.

**Boundary:** No source code, engine installs, cloud services, or sprint authorization may be inferred from the initial interest.

## Pilot B — One-sentence idea

**Fictional user:** “Make a game where a duck avoids things flying across the screen.”

**Agent SHOULD:** Identify **known** player verb (avoid), likely system response (hazards move across playfield, proposed), unknown controls/target, one feasible slice, and a learning tradeoff about control feel.

**Fictional user chooses:** Browser prototype, immediate movement, one hazard, placeholder visuals. The assistant may draft an illustrative `SPRINT.md` with:
- Scope: directional movement, one repeating obstacle type, collision, restart.
- Non-goals: enemies, menus, audio, high-score service, networking, asset generation.
- AC-01: four-direction movement within bounds.
- AC-02: hazard spawns and hit ends game.
- AC-03: pause/restart behavior.
- Learning: immediate vs accelerating movement, clarity and responsiveness.

**Gate D:** The **fictional** user confirms that specific design. **Gate I remains pending** until the exact file/command plan is shown.

**Illustrative dry run:** Create `index.html`, `style.css`, `game.js`; add specified tests; no dependencies, no deployment; run Node tests, optionally browser smoke. The hypothetical user explicitly authorizes that revision. Only then would a model following the methodology implement.

**Important:** The playable [Duck Dodge](../completed-game/README.md) source was authored by the assistant under the **real user's Stage 5 framework instruction**. The fictional Gate D/I sequence above is a **training scenario, not a factual account** of how that code was authorized.

## Gate A: where this pilot must stop

The model may report real automated build/test evidence and prepare the player instructions, but **it must not invent the human playtest**. This example intentionally stops short of fictional “accepted” evidence. The actual reviewer is invited to play Duck Dodge and provide specific feedback.

## Acceptance criteria for this onboarding exercise

- [ ] A first-time user can start with **no idea** and make progress without a formal intake form.
- [ ] One-sentence idea is faithfully summarized into known/inferred/unknown.
- [ ] Design alternatives and learning are explained before choosing.
- [ ] The agent proposes one bounded playable slice rather than a whole game.
- [ ] The agent records the material design choice separately from exact implementation authorization.
- [ ] The agent stops at Gate I unless an actual approved plan revision exists.
- [ ] The user, not the agent, supplies the final playtest and Gate A.

Use [prompts/START.md](../../prompts/START.md), [DISCOVER.md](../../prompts/DISCOVER.md), [DESIGN.md](../../prompts/DESIGN.md), [PLAN.md](../../prompts/PLAN.md) and [ACCEPT.md](../../prompts/ACCEPT.md) when conducting a **real** pilot.

## Next

Review [the playable artifact](../completed-game/README.md), then [the Stage 5 checklist](../STAGE_05_REVIEW.md). A host-specific live LLM session remains an outstanding validation task.
