# Failure Recovery: Stop, Preserve, Reconcile

Failures are expected in development. The goal is not to avoid every problem; it is to **keep the project safe and make the next action explicit**, without rewriting evidence or expanding permissions.

## When to use

Use when a test fails, a plan is stale, a coding agent edited an unexpected path, a remote command times out, or a user rejects a playable prototype.

## Classify the failure

| Failure | Immediate safe response |
| --- | --- |
| Test/build failure inside approved scope | Record actual output, diagnose, correct only within valid Gate I |
| New file/dependency needed | Stop, revise `PLAN.md`, obtain renewed Gate I |
| Unauthorized file change | Stop, disclose exact diff, preserve work, ask user about rollback or plan revision |
| Missing or ambiguous approval | Fail closed, set safe state, ask for evidence or renewed consent |
| Secret/credential exposure | Stop reads/transfers, avoid repeating secret, discuss containment with human |
| Remote timeout | Treat outcome unknown; inspect actual state before retrying |
| Human playtest rejection | Preserve `REVIEW.md` verdict, propose refinement/re-design, seek needed gates |
| Conflicting project files | Report conflict, establish safest authority, reconcile with human |

## The recovery sequence

1. **Stop** the risky action; don't repeatedly retry.
2. **Record verified facts**: current file diff, command and known result, status, affected paths, possible external effects.
3. **Separate assumptions**: what may have happened but wasn't confirmed?
4. **Check authorization**: does the current plan still cover the proposed correction?
5. **Propose bounded remedy**: smallest safe fix, exact files/commands, rollback and tests.
6. **Request necessary human gate**: Gate D if intended behavior changes; new Gate I if technical scope changes; Gate A after retest.
7. **Update durable state**: blockers, next actor, and actual evidence in `STATE.md`, `PLAN.md` and `REVIEW.md`.

Don't force-reset Git or delete uncommitted work without an explicitly reviewed recovery operation.

## Example: failed build after package install

An authorized plan expected package version 1.x, but the installer pulled 2.x and changed a lockfile not in scope. The agent should stop, report actual version/lockfile changes and risks, then ask whether to revert within safe authorized recovery or approve a revised plan. It should not silently continue and claim the original version was used.

## Example: remote workflow interruption

A home-machine agent starts an authorized export, then a school-browser session loses connection. The coordinator cannot assume the export failed. Reopen the actual target workspace and verify artifacts, timestamps, command logs and final state before rerunning. Never publish an unverified artifact.

## Retrospective as learning

A useful review explains why the failure happened and what control could prevent recurrence: clearer scope, smaller slice, tighter exclusions, better tests or different learning checkpoint. It should not be a blame exercise or a fake “everything went smoothly” report.

## Common failures

**Silent repair:** AI edits new files to “fix” errors without Gate I. Stop and re-plan.

**Overreaction:** Delete the entire repository to roll back one file. Use precise recovery.

**Erase negative feedback:** Rewrite prior reviews. Preserve history.

## Related

[Refinement](../lifecycle/refine.md) · [Resumption](../agents/handoff.md) · [Permissions](../agents/permissions.md)
