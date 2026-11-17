#!/usr/bin/env python3
"""ADDF Light Games validator: read-only, stdlib-only, no subprocess/network.

Validates the *structure and recorded state* of a game project's Markdown
brain and sprint pack. It cannot authenticate human consent, play games,
or prove a coding agent behaved correctly. See scripts/README.md.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote

from light_schema import (CORE, SPRINT, FIELDS, ENUMS, ID_FIELDS,
                          EXPECTED_STAGES, ADVANCED, REVIEW_READY, PENDING)

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
KEY = re.compile(r"^\s*-\s+([A-Za-z]\w*):\s*(.*?)\s*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ID = {"D":re.compile(r"^D-\d{3}(?:\s+—\s+.+)?$"),
      "B":re.compile(r"^B-\d{3}(?:\s+—\s+.+)?$"),
      "AC":re.compile(r"^AC-\d{2}(?:\s+—\s+.+)?$")}

@dataclass
class Finding:
    level: str
    code: str
    file: str
    message: str

class Result:
    def __init__(self):
        self.findings: list[Finding] = []
        self.files_checked = 0
    def emit(self, level, code, file, message):
        self.findings.append(Finding(level, code, str(file), message))
    @property
    def status(self):
        levels = {f.level for f in self.findings}
        return "FAIL" if "fail" in levels else "WARN" if "warn" in levels else "PASS"

class Document:
    """Only explicitly named contract files are read. Fenced examples are ignored."""
    def __init__(self, root: Path, relative: str, result: Result):
        self.root, self.path, self.result = root, relative, result
        self.loaded = False
        self.lines: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.sections: dict[str, list[str]] = {}
        target = root / relative
        try:
            if not target.resolve().is_relative_to(root.resolve()):
                result.emit("fail", "L-F001", relative, "File resolves outside project root")
                return
            if not target.is_file():
                result.emit("fail", "L-F001", relative, "Required Markdown file is missing")
                return
            raw = target.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as e:
            result.emit("fail", "L-F001", relative, f"Cannot read: {type(e).__name__}")
            return
        self.loaded = True
        result.files_checked += 1
        fence = None
        for line in raw.splitlines():
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if m:
                if fence is None:
                    fence = m.group(1)[0]
                elif fence == m.group(1)[0]:
                    fence = None
                self.lines.append("")
            else:
                self.lines.append("" if fence else line)
        section = None
        for line in self.lines:
            m = HEADING.match(line)
            if m:
                level, text = len(m.group(1)), m.group(2).strip()
                self.headings.append((level, text))
                if level == 2:
                    section = text
                    self.sections.setdefault(text, [])
            elif section is not None:
                self.sections[section].append(line)

    def fields(self, section: str) -> dict[str, str]:
        found = {}
        for line in self.sections.get(section, []):
            m = KEY.match(line)
            if m:
                if m.group(1) in found:
                    self.result.emit("fail", "L-F002", self.path,
                                     f"Duplicate - {m.group(1)}: in ## {section}")
                found[m.group(1)] = m.group(2)
        return found

    def validate_shape(self, title: str, sections: list[str], fields: dict):
        if not self.loaded:
            return
        h1 = [t for level, t in self.headings if level == 1]
        if title == "sprint":
            valid_title = len(h1) == 1 and bool(re.fullmatch(r"Sprint (NNN|\d{3}) — .+", h1[0]))
        else:
            valid_title = h1 == [title]
        if not valid_title:
            self.result.emit("fail", "L-F002", self.path, f"Invalid H1; expected {title!r}, found {h1!r}")
        actual = [t for level,t in self.headings if level == 2]
        order = []
        for section in sections:
            if section not in actual:
                self.result.emit("fail", "L-F002", self.path, f"Missing ## {section}")
            else:
                order.append(actual.index(section))
                if actual.count(section) != 1:
                    self.result.emit("fail", "L-F002", self.path, f"Duplicate ## {section}")
        if order != sorted(order):
            self.result.emit("fail", "L-F002", self.path, "Required H2 headings are out of order")
        for section, keys in fields.items():
            data = self.fields(section)
            for key in keys.split():
                if key not in data:
                    self.result.emit("fail", "L-F002", self.path, f"Missing - {key}: under ## {section}")

    def ids(self, kind: str):
        values = [text.split()[0] for level,text in self.headings
                  if level == 3 and ID[kind].fullmatch(text)]
        for x in sorted(set(values)):
            if values.count(x) != 1:
                self.result.emit("fail", "L-F005", self.path, f"Duplicate {kind} identifier {x}")
        return values

    def enum(self, section, key):
        value = self.fields(section).get(key)
        if value is not None and value not in ENUMS[key].split():
            self.result.emit("fail", "L-F004", self.path,
                             f"Invalid {key}={value!r}; expected {ENUMS[key]}")

    def links(self):
        if not self.loaded:
            return
        for line in self.lines:
            for m in LINK.finditer(line):
                link = m.group(1).split()[0].strip("<>")
                if not link or link.startswith(("http://", "https://", "mailto:", "#", "data:")):
                    continue
                target = (self.root / self.path).parent / unquote(link.split("#")[0].split("?")[0])
                if not target.resolve().is_relative_to(self.root.resolve()):
                    self.result.emit("fail", "L-F006", self.path, f"Relative link escapes root: {link}")
                elif not target.exists():
                    self.result.emit("fail", "L-F006", self.path, f"Broken relative link: {link}")

def meaningful(value):
    return value is not None and value not in PENDING

def decision_entries(doc: Document, kind: str):
    """Find real H3 entries and check their fields, not illustrative fenced examples."""
    if not doc.loaded:
        return
    ids = doc.ids(kind)
    if not ids:
        return
    source = "\n".join(doc.lines)
    # Split at actual heading boundaries, with IDs appearing before sections/prose.
    for m in re.finditer(r"(?m)^###\s+(" + kind + r"-\d{3})(?:\s+—\s+[^\n]+)?$", source):
        start = m.end()
        next_h = re.search(r"(?m)^#{2,3}\s+", source[start:])
        end = start + next_h.start() if next_h else len(source)
        block = source[start:end]
        keys = {x.group(1) for l in block.splitlines() if (x := KEY.match(l))}
        for key in ID_FIELDS[kind].split():
            if key not in keys:
                doc.result.emit("fail", "L-F002", doc.path, f"{m.group(1)} missing - {key}:")

def check_operations(plan: Document, result: Result, required: bool):
    """No broad wildcard or traversal operation. Does NOT authenticate historical scope."""
    operations = []
    for line in plan.sections.get("Exact file operations", []):
        if not line.strip().startswith("|"):
            continue
        cells = [v.strip().strip("`") for v in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] not in {"create", "modify", "move", "delete"}:
            continue
        operations.append(cells[:2])
        path = cells[1]
        if (path.lower() in {"", "all", "any", "none"} or path.startswith("/")
                or ".." in Path(path).parts or any(x in path for x in ("*", "?", "{", "}"))):
            result.emit("fail", "L-F007", plan.path, f"Unsafe or unbounded operation path: {path}")
    if required and not operations:
        result.emit("fail", "L-F007", plan.path, "Authorized plan has no concrete operation rows")
    if required:
        result.emit("warn", "L-H002", plan.path,
                    "Current operation scope is checked, but historical human-approved scope cannot be authenticated")

def validate(root: Path, *, mode="project", sprint_template: Path | None = None) -> Result:
    result = Result()
    if not root.is_dir():
        result.emit("fail", "L-F001", root, "Root is not a directory")
        return result
    core = {name: Document(root, name, result) for name in CORE}
    for name,(title,sections) in CORE.items():
        core[name].validate_shape(title, sections.split("|"), FIELDS.get(name, {}))
        core[name].links()
    agents = core["AGENTS.md"]
    security = core["SECURITY.md"]
    game = core["GAME.md"]
    state = core["STATE.md"]
    for section,keys in (("Edition and scope", ["framework_edition"]),):
        for key in keys: agents.enum(section,key)
    for key in ("execution_mode", "network_access", "secret_handling"):
        security.enum("Execution environment",key)
    for key in ("project_origin","game_target"):
        game.enum("Project identity", key)
    for key in ("lifecycle_stage","sprint_status"):
        state.enum("Identity and state",key)
    state.enum("Active authorization","authorized")
    state.enum("Next action","actor")
    decision_entries(core["DECISIONS.md"],"D")
    decision_entries(core["planning/BACKLOG.md"],"B")
    sid = state.fields("Identity and state")
    approval = state.fields("Active authorization")
    gate_summary = state.fields("Gate evidence")
    game_id = game.fields("Project identity").get("project_id")
    status = sid.get("sprint_status")
    stage = sid.get("lifecycle_stage")
    active = sid.get("active_sprint")
    if game_id and game_id!="undecided" and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", game_id):
        result.emit("fail","L-F003","GAME.md",f"Invalid project_id={game_id}")
    if game_id and sid.get("project_id")!=game_id:
        result.emit("fail","L-F011","STATE.md","Project ID disagrees with GAME.md")
    if status in EXPECTED_STAGES and stage!=EXPECTED_STAGES[status]:
        result.emit("fail","L-F004","STATE.md",f"Stage/status mismatch: {stage}/{status}")
    if active and active!="none" and not re.fullmatch(r"sprint-\d{3}",active):
        result.emit("fail","L-F003","STATE.md",f"Invalid sprint ID {active}")
    if approval.get("authorized")=="yes" and active=="none":
        result.emit("fail","L-F009","STATE.md","No active sprint, yet authorized=yes")

    docs = {}
    if mode=="template":
        if sprint_template is None or not sprint_template.is_dir():
            result.emit("fail","L-F001","sprint-template","Template mode requires --sprint-template folder")
        else:
            docs = {name:Document(sprint_template,name,result) for name in SPRINT}
        if (active!="none" or status!="discovering" or stage!="research"
                or approval.get("authorized")!="no" or approval.get("plan_revision")!="none"
                or gate_summary.get("gate_i")!="pending" or gate_summary.get("gate_a")!="pending"):
            result.emit("fail","L-F010","STATE.md","Blank template must be discovering with no authorization")
        if (root/"planning/sprints").exists():
            result.emit("fail","L-F001","planning/sprints","Blank starter may not pre-create sprint folders")
    elif active and re.fullmatch(r"sprint-\d{3}",active):
        docs = {name:Document(root,f"planning/sprints/{active}/{name}",result) for name in SPRINT}
    elif status in ADVANCED or approval.get("authorized")=="yes":
        result.emit("fail","L-F001","STATE.md","Advanced state requires active sprint and full three-file pack")

    for name,doc in docs.items():
        doc.validate_shape("sprint",SPRINT[name].split("|"),FIELDS[name])
        doc.links()
        metadata = doc.fields("Sprint metadata")
        for key in ("sprint_kind","status"): doc.enum("Sprint metadata",key)
        if not re.fullmatch(r"r\d+",metadata.get("file_revision","")):
            result.emit("fail","L-F004",doc.path,"file_revision must be rN")
        if mode=="project" and metadata.get("sprint_id")!=active:
            result.emit("fail","L-F011",doc.path,"sprint_id disagrees with STATE.md")
        if game_id and metadata.get("project_id")!=game_id:
            result.emit("fail","L-F011",doc.path,"project_id disagrees with GAME.md")
        if name=="SPRINT.md": doc.enum("Design approval — Gate D","gate_d_status")
        if name=="PLAN.md": doc.enum("Implementation approval — Gate I","gate_i_status")
        if name=="REVIEW.md": doc.enum("Human acceptance — Gate A","gate_a_status")
    if len(docs)!=3 or not all(d.loaded for d in docs.values()):
        return result

    kinds = {d.fields("Sprint metadata").get("sprint_kind") for d in docs.values()}
    if len(kinds)!=1:
        result.emit("fail","L-F011","sprint-pack","Sprint kinds differ across files")
    sprint,plan,review = docs["SPRINT.md"],docs["PLAN.md"],docs["REVIEW.md"]
    d = sprint.fields("Design approval — Gate D")
    i = plan.fields("Implementation approval — Gate I")
    a = review.fields("Human acceptance — Gate A")
    ac = sprint.ids("AC")
    observed = review.ids("AC")
    if status in ADVANCED and not ac:
        result.emit("fail","L-F008",sprint.path,"Advanced sprint has no real AC-## entries")
    if status in REVIEW_READY:
        if set(ac)!=set(observed):
            result.emit("fail","L-F008",review.path,
                        f"Acceptance criteria not covered: expected {sorted(set(ac))}, got {sorted(set(observed))}")
        source = "\n".join(review.lines)
        for criterion in observed:
            m = re.search(r"(?ms)^###\s+"+re.escape(criterion)+r"\s+—[^\n]*\n(.*?)(?=^#{2,3}\s+|\Z)",source)
            if not m or not re.search(r"(?m)^- result: (pass|fail|partial|not_tested)$",m.group(1)):
                result.emit("fail","L-F008",review.path,f"{criterion} has no valid - result:")
    if d.get("gate_d_status")=="approved" and (
        not meaningful(d.get("human_response")) or not meaningful(d.get("recorded_from"))
        or d.get("approved_sprint_revision")!=sprint.fields("Sprint metadata").get("file_revision")
    ):
        result.emit("fail","L-F010",sprint.path,"Gate D claims approval without recorded human choice and matching revision")
    current_auth = approval.get("authorized")=="yes" or status=="implementing"
    historic_auth = i.get("gate_i_status")=="authorized"
    check_operations(plan,result,current_auth or historic_auth)
    if current_auth or historic_auth:
        if current_auth and (approval.get("authorized")!="yes" or not historic_auth):
            result.emit("fail","L-F009",plan.path,"Implementation requires STATE.authorized=yes and PLAN Gate I=authorized")
        if approval.get("authorized")=="yes" and status in {"accepted","rejected"}:
            result.emit("fail","L-F009","STATE.md","Terminal sprint must revoke active authorization")
        if d.get("gate_d_status") not in {"approved","not_required"}:
            result.emit("fail","L-F010",sprint.path,"Unresolved Gate D")
        if (i.get("plan_revision")!=plan.fields("Sprint metadata").get("file_revision")
                or i.get("linked_sprint_revision")!=sprint.fields("Sprint metadata").get("file_revision")
                or (current_auth and approval.get("plan_revision")!=i.get("plan_revision"))):
            result.emit("fail","L-F009",plan.path,"Gate I / plan / sprint revision mismatch")
        if (not meaningful(i.get("human_response")) or not meaningful(i.get("recorded_from"))
                or (current_auth and not meaningful(approval.get("authorized_by")))):
            result.emit("fail","L-F010",plan.path,"Gate I response/source/authorization evidence missing")
        if not meaningful(i.get("authorized_operations")):
            result.emit("fail","L-F007",plan.path,"Gate I has no finite operation reference")
        if current_auth and (
            approval.get("scope_reference")!=f"planning/sprints/{active}/PLAN.md"
            or not meaningful(gate_summary.get("gate_i"))
        ):
            result.emit("fail","L-F009","STATE.md","Active Gate I scope reference or evidence summary missing")
        result.emit("warn","L-H001",plan.path,"Human-approval text cannot be independently authenticated")
    if status=="accepted":
        if (a.get("gate_a_status") not in {"accepted","accepted_with_conditions"}
                or not meaningful(a.get("human_response")) or not meaningful(a.get("recorded_from"))
                or not meaningful(gate_summary.get("gate_a"))):
            result.emit("fail","L-F010",review.path,"Accepted sprint missing recorded human Gate A")
        if a.get("outstanding_release_blockers")!="none":
            result.emit("fail","L-F010",review.path,"Accepted sprint has unresolved/unknown release blockers")
        result.emit("warn","L-H001",review.path,"Human playtest and acceptance cannot be independently authenticated")
    if status=="rejected" and a.get("gate_a_status")!="rejected":
        result.emit("fail","L-F010",review.path,"Rejected sprint missing rejected Gate A")
    if mode=="template" and (
        i.get("gate_i_status")!="pending" or a.get("gate_a_status")!="pending"):
        result.emit("fail","L-F010","sprint-template","Distribution templates cannot pre-approve Gate I or A")
    return result

def main(argv=None):
    parser=argparse.ArgumentParser(description="Validate ADDF Light Games file contracts (read-only, stdlib only)")
    parser.add_argument("root",type=Path,help="Game project root or minimal starter folder")
    parser.add_argument("--mode",choices=["project","template"],default="project")
    parser.add_argument("--sprint-template",type=Path,help="Required in template mode")
    parser.add_argument("--format",choices=["text","json"],default="text")
    parser.add_argument("--strict",action="store_true",help="Exit nonzero on WARN as well as FAIL")
    args=parser.parse_args(argv)
    r=validate(args.root,mode=args.mode,sprint_template=args.sprint_template)
    if args.format=="json":
        print(json.dumps({"status":r.status,"files_checked":r.files_checked,
                          "findings":[asdict(f) for f in r.findings]},indent=2))
    else:
        print(f"ADDF Light Games validation: {r.status} ({r.files_checked} files read)")
        for f in r.findings:
            print(f"{f.level.upper():4} {f.code} {f.file}: {f.message}")
        if not r.findings:
            print("No recorded-state contract issues found; human consent and gameplay still require real verification.")
    return 1 if r.status=="FAIL" or (args.strict and r.status=="WARN") else 0

if __name__=="__main__":
    sys.exit(main())
