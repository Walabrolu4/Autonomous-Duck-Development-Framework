# RESUME — Recover an ADDF Light Games project across agents and sessions

**When to use:** New conversation, context exhaustion, an interruption, changed device, different model, or handoff from orchestrator to coding agent. **Capability:** Initial Research read and reconciliation. **No automatic code continuation.**

## Copyable agent instruction

You are resuming a **file-first** ADDF Light Games project. Treat old chats and predecessor summaries as hints; verify authoritative records and actual repository state.

1. **Safe read order:** `SECURITY.md` first, then `AGENTS.md`, `STATE.md`, `GAME.md`, `DECISIONS.md`. If an active sprint is named, read `planning/sprints/sprint-NNN/{SPRINT.md,PLAN.md,REVIEW.md}`. Check `planning/BACKLOG.md` only if needed.
2. **Evidence audit:** Identify exact last `sprint_status` and lifecycle stage, the human design approval, current `PLAN.md` revision and Gate I source, Gate A review, blockers and next actor. Compare with actual branch, diff, relevant files and recorded commands where tools and permission allow.
3. **Contradictions:** If chat claims implementation authorization but the current plan or human evidence disagrees, **fail closed**. Report mismatch; set/advise `awaiting_approval` or `paused`. Never manufacture or replay consent.
4. **Change detection:** A materially revised `PLAN.md`, new dependency, changed worktree, or expanded risk invalidates old Gate I. Even if past approval exists, verify it covers the present scope and risk before coding.
5. **Tool availability:** Distinguish host capabilities from permission. Not every assistant can execute local code, access GitHub or read files. If you cannot inspect facts, mark `not_verified` and ask the user to supply the relevant safe records instead of guessing.
6. **Restore state:** Summarize the latest actually completed work, unfinished/failed operations, evidence gaps and exactly **one safe next action**. Update `STATE.md`/handoff notes only if safe edits are authorized.
7. **Choose next prompt:** [START](START.md), [DISCOVER](DISCOVER.md), [RESEARCH](RESEARCH.md), [DESIGN](DESIGN.md), [PLAN](PLAN.md), [IMPLEMENT](IMPLEMENT.md), [REFINE](REFINE.md) or [ACCEPT](ACCEPT.md) based on the **verified** state.

**Never:** Resume implementation simply because the last chat said “continue,” run a lost command twice without checking its side effects, fabricate tool output, access excluded secrets, self-accept, auto-merge or deploy.

**Output contract:**
- Project, active sprint, current branch and last **verified** lifecycle stage/status.
- Gate D / I / A evidence references, or `pending | unknown`.
- Exact current Gate I revision and valid permitted operations—or `not_authorized`.
- Completed actions vs pending, with tests actually verified.
- Files reviewed and missing/conflicting records.
- **One next safe action** and any required human decision.

**Stop condition:** If approval or current project facts are unclear, stop without implementation and request a precise reconciliation. Otherwise guide the user to the appropriate prompt, respecting all gates.
