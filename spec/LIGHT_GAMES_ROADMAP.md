# ADDF Light Games — Revised Framework Sprint Roadmap

**Edition:** ADDF Light Games · **Branch:** `ADDF_light_games`  
**Roadmap update:** November 17, 2026 · **Scope:** planning only  
**Decision:** Add **Stage 7B — Continuous-Session and Cross-Provider Compatibility** before Stage 8 branding. Keep the existing stage numbering and independent original-ADDF `main` branch.

> **Status/authority:** This roadmap reflects the human's request to reschedule the compatibility work before branding. It does **not** constitute Gate I authorization to execute any Stage 7B technical plan, edit source code, install tools, publish a site, or change subscription authentication. Every Stage 7B sprint ends with human verification and permission to advance. These are **framework development sprints**, not `sprint-NNN` files inside a user's game project.

## 1. Updated release sequence

| Stage | Milestone | Status | Exit / next gate |
| --- | --- | --- | --- |
| 0 | Set up separate `ADDF_light_games` branch | **Approved / complete** | Preserve original `main` |
| 1 | Framework philosophy, roles, lifecycle and gates | **Approved / complete** | Normative specification |
| 2 | Repository architecture and project/sprint file contracts | **Approved / complete** | Six core files, three sprint contracts |
| 3 | Starter Kit and Quick Start | **Approved / complete** | Initial game-project setup |
| 4 | Agent-neutral prompts and optional provider adapters | **Approved / complete** | Existing adapters still optional |
| 5 | Pilot games and end-to-end test artifacts | **Approved / complete** | Automated tests; first-hand human playtest later reported; provider trials tracked separately |
| 6 | Read-only validator and branch-only CI | **Approved / complete** | Structural and synthetic policy checks |
| **7A** | Complete Markdown wiki and generated `MANUAL.md` | **Implemented / formal stage review pending** | Documentation and manual drift checks; human sign-off still required |
| **7B.1** | **Continuous-session workflow controller** | **New / not started** | Human validates same-chat mode changes without gate bypass |
| **7B.2** | **Provider-neutral skills and optional integrations** | **New / not started** | Codex + Google Antigravity documented and usable without mandatory Claude/OpenClaw/T3 |
| **7B.3** | **Same-thread compatibility test, regression coverage and documentation refresh** | **New / not started** | Actual human-reviewed results; regenerate `MANUAL.md`; user approves Stage 7B |
| **8** | Branding and ADDF Light Games logo | **Blocked until Stage 7B approval** | Visual system review |
| 9 | Light-specific website and distribution | **Not started** | Separate preview, no accidental full-ADDF site overwrite |
| 10 | Final installation, cross-provider and release acceptance | **Not started** | v1.0 readiness and explicit release authorization |

**Dependency:** Finish/reconcile Stage 7A review, then run 7B.1 → 7B.2 → 7B.3 sequentially. **Do not begin Stage 8** until the human approves Stage 7B after reviewing actual tests. A new stage number is unnecessary; the old Branding Stage 8, Website Stage 9 and Release Stage 10 retain their identities.

## 2. Why this is a separate pre-branding stage

The user's live fresh-session Codex → Gemini exercise reportedly passed **all six handoff checks**. However, the user identified substantial interaction friction: switching workflow modes or agents should not require a **new visible conversation**. Those reported results establish useful **user-reported fresh-session handoff evidence**, not verified support for same-thread provider switching.

The current framework already permits one agent to perform Research, Design and Develop roles. Its nine distinct prompts and “stop/next prompt/new session” language nevertheless encourage a fragmented experience. Change the **default interaction routing**, not the three human gates or their authorization semantics.

The central experience becomes **one game project, one visible conversation, many safe modes**. A T3 Code model switch may create a provider-specific *internal* session under the same visible conversation; the incoming model must reconcile actual project files and approval evidence even if the UI shares chat context. A framework cannot force an unsupported host to retain a visible thread.

## 3. Sprint 7B.1 — Continuous-session workflow controller

**Goal:** One AI should move between Research → Design → Plan → Implement → Refine → Acceptance during the **same conversation** after the required human interactions, without repeatedly invoking a different prompt or starting over.

**Intended modifications:**
- `spec/FRAMEWORK_SPEC.md`, `spec/WORKFLOW_STATES.md`, `spec/APPROVAL_POLICY.md`: state explicitly that **gate stop = pause for human in the current conversation**, not forced session termination. Keep lifecycle stages and capabilities distinct.
- `starter-kit/minimal/AGENTS.md`: default to continuous conversation; auto-route the *next safe capability* from verified state and latest human request. Still honor `SECURITY.md` first and scope/gate boundaries.
- `prompts/LIGHT_GAMES.md`: identify a **single entry point** and clarify that the nine prompts are internal reusable procedures, not nine mandatory separate conversations.
- Add a provider-neutral `prompts/ROUTE.md` (or equivalent shared router) that selects workflow action from `STATE.md`, the active sprint, actual approvals, and human request. Routing does **not** authorize implementation.
- Review/edit `prompts/START.md`, `DISCOVER.md`, `RESEARCH.md`, `DESIGN.md`, `PLAN.md`, `IMPLEMENT.md`, `REFINE.md`, `ACCEPT.md`, `RESUME.md` so transitions stay in the same chat by default.
- `QUICK_START.md`: replace “open a new session to change modes” implication with a concrete same-chat script and one-command continuation.
- Avoid new mandatory `STATE.md` keys unless a real test proves they are necessary. Existing `lifecycle_stage`, `sprint_status`, Gate D/I/A records and `plan_revision` should suffice. Do not add a redundant “current model” authority field.

**Required scenarios:**
1. Same conversation: Research → Design → Plan; agent pauses for actual Gate D/I messages, then resumes in-place.
2. A user asks “switch to Develop” without approved Gate I; agent **refuses source edits** but stays available in the same chat.
3. Exact authorized Gate I permits only named paths/commands; the agent may enter Develop **in that same chat**.
4. Switching Develop → Research for investigation does not grant new implementation authority or rewrite the approved plan.
5. The user can request a new design direction without accidentally keeping stale Gate I; the agent marks scope invalid and requests new approval.
6. A test's passing status never becomes Gate A. Only actual human acceptance closes the sprint.

**Sprint exit:** The human verifies behavior and reviews changes. **Stop before 7B.2.**

## 4. Sprint 7B.2 — Subscription-first, provider-neutral adapters

**Goal:** A game project works with **Codex only, Gemini/Google Antigravity only, both, or manual chat**, with Claude Code and OpenClaw strictly optional. T3 Code is an optional interface, **not a dependency** or an approval authority.

**Intended modifications:**
- Preserve one canonical neutral workflow/skill contract, with provider skills as thin host-specific adapters. Avoid maintaining competing gate logic.
- Update `integrations/codex/` and `integrations/LIGHT_GAMES.md` to describe continuous-session routing and host-neutral files.
- Add a **Google Antigravity** adapter/instructions, using only first-party or currently supported authentication/integration surfaces; do not create OAuth/token proxies, scrape session credentials, or assume consumer subscription access is transferable.
- Add an **optional T3 Code usage guide** for same-visible-thread model switches, provider setup, workspace/worktree verification, and local safety/supervision settings. Its exact feature and account compatibility must be confirmed against the installed version and current official docs.
- Retain `integrations/claude-code/` and `integrations/openclaw/` as **optional**; neither may be required for normal onboarding.
- Keep separate host permission prompts and ADDF's **human Gate I** conceptually independent.

**Acceptance:** A plain Markdown game project can follow a full sprint using a single provider; available host adapters do not force purchase of extra API credits. Document unsupported authentication/switching combinations honestly. No unverified promise that OpenClaw, T3 Code or Antigravity can autonomously share all consumer subscriptions.

**Sprint exit:** Human reviews integration design and tests that can be genuinely run. **Stop before 7B.3.**

## 5. Sprint 7B.3 — Live compatibility, validator coverage and documentation synchronization

**Goal:** Verify the interaction promises end to end and ship coherent documentation **before branding starts**.

**Tests to add and execute where tools permit:**
- **Same model, same visible conversation:** full Research → Design → approved Plan → Implement → Refine → human Gate A with no chat restart.
- **Codex → Gemini and Gemini → Codex in the same T3 Code visible thread:** incoming provider reads the current project, verifies Gate D/I/A and worktree; no manual transcript paste. Distinguish *visible thread* from per-provider internal session.
- **No Gate I:** a model-switch or mode-switch cannot turn an unapproved plan into source edits.
- **Stale Gate I:** changed plan revision, commands, paths, dependencies, risks or unexpected worktree state forces re-approval even if chat history asserts otherwise.
- **Scope containment:** a model may only modify exact authorized files/commands; out-of-scope change stops safely.
- **No self-acceptance:** technical tests leave Gate A pending until human playtest.
- **Manual-chat fallback:** no installed provider-specific skill is needed to work in Research/Design and prepare proposed Markdown.
- **Single-provider fallback:** if T3 Code is unavailable or its version cannot support same-thread switches, a native Codex-only or Gemini-only full sprint still works.

**Test provenance:** Mark *executed and witnessed*, *user-reported*, *automated synthetic*, *documentary only* and *not tested* separately. A prompt/document change by itself is not a successful live LLM run.

**Verification and documentation changes:**
- Extend `examples/` with same-conversation and same-thread scenarios and exact expected outcomes.
- Add synthetic routing/gate boundary tests; update `scripts/` validator only for real new contract rules, without claiming it authenticates human consent.
- Update `docs/light-games/` wiki guidance (first session, prompt catalog, handoff, Codex, optional provider adapters, FAQ and limitations) and the ordered `manifest.txt` as needed.
- Include the **Remote Development and Access** guide (`docs/light-games/reference/remote-development.md`) as a required framework reference chapter, with iPad + T3 Code + VS Code remote setup, Git worktree verification, private preview/port forwarding, approved test execution, streamed-engine caveats, source-control safety, security and Gate A playtest evidence. Remote software and any per-game runbook remain optional.
- Test remote-access workflow examples by distinguishing documentation-only guidance, automated checks and actual human device/host trials. Do not mark remote iPad, preview or native engine streaming verified without a real run.
- **Regenerate root `MANUAL.md` from source wiki** using `python3 scripts/build_light_manual.py --write`; CI must pass `--check --verify-links`.
- Update Light-only CI/regression coverage and a Stage 7B review checklist; leave inherited full ADDF site and `main` unchanged.

**Sprint exit:** The human manually reviews the actual provider tests, approval boundaries, affected files and regenerated manual. Only then approve Stage 7B and permit **Stage 8 branding**.

## 6. Change and non-change boundaries

**Core behavior to change:** routing/continuation wording and skill discovery so mode transitions and human responses happen within an ongoing conversation. Provider changes require *lightweight state re-verification* but not a new visible conversation when the host supports it.

**Preserve exactly:** Five lifecycle stages; Research, Design and Develop permissions; Gate D/I/A; precise plan revision and special-effect approval; six core Markdown files; three-file active sprint pack; safety-first read order; no fake test or human evidence.

**Out of scope for Stage 7B:** Branding/logo, public website, production deployment, merging Light into `main`, mandatory T3 Code/OpenClaw/Claude dependencies, an always-on autonomous coordinator, unauthorized account/credential sharing, and changing the user's installed subscriptions.

**Automatic status:** None of 7B.1/7B.2/7B.3 is implemented or approved just because this roadmap was updated. The existing Stage 7A wiki/manual is not automatically re-approved by this new plan.

## 7. Human review and stage boundary

The human requested this roadmap change **before branding**. The plan is now the proposed Stage 7B execution sequence, not a blanket authorization to implement all three sprints at once.

**Next step:** Human may review this roadmap and explicitly authorize **7B.1 only** after resolving Stage 7A's formal review. At the end of 7B.1, stop for verification before undertaking 7B.2. Repeat for 7B.3. The Stage 8 brand sprint remains blocked until the entire Stage 7B is verified and approved.

## Related source documents

- [Framework specification](FRAMEWORK_SPEC.md)
- [Workflow states](WORKFLOW_STATES.md)
- [Approval policy](APPROVAL_POLICY.md)
- [Project file contracts](PROJECT_FILE_CONTRACTS.md)
- [Sprint file contracts](SPRINT_FILE_CONTRACTS.md)
- [Current prompt catalog](../prompts/LIGHT_GAMES.md)
- [Integration directory](../integrations/LIGHT_GAMES.md)
- [Light wiki home](../docs/light-games/index.md)
- [Generated manual](../MANUAL.md)
