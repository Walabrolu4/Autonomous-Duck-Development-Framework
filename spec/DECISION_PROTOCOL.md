# ADDF Light — Guided Discovery and Decision Protocol

**Status:** Phase 01 draft — requires human verification  
**Owner:** Human directs significant choices; AI researches, teaches, proposes, records  
**Related:** [Framework Specification](FRAMEWORK_SPEC.md) · [Workflow States](WORKFLOW_STATES.md) · [Approval Policy](APPROVAL_POLICY.md)

## 1. Purpose

A user should be able to start from a vague idea, or no idea, **without writing a novel**. ADDF Light turns ambiguous intention into small, informed, reversible decisions. It does not blindly generate a whole game and ask the user to approve an unexpected outcome afterward.

The agent should be a thoughtful facilitator: ask less, explain better, record what matters, and defer decisions until there is a reason to make them.

## 2. The three entry routes

### Route A — No idea at all

Ask one open, accessible starting question, such as:

> “Would you rather build something about movement, puzzles, or strategy—or should I suggest three tiny game concepts?”

If the user wants suggestions, offer **two or three distinct small concepts**. For each, show:

- Core player action (one sentence).
- Intended emotion or skill (one sentence).
- First playable proof of concept (one sentence).
- Biggest uncertain mechanic/technical constraint.

Do not generate the full game design before the user selects a direction.

### Route B — One-sentence idea

Reflect the idea concisely, separating:

- **Known:** words and constraints explicitly provided.
- **Inferred:** plausible interpretation, not yet confirmed.
- **Open:** matters necessary for a testable first sprint.

Ask the highest-impact question first, not a ten-item questionnaire. Propose a minimal experiment if the user is unsure.

### Route C — Existing project

Read only safe, relevant repository context. Offer:

1. Observed stack and what appears runnable.
2. Current known behavior, distinguishing verified from inferred.
3. Existing design intent from project records.
4. Risks and unknowns.
5. One proposed milestone with visible validation.

Do not erase existing files or impose default starter templates without a reviewed import plan. Existing-user intent takes precedence over invented project goals.

## 3. Question budget and response pacing

- **Default:** one consequential question per assistant turn.
- **At most three related consequential questions** in one batch when the user opts for speed or the questions genuinely must be considered together.
- Do not ask for information already in project files or the user’s current instructions.
- Avoid interrogating the user about cosmetic options, naming, file layout, or technical minutiae when safe defaults suffice.
- Offer **“I don't know yet”** and **“show me a small prototype”** pathways.
- Explain why the current question affects what is built; avoid motivational filler.
- Keep suggestions short by default, but provide a link to a deeper research note when the decision is technical.
- After a choice, summarize in a few lines what changed and continue the lifecycle.

These are facilitation defaults, not hard limits that prevent a user from requesting a detailed workshop.

## 4. Decision classification

| Tier | Typical examples | Agent responsibility | Human control |
| --- | --- | --- | --- |
| **T0 — Routine** | Local variable names, formatting within style rules, harmless documentation organization | Choose according to conventions; log only if noteworthy | No separate gate |
| **T1 — Significant** | Core mechanic, input model, level pacing, engine/platform choice, gameplay feedback style, new systems | Explain alternatives and recommend a path | **Gate D** human choice |
| **T2 — High-impact** | Monetary services, networked gameplay involving user data, licensing/IP risk, destructive migrations, public deployment, new privileged credentials | Investigate risks; offer safer alternatives; require explicit scope and rollback assessment | **Gate D**, stronger **Gate I**, separate special authorization where needed |

Tier reflects **consequence and reversibility**, not whether the underlying code looks simple. If a “routine” change changes user-visible behavior or cost, escalate to T1/T2.

## 5. The decision briefing format

For every T1 or T2 choice, provide a compact briefing:

**Decision:** What must be chosen?  
**Why now:** What future work depends on it?  
**Option A / Option B / [Option C]:** Genuine alternatives, not strawmen.  
**Tradeoffs:** Player impact, production complexity, performance, accessibility, maintenance, learning, reversibility.  
**Evidence / uncertainty:** Links, actual docs, measurements, or clear hypothesis labels.  
**Recommendation:** Agent proposal with rationale.  
**Human question:** One clear selection, deferral, or research request.

Do **not** overwhelm the user with every possible variation. Discuss only factors capable of changing the implementation decision.

## 6. Learning checkpoints

At least one meaningful **learning checkpoint** should be considered in every sprint. It is not necessarily a quiz. The goal is that a user learns why the system is built the way it is.

Suggested structure:

1. **Concept:** Explain one relevant game design or engineering principle, in plain language.
2. **Concrete example:** Show how it affects the current game.
3. **Tradeoff:** Compare two approaches or constraints.
4. **Prediction:** Ask what the user expects to happen during a simple playtest, when useful.
5. **Test:** Have the user observe the result during the actual prototype/playtest.
6. **Reflection:** Record whether the result supported the user's prediction and whether the design changes.

Examples:

- *Movement feel:* acceleration-based versus instant-speed movement.
- *AI enemies:* rule-based finite-state machines versus goal scoring.
- *Difficulty:* increasing spawn rate versus reducing recovery time.
- *Player feedback:* animation-only signaling versus sound plus visual cue.
- *Level design:* safe introductory encounter versus immediate challenge.

Avoid creating fake exams, patronizing explanations, or required “correct answers” unrelated to the user's decision.

## 7. Research before committing

Research is useful when an unknown could change scope, viability, technical cost, or user experience. Keep it focused on the **current sprint**.

A small research record should include:

- Question or hypothesis.
- Source URL, specific repository document, test script, or measurement.
- What the evidence actually supports.
- Remaining uncertainty.
- Options and implications.
- Proposed experiment or recommendation.
- Human outcome (selected / deferred / rejected / requested more research).

**Evidence grades:** verified, inferred, proposed, unknown. Do not convert a plausible guess into a source-backed fact. If no authoritative evidence is available, propose a limited spike and label it as such.

Research does not authorize implementation or decide among consequential alternatives without the user.

## 8. From decisions to project files

Proposed ownership in Phase 02:

| Information | Canonical destination | Update moment |
| --- | --- | --- |
| Stable game goals, experience pillars, platform constraints | `GAME.md` | Once the human confirms or changes intent |
| Significant choices and alternatives, with traceable IDs (`D-001`) | `DECISIONS.md` | When choice is made, deferred, reversed, or superseded |
| Unresolved questions and next research action | `SPRINT.md` and/or `STATE.md` | During discovery and planning |
| Selected next playable milestone and acceptance tests | `SPRINT.md` | At Gate D |
| Exact execution scope and Gate I record | `PLAN.md` | Before and when authorizing implementation |
| Observed playtest outcome and Gate A verdict | `REVIEW.md` | After human evaluation |
| Current position and immediate next action | `STATE.md` | Whenever a stage or approval changes |
| Future ideas and rejected/deferred scope | `planning/BACKLOG.md` | When not needed for the current sprint |

The agent generates/updates these, but project intent and human approvals remain human-controlled. Decisions must **not** exist only inside a chat response.

## 9. Decision record minimum

A material decision entry should include:

```md
### D-001 — [Question]
- Sprint: sprint-001
- Status: chosen | deferred | rejected | superseded
- Tier: T1 | T2
- Context: [why needed]
- Options: [real alternatives]
- Recommendation: [AI suggestion, if any]
- Human choice: [actual wording or linked approval]
- Evidence: [source/test or "not yet verified"]
- Consequences: [what it changes in scope, design, or tests]
- Revisit when: [specific observation or trigger]
```

Never fill “Human choice” with an agent inference. Label unanswered decisions as deferred rather than silently picking the recommendation.

When changing a decision, add a new entry referencing the superseded ID, or preserve a dated update history. Do not destroy the reasoning for the earlier choice.

## 10. Worked example: first game from nothing

**User:** “I want to make a game, but I don't know what kind.”

**AI (discover):** “Would you prefer a small dodge game about reaction time, a puzzle about connecting paths, or a simple two-unit tactics game? Each can have a first playable browser version with placeholder art.”

**User:** “Dodge game.”

**AI (research/design):** “Two practical movement styles: immediate directional movement (easy to learn and test) or acceleration-based movement (more expressive but needs tuning). I'd prototype immediate movement for Sprint 001, then test whether it feels too rigid. Which do you prefer?”

**User:** “Immediate, for now.”

The agent records this as `D-001`, drafts a first sprint such as “move a character to avoid one repeating hazard,” proposes acceptance criteria, and shows the scoped file/command plan. **It does not begin building until Gate I.**

**AI (implementation authorization):** “The plan creates the Phaser project source and one test, installs the approved dependency, and runs the browser build. Do you approve this exact scope?”

**User:** “Yes, approve Sprint 001 plan revision 1, with no deployment.”

Only then may the coding agent implement within the approved scope.

**AI (acceptance):** “Please launch the playable build, confirm input responsiveness, and report whether avoiding the hazard is clear. Here's what passed in automated checks and what remains unverified.”

**User:** “The hazard isn't visually obvious; revise it.”

The agent records the observation, proposes an in-scope correction or a revised plan, then returns for a human retest. It does **not** accept the sprint because compilation succeeded.

## 11. Anti-patterns and required recovery

| Anti-pattern | Recovery |
| --- | --- |
| Ten onboarding questions before any useful suggestion | Summarize known context; ask the single highest-impact question |
| One-shotting a full game from a concept pitch | Propose a minimal playable slice and defer the rest to backlog |
| Pretending an AI recommendation is human design approval | Mark choice as proposed and ask Gate D |
| Repeating research without helping the user decide | State evidence, concrete tradeoff, recommendation, and decision question |
| Asking for user consent for every trivial line of code | Honor the approved plan; avoid unnecessary T0 gates |
| Requiring user to hand-write extensive Markdown | Draft records automatically; ask user to verify consequential content |
| Treating test success as player acceptance | Prepare human playtest checklist; wait for Gate A |
| Changing an old decision silently | Record supersession and update dependent scope/tests |
| Inferring user understanding from “okay” | Offer optional explanation and observe choices/playtesting, never claim comprehension without evidence |
| Losing a decision when switching models | Recover from `DECISIONS.md` and `STATE.md`; reconcile with current user |

## 12. Manual verification for Phase 01

- [ ] Each entry route requires minimal initial user writing.
- [ ] Distinguishes agent choice from human-owned choices.
- [ ] Includes “not sure yet” paths and reversible experiments.
- [ ] Makes research accountable to evidence and uncertainty.
- [ ] Connects learning to actual implementation and testing decisions.
- [ ] Provides a concrete, realistic first-sprint interaction.
- [ ] Does not conflate design consent, implementation authorization, and human acceptance.

**Status:** Draft for explicit human approval before Phase 02.
