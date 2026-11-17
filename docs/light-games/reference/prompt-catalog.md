# Prompt Catalog: What to Ask the Agent Next

The nine **agent-neutral lifecycle prompts** live under the framework distribution's `prompts/` directory. They're useful as copyable instructions in ordinary chat and as a common contract behind optional provider skills.

## When to use

Use when choosing the next command for a new or resumed project, switching models, or diagnosing why a coding agent skipped an approval checkpoint.

## Prompt lookup

| Prompt | Use it when | Safe stop point |
| --- | --- | --- |
| **START** | First encounter or unknown stage | Entry route, verified context, one question |
| **DISCOVER** | No idea, broad idea, unsure player verb | Small concepts and actual user direction |
| **RESEARCH** | Technical/design uncertainty could change next slice | Sourced findings and meaningful decision |
| **DESIGN** | Ready to define a testable outcome | Sprint and actual Gate D |
| **PLAN** | Want exact technical operations | Dry-run `PLAN.md`, stop for Gate I |
| **IMPLEMENT** | Current plan revision genuinely authorized | Actual edits/test results within scope |
| **REFINE** | Playtest/test reveals an issue | In-scope fix or revised Gate I |
| **ACCEPT** | A runnable/inspectable deliverable exists | Human Gate A and retrospective |
| **RESUME** | New session or model context loss | Verified state and one safe next step |

The [canonical prompt catalog](../../../prompts/LIGHT_GAMES.md) links to all nine full text files. The original `prompts/README.md` and mode folders still belong to the inherited full ADDF edition.

## How to select one prompt

Do **not** automatically chain START→DISCOVER→RESEARCH→DESIGN→PLAN→IMPLEMENT→ACCEPT in a single autonomous run. Choose the prompt that matches the **verified** status in `STATE.md` and stop at the next meaningful gate.

For example, `awaiting_approval` means show `PLAN.md` and request Gate I; it does not mean “IMPLEMENT as soon as the agent sees a plan file.”

## Example — handoff from browser to coding agent

In a browser chat, the human selected one mechanic and the agent drafted `SPRINT.md`. Later they open Codex on the project repo. The first Codex action is RESUME: read the files, verify status/approval, then PLAN if technical scope remains unfinished. Gate D from the browser conversation **does not** substitute for Gate I in the coding environment.

If no file tools exist, the assistant supplies proposed Markdown and explicit limitations rather than claiming it changed the repository.

## Provider adapters

- Claude Code: optional skill in `.claude/skills/addf-light-games/SKILL.md`.
- Codex: optional skill in `.agents/skills/addf-light-games/SKILL.md`.
- OpenClaw: optional workspace skill and coordinator playbook.

Each adapter is a host-friendly wrapper, not an independent approval authority or proof of live integration testing. Check that your installed host actually discovers and follows the skill before relying on it.

## Common failures

**Prompt as magic automation:** A pasted IMPLEMENT prompt authorizes unplanned writes. The actual human Gate I still matters.

**Wrong branch/version:** Use original full-ADDF prompts while intending Light. Check the edition and project instructions.

**No evidence after execution:** A model tells a story about tests. Require actual command output or mark not verified.

## Related

[Model-neutral catalog](../../../prompts/LIGHT_GAMES.md) · [Agent contract](../agents/operating-contract.md) · [Quick reference](../guides/quick-reference.md)
