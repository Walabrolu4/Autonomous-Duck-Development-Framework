# ACCEPT — Prepare a human playtest and record the real verdict

**When to use:** Implementation/refinement results are available for human verification. **Capability:** Reporting and review. **No automatic implementation or acceptance authority.**

## Copyable agent instruction

Read `SECURITY.md`, `AGENTS.md`, current `STATE.md`, `SPRINT.md`, `PLAN.md` and `REVIEW.md` for the active sprint. Check the **exact approved acceptance criteria**, real execution evidence and build availability. Never invent a playable URL.

1. **Evidence preparation:** For every `AC-##`, list the original intended behavior, method and current `pass | fail | partial | not_tested` with source. Automated checks remain distinguishable from human playtests.
2. **Build/run details:** State the verified platform/device, launch method, controls, setup and known issues. If not runnable, report the blocker instead of claiming readiness.
3. **Human test:** Give a concise checklist tied to the real `AC-##` entries: what to try, what should happen, where to notice feedback and how to report a surprising result.
4. **Play experience:** Ask for the user's own observations of responsiveness, clarity, fairness, onboarding, accessibility and whatever the actual sprint targeted. Do not claim the human liked or understood it until they say so.
5. **Gate A:** Ask the user to choose `accepted`, `accepted_with_conditions`, `needs_refinement`, `rejected` or `paused`; these are review verdicts, not AI recommendations.
6. **Record honestly:** Only after a clear user response, transcribe the actual wording/reference into the current `REVIEW.md` review round; preserve prior rounds and conditions. Release-blocking conditions remain blockers.
7. **Update state:** If accepted and no unresolved blocking conditions, mark sprint `accepted` and close it with a short retrospective and backlog handoff. Otherwise record `rejected`, `refining` or `paused` as appropriate, **without overwriting old verdicts**.
8. **Next sprint:** May recommend, but not create or implement it without the user's choice and subsequent gates.

**Critical distinction:** Automated tests, screenshots, compilation and an agent's own review do **not** constitute Gate A. `REVIEW.md` may be drafted before human testing, but `gate_a_status` remains `pending` until the actual verdict. “Accepted with conditions” must not be silently converted to unconditional release.

**Output contract before human verdict:**
- Verified build/run access or accurate blocker.
- Compact criterion-by-criterion evidence table.
- Specific human playtest steps.
- Known limitations and any material uncertainty.
- **One explicit Gate A question**, then stop.

**Output contract after human verdict:** Actual user response, review round, state transition, unresolved conditions, optional next-sprint proposal. Do not claim a full game release unless separately approved.
