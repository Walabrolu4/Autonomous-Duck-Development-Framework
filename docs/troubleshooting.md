[Home](index.md)

# Troubleshooting

Each scenario below is self-contained — jump directly to the one you need. Every scenario includes what happened, what to do, and how to prevent it in the future.

---

## The Builder Touches Files Outside the Blueprint

**What happened:** You review `implementation_log.md` and find files listed that were not in `dry_run.md` or `blueprint.md`.

**What to do:**

1. Do not commit.
2. Revert the unauthorized changes: `git checkout sprint/NNN -- [filename]`
3. Record the violation in `retrospective.md`.
4. Add a constraint to `AGENTS.md`: *"Do not modify files outside the approved blueprint scope under any circumstances."*
5. Re-run the sprint from [Step 6 (Authorize and Build)](sprint-workflow.md#step-6--authorize-and-build) with the corrected scope explicitly stated in the authorization message.

**Prevention:** The [Sanity Audit](prompts.md#sanity-audit) at Step 4 catches scope bleed before it happens. Running it every sprint is the primary prevention mechanism. See [AGENTS.md](file-reference/agents.md) for adding permanent constraints.

---

## You Realize Mid-Sprint the Blueprint Is Wrong

**What happened:** While reviewing the Builder's work, you notice the blueprint is missing a constraint, contains a wrong assumption, or will produce the wrong outcome.

**What to do:**

1. Stop the Builder session immediately. Do not let it continue against a blueprint you know is wrong.
2. Revert any changes made so far: `git checkout sprint/NNN`
3. Return to the Architect session. Write your corrections in [`blueprint_feedback.md`](file-reference/sprint-files.md#blueprint_feedbackmd).
4. Run the [Sprint Pack Generation prompt](prompts.md#sprint-pack-generation) again with `blueprint_feedback.md` loaded.
5. Re-run the dry run against the revised blueprint before authorizing again.

Catching a blueprint error before the full sprint is implemented saves far more time than it costs. This is not a failure — it is the system working as designed.

---

## You Hit a Rate Limit or Token Limit Mid-Session

**What happened:** The Architect or Builder session is interrupted by a rate limit, token limit, or network error.

**What to do:**

1. Before closing the interrupted session, save any partial output to the relevant file (`blueprint.md`, `dry_run.md`, etc.).
2. Update `STATE.md` to reflect where you stopped and what was in progress.
3. Open a new session with any available model. Load `AGENTS.md`, `STATE.md`, and the relevant sprint files.
4. Continue from where you stopped.

Because the state is in the files, the new session has full context. The model does not matter. The files do.

---

## The Sprint Fails Acceptance Criteria

**What happened:** The Builder ran the verification commands and tests are failing, or the build did not complete.

**What to do:**

1. Do not commit.
2. Record the failure output in `implementation_log.md`.
3. Return to the Builder session. Paste the failing test output and ask for a fix, constrained to the same `blueprint.md` and `acceptance.md`.
4. The Builder must produce a new `dry_run.md` for the fix before implementing it — even if the fix is small.
5. If the failing tests reveal a gap in the blueprint (the Builder cannot fix the failure within the approved scope), return to the Architect to revise the blueprint.

---

## The Blueprint Conflicts with DOMAIN.md

**What happened:** The Architect generated a blueprint that contradicts a rule in `DOMAIN.md` — for example, it proposes cloud sync for a project where `DOMAIN.md` explicitly says cloud sync is out of scope.

**What to do:**

1. Do not use the blueprint.
2. In `blueprint_feedback.md`, quote the specific `DOMAIN.md` rule that the blueprint violates.
3. Return to the Architect session and run the Sprint Pack Generation prompt again with `blueprint_feedback.md` loaded.
4. If the conflict reveals that `DOMAIN.md` is genuinely out of date (you have actually decided to add cloud sync), update `DOMAIN.md` first, create a `DECISIONS.md` entry recording the scope change, then generate a new blueprint.

See [DOMAIN.md reference](file-reference/domain.md) for guidance on when and how to update the domain file.

---

## STATE.md Is Out of Date When You Return {#statemd-is-out-of-date-when-you-return}

**What happened:** `STATE.md` was not updated at the close of the last session, or it was updated incompletely.

**What to do:**

1. Load `DOMAIN.md`, `AGENTS.md`, and the most recent sprint folder.
2. Run the [Resumption Prompt](prompts.md#resumption). Ask the Architect to reconstruct the current state from the files that do exist.
3. Use the Architect's reconstruction to manually update `STATE.md`.
4. Add a reminder to the top of `AGENTS.md`: *"Always update STATE.md at the close of every session. Do not close a session without completing this step."*

**Prevention:** Updating `STATE.md` before closing any session is the single most important habit in this framework. Make it the last action, every time, without exception. See [Step 8: Resumption](lifecycle/08-resumption.md) for why this matters.

## See Also

- [Sprint Workflow](sprint-workflow.md)
- [Quick Reference](quick-reference.md)
- [STATE.md](file-reference/state.md)
