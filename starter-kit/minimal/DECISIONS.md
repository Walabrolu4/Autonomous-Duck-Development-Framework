# Decision Log

> Human-owned significant choices live here. The agent offers research/tradeoffs and transcribes the **actual** human choice. No template entry counts as consent. Routine T0 decisions need not be logged.

## Decision index

No decisions have been made in this blank project.

When the user makes or defers a consequential decision, allocate the next unused ID `D-001`, `D-002`, ... and add a link to the record in the relevant section below. Never recycle an ID after rejection or supersession.

## Active decisions

No active human decisions yet.

For a real chosen decision, create an entry under this heading with this required structure:

```md
### D-001 — [specific question]
- status: chosen
- tier: T1
- sprint: sprint-001
- context: [why it matters]
- options: [actual alternatives presented]
- evidence: [real source/test or unknown]
- ai_recommendation: [agent suggestion, or none]
- human_choice: [actual user response or stable reference]
- rationale: [user rationale or not_recorded]
- implications: [behavior, scope, tests]
- supersedes: none
- revisit_when: [specific trigger or not_scheduled]
```

**Example above is a schema illustration only.** Do not leave it as an actual `D-001` decision in the live record. On real entries, supported `status` values are `chosen`, `deferred`, `rejected` and `superseded`; `tier` is `T1` or `T2`; `sprint` is `sprint-NNN` or `project-wide`.

## Deferred questions

No material choice deferred yet.

When a user says “not sure,” record the actual question, options, evidence, `human_choice: pending`, and a specific experiment or revisit trigger. Do **not** auto-select the agent recommendation.

## Superseded and rejected decisions

None.

When replacing a choice, preserve the earlier record and its reasoning; mark it `superseded` and add a **new** decision ID referencing the old one via `supersedes`. Do not delete human decision history.

**Record source policy:** Quote an actual human reply when available in the current session or link to an existing durable review. If no source is available, mark the decision unresolved instead of inventing consent.
