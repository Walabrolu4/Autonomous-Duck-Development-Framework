# Source Summary

## Purpose

Summarize one source and extract the parts that matter to the project.

## When to Use

Use this after loading an article, documentation page, specification, PDF excerpt, or other source.

## Mode

Research Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- The source being summarized
- Relevant `research/sources.md`, if present

## Prompt

```text
You are operating in Research Mode for [PROJECT NAME].

Summarize this source:
[SOURCE NAME OR FILE]

Focus on:
- Relevance to the active project, release, feature, or sprint
- Constraints the source introduces
- Risks or unknowns
- Terminology that should be checked against DOMAIN.md

Do not make decisions. Do not write implementation files.
```

## Expected Output

- Source summary.
- Key points.
- Relevance rating.
- Risks and open questions.
- Suggested `research/sources.md` row.

## Notes

Keep source summaries short enough that future sessions can scan them quickly.
