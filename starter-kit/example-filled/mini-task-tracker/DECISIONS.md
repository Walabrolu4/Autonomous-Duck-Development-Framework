# DECISIONS.md - Mini Task Tracker

Record every decision that would be costly or confusing to reverse here.

## Open and Active Decisions

### Decision 001 - Use localStorage for persistence

**Status:** Accepted  
**Date:** 2026-06-01  
**Decided by:** Operator

#### Context

Mini Task Tracker needs task persistence across browser reloads without a backend.

#### Decision

Store the TaskList as serialized JSON in `localStorage`.

#### Tradeoffs

This keeps v0.1 simple and local-only. It does not protect against browser data clearing or support cross-device sync.

#### Consequences

Validation must handle malformed stored JSON and reset safely if data cannot be parsed.

### Decision 002 - Single-file HTML implementation

**Status:** Accepted  
**Date:** 2026-06-01  
**Decided by:** Operator

#### Context

The v0.1 app is intentionally small and should open directly in a browser.

#### Decision

Use one `index.html` file with linked `style.css` and `app.js`.

#### Tradeoffs

The structure is easy to inspect. It is not optimized for large features.

#### Consequences

Future features should remain small or trigger a refactor decision.

### Decision 003 - No build tool for v0.1

**Status:** Accepted  
**Date:** 2026-06-01  
**Decided by:** Operator

#### Context

Build tooling would add setup work without improving the v0.1 user goal.

#### Decision

Do not use a bundler, package manager, transpiler, or framework in v0.1.

#### Tradeoffs

Manual testing is enough for v0.1, but larger behavior may need tooling later.

#### Consequences

Any new dependency requires a new decision before authorization.

## Resolved Decisions

None.
