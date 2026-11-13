# IMPLEMENT — Execute only the human-authorized sprint plan

**When to use:** The human explicitly authorized a specific active `PLAN.md` revision, operations and commands. **Capability:** Develop. **Not a general “build whatever is needed” prompt.**

## Copyable agent instruction

Before writing implementation code or running commands, **verify**:
- `SECURITY.md` and `AGENTS.md` read/obeyed; tool permissions available but not interpreted as approval.
- `STATE.md` identifies active sprint and a **valid, non-stale Gate I** authorization, with an actual human response reference.
- `SPRINT.md` has a bounded goal, acceptance checks and valid Gate D decision/non-required rationale.
- `PLAN.md` revision, linked sprint revision, file operations, exact commands, dependency versions and special-approval records match what the user approved.
- Worktree, branch and file state are inspected safely for conflicts or unrelated human changes. If approval history cannot be verified, **STOP** and request Gate I again.

**Implement within scope only:**
1. Change only the approved paths with listed operations. Do not widen globs, reinitialize git, wipe uncommitted changes, rename unrelated assets, or modify permission rules.
2. Run only approved commands in approved directories. Installing dependencies, reaching external network services, publishing builds or spending money requires the **specific** permission in the plan plus separate special approval when needed.
3. Work in small increments that make the agreed `AC-##` behavior observable. Preserve the user-selected game feel and documented constraints.
4. Verify using approved tests/builds where possible. For each command, record **actual** result, exit code or inability to run, and environment. Never invent passes.
5. Append an accurate `PLAN.md` **Execution record** containing changed paths, commands, diffs/commits if real, limitations and deviations.
6. Prepare `REVIEW.md` results for every actual `AC-##`; mark manual player tests `not_tested` until the human supplies evidence.
7. Propose a next transition to `refining` on failure/feedback or `awaiting_acceptance` if the deliverable is ready. **Do not self-accept.**

**Mandatory stop/replan:** A needed file/command/dependency not in the plan, a new engine/plugin, changed player goal, security/privacy issue, paid service, external deployment, or greater risk. Report exactly which boundary changed; preserve safe work; move to `awaiting_approval`; revise `PLAN.md` and request a new Gate I. A small fix inside the still-valid authorized scope may continue, but it must not expand it.

**Never** claim a command ran unless the tool actually returned results. If execution tools are missing, give the user exact proposed edits and commands **without claiming implementation**; request the user to run them and provide evidence.

**Output contract:**
- Authorization evidence: sprint, approved plan revision, allowed scope.
- Actual changed files and commands run, with results/failures.
- Acceptance checks automated vs requiring human test.
- Deviations, blockers and risks.
- Next state and precise **human verification step**.

**Stop condition:** All currently authorized work is accurately documented and ready for [ACCEPT](ACCEPT.md), or a re-plan / human decision is required. No merge or publish by default.
