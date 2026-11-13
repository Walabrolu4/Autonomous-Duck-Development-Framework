# ADDF Light — Validation, Ownership, and Migration

**Status:** Stage 2 approved rules · not yet an executable validator  
**Depends on:** [Repository Architecture](REPOSITORY_ARCHITECTURE.md) · [Project File Contracts](PROJECT_FILE_CONTRACTS.md) · [Sprint File Contracts](SPRINT_FILE_CONTRACTS.md)  
**Runtime authority:** [Approval Policy](APPROVAL_POLICY.md) · [Workflow States](WORKFLOW_STATES.md)

## 1. Quality model

ADDF Light must be **simple to start, hard to accidentally misuse, and easy to audit**. Validation exists to catch obvious contract violations, not to pretend that an automated parser can prove the user actually consented or that a game is fun.

Three kinds of checks:

1. **Static checks:** file existence, heading names, field names, ID formats, cross-references, enum values, broken relative links.
2. **Process checks:** stage transition legality, human approval evidence present, scope deviation recognized, review completeness, safe resumption.
3. **Human checks:** design fit, level/playability, accessibility, quality of learning, acceptance. These cannot be delegated to a checkbox-generating agent.

Stage 6 may implement a lightweight validator; Stage 2 defines its expected behavior.

## 2. Required startup validation

| Project type | Must exist immediately | Not yet required |
| --- | --- | --- |
| Blank, not yet initialized | `SECURITY.md`, `AGENTS.md`, `GAME.md`, `STATE.md`, `DECISIONS.md`, `planning/BACKLOG.md` | Sprint directory and game source |
| Guided discovery, no chosen sprint | Same six; unknown values accepted | `SPRINT.md`, `PLAN.md`, `REVIEW.md` |
| Active sprint (design or later) | All six + active sprint's three documents | Extra release/feature/risk documents |
| Existing project adoption | Existing files remain untouched; read-only inventory first | Immediate copy/replacement of conflicting filenames |
| Accepted sprint | Nine files + actual human Gate A and result evidence | A particular cloud platform or engine |

Do not fail a blank starter kit merely because a user has not chosen a game title. Do fail a project if it claims implementation permission without a concrete Gate I.

## 3. Static validation rules

| Rule ID | Check | Error condition | Recommended behavior |
| --- | --- | --- | --- |
| `L-F001` | Required file paths | Missing mandatory file for current phase | Explain path and whether creation requires user approval |
| `L-F002` | Required headings and keys | Heading/key omitted or duplicated | Report exact file + heading/key |
| `L-F003` | Project/sprint IDs | Invalid ID or cross-file mismatch | Stop unsafe state changes |
| `L-F004` | Enum values | Unknown stage/status/revision | Show expected values |
| `L-F005` | Unique references | Duplicate `D-###`, `B-###` or `AC-##` in same namespace | Require human-guided correction |
| `L-F006` | Cross-document links | Broken required relative link | Show source and target |
| `L-F007` | Scope integrity | `PLAN.md` lists broad wildcard or unspecified file operations | Block authorization |
| `L-F008` | AC coverage | Review lacks an explicit result for an acceptance criterion | Block final acceptance |
| `L-F009` | Plan revision linkage | Gate I refers to a different plan revision | Block implementation |
| `L-F010` | Evidence placeholder | Claims passed/approved/accepted but source marked `pending` or unknown | Block state advancement |
| `L-F011` | Section consistency | `STATE.md` and active triplet disagree on sprint kind/ID | Request reconciliation |
| `L-F012` | Optional modules | Missing non-required docs | **Do not** fail validation |

Future validator outputs should use `pass`, `warn`, or `fail`, including file and rule ID; no fabricated success when a check could not be run.

## 4. Process invariants

### 4.1 Before code changes

**All required:**
- Active `SPRINT.md` contains a narrow goal and observable acceptance criteria.
- Gate D is recorded for consequential choices, or specifically marked `not_required` with a reason.
- Active `PLAN.md` specifies exact file operations and allowed commands.
- Gate I is an actual human approval for that plan revision and scope.
- No unapproved dependencies, network effects, secrets access or prohibited file paths.
- The repo/worktree state is known sufficiently to prevent overwriting unrelated work.

If one precondition is missing, do not edit implementation files; stop at `awaiting_approval` or `paused` with an actionable next step.

### 4.2 Before declaring `awaiting_acceptance`

- Agent reports exactly what it changed and which commands ran.
- Failed, skipped or unrun automated tests are visible.
- A usable build/instructions or accurately stated blocker is available.
- Every `AC-##` has an entry in `REVIEW.md`, even when `not_tested`.
- Known limitations and reproducible manual test instructions are documented.
- No silent deployment or merge occurred.

### 4.3 Before declaring `accepted`

- Human actually tested or reviewed the deliverable appropriate for `sprint_kind`.
- Gate A contains the human verdict/evidence.
- Release blockers are resolved or the result remains conditional and not releasable.
- State updates reference the exact accepted sprint/review round.
- A handoff/retrospective notes important learnings and future backlog.

**Never treat an automated code/test check as a human playtest.** A validator may flag missing acceptance evidence, but may not sign acceptance.

## 5. Approval integrity checks

Automated code cannot confirm that text represented as “human response” was truly authored by the user; it can only check format and consistency. Therefore:

- Gate D/I/A must refer to actual user-visible interaction or durable review artifact.
- Approval records must identify exactly what was shown to the user (revision and scope).
- `Gate I: authorized` with `human_response: pending` is invalid.
- A design-choice approval in `SPRINT.md` never authorizes code.
- A human review saying “tested it, looks good” cannot authorize **future** out-of-scope code.
- On a resumed session without trustworthy approval evidence, authorization degrades to `no`, and agent must request it again.
- A changed plan that materially expands scope invalidates previous Gate I even if the approval text remains in history.

When a user approves a design and a plan together, the record must include two distinct scope references—Gate D and Gate I—to avoid conflating them.

## 6. Write ownership by lifecycle and capability

| Document or code | Research capability | Design capability | Develop capability | Human-only authority |
| --- | --- | --- | --- | --- |
| `SECURITY.md` | Read; propose tighter exclusions | Draft restrictions for review | Read; never relax | Approve weakening/exception |
| `AGENTS.md` | Read | Draft revision proposals | Read, obey | Adopt/change operating permissions |
| `GAME.md` | Gather facts/suggestions | Draft/update approved intent | Read | Decide user goals |
| `DECISIONS.md` | Propose evidence/questions | Record decisions with human evidence | Read | Make T1/T2 choices |
| `BACKLOG.md` | Suggest candidates | Maintain/prioritize proposed work | Read | Set consequential priority |
| `STATE.md` | Document research stage (where allowed) | Update verified stages/approvals | Update actual build results via approved record | Approve gates; reconcile conflicts |
| `SPRINT.md` | Add cited research/questions only during planning | Create/edit design and acceptance checks | Read, no unilateral scope rewrite | Gate D and scope changes |
| `PLAN.md` | No implementation planning edits | Draft dry-run plan and revise for approval | Append actual execution record after Gate I | Gate I, commands/dependencies/scope |
| `REVIEW.md` | Add sourced research only if necessary | Prepare checklist and retrospective | Append actual tests and technical results | Gate A and first-hand playtest verdict |
| Game source/tests/assets | No writes | No writes | **Authorized Gate I scope only** | Grant scopes and special side effects |

Agent roles can be performed by **one underlying LLM**, but role boundaries and permitted writes still apply. An orchestrator may schedule/read tasks but cannot authorize itself.

## 7. Mapping from original ADDF to Light

This table maps **conceptual responsibilities**, not filenames that should be mechanically renamed.

| Full ADDF component | Light destination | Preservation rule |
| --- | --- | --- |
| `AGENTS.md` (3 modes, permission levels) | `AGENTS.md` | Preserve capability boundaries and dry-run gate in simpler language |
| `DOMAIN.md` | `GAME.md` | Keep user-facing goals and constraints; domain-specific advanced docs optional |
| `STATE.md` | `STATE.md` | Add explicit stage/status, approval references and next action |
| `DECISIONS.md` | `DECISIONS.md` | Preserve rationale/history and human authority |
| `SECURITY.md` | `SECURITY.md` | Keep exclusions and forbidden operations explicit |
| `COMMANDS.md` | `PLAN.md` commands; optional `COMMANDS.md` | Preserve reproducible commands without forcing an extra file |
| `QUESTIONS.md` | `SPRINT.md` unknowns; `STATE.md` blockers | Maintain visibility; optional separate cross-sprint list |
| `RISKS.md` | `SPRINT.md` risks; `PLAN.md` rollback; optional `planning/RISKS.md` | Do not lose security or migration risks |
| `GIT_STRATEGY.md` | `AGENTS.md` guardrails; `PLAN.md` operations | Preserve branch/recovery protection |
| `STYLE_GUIDE.md` | `GAME.md` pillars; optional design/style docs | Keep art direction when relevant |
| `PROMPT_CHANGELOG.md` | Framework `CHANGELOG.md`; optional project prompt version notes | Not required for each game |
| `planning/backlog.md` | `planning/BACKLOG.md` | Keep future outcomes but normalize ID/status |
| Sprint `requirements.md` | `SPRINT.md` | Maintain goal and testable requirements |
| Sprint `blueprint.md` | `SPRINT.md` (design) and `PLAN.md` (technical actions) | Separate what from how |
| Sprint `acceptance.md` | `SPRINT.md` criteria + `REVIEW.md` results | Define criteria *before* code; record observations afterward |
| Sprint `dry_run.md` | `PLAN.md` | Keep exact paths/commands and stop-before-approval |
| Sprint `implementation_log.md` | `PLAN.md` execution record | Report actual commands, not intent |
| Sprint `human_review.md` | `REVIEW.md` | Require human verdict |
| Sprint `retrospective.md` | `REVIEW.md` | Preserve learning and next steps |
| Sprint `rollback_log.md` | `PLAN.md` rollback + `REVIEW.md` refinement | Preserve significant reversal evidence |
| `planning/features/`, `planning/releases/` | Optional advanced modules | Do not force advanced tree at project initialization |

**No blind migration:** An existing ADDF project may contain valuable decisions, documentation, and code. Stage 3+ must offer an explicit *read-only audit → proposed mapping → human approval → copy/migrate → validate* procedure; never delete the original structure or adopt Light by silent renames.

## 8. Stage-ordered verification strategy

| Stage | What can be validated | What must wait |
| --- | --- | --- |
| **2 — Contracts** | Internal consistency, schema completeness, owner/permission definitions, review checklist | Real file/template conformance |
| **3 — Starter kit** | Blank startup and first-sprint file shape | Agent prompt behavior and real code execution |
| **4 — Agents** | Model prompt compliance in simulations, no auto-authorize | End-to-end user playtesting |
| **5 — Pilots** | Start-from-zero, one-sentence, existing-project flows and human gates | Full docs/release packaging |
| **6 — Validator** | Static IDs/headings/links/enum/gate consistency | Proving human comprehension or fun |
| **7 — Wiki/manual** | Links, content coverage, generated manual drift | Production web distribution |
| **8 — Branding** | Light logo uses brand rules and assets work | Public site signoff |
| **9 — Website** | Preview build/navigation/downloads without affecting original `main` | Release accept |
| **10 — Release** | Full traceable acceptance, versioning and distribution checks | Further feature cycles |

## 9. Failure and recovery conditions

| Failure | Required response |
| --- | --- |
| Missing core project file | Explain which contract is missing; propose safe creation step |
| No idea provided | Begin guided discovery; do not ask user for full design document |
| User says “I don't know” on a T1 choice | Offer reversible prototype or focused research; mark deferred |
| Accidental out-of-scope write | Stop, disclose diff, preserve work, ask about rollback or new plan; never hide it |
| User rejects playtest | Preserve review, propose refinement, check Gate I scope before edits |
| Agent context ends | Save truthful checkpoint and resume using source files; re-verify permission |
| Unrecognized secrets in source inventory | Stop ingestion, update exclusions, ask for secure path |
| Conflicting approval records | Fail closed; request a human decision |
| Website build passes but deploy permission absent | Keep preview local/private; do not publish |
| Validation tool cannot check a feature | Output `not_verified` rather than success |

## 10. Acceptance for Stage 2 and handoff to Stage 3

Stage 2 is complete only when a human verifies:

- [ ] Minimal project paths and exact required headings/keys are defined.
- [ ] Project and sprint contracts have distinct owners and no contradictory status terminology.
- [ ] Gate D, Gate I and Gate A records cannot be mistaken for one another.
- [ ] Scope changes invalidate stale authorization.
- [ ] An agent cannot invent human review, passing tests or citations.
- [ ] Original ADDF maps cleanly into Light, without deletion or irreversible migration.
- [ ] Static validators are planned, not falsely claimed to exist now.
- [ ] Starter kit and prompt development remain unstarted pending signoff.

**Stage 2 approved by the user on 2026-11-12.** Stage 3 will physically create starter-kit templates, the Quick Start, and shape checks; begin Stage 3 only on a separate user instruction. No starter-kit work was done as part of this approval.
