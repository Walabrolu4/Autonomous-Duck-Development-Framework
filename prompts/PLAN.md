# PLAN — Dry run first; request exact implementation authorization

**When to use:** A human-selected sprint has a draft/approved `SPRINT.md`; exact file operations and tool effects must be exposed. **Capability:** Design. **No game implementation writes.**

## Copyable agent instruction

Read `SECURITY.md`, `AGENTS.md`, `STATE.md`, `GAME.md`, related `DECISIONS.md`, and the active `SPRINT.md`. Verify sprint ID, agreed goal and acceptance checks. Inspect relevant project tree/readme/code **read-only**, excluding secrets.

Create or revise the **active sprint** `PLAN.md` from the approved Stage 3 template. This is a **dry run**; preparing it does not grant permission to execute.

Document:
1. **Inputs and human design decisions:** selected `SPRINT.md` revision, actual Gate D evidence or valid T0-only `not_required` rationale. Flag unresolved choices.
2. **Exact file operations:** `create/modify/move/delete` path, linked `AC-##`, specific intended change, possible conflict/overwrite and recovery. Avoid wildcard “as needed” scope.
3. **Commands:** exact command, working directory, expected outputs and side effects; state which are reads, tests, builds, installs, network calls, or deployments.
4. **Dependencies, assets, and tools:** name/version or pin policy, source/provenance, relevant license, downloads, API costs and any credentials. Unknown versions remain unknown until verified.
5. **Sequence:** small implementation increments, checks and stoppage criteria.
6. **Verification plan:** relevant automated tests, manual game/playtest steps, evidence paths and limitations.
7. **Risks and rollback:** destructive actions, repository conflicts, external exposure, data and privacy risks, recovery steps.
8. **Open ambiguities:** resolve materially important ones before implementation.
9. **Gate I:** set `plan_revision: rN`, `gate_i_status: pending`, `human_response: pending`, `authorized_operations: none`, `authorized_commands: none`. Request **explicit** user approval for that revision and exact scope.

Show the user a compact *human review summary* of planned creates/modifies/deletes, commands, dependencies, special effects, risks and acceptance outcome. Ask one clear question:

> “Do you authorize **Sprint NNN `PLAN.md` revision rN** for precisely these files, commands and dependencies, with these exclusions? Or should I revise it?”

**Do not** record "authorized" until the human actually responds clearly. A message approving the *concept* alone is not Gate I. A single explicit response can approve both D and I only if both choice and exact plan were shown and separately recorded.

**Revision integrity:** New paths, dependency versions, commands, remote side effects, changed outcome, or increased risk invalidate previous Gate I. Preserve earlier authorization history, increment revision, mark `stale` or `pending`. Any special operation—publishing, merging, spend, secret access, destructive operation—requires its **own explicit permission**.

**Output contract:**
- Current plan revision, dependencies and source files inspected.
- Exact file/command/dependency table and any exclusions.
- Test and rollback strategy, unknowns.
- **Gate I status and human approval evidence** (or `pending`).
- One explicit authorization question, then stop.

**Stop condition:** Await human Gate I. No code edits, install/build commands with side effects, or deployment. [IMPLEMENT](IMPLEMENT.md) is forbidden until that gate is verified.
