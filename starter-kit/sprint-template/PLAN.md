# Sprint NNN — Implementation Plan

> **Distribution template only.** No implementation work is authorized by copying this file. The agent must first complete the sprint design and fill this dry run with exact paths and commands; then stop for explicit human Gate I on the displayed revision.

## Sprint metadata

- sprint_id: sprint-001
- sprint_kind: playable-slice
- project_id: undecided
- file_revision: r1
- status: draft

Keep the sprint ID, kind and project ID consistent with the active `SPRINT.md` and `GAME.md`. The plan revision in Gate I must equal this file's current revision.

## Inputs and assumptions

- Linked sprint: `planning/sprints/sprint-001/SPRINT.md` (after actual installation).
- Linked sprint revision: unknown.
- Design approval Gate D: pending.
- Existing code/branch inspection: not_verified.
- Open implementation assumptions: unknown.

Do not invent a clean working tree, installed dependency or valid approval. Inspect authorized context safely.

## Exact file operations

**No operations proposed yet.** Before asking for Gate I, replace with a narrow table including **every** proposed create/modify/move/delete:

| Operation | Exact path | Purpose / linked AC | Boundary / overwrite risk | Recovery |
| --- | --- | --- | --- | --- |
| none | none | No planned implementation | No writes authorized | Not applicable |

Allowed operations: `create`, `modify`, `move`, `delete`. Avoid blanket “any files needed” or entire-repository wildcards. If generated files may be numerous, explicitly bound their directory, types and count/range.

## Commands and external side effects

**No commands authorized yet.** Specify the exact commands, working directory, dependencies, expected files/network access and side effects **before** Gate I.

| Command | Working directory | Purpose | Side effects / approval |
| --- | --- | --- | --- |
| none | none | No command selected | Nothing may be run as implementation |

Build/test execution is not permission for package installs or deployment. Require separate explicit approval for publishing, money, secrets, privilege changes or destructive operations.

## Dependencies and assets

- New packages or engine versions: none authorized.
- Expected downloads / external sources: none authorized.
- Third-party/generated asset licensing and provenance: not_applicable until assets selected.
- Credential/API needs: none authorized.

Each proposed dependency must list name, version or pin policy, provenance, licenses/risks and network effects. If an agent discovers an unplanned requirement, **stop** and ask for revised Gate I.

## Implementation sequence

1. Inspect the approved paths and record current state.
2. Make the smallest change needed for one acceptance criterion.
3. Run only approved verification commands.
4. Record exact changed paths and actual results in the execution record.
5. Prepare `REVIEW.md` for human testing; never self-accept.

This is an example sequence, **not** permission to perform these steps. Refine it to match the actual sprint.

## Verification plan

- Acceptance criteria to cover: none yet.
- Automated tests: not_planned.
- Manual playtest or inspection: not_planned.
- Expected evidence locations: pending.
- Definition of ready for human review: all tests/errors honestly reported and the deliverable accessible or blocker documented.

Each actual `AC-##` must have a matching result in `REVIEW.md`, including `not_tested` when unverified.

## Risks, rollback and stop conditions

- Known risks: not_assessed.
- How to reverse changes without losing unrelated work: not_defined.
- Stop on out-of-scope path, command, dependency, cost, secret, network, public deployment, incompatible project state or changed design goal.
- If rollback is requested, present exact steps and get appropriate authorization; never force-reset unrelated work.

Fill concrete rollback and risk notes before Gate I.

## Open ambiguities

- All implementation details are currently open.
- Required human decisions: first choose the actual sprint and design in `SPRINT.md`.
- Other unknowns: none established.

Stop at `awaiting_approval` until actionable ambiguities are resolved and the specific plan is authorized.

## Implementation approval — Gate I

- plan_revision: r1
- linked_sprint_revision: unknown
- gate_i_status: pending
- authorized_operations: none
- authorized_commands: none
- dependency_approvals: none
- separate_special_approvals: none
- human_response: pending
- recorded_from: pending
- conditions: none

**Never** change `gate_i_status` to `authorized` based on an agent recommendation or template content. Valid approval identifies the actual revision, paths, commands, dependencies and conditions and is recorded from a real human response.

If the material scope changes, preserve the old approval record under a new `### Prior authorization records` heading, increment the plan revision, set the current gate `stale` or `pending`, and seek renewed approval. A revised scope cannot inherit consent.

## Execution record

- Implementation started: no.
- Actual file changes: none.
- Commands actually run: none.
- Automated test results: not_tested.
- Verified build/preview: not_verified.
- Deviations from approved scope: none reported.
- Next safe action: complete dry-run plan; request Gate I.

After real authorization, append the actual work and evidence here. Do not replace failures with anticipated successes or fabricate execution history.
