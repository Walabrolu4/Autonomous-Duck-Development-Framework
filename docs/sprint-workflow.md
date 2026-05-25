[Home](index.md)

# Sprint Workflow

## Overview

The sprint workflow is the step-by-step operating loop for any task larger than a quick patch. It applies to [Mode 2 (Feature Sprint)](modes/feature-sprint.md), [Mode 3 (Refactor/Migration)](modes/refactor-migration.md), and [Mode 4 (Data Ingestion)](modes/data-ingestion.md). Each step names what the human does, not just what the AI produces.

A sprint produces: `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`, `implementation_log.md`, `human_review.md`, `retrospective.md`, and an updated `STATE.md`.

---

## Step 1 — Pre-Flight Gate

**What the human does:** Check `QUESTIONS.md` for any open items that would prevent a sound blueprint. Check `RISKS.md` for unresolved High severity risks. Confirm the sprint branch has been created in git.

**Main artifact:** Verified QUESTIONS.md, RISKS.md, git branch.

**Gate question to ask yourself:** Is there anything I do not yet know that would cause the Architect to make a wrong assumption? If the answer is yes, resolve it now. Do not generate a blueprint against an unknown.

---

## Step 2 — Prime the Architect

**What the human does:** Open a fresh Architect session. Load `AGENTS.md`, `STATE.md`, `DOMAIN.md`, and any recent `DECISIONS.md` entries. Run the [Sprint Pack Generation prompt](prompts.md#sprint-pack-generation).

**Main artifact:** `requirements.md`, `blueprint.md`, `acceptance.md`

---

## Step 2B — Human Blueprint Review Gate

**What the human does:** Read `blueprint.md` carefully before authorizing anything. Verify each Architect assumption listed at the bottom of the file. Ask yourself:

- Does this blueprint match what I actually want built?
- Does any assumption conflict with `DOMAIN.md`?
- Are there files listed that should not be touched this sprint?
- Is the scope narrower or broader than intended?

If any assumption is wrong, write your corrections in [`blueprint_feedback.md`](file-reference/sprint-files.md#blueprint_feedbackmd) and return to Step 2 for a revised blueprint. Do not skip this gate.

**Main artifact:** `blueprint_feedback.md` (if corrections needed)

> A flawed blueprint produces a flawed build. Catching a problem here takes minutes. Catching it after implementation takes hours.

---

## Step 3 — Pre-Flight Dry Run

**What the human does:** Open a new Builder session. Load the sprint files. Run the [Builder Pre-Flight Dry Run prompt](prompts.md#dry-run). Wait for the `dry_run.md` report. The Builder stops after producing it.

**Main artifact:** `dry_run.md`

**Gate question to ask yourself:** Does every file in `dry_run.md` appear in `blueprint.md`? If the Builder intends to touch a file not in the blueprint, that is scope creep. Send it back before any code is written.

---

## Step 4 — Architect Sanity Audit

**What the human does:** Paste `requirements.md`, `blueprint.md`, `acceptance.md`, and `dry_run.md` into the Architect session. Run the [Architect Sanity Audit prompt](prompts.md#sanity-audit). The Architect checks for hidden scope bleed, missing verification commands, and undeclared dependencies.

**Main artifact:** Permission approval or rejection with required changes.

---

## Step 5 — Dependency Approval Gate

**What the human does:** If the dry run or audit revealed any new dependencies (npm packages, pip packages, external APIs), create a `DECISIONS.md` entry for each before authorizing the build.

**Main artifact:** Updated `DECISIONS.md`

**Why before the build?** A dependency added without a decision record is a dependency that future AI sessions will not know the reasoning for. If you later need to audit which sprint introduced a vulnerable library, the ADR tells you why it was added and who approved it.

---

## Step 6 — Authorize and Build

**What the human does:** Type the [Builder Implementation Authorization message](prompts.md#implementation-authorization) in the Builder session. The Builder implements according to the approved blueprint and logs every change in `implementation_log.md`.

**Main artifact:** Source files, `implementation_log.md`

---

## Step 7 — Run Verification

**What the human does:** The Builder runs all commands listed in `acceptance.md` and `COMMANDS.md` and pastes the raw terminal output into `implementation_log.md`. Read the actual output — not just the summary.

**Main artifact:** Terminal output in `implementation_log.md`

> "Tests passed" in a summary can mean 1 test passed and 47 were skipped. The raw output tells you what actually ran.

---

## Step 8 — Architect Reviews Output

**What the human does:** Paste `acceptance.md`, `dry_run.md`, and `implementation_log.md` into the Architect session. Run the [Architect Implementation Review prompt](prompts.md#implementation-review).

**Main artifact:** Architect review — approved, or a list of required fixes.

---

## Step 9 — Human Approval Gate

**What the human does:** Work through the five gates in `human_review.md`. All five must pass before committing.

1. **Scope:** Does `implementation_log.md` list only files that appeared in `dry_run.md`?
2. **Tests:** Are passing test results present in `implementation_log.md`?
3. **Debt:** Are all known issues from this sprint recorded in `planning/backlog.md`?
4. **Decisions:** Do all new dependencies have `DECISIONS.md` entries?
5. **State:** Does `STATE.md` reflect the completed sprint status?

---

## Step 10 — Commit, Update, Reset {#step-10--commit-update-reset}

**What the human does:** Commit the sprint branch. Merge to `dev`. Update `STATE.md`. Complete `retrospective.md`. Close the Builder thread.

**Main artifact:** Git commit, updated `STATE.md`, `retrospective.md`

**The reset is not optional.** Closing the Builder thread is how the framework prevents context bleed from accumulating across sprints. The next sprint starts from what is in the files — not from what was in the conversation. Close it every time.

## See Also

- [Operating Modes](modes/index.md)
- [Sprint Files](file-reference/sprint-files.md)
- [Prompt Catalog](prompts.md)
