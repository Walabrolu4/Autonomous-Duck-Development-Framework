# Wiki_Notes.md — Ongoing Notes and Considerations

This file is maintained automatically during wiki creation sessions. Any LLM working on the wiki documentation should read this file before starting work and add to it whenever a decision, ambiguity, inconsistency, or structural consideration is found.

**Do not delete resolved entries — mark them as resolved so the history is preserved.**

---

## How to Add a Note

Use this format:

```
### NOTE-[NNN]: [Short title]
**Date:** [YYYY-MM-DD]
**Found on page:** [file being written when this was discovered]
**Status:** Open / Resolved / Deferred
**Note:** [What was found — the ambiguity, inconsistency, decision needed, or consideration]
**Resolution:** [Leave blank if open. Fill in when resolved.]
```

---

## Open Notes

*No open notes.*

---

## Resolved Notes

### NOTE-001: Phase 2 has no individual checkboxes in WIKI_TODOS.md
**Date:** 2026-05-25
**Found on page:** `docs/WIKI_TODOS.md` (Phase 2 block)
**Status:** Resolved
**Note:** Phase 2 is described as a block of instructions but has no individual `- [ ]` checkboxes. The summary count table lists "35 files to touch" but the actual file count is 40 (12 root + 9 lifecycle + 7 modes + 12 file-reference). The "Total pages to write: 35" in WIKI_GUIDE.md appears to be a counting error in the source document — the actual structure has 40 files.
**Resolution:** Treated Phase 2 as a single block task. Wrote breadcrumb + See Also stubs to all 40 files. No individual boxes to check. Proceeded to Phase 3.

### NOTE-002: WIKI_GUIDE.md says "Total pages to write: 35" but structure has 40 files
**Date:** 2026-05-25
**Found on page:** `docs/WIKI_GUIDE.md` (Wiki Structure at a Glance section)
**Status:** Resolved
**Note:** Counting the files in the structure tree: 12 root docs + 9 lifecycle + 7 modes + 12 file-reference = 40. The "35" figure in WIKI_GUIDE is wrong by 5. Does not block any work — just a documentation inconsistency in the guide itself.
**Resolution:** Proceeded with 40 files as the correct target. All 40 created, stubbed, and fully populated. Wiki complete.
