# ADDF Light — Workflow States and Transitions

**Status:** Phase 01 draft; pending human sign-off  
**Applies to:** Every project and sprint following the Light edition  
**Owner:** Design-stage coordinator; status changes subject to the approval policy  
**Related:** [Framework Specification](FRAMEWORK_SPEC.md) · [Approval Policy](APPROVAL_POLICY.md) · [Decision Protocol](DECISION_PROTOCOL.md)

## 1. Two distinct concepts

**Lifecycle stage** answers *what kind of work is being done*: Research, Design / Ideation, Implement, Refine, Acceptance.

**Sprint status** answers *what must happen next and what is allowed*: discovering, designing, awaiting_approval, implementing, refining, awaiting_acceptance, accepted, rejected, paused.

Never equate “in the Implement stage” with “authorized to write code.” The implementation approval record is an independent precondition.

## 2. State inventory

| Status | Meaning | Typical visible stage | Allowed next states |
| --- | --- | --- | --- |
| `discovering` | Explore an idea, inspect existing project, investigate unknowns; no approved sprint design yet | Research | `designing`, `paused` |
| `designing` | Evaluate options, choose scope, set observable criteria, draft plan | Design / Ideation | `awaiting_approval`, `discovering`, `paused` |
| `awaiting_approval` | Written plan awaits **implementation** authorization; no game edits | Design / Ideation | `implementing`, `designing`, `paused` |
| `implementing` | Agent executes exactly authorized changes and commands | Implement | `refining`, `awaiting_acceptance`, `awaiting_approval`, `paused` |
| `refining` | Diagnose failures, use playtest feedback, re-run authorized fixes; re-plan if needed | Refine | `awaiting_acceptance`, `awaiting_approval`, `designing`, `paused` |
| `awaiting_acceptance` | Deliverable and review evidence are ready for human test and verdict | Acceptance | `accepted`, `rejected`, `refining`, `paused` |
| `accepted` | Human signed acceptance; records closed | Acceptance | **Terminal** for that sprint |
| `rejected` | Human rejected delivered outcome; recorded verdict and reason | Acceptance | `designing`, `refining`, `paused` or terminal if abandoned |
| `paused` | Work is blocked, canceled, interrupted, or awaiting an external precondition | Any | Previous safe non-terminal state after reconciliation |

A research-only feasibility spike may end in `awaiting_acceptance` with a human evidence review, but must say “research spike—not playable implementation.” Do not label a research conclusion as a completed game feature.

## 3. Required persistent state

Phase 02 will define exact Markdown headings; logically every `STATE.md` must provide:

- Project identifier and active sprint ID.
- Current lifecycle stage and one valid sprint status.
- Last completed human gate **with evidence reference**.
- Active implementation authorization ID and scope digest, if any.
- Outstanding consequential questions or blockers.
- Latest verified build/test or playtest evidence, if any.
- The immediate next action, responsible actor, and expected file update.
- Last confirmed timestamp/date if available; “unknown” instead of invented time.

Agent assertions alone may not populate approval evidence fields. Each signed gate must identify an actual human response, review, or external approval artifact.

## 4. Lifecycle transition protocol

On every proposed transition, the agent must:

1. Read the current `STATE.md` and the active sprint's `SPRINT.md`, `PLAN.md` and `REVIEW.md` if present.
2. Check whether the target state is in the transition table.
3. Check whether the relevant human gate is completed and non-stale.
4. Ensure no pending blockers invalidate the transition.
5. Update the appropriate authoritative file(s) before or together with `STATE.md`.
6. Report the transition in one short sentence, including what the user can do next.

A status change is not itself an approval. An approval is a separate human-authored event verified by [Approval Policy](APPROVAL_POLICY.md).

## 5. From a blank project to Sprint 001

**Initialize in `discovering`.** Only a working hypothesis or one-sentence user intent is required. The agent guides discovery.

**Transition to `designing`** once enough direction exists for a testable next milestone. Unknowns can remain if explicitly identified as assumptions or experiments.

**Record Gate D** for significant design choices. If declined, remain `designing`. If the decision is deferred, choose a reversible experiment or continue research; do not infer the choice.

**Prepare `SPRINT.md` and `PLAN.md`** and transition to `awaiting_approval`. Scope is still proposed.

**Record Gate I** in `PLAN.md` and verify the authorized scope digest is current. Only then transition to `implementing`.

**Implement and verify** within scope. If all tests/evidence are ready, enter `awaiting_acceptance`; if correction is needed, enter `refining`.

**Acceptance** is human-led; the user may accept, reject, request refinement, or pause. No default auto-accept timer exists.

## 6. Design approval versus implementation approval

Design approval must be recorded before implementation authorization is requested when significant choices exist. However, one conversational interaction can explicitly approve both **only if** the human has already been shown both the design choice and exact implementation plan and clearly authorizes both. Merely saying “sounds good” to a design sketch does not authorize file edits.

Gate D selects **what** outcome and approach the user wants; Gate I authorizes **which files/commands/dependencies** the agent may use. Gate A confirms **whether the result actually works for the user**.

## 7. Scope change and rollback transitions

A scope change after Gate I includes:

- Writing outside the approved file set.
- Adding, removing, or upgrading a dependency not included in the plan.
- Changing the requested user experience or accepted design direction.
- Introducing new network traffic, credentials, services, spending, or deployment actions.
- Deleting/renaming significant files or changing the data format.
- A new risk requiring higher permission.

The agent must **stop**, record what differs, revise `PLAN.md` (and `SPRINT.md` where applicable), invalidate the old authorization, transition to `awaiting_approval`, and request renewed Gate I.

If reverting approved changes is needed, propose explicit rollback actions. Do not force-reset, delete unrelated work, or automatically rewrite uncommitted human changes.

## 8. Refinement and rejection

A user may identify problems at any point. Record:

- What was observed (not merely “bad”).
- Reproduction steps, where possible.
- Whether the issue violates an existing acceptance criterion or constitutes a new requirement.
- Minimum correction proposal and tests.

**Existing-scope bug fix:** `refining` may use the still-valid Gate I *only if* the precise file/command scope and risk envelope remain unchanged.

**Expanded or changed scope:** transition to `awaiting_approval` for a revised plan.

**Human rejection:** enter `rejected` and preserve the original verdict. A new refinement attempt does not erase rejection. The agent can continue under a new review round or a new sprint after the user directs it.

**Abandonment:** record why and preserve a safe checkpoint. Do not convert rejection or abandonment into “accepted.”

## 9. Pauses, context loss, and resumption

On interruption:

1. Save last verified status, incomplete operations, test failures, and the next safe action.
2. Do not fabricate completion for an interrupted command or deployment.
3. Resume by reading file state and comparing it with source-control diffs and verifiable evidence.
4. If the status conflicts with authorization, **prefer the safer restriction** and ask for clarification.
5. An agent cannot resume directly into `implementing` unless a still-valid written authorization covers exactly the current plan and files; otherwise return to `awaiting_approval`.
6. If previous chat or tool memory disagrees with repository records, stop and reconcile; neither stale chat nor stale files should silently override fresh human instructions.

## 10. Cross-agent handoff

A different agent may replace the current agent if it can read:

- `AGENTS.md`, `SECURITY.md`, `STATE.md`;
- `GAME.md` and `DECISIONS.md` for project intent;
- The active `SPRINT.md`, `PLAN.md`, `REVIEW.md` for work-specific scope and evidence.

It must summarize the **current authorized next action**, unresolved risks, and which artifact supports the last approval. It must not continue code modification based solely on a predecessor's claim.

## 11. Conformance scenarios

| Scenario | Correct resulting status | Can edit game code? |
| --- | --- | --- |
| User says “make a small dodge game” | `discovering` | No |
| User chooses a 2D browser target; criteria drafted | `designing` | No |
| Sprint and file plan prepared, no explicit permission | `awaiting_approval` | No |
| User approves design but not file/command plan | `awaiting_approval` | No |
| User authorizes plan with listed files and commands | `implementing` | Yes, within exact scope |
| Agent discovers it needs an extra dependency | `awaiting_approval` | No further edits until approved |
| Build succeeds, user has not playtested | `awaiting_acceptance` | No new unapproved edits |
| User finds a collision bug in approved file scope | `refining` | Only within still-valid scope |
| User says the level is not acceptable | `rejected` | No new code without an authorized correction scope |
| User tests again and explicitly approves | `accepted` | Sprint closed |
| Context resets and approval cannot be verified | `awaiting_approval` or `paused` | No |

## 12. Phase 01 manual verification

- [ ] Every status is defined exactly once.
- [ ] There is a route from `discovering` to `accepted` without skipping authorization.
- [ ] No route to `implementing` exists without Gate I.
- [ ] A test pass never changes status to `accepted` automatically.
- [ ] A rejected sprint cannot be rewritten as accepted by an AI.
- [ ] An interruption cannot implicitly renew authorization.
- [ ] Revisions within authorized scope and scope-expanding revisions have different handling.

**Status:** Proposed policy, awaiting the human's explicit Phase 01 sign-off.
