# Research Notes

**Question being researched:** localStorage limits and browser compatibility  
**Date:** 2026-06-01  
**Mode:** Research Mode

## Findings

- Most browsers provide roughly 5MB of localStorage per origin.
- Mini Task Tracker does not need cross-tab sync for v0.1 because it is single operator.
- JSON serialization is sufficient for the flat TaskList data model.

## Open Items

- Confirm Safari behavior for private browsing and storage quota.
