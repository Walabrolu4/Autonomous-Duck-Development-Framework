# ADDF Light — Framework Specification

**Edition:** ADDF Light, first implementation candidate  
**Status:** Phase 01 draft; requires human verification before Phase 02  
**Parent methodology:** Autonomous Duck Deployment Framework (ADDF), framework v3.5  
**Canonical branch:** `feature/addf-light`  
**Document owner:** framework design / human maintainer  
**Related contracts:** [Workflow States](WORKFLOW_STATES.md) · [Approval Policy](APPROVAL_POLICY.md) · [Decision Protocol](DECISION_PROTOCOL.md)

> **The AI manages the process; the human owns the decisions; each sprint produces verifiable progress.**

## 1. Purpose and success criteria

ADDF Light is a file-first methodology for collaborative, iterative development with AI agents. It reduces the *operator's burden* while preserving meaningful control, durable project memory, safe implementation boundaries, and testable outcomes.

It is a complete sibling edition, not a stripped-down tutorial and not a different tool product. It must work with human-directed chats as well as coding agents; no account, provider, engine, or paid orchestration service is inherently required.

Game development is the first supported demonstration domain because playable feedback makes the acceptance cycle concrete. The core method must remain adaptable to other software and interactive projects.

A first-time user succeeds when they can:

1. Begin with **no idea**, **one sentence**, or **an existing project**.
2. Explain an intended user/player experience through short, useful questions rather than writing a lengthy specification.
3. Understand and choose between consequential design alternatives.
4. See a bounded sprint goal, a credible implementation plan, risks, and tests *before* any code is changed.
5. Approve the implementation scope explicitly.
6. Test a playable or otherwise directly observable deliverable, provide feedback, and request refinement.
7. Personally accept or reject the outcome.
8. Resume with a new AI session using repository files instead of relying on chat history.

## 2. Relationship to full ADDF

Both editions share the same foundational principles:

- **The files are the project.** Repository Markdown is the durable source of truth; chats are ephemeral working context.
- **A duck cannot invent project intent.** AI may propose options; the human controls meaningful product, design, and risk decisions.
- **Cleaner context beats more context.** Load the smallest verified file set needed for the current step.
- **Research is not implementation authorization.** Seeing a possible solution is not permission to build it.
- **Automated tests are evidence, not human acceptance.** Agents do not approve their own outcome.
- **Traceability matters.** Approved scope, source/evidence, changes, results, and next steps are reconstructable.

Differences from full ADDF:

| Dimension | Original ADDF | ADDF Light |
| --- | --- | --- |
| Reader's interface | Explicit engineering modes, extensive operating protocol | Five visible, repeated lifecycle stages |
| Initial setup | Broad project brain and separate sprint artifacts | AI-guided discovery and a smaller mandatory project brain |
| Sprint records | Separate requirements/blueprint/acceptance/dry-run/log/review | Consolidated `SPRINT.md`, `PLAN.md`, `REVIEW.md` with mandatory sections |
| Human decisions | Formal reviews and permission tiers | Three intuitive human gates, with formal escalation when needed |
| Scope | General engineering and release governance | Game/interactive projects first; optional advanced records |
| Documentation | Extensive | Equally rigorous, but layered: Quick Start → wiki → full manual |
| Agents | Model-agnostic prompts/modes | Same, with guided interviews and first-class learning checkpoints |

**Non-goal:** Removing review merely because a user is inexperienced. Light reduces unnecessary files and repetitive formality—not the human's decision rights.

## 3. Supported starts

### A. No idea

The agent offers two or three **small, differentiated** starting directions, each describing who plays, the core action, and how the experience could be verified in a first sprint. The agent asks one consequential question at a time when practical, permits “not sure,” and records provisional answers. It must not claim a complete game vision is known.

### B. One-sentence idea

The agent extracts the likely player action, intended experience, constraints, and unknowns; labels assumptions; asks only what is necessary to define a first playable milestone; and offers a small vertical slice rather than a complete production roadmap.

### C. Existing project

The agent first reads approved repository files and inspects the codebase **without changing it**. It reports the current project facts, unverified assumptions, immediate risks, existing run/test commands, and a possible first sprint. It must not overwrite user documentation, reinitialize Git, migrate dependencies, or change the engine without separate authorization.

## 4. The five-stage lifecycle

Every substantive sprint moves through:

**Research → Design / Ideation → Implement → Refine → Acceptance**

These are *user-facing lifecycle stages*, not permission levels. Internally, actions still obey Research / Design / Develop write boundaries inherited from ADDF. A stage may loop backward when evidence requires it.

| Stage | Purpose | Inputs | Agent outputs | Human role | Exit condition |
| --- | --- | --- | --- | --- | --- |
| Research | Reduce uncertainties relevant to the next slice | User goal, current files, concrete questions | Evidence, alternatives, unknowns, risk notes | Clarify what matters; review consequential findings | Enough evidence to choose a design or an explicitly labeled experiment |
| Design / Ideation | Choose one testable outcome and approach | Research, constraints, backlog | Recommended direction, alternatives, `SPRINT.md` draft, acceptance checks | Make or defer consequential choices; approve sprint design | Documented design decision and bounded, testable sprint scope |
| Implement | Deliver the approved change | Approved `SPRINT.md` and `PLAN.md` | Source changes, test/build results, changed-file report | Review dry-run scope and grant authorization before edits | Change matches scope or stops for re-approval |
| Refine | Respond to observed failure and player feedback | Build, tests, playtest observations | Diagnosis, small correction plan, revised evidence | Describe observations, prioritize, approve expanded scope | Evidence supports readiness for human acceptance or a documented stop |
| Acceptance | Validate the user-facing outcome | Acceptance checks, evidence, human test | Prepared `REVIEW.md`, limitations, suggested next sprint | Perform test; record verdict; accept, reject, or defer | **Human-authored** verdict plus state update; only accepted work closes normally |

A failed or unresolved stage is not hidden by moving forward. The agent records the blocker, suggests a next action, and stops where authorization would be required.

## 5. Sprint definition and sizing

A **sprint** is one bounded piece of work producing one independently observable outcome, with acceptance criteria set *before implementation*. A sprint is not necessarily a calendar week.

Default rules:

1. **One user-visible outcome.** For games, prefer an interactive, playable, or measurable slice.
2. **Minimal dependencies.** Do not combine unrelated mechanics, art pipelines, networking, and deployment in one sprint.
3. **Observable acceptance.** “The game is fun” is not testable; “the player can move and reliably avoid obstacles for 30 seconds” is.
4. **Learning objective.** Identify the most consequential concept or tradeoff the user should understand this sprint.
5. **Timebox as a constraint, not a promise.** The agent can suggest reducing scope rather than inventing timing certainty.
6. **No cross-sprint blank-document forest.** Create the next sprint only when it is chosen.
7. **Research-only spikes are allowed** when the deliverable is a demonstrable feasibility answer, but must be labeled as a spike; they are not claimed as playable features.

A sprint must not be described as accepted simply because code exists, builds pass, or the agent says it is complete.

## 6. Project brain: conceptual minimum

Phase 02 will define final schemas. The Phase 01 architecture decision is to maintain:

- `AGENTS.md` — executable behavioral rules for agents and tools.
- `GAME.md` — living game vision, player experience, constraints, and explicit unknowns.
- `STATE.md` — current stage/sprint, approved state, blockers, next action.
- `DECISIONS.md` — human decisions and material agent defaults with rationale.
- `SECURITY.md` — secret exclusions, unsafe commands, and external access policy.
- `planning/BACKLOG.md` — candidate playable slices, dependencies, and deferred work.
- `planning/sprints/sprint-NNN/SPRINT.md` — goal, research, chosen design, acceptance checks.
- `planning/sprints/sprint-NNN/PLAN.md` — dry run: file list, tools, commands, dependencies, risks, approval record.
- `planning/sprints/sprint-NNN/REVIEW.md` — tests, human feedback, refinement, and human acceptance.

A user should not have to author these manually. The agent maintains them and asks for review when the contents represent a meaningful commitment.

**Authority principle:** Stage/status and authorized scope come from the project brain, not an agent's memory of a prior conversation.

## 7. Permissions and agents

The three internal capabilities are:

| Capability | May do | Must not do |
| --- | --- | --- |
| Research | Read permitted context, gather and cite evidence, update research sections and open questions | Edit game code, declare architecture chosen, invent sources, claim approval |
| Design | Draft/update vision, sprint, decisions, acceptance tests, and implementation plan | Edit game code, claim user made a decision not actually made |
| Develop | After authorization, edit **only** approved game/source/test files and run approved commands | Widen scope, add unapproved dependencies, access secrets, self-accept |

Design can prepare a plan; Develop cannot bypass it. Refinement with new code changes is again Develop work and must be covered by active authorization. A change in file scope, dependencies, external side effects, or risk tier requires a revised plan and renewed approval.

No agent may merge/publish, spend money, change access controls, delete unrelated files, or contact third parties without separately explicit authority.

## 8. Human gates

There are exactly three mandatory classes of human control. They can be lightweight conversational approvals, but the record must be clear.

**Gate D — Design decision.** Confirms the significant sprint direction and acceptance goal. An explicit rejection returns to Design.

**Gate I — Implementation authorization.** Confirms the precise planned writes, commands, dependencies, tests, and risks in `PLAN.md`. This gate must happen *before code changes*, including for “quick fixes” that modify source.

**Gate A — Human acceptance.** Records first-hand playtest or comparable user verification and a final verdict in `REVIEW.md`. The agent may prepare questions and evidence but cannot sign.

Detailed semantics and failure cases: [Approval Policy](APPROVAL_POLICY.md).

## 9. Learning by making decisions

Light must teach at moments where understanding alters implementation. For significant choices, the agent:

1. Asks what outcome matters.
2. Explains **two or three materially different options** in plain language.
3. States tradeoffs, recommended default, evidence, and uncertainty.
4. Asks one clear decision question; “I don't know yet” is acceptable.
5. Records the actual choice or provisional experiment, not a fictional commitment.
6. Revisits a provisional choice when playtesting supplies new evidence.

A tutorial dump, repeated quiz, or lecture before every code edit violates the Light intent. The goal is informed agency, not bureaucratic friction.

See [Decision Protocol](DECISION_PROTOCOL.md).

## 10. Research and evidence rules

Research claims must carry a URL, document path, command output, measurement, or first-hand observation. Distinguish:

- **Verified:** supported by visible evidence;
- **Inferred:** reasonable but not directly proven;
- **Proposed:** recommendation or hypothesis;
- **Unknown:** requires research or experiment.

Never invent citations, test outcomes, numbers, package versions, or compatibility statements. When external information cannot be verified, recommend a small experiment or defer the decision.

## 11. Stop and escalation conditions

An agent must stop and request human input when:

- No defensible first-sprint goal can be extracted without a consequential choice.
- User intent conflicts with documented project constraints.
- Proposed code edits exceed the authorized paths or commands.
- A new package, API credential, external account, paid service, or network integration is needed.
- A security, privacy, data-loss, licensing, or external-deployment risk emerges.
- Tests fail in a way that changes project scope.
- Files contradict chat history, recorded approvals, or each other.
- The agent reaches Acceptance without a human-authored review.

Safe actions after stopping: report precisely what happened, preserve status/evidence, suggest next choices, and **do not claim completion**.

## 12. Portability and advanced escalation

Light must be usable with manual chat, Claude Code, Codex, and optional orchestrators without changing the decision record or source of truth. Tool-specific adapters may supplement, never override, `AGENTS.md`.

For complicated migrations, regulated systems, major data operations, multi-team releases, or risky refactors, Light either generates optional advanced records or recommends full ADDF. The process is explicitly **upward compatible**; a small project is never penalized for starting Light.

## 13. Phase 01 review and acceptance

This specification is **not implemented agent behavior**. It defines how later templates, prompts, tests, wiki, and website must behave.

Manual review checklist:

- [ ] Can a reader explain what Light is without confusing it with an autonomous coding service?
- [ ] Are the three supported project starts defined?
- [ ] Are the five stages and their exit conditions unambiguous?
- [ ] Is it impossible to infer implementation authorization from design approval?
- [ ] Does human acceptance remain separate from automated tests?
- [ ] Are the nine conceptual project files and their ownership clear?
- [ ] Are research, learning, and new-dependency decisions safe?
- [ ] Is a return to planning required after scope expansion?
- [ ] Do [Workflow States](WORKFLOW_STATES.md), [Approval Policy](APPROVAL_POLICY.md), and [Decision Protocol](DECISION_PROTOCOL.md) agree?

**Phase 01 exit gate:** A human verifies the four `spec/` files on the Light branch and approves the framework contract. Only then may Phase 02 begin.

---
**Source basis:** Original repository `README.md`, `AGENTS.md`, `START_HERE.md`, `docs/sprint-loop.md`, `docs/project-brain.md`, and the approved ADDF Light implementation roadmap. This is a **proposed Light adaptation**, not a claim that the original ADDF already uses this five-stage interface.
