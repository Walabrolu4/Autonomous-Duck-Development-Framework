# Sprint NNN — Review and Acceptance

> **Distribution template only.** Human acceptance is not granted by copying this file. The agent prepares evidence and playtest steps, then asks the human for a verdict. Failed or incomplete work remains visible.

## Sprint metadata

- sprint_id: sprint-001
- sprint_kind: playable-slice
- project_id: undecided
- file_revision: r1
- status: draft

Keep these values aligned with the sprint design, plan and current `STATE.md`.

## Build and test evidence

- Verified source/commit: not_verified.
- Changed files: none documented.
- Build command and result: not_tested.
- Automated tests: not_tested.
- Device/browser/engine and versions: unknown.
- Playable artifact/preview: not_verified.
- Reproduction commands for human: not_verified.

Do not invent a build, result, screenshot, URL, performance number or passing status. A blocked build is a real result that requires an explanation, not a fabricated preview.

## Acceptance criteria results

No actual `AC-##` criteria have been supplied by `SPRINT.md` yet.

**After the sprint's acceptance criteria exist**, add exactly one result for **each actual** `AC-##` ID, using these fields:

```md
### AC-01 — [same title as SPRINT.md]
- result: not_tested
- method: manual-playtest
- performed_by: unknown
- environment: unknown
- evidence: not_recorded
- notes: not_observed
```

Allowed `result`: `pass`, `fail`, `partial`, `not_tested`. Allowed `method`: `automated`, `manual-playtest`, `manual-inspection`. Allowed `performed_by`: `agent`, `human`, `CI`, `unknown`. Human performance requires actual human observation; an AI test doesn't qualify.

## Playtest instructions

1. Obtain the **verified** run/build instructions from the implementation execution record.
2. Open the actual build if available; otherwise record the blocker and do **not** pretend the human can play.
3. Try each acceptance action from `SPRINT.md` and compare with its stated `pass_condition`.
4. Note input responsiveness, visibility of game feedback, accessibility constraints and anything surprising.
5. Report concise observations and a verdict; even one concrete failure is useful.

- Verified launch command or URL: pending.
- Controls/actions to try: pending actual sprint criteria.
- Reproduction steps for defects: pending.
- Human test instructions should be short enough to follow without reading the entire framework manual.

## Human observations

- Human playtest performed: no evidence yet.
- First-hand observations: pending.
- Reproduction steps or device limitations: pending.

Only add actual user-provided observations. The agent may invite feedback but cannot impersonate a tester.

## Refinement rounds

No refinement rounds yet.

When feedback or a test failure arises, add a new entry `round-1`, `round-2`, etc. Each round must preserve:
- trigger and actual observation or failing test;
- verified diagnosis or labeled hypothesis;
- fix scope and whether original Gate I still covers it;
- revised plan/approval if scope expands;
- actual retest results;
- request for another human review.

Never overwrite previous rejection, user notes or evidence.

## Known limitations and deferred work

- Known limitations: unknown until verified.
- Deferred features: none linked yet.
- Release blockers: unknown until acceptance checks are assessed.

Do not call a blocker “resolved” without evidence.

## Human acceptance — Gate A

- review_round: round-1
- gate_a_status: pending
- human_response: pending
- recorded_from: pending
- conditions: none
- outstanding_release_blockers: unknown
- next_action: Prepare real build/test evidence and request human testing.

Human verdict options: `accepted`, `accepted_with_conditions`, `needs_refinement`, `rejected`, `paused`. Only a clear real response may change this field. A user may accept with conditions, but unresolved **release-blocking** issues prevent unconditional accepted/releasable state.

## Sprint retrospective and handoff

- Promised vs. observed outcome: not_evaluated.
- What changed and why: not_recorded.
- What the human learned or observed: not_observed.
- Decisions or backlog items to carry forward: none recorded.
- Current `STATE.md` reference: pending active sprint.
- Next safe step: Do not mark accepted until Gate A exists.

This retrospective cannot substitute for human acceptance. When the session ends, report precise status and unresolved work so a different agent can resume safely.
