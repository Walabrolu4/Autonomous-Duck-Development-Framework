# Troubleshooting ADDF Light Games

Use symptoms and **actual evidence** to recover. Don't repair an approval failure by writing a fake approval, or an implementation failure by expanding scope without human review.

## When to use

Use when onboarding feels stuck, a skill isn't discovered, the validator fails, a sprint can't close, or another agent resumes with contradictory state.

## Common problems

### “I don't know what to make”

Start at DISCOVER and ask for two or three **mechanically different** small ideas. The user can select one or ask for a reversible experiment; no full GDD is necessary.

### “The agent keeps asking too many questions”

Limit to one consequential question per turn by default. Let the agent choose T0 routine details within approved scope. Put irrelevant future preferences into the backlog, not the current session.

### “A blank starter kit fails validation”

Check whether the exact six Light `minimal/` files were copied, not the original full `starter-kit/blank/`. An unstarted project should have `active_sprint: none`, `discovering`, `authorized: no`, and no sprint folder. Run the validator in `--mode template` if checking the distribution starter templates themselves.

### “Missing SECURITY.md / required heading”

The validator reports `L-F001` or `L-F002`. Inspect the file; don't overwrite an existing human-owned file to silence the check. Create a missing new-project file or propose a reviewed migration.

### “The agent says it has permission but validation fails”

Inspect `STATE.md`, the exact `PLAN.md` revision, Gate I human response and source, and current worktree. If any mismatch or unverified source exists, **stop and request renewed consent** rather than fabricating text.

### “The human chose the mechanic, so why hasn't it coded?”

Gate D selected a design. The coding agent must still show exact file paths, commands, dependencies, risks and rollback, then obtain Gate I on that scope.

### “A new dependency is needed mid-sprint”

Stop implementation, revise `PLAN.md` to rN+1, disclose new install/network/license effects and request fresh Gate I. Don't silently extend r1.

### “The build passed but the sprint won't close”

Check whether the human has actually run the game and given a Gate A verdict. Automated test success does not equal human acceptance. Ensure each `AC-##` has a result and known release blockers are visible.

### “The game opens but feels wrong”

Record a concrete observation, classify it against original criteria, and propose one minimal correction. Use existing Gate I only if scope remains valid; otherwise re-plan.

### “The new Claude/Codex skill isn't loading”

Verify the exact installed skill path, frontmatter and host version. Ensure you installed into the **game project**, not merely left files in the framework repo. Do not weaken permissions or overwrite existing instructions. Stage 5 host-specific tests remain a separate task.

### “OpenClaw didn't reach my home PC”

An adapter skill is **not a remote transport**. Configure trusted workspace and connection only after a separate user-approved setup. Don't claim background work or machine access unless actually available.

### “A resumed model wants to repeat a command”

First verify whether the command already ran and what side effects occurred. If outcome is uncertain, avoid blind retries—especially package installs, deletes, deploys or Git operations.

### “The documentation and MANUAL.md disagree”

The wiki under `docs/light-games/` is canonical. The manual is generated. Run `python3 scripts/build_light_manual.py --check` to detect drift, regenerate only in a reviewed Stage 7 documentation change, and never manually edit the generated manual.

## Escalation

If the problem is a **material design choice**, return to the human Gate D. If it is **technical scope/permission**, return to Gate I. If it's **player experience**, ask for human Gate A or refinement. If it's **security, data loss or privacy**, stop affected work and seek explicit recovery authorization.

## Related

[Failure recovery](../quality/failure-recovery.md) · [Validator](../quality/validation.md) · [Handoff](../agents/handoff.md) · [FAQ](faq.md)
