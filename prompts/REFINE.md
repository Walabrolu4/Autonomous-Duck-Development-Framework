# REFINE — Diagnose feedback; don't silently expand scope

**When to use:** A build/test failed or a human playtest identified a problem with a sprint's agreed outcome. **Capability:** Diagnose in Research/Design; change code only as Develop under **still-valid Gate I**.

## Copyable agent instruction

Read `SECURITY.md`, `AGENTS.md`, `STATE.md`, active `SPRINT.md` and `REVIEW.md`; inspect relevant parts of `PLAN.md` and actual build/test evidence. Start by identifying **what was observed** and whether it violates an existing `AC-##` or introduces a new requirement.

1. **Evidence:** Quote the user's concrete observation or an actual failing test, plus reproduction steps/device/input if known. Mark uncertain diagnosis as a hypothesis.
2. **Classification:**
   - **Within approved plan:** same intended outcome, approved file paths and operations, allowed commands/dependencies, no higher risk. A bounded bug fix may be carried out under Gate I if authorization still valid.
   - **Expanded scope:** new paths, packages, commands, assets, user-visible behavior, credentials, external effect, cost or increased risk. **Stop** and revise `PLAN.md` to `rN+1`; invalidate the old Gate I and ask the human before editing.
   - **New feature/experiment:** move to the backlog or re-enter Design and Gate D if it changes sprint intent. Don't smuggle unrelated ideas into “bug fixing.”
3. **Learning checkpoint:** If the test challenges a game-design hypothesis, explain briefly what the new evidence says about player feel, mechanic feedback, challenge, or system behavior.
4. **Plan correction:** Specify minimal changes, exact verification actions and rollback. Identify whether fresh Gate I is necessary. If no code edits are authorized, show a proposed plan only.
5. **Execution:** For a valid in-scope authorization, make only the permitted corrections and report actual test/command results. Never mark unrun tests passing.
6. **Records:** Add a new `round-N` entry to `REVIEW.md`, preserve old failed results, human rejection and previous Gate A rounds. Update `STATE.md` to `refining` or `awaiting_approval` as appropriate.
7. **Retest:** Ask the human to repeat relevant playtest actions; prepare a new human acceptance round only after the deliverable is actually ready.

**Prohibited:** automatically treating a criticism as permission to change design direction; inventing a clean test result; hiding failed attempts; deleting old review rounds; implementing a new dependency before renewed Gate I; closing sprint without human verdict.

**Output contract:**
- Observation and `AC-##` relation.
- Root cause (`verified` or `hypothesis`).
- Scope classification: `within existing Gate I` / `requires new Gate I` / `new design choice`.
- Minimal correction plan and expected retest.
- Actual file/test changes if any, revised plan reference and one next human action.

**Stop condition:** A specific correction plan is approved or already in scope and tested, or human needs to authorize new scope. Move to [ACCEPT](ACCEPT.md) only when review evidence and human instructions can support it.
