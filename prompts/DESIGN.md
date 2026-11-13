# DESIGN — Select one testable game slice

**When to use:** Enough research/ideation exists to propose the next game sprint and acceptance criteria. **Capability:** Design. **No implementation writes.**

## Copyable agent instruction

Work inside the **user's game project**, not the framework distribution repository. Read the safe project brain under `SECURITY.md` and use the latest **actual** `GAME.md`, `DECISIONS.md`, `STATE.md` and backlog context.

1. Propose **one user-observable result**—for a game, preferably a small playable vertical slice. Identify the exact player action, system response and what a human will test. If research-only, label it `research-spike`.
2. Review focused evidence, uncertainties, accessibility constraints, platform assumptions, and alternative approaches. Clearly separate agent recommendations from actual human choices.
3. For each significant T1/T2 choice, explain tradeoffs and ask for a human **Gate D** decision. Respect `not sure` and `defer`; allow a reversible experiment if the human wants one.
4. Choose a candidate `B-###` backlog item or propose one without assuming its priority was approved.
5. Once the **human selects the milestone**, instantiate the **three-file sprint pack** from the Stage 3 `sprint-template/` distribution, at the next `planning/sprints/sprint-NNN/`. Do **not** pre-create future sprints.
6. Fill `SPRINT.md`: why, player outcome, `### In scope` / `### Out of scope`, sourced research, alternatives and learning checkpoint, decision IDs, risks, constraints, and actual `AC-##` acceptance criteria.
7. Acceptance checks must state observable action/setup/pass condition, testing method and evidence expected; avoid empty/vague claims such as “fun” or “works.” A research spike defines a verifiable knowledge outcome.
8. Record **the actual** Gate D response in `SPRINT.md` and `DECISIONS.md`. If there are no material design forks, justify `gate_d_status: not_required`; do not invent a human choice.
9. Update `STATE.md` to `designing` only when consistent with the Stage 1 state machine. Do not enter `implementing` or mark authorization.

**Learning:** Include one relevant mechanic, game-system or level-design tradeoff and how it will be tested; avoid tests of the human's memorization.

**Do not:** write game code, create assets, install packages, alter test files, choose consequential direction without consent, or treat design approval as Gate I.

**Output contract:**
- Sprint ID and one-sentence playable goal.
- Scope in/out and design options.
- At least one meaningful acceptance criterion `AC-##` with method and pass condition.
- Learning checkpoint and risks/unknowns.
- Gate D `approved | pending | not_required` with real evidence or reason.
- Created/updated Markdown paths, with any human decision still needed.

**Stop condition:** Design direction is explicitly resolved (or validly non-required), and the next step is a **dry-run `PLAN.md`**. Do not auto-run [IMPLEMENT](IMPLEMENT.md); move to [PLAN](PLAN.md).
