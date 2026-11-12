# ADDF Light — Approval and Authorization Policy

**Status:** Phase 01 draft — requires human verification  
**Authority:** Human operator / project owner  
**Related:** [Framework Specification](FRAMEWORK_SPEC.md) · [Workflow States](WORKFLOW_STATES.md) · [Decision Protocol](DECISION_PROTOCOL.md)

## 1. Purpose

ADDF Light is intentionally guided and easy to use, but **agent convenience never substitutes for human authorization**. There are three distinct gates:

| Gate | What the user approves | Record | Trigger |
| --- | --- | --- | --- |
| **D — Design choice** | The desired behavior and consequential design approach | `DECISIONS.md` referenced in `SPRINT.md` | Before finalizing a sprint that depends on a significant human choice |
| **I — Implementation authorization** | Exact paths, commands, dependencies, tests, and side effects | `PLAN.md` | **Before any implementation/source file changes** |
| **A — Acceptance** | Evidence-backed outcome after first-hand testing or review | `REVIEW.md` | Before a sprint can close as accepted |

The user may reject, request revision, defer, or withdraw approval. The agent records this accurately. It must **not** interpret a conversational acknowledgment, a tool success, or a passing test as human acceptance or broad permission.

## 2. Roles and permissions

- **Human operator:** Owns project intent, approves significant choices, implementation scope, external effects, and the final verdict.
- **Research role:** Produces evidence and uncertainty; cannot make design commitments or modify product code.
- **Design role:** Drafts requirements, options, plans, and review forms; may not write implementation code.
- **Develop role:** May change approved files after a valid Gate I, run only approved commands, and report verification evidence. May not self-approve.
- **Automated testing/CI:** Provides independently inspectable results, not a substitute for Gate A.

The stages Research → Design → Implement → Refine → Acceptance describe the **user experience**; these roles describe allowed **write actions**. Stage names alone never grant new permissions.

## 3. Gate D — Significant design decisions

A decision is consequential when it changes intended experience, user-visible behavior, architecture, scope, technology, cost, reversibility, risk, privacy, or external dependencies.

Before asking for Gate D, the agent must present:

1. **Question and context:** what needs to be decided and why now.
2. **Two or three practical alternatives** when genuine alternatives exist; do not invent false options.
3. **Tradeoffs:** player impact, learning goals, implementation cost/complexity, risks, and reversibility.
4. **Recommendation:** clearly labeled as the agent's suggestion, not an approved choice.
5. **Unknowns:** what is unverified and what experiment could settle it.
6. **One direct question**, permitting “not sure yet” or “research more.”

Valid outcomes:

- **Chosen:** record the user's selection, its rationale, and where it constrains the sprint.
- **Deferred:** retain the open question, identify a reversible default or research spike only if the user allows that approach.
- **Rejected:** return to Design/Research.
- **Withdrawn:** update the decision log and invalidate affected sprint plans.

A low-impact internal implementation detail may be chosen by the agent within an already approved approach; log it when useful, without repeated approval requests.

## 4. Gate I — File-level implementation authorization

**Gate I is mandatory before the first change to source code, project dependencies, runtime configuration, asset files, tests, or deployment configuration.** Drafting `PLAN.md` and research/design Markdown is not itself implementation.

The proposed `PLAN.md` must contain:

- Sprint ID, link to the approved `SPRINT.md`, and plan revision/identifier.
- **Create, modify, delete, and move paths** (exact paths or narrowly bounded directories/globs with a clear expansion limit).
- Commands to run and their possible side effects, including downloads/installations/network access.
- Dependencies to add/upgrade/remove, with version or pinned resolution policy where possible.
- Risks, secrets boundaries, external services, irreversible operations, and rollback approach.
- Testing and verification strategy.
- Ambiguities requiring human choice.
- An explicit **authorization section** recording who approved *which revision* and what exceptions, if any, were granted.

**Proposed is not authorized.** An agent must stop after proposing the plan and ask for permission to implement.

Examples of explicit authorization:

> “I approve Sprint 001, Plan revision 2, including the listed files and npm install; implement within that scope.”

> “Approved: the five listed changes only. Do not modify assets or dependencies.”

Insufficient:

- “Looks interesting.”
- “Let's do this” said about a concept before seeing the file plan.
- Prior permission for a different sprint.
- An unsigned check box or agent-generated statement saying “approved.”
- Silence or time passing.
- A GitHub branch existing or a CI job passing.

A single message may satisfy Gate D and I **only when** the user has been shown both the concrete design choice and the full implementation scope, and explicitly approves both.

## 5. Approval validity and stale plans

Implementation authorization is valid only for the displayed plan revision and scope.

**Invalidate Gate I and return to `awaiting_approval` if any of these change:**

- Files outside the approved set would be edited, moved, or deleted.
- Dependency list, version, install procedure, or required permission changes.
- A command with new side effects or an unapproved external service is required.
- User-facing outcome or accepted design changes materially.
- Risk tier increases (security/privacy, data migration, external publication, money, destructive action).
- Source state changed enough that the plan no longer describes what will actually be edited.
- The human withdraws or narrows approval.

The agent preserves current work safely, documents the deviation, revises `PLAN.md`, and asks the human again. **No self-escalation.**

An approved plan may include bounded retries and minor bug fixes without re-approval if they stay within its specified paths, commands, risk envelope, and intended behavior.

## 6. Special permissions

The following actions require **separate, explicit** consent even if general implementation is approved:

| Special operation | Required guard |
| --- | --- |
| Delete substantial data, reset Git history, or overwrite unrelated human changes | Specific affected paths and recovery plan |
| Add credentials, read secrets, transmit private source or personal data | Clear scope and security review; never print secrets |
| Install unknown packages, run remote installers, or execute downloaded scripts | Explain provenance, exact command, and consequences |
| Deploy/publish publicly, merge to protected branches, alter access controls | Explicit environment/repository authorization |
| Contact external parties, make purchases, incur paid API usage | Explicit separate user approval and boundaries |
| Run background/unattended operations | Explicit duration, scope, stop conditions, and accountability where tooling supports it |

Do not infer authorization to perform these actions from a broad “build the game” instruction.

## 7. Gate A — Human acceptance

Acceptance is based on the *experience*, not just the existence of code.

Before requesting Gate A, the agent prepares `REVIEW.md` with:

- The original acceptance checks from `SPRINT.md`.
- Changed-file summary and build/test evidence with reproducible commands.
- A playable build or direct way to inspect the outcome, when applicable.
- Human playtest instructions, observations to record, known issues, and accessibility/device constraints where relevant.
- Empty verdict fields for **accepted**, **accepted with conditions**, **needs refinement**, **rejected**, or **paused**.

Only the human enters or explicitly provides the acceptance verdict. The agent may transcribe a clear human verdict with a source reference, but must not invent the user’s playtest experience, sign on their behalf, or silently close the sprint.

**Accepted with conditions** means the specified conditions remain tracked. It must not be represented as unconditional acceptance, and unaddressed release-blocking conditions prevent release.

**Needs refinement** returns to `refining` or planning, within the limits of an existing valid Gate I.

**Rejected** preserves the verdict and reasons, then requires the user to choose whether to revise or abandon the sprint. A later review round must not overwrite the old verdict.

## 8. Reviewable approval records

Each gate record should include:

- Gate code (`D`, `I`, or `A`), sprint ID, related decision or plan revision.
- Human actor, decision, and date/time **if actually known**.
- Evidence: user response, reviewed document, ticket, signed pull-request review, or other durable record.
- Conditions and boundaries.
- Agent transcription note if recorded from conversational approval.

In this file-first method, the user need not manually type the entire record; the agent can transcribe it from an actual explicit approval. An unverified statement in an agent-created file is not independent evidence of human consent.

## 9. Fail-closed examples

| Situation | Correct behavior |
| --- | --- |
| User chooses platform but has not seen file/command plan | Record Gate D; **stop before code edits** |
| Plan includes npm dependency, user approves only code | Do not install; revise or ask for explicit dependency approval |
| Agent needs another file after starting | Stop, disclose exact file and reason, revise plan, request Gate I again |
| Tests pass but user has not played | Mark `awaiting_acceptance`, not `accepted` |
| User playtests and reports a crash | Record defect; propose a correction; use valid approved scope or seek re-approval |
| User says “reject Sprint 002” | Record `rejected`; do not quietly close or mark accepted |
| Session resumes without verifiable prior authorization | Return to `awaiting_approval` or `paused` |
| User has not asked for deployment | Do not publish the game |

## 10. Manual verification for Phase 01

- [ ] Distinguishes design choices, file-authorized execution, and experiential acceptance.
- [ ] Lists exactly what a plan must expose before implementation.
- [ ] Specifies when approvals become stale.
- [ ] Prevents AI self-authorization, self-acceptance, and silent deployment.
- [ ] Handles rejections, revisions, uncertain user choices, and resumption.
- [ ] Agrees with [Workflow States](WORKFLOW_STATES.md) and [Decision Protocol](DECISION_PROTOCOL.md).

**Status:** Draft for human verification. This document cannot authorize its own adoption.
