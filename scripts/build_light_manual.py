#!/usr/bin/env python3
"""Build one deterministic Markdown manual from the canonical Light Games wiki.

Uses only the Python standard library. No network requests or external packages.
--check checks MANUAL.md without writing; --write generates it deliberately.
--verify-links checks source-wiki relative links and manifest completeness.

The wiki source of truth is docs/light-games/, ordered by manifest.txt.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "docs" / "light-games"
MANIFEST = WIKI / "manifest.txt"
OUTPUT = ROOT / "MANUAL.md"
BLOB = "https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/blob/ADDF_light_games/"
TREE = "https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework/tree/ADDF_light_games/"
LINK = re.compile(r"(\[[^\]]+\])\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
EXTERNAL = re.compile(r"^(?:https?://|mailto:|data:)", re.I)


def slug(text: str) -> str:
    """Stable simple ASCII slug, independent of GitHub's implicit anchors."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-") or "section"


def page_id(rel: str) -> str:
    assert rel.endswith(".md")
    return "wiki-" + rel[:-3].replace("/", "--").replace("_", "-")


def source_pages() -> list[str]:
    entries = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item or item.startswith("#"):
            continue
        path = WIKI / item
        if Path(item).is_absolute() or not path.resolve().is_relative_to(WIKI.resolve()):
            raise ValueError(f"Invalid manifest path: {item}")
        if not item.endswith(".md") or not path.is_file():
            raise ValueError(f"Missing/non-Markdown wiki source: {item}")
        if item in entries:
            raise ValueError(f"Duplicate manifest chapter: {item}")
        entries.append(item)
    if not entries or entries[0] != "index.md":
        raise ValueError("First chapter must be index.md")
    actual = {p.relative_to(WIKI).as_posix() for p in WIKI.rglob("*.md")}
    missing = sorted(actual - set(entries))
    if missing:
        raise ValueError(f"Wiki pages not in manifest: {', '.join(missing)}")
    return entries


def active_lines(content: str):
    """Do not rewrite or inspect literal Markdown links inside fenced code."""
    fence = None
    for line in content.splitlines():
        found = FENCE.match(line)
        if found:
            token = found.group(1)[0]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            yield line, False
        else:
            yield line, fence is None


def chapter_title(content: str, rel: str) -> str:
    headings = [m.group(2) for line,active in active_lines(content)
                if active and (m := HEADING.match(line)) and len(m.group(1)) == 1]
    if len(headings) != 1:
        raise ValueError(f"{rel}: expected exactly one H1 heading, got {len(headings)}")
    return headings[0]


def heading_slugs(content: str) -> set[str]:
    result = set()
    occurrences: dict[str, int] = {}
    for line,active in active_lines(content):
        match = HEADING.match(line) if active else None
        if match and len(match.group(1)) >= 2:
            base = slug(match.group(2))
            index = occurrences.get(base, 0)
            occurrences[base] = index + 1
            result.add(base if index == 0 else f"{base}-{index + 1}")
    return result


def resolve_link(rel: str, address: str, pages: set[str]):
    """Return a local anchor or canonical GitHub URL; raise on broken links."""
    if EXTERNAL.match(address):
        return address
    if address.startswith("#"):
        return "#" + page_id(rel) + "--" + address[1:]
    base, _, fragment = address.partition("#")
    target = ((WIKI / rel).parent / unquote(base)).resolve()
    if not target.is_relative_to(ROOT.resolve()):
        raise ValueError(f"{rel}: link escapes repository: {address}")
    if not target.exists():
        raise ValueError(f"{rel}: broken relative link: {address}")
    if target.is_relative_to(WIKI.resolve()):
        target_rel = target.relative_to(WIKI).as_posix()
        if target_rel not in pages:
            raise ValueError(f"{rel}: wiki link points to unlisted page: {target_rel}")
        return "#" + page_id(target_rel) + ("--" + fragment if fragment else "")
    target_rel = target.relative_to(ROOT).as_posix()
    url = (TREE if target.is_dir() else BLOB) + quote(target_rel, safe="/")
    return url + ("#" + fragment if fragment else "")


def transform_page(rel: str, content: str, pages: set[str]) -> str:
    title = chapter_title(content, rel)
    chapter = page_id(rel)
    out = [f'<a id="{chapter}"></a>', f"## {title}", ""]
    fence = None
    occurrences: dict[str, int] = {}
    for line in content.splitlines():
        hit = FENCE.match(line)
        if hit:
            token = hit.group(1)[0]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            out.append(line)
            continue
        if fence is not None:
            out.append(line)
            continue
        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            if level == 1:
                continue
            base = slug(heading.group(2))
            count = occurrences.get(base, 0)
            occurrences[base] = count + 1
            part = base if count == 0 else f"{base}-{count + 1}"
            out.append(f'<a id="{chapter}--{part}"></a>')
            out.append("#" * min(6, level + 1) + " " + heading.group(2))
            continue

        def replacement(match):
            label, address = match.group(1), match.group(2)
            return label + "(" + resolve_link(rel, address, pages) + ")"

        out.append(LINK.sub(replacement, line))
    return "\n".join(out).strip() + "\n"


def verify_source_links(chapters: list[str]) -> list[str]:
    errors = []
    pages = set(chapters)
    for rel in chapters:
        body = (WIKI / rel).read_text(encoding="utf-8")
        targets = heading_slugs(body)
        for line, active in active_lines(body):
            if not active:
                continue
            for hit in LINK.finditer(line):
                addr = hit.group(2)
                try:
                    resolve_link(rel, addr, pages)
                    if EXTERNAL.match(addr):
                        continue
                    base, _, fragment = addr.partition("#")
                    if addr.startswith("#"):
                        fragment = addr[1:]
                        target_rel = rel
                    else:
                        dest = ((WIKI / rel).parent / unquote(base)).resolve()
                        target_rel = dest.relative_to(WIKI).as_posix() if dest.is_relative_to(WIKI.resolve()) else ""
                    if fragment and target_rel in pages:
                        actual = targets if target_rel == rel else heading_slugs((WIKI / target_rel).read_text(encoding="utf-8"))
                        if fragment not in actual:
                            errors.append(f"{rel}: link fragment #{fragment} not present in {target_rel}")
                except ValueError as e:
                    errors.append(str(e))
    return errors


def build_manual(chapters: list[str]) -> str:
    pages = set(chapters)
    titles = [(rel, chapter_title((WIKI / rel).read_text(encoding="utf-8"), rel)) for rel in chapters]
    out = [
        "# ADDF Light Games — Complete Manual",
        "",
        "> **AUTO-GENERATED — DO NOT EDIT THIS FILE BY HAND.**",
        "> Canonical prose lives in `docs/light-games/`, ordered by `docs/light-games/manifest.txt`.",
        "> Rebuild with `python3 scripts/build_light_manual.py --write`; verify with `--check`.",
        "",
        "**Edition:** ADDF Light Games · **Branch:** `ADDF_light_games`",
        "**Documentation authority:** Approved `spec/` contracts take precedence over explanatory wiki text.",
        "**Publication status:** Stage 7 documentation candidate; not a claim of live Claude/Codex/OpenClaw validation.",
        "",
        "## Contents",
        "",
    ]
    for number, (rel, title) in enumerate(titles, 1):
        out.append(f"{number}. [{title}](#{page_id(rel)})")
    out.extend(["", "---", ""])
    for rel in chapters:
        body = (WIKI / rel).read_text(encoding="utf-8")
        out.append(transform_page(rel, body, pages).rstrip())
        out.extend(["", "---", ""])
    return "\n".join(out).rstrip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Regenerate root MANUAL.md")
    mode.add_argument("--check", action="store_true", help="Check committed manual is current (default)")
    parser.add_argument("--verify-links", action="store_true", help="Check canonical wiki relative links")
    args = parser.parse_args(argv)
    try:
        chapters = source_pages()
        errors = verify_source_links(chapters)
        if errors:
            for error in errors:
                print("ERROR: " + error, file=sys.stderr)
            return 1
        generated = build_manual(chapters)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.write:
        OUTPUT.write_text(generated, encoding="utf-8", newline="\n")
        print(f"Generated MANUAL.md from {len(chapters)} wiki chapters ({len(generated)} characters).")
        return 0
    if not OUTPUT.exists():
        print("ERROR: MANUAL.md missing; run --write", file=sys.stderr)
        return 1
    committed = OUTPUT.read_text(encoding="utf-8")
    if committed != generated:
        print("ERROR: MANUAL.md is stale; regenerate with --write and commit changes", file=sys.stderr)
        return 1
    print(f"PASS: {len(chapters)} wiki chapters; links resolve; MANUAL.md matches generated text.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
