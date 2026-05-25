[Home](../index.md) → [Operating Modes](index.md) → Mode 2: Feature Sprint

# Mode 2: Feature Sprint

## Use For

New features, new routes, new components, new integrations, or any change that touches more than one file or introduces new business logic.

This is the primary mode for development. The full 10-step [Sprint Workflow](../sprint-workflow.md) applies.

---

## Pre-Flight Checklist

Before opening any AI session for a Feature Sprint, confirm:

1. No open items in `QUESTIONS.md` that would prevent a sound blueprint
2. No unresolved High severity risks in `RISKS.md`
3. Architect is loaded with `AGENTS.md` + `STATE.md` + `DOMAIN.md`
4. Sprint branch has been created in git
5. Sprint folder has been initialized (`planning/sprints/sprint_NNN/`)

If any of these conditions are not met, resolve them before generating the Sprint Pack. A blueprint built against an unknown produces a build built against the wrong assumptions.

---

## Workflow

Mode 2 follows the full 10-step Sprint Workflow. See [Sprint Workflow](../sprint-workflow.md) for the complete step-by-step guide.

At a high level:
- Architect generates the Sprint Pack (Steps 1–2)
- Human reviews the blueprint and dry run (Steps 2B–4)
- Builder implements with logging (Steps 5–7)
- Architect and human review output (Steps 8–9)
- Commit, update STATE.md, close Builder thread (Step 10)

## See Also

- [Sprint Workflow](../sprint-workflow.md)
- [Step 5: Full-Scale Development](../lifecycle/05-full-scale-development.md)
- [Sprint Pack Generation prompt](../prompts.md#sprint-pack-generation)
