# RISKS.md - Mini Task Tracker

## Risk 001 - localStorage size limit

**Risk:** A very large task list could exceed browser storage limits.  
**Severity:** Low  
**Probability:** Low  
**Status:** Open  
**Mitigation:** Keep v0.1 scoped to a small personal task list.

## Risk 002 - Data loss if browser data is cleared

**Risk:** Tasks disappear if the operator clears browser storage.  
**Severity:** Medium  
**Probability:** Medium  
**Status:** Open  
**Mitigation:** Document local-only persistence and consider export in v0.2.

## Risk 003 - Scope creep to server-side persistence

**Risk:** Requests for sync, sharing, or accounts could push v0.1 beyond its local-only goal.  
**Severity:** Medium  
**Probability:** Medium  
**Status:** Mitigated  
**Mitigation:** Keep server storage, accounts, and sharing out of v0.1 scope.
