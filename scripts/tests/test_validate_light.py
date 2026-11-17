"""Stage 6 executable validator regression tests. Stdlib only; no remote calls.

Synthetic Gate D/I/A records below are fixtures, NOT actual human approval.
Run from repo root: python3 -m unittest discover -s scripts/tests -v
"""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

SCRIPTS=Path(__file__).resolve().parents[1]
REPO=SCRIPTS.parent
sys.path.insert(0,str(SCRIPTS))
import light_schema as schema
import validate_light as validator

def make_doc(title, sections, values=None):
    values=values or {}
    lines=[f"# {title}"]
    for h in sections:
        lines+=["",f"## {h}"]
        lines += [f"- {k}: {v}" for k,v in values.get(h,{}).items()]
    return "\n".join(lines)+"\n"

def initial(root):
    vals={
      "AGENTS.md":{"Edition and scope":{"framework_edition":"addf-light","contract_version":"0.1-draft","project_name":"unknown"}},
      "SECURITY.md":{"Execution environment":{"execution_mode":"unknown","network_access":"human-approved-only","secret_handling":"never-load"}},
      "GAME.md":{"Project identity":{"project_id":"pilot","working_title":"unknown","project_origin":"no-idea","game_target":"undecided"},
                 "Current playable hypothesis":{"prototype_goal":"unknown","player_action":"unknown","observable_result":"unknown"}},
      "STATE.md":{"Identity and state":{"project_id":"pilot","active_sprint":"none","lifecycle_stage":"research","sprint_status":"discovering","last_verified_at":"unknown"},
                  "Gate evidence":{"gate_d":"pending","gate_i":"pending","gate_a":"pending"},
                  "Active authorization":{"plan_revision":"none","scope_reference":"none","authorized":"no","authorized_by":"none"},
                  "Next action":{"actor":"agent","action":"Ask the first meaningful question"}},
    }
    for path,(h1,heads) in schema.CORE.items():
        p=root/path
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(make_doc(h1,heads.split("|"),vals.get(path)),encoding="utf-8")

def write_field(path,key,value):
    text=path.read_text(encoding="utf-8")
    result,n=re.subn(r"(?m)^(- "+re.escape(key)+r": ).*$",lambda m:m.group(1)+value,text,count=1)
    if not n: raise AssertionError(f"Missing {key} in {path}")
    path.write_text(result,encoding="utf-8")

def sprint(root,actual=True):
    folder=root/("planning/sprints/sprint-001" if actual else "sprint-template")
    folder.mkdir(parents=True,exist_ok=True)
    meta={"sprint_id":"sprint-001","sprint_kind":"playable-slice","project_id":"pilot","file_revision":"r1","status":"draft"}
    values={
      "SPRINT.md":{"Sprint metadata":meta,"Design approval — Gate D":{"gate_d_status":"pending","decision_references":"none","human_response":"pending","recorded_from":"pending","approved_sprint_revision":"none","conditions":"none"}},
      "PLAN.md":{"Sprint metadata":meta,"Implementation approval — Gate I":{"plan_revision":"r1","linked_sprint_revision":"r1","gate_i_status":"pending","authorized_operations":"none","authorized_commands":"none","dependency_approvals":"none","separate_special_approvals":"none","human_response":"pending","recorded_from":"pending","conditions":"none"}},
      "REVIEW.md":{"Sprint metadata":meta,"Human acceptance — Gate A":{"review_round":"round-1","gate_a_status":"pending","human_response":"pending","recorded_from":"pending","conditions":"none","outstanding_release_blockers":"unknown","next_action":"Playtest later"}},
    }
    for name,heads in schema.SPRINT.items():
        title=f"Sprint {'001' if actual else 'NNN'} — "+{"SPRINT.md":"First movement","PLAN.md":"Implementation Plan","REVIEW.md":"Review and Acceptance"}[name]
        (folder/name).write_text(make_doc(title,heads.split("|"),values[name]),encoding="utf-8")
    if actual:
        p=folder/"SPRINT.md"
        p.write_text(p.read_text().replace("## Acceptance criteria","## Acceptance criteria\n\n### AC-01 — Move\n- method: manual-playtest\n- setup: desktop\n- action: arrows\n- pass_condition: avatar moves\n- evidence: review\n- release_blocking: yes\n"),encoding="utf-8")
    return folder

def authorized(root):
    folder=sprint(root)
    state=root/"STATE.md"
    for k,v in {"active_sprint":"sprint-001","lifecycle_stage":"implement","sprint_status":"implementing","plan_revision":"r1","scope_reference":"planning/sprints/sprint-001/PLAN.md","authorized":"yes","authorized_by":"SYNTHETIC_TEST","gate_d":"D-001 fixture","gate_i":"r1 fixture"}.items():
        write_field(state,k,v)
    for k,v in {"gate_d_status":"approved","human_response":"SYNTHETIC","recorded_from":"SYNTHETIC_TEST","approved_sprint_revision":"r1"}.items():
        write_field(folder/"SPRINT.md",k,v)
    for k,v in {"gate_i_status":"authorized","authorized_operations":"exact listed operations","human_response":"SYNTHETIC","recorded_from":"SYNTHETIC_TEST"}.items():
        write_field(folder/"PLAN.md",k,v)
    p=folder/"PLAN.md"
    p.write_text(p.read_text().replace("## Exact file operations","## Exact file operations\n| Operation | Exact path | Purpose | Boundary | Recovery |\n| --- | --- | --- | --- | --- |\n| create | game.js | AC-01 | only movement | delete newly added file |"),encoding="utf-8")
    return folder

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root=Path(tmp.name)/"game"
        self.root.mkdir()
        initial(self.root)
    def check(self,mode="project",sprint_template=None):
        return validator.validate(self.root,mode=mode,sprint_template=sprint_template)
    def failed(self,code):
        return any(f.level=="fail" and f.code==code for f in self.check().findings)

    def test_blank_project_passes(self):
        self.assertEqual(self.check().status,"PASS")
    def test_uninstantiated_sprint_templates_pass(self):
        folder=sprint(self.root,actual=False)
        self.assertEqual(self.check("template",folder).status,"PASS")
    def test_missing_core_file(self):
        (self.root/"SECURITY.md").unlink()
        self.assertTrue(self.failed("L-F001"))
    def test_missing_required_heading(self):
        p=self.root/"AGENTS.md";p.write_text(p.read_text().replace("## Session startup","## Wrong heading"))
        self.assertTrue(self.failed("L-F002"))
    def test_invalid_state_enum(self):
        write_field(self.root/"STATE.md","sprint_status","automatic")
        self.assertTrue(self.failed("L-F004"))
    def test_duplicate_decisions(self):
        p=self.root/"DECISIONS.md"
        with p.open("a") as f:f.write("\n### D-001 — A\n### D-001 — B\n")
        self.assertTrue(self.failed("L-F005"))
    def test_broken_link(self):
        with (self.root/"GAME.md").open("a") as f:f.write("\n[missing](no-such-file.md)\n")
        self.assertTrue(self.failed("L-F006"))
    def test_valid_design_sprint(self):
        sprint(self.root)
        for k,v in {"active_sprint":"sprint-001","lifecycle_stage":"design","sprint_status":"designing"}.items():
            write_field(self.root/"STATE.md",k,v)
        self.assertEqual(self.check().status,"PASS")
    def test_missing_active_sprint_pack(self):
        for k,v in {"active_sprint":"sprint-001","lifecycle_stage":"design","sprint_status":"awaiting_approval"}.items():
            write_field(self.root/"STATE.md",k,v)
        self.assertTrue(self.failed("L-F001"))
    def test_active_sprint_id_mismatch(self):
        f=sprint(self.root)
        for k,v in {"active_sprint":"sprint-001","lifecycle_stage":"design","sprint_status":"designing"}.items():
            write_field(self.root/"STATE.md",k,v)
        write_field(f/"PLAN.md","sprint_id","sprint-002")
        self.assertTrue(self.failed("L-F011"))
    def test_implementing_without_gate_i(self):
        sprint(self.root)
        for k,v in {"active_sprint":"sprint-001","lifecycle_stage":"implement","sprint_status":"implementing"}.items():
            write_field(self.root/"STATE.md",k,v)
        self.assertTrue(self.failed("L-F009"))
    def test_synthetic_gate_i_yields_warning_not_authenticated(self):
        authorized(self.root)
        r=self.check()
        self.assertEqual(r.status,"WARN",r.findings)
        self.assertTrue(any(f.code=="L-H001" for f in r.findings))
    def test_stale_plan_revision(self):
        f=authorized(self.root)
        write_field(f/"PLAN.md","file_revision","r2")
        self.assertTrue(self.failed("L-F009"))
    def test_unbounded_operation(self):
        f=authorized(self.root);p=f/"PLAN.md"
        p.write_text(p.read_text().replace("| create | game.js |","| create | **/* |"))
        self.assertTrue(self.failed("L-F007"))
    def test_no_concrete_operation(self):
        f=authorized(self.root);p=f/"PLAN.md"
        p.write_text(p.read_text().replace("| create | game.js |","| none | game.js |"))
        self.assertTrue(self.failed("L-F007"))
    def test_accepted_without_human_gate_a(self):
        authorized(self.root)
        for k,v in {"lifecycle_stage":"acceptance","sprint_status":"accepted","authorized":"no"}.items():
            write_field(self.root/"STATE.md",k,v)
        self.assertTrue(self.failed("L-F010"))
    def test_missing_review_criterion(self):
        authorized(self.root)
        for k,v in {"lifecycle_stage":"acceptance","sprint_status":"awaiting_acceptance"}.items():
            write_field(self.root/"STATE.md",k,v)
        self.assertTrue(self.failed("L-F008"))
    def test_valid_structural_acceptance_only_warns(self):
        f=authorized(self.root)
        for k,v in {"lifecycle_stage":"acceptance","sprint_status":"accepted","authorized":"no","gate_a":"SYNTHETIC round-1"}.items():
            write_field(self.root/"STATE.md",k,v)
        for k,v in {"gate_a_status":"accepted","human_response":"SYNTHETIC","recorded_from":"SYNTHETIC_TEST","outstanding_release_blockers":"none"}.items():
            write_field(f/"REVIEW.md",k,v)
        p=f/"REVIEW.md"
        p.write_text(p.read_text().replace("## Acceptance criteria results","## Acceptance criteria results\n### AC-01 — Move\n- result: pass\n- method: manual-playtest\n- performed_by: human\n- environment: synthetic\n- evidence: SYNTHETIC\n- notes: simulated\n"),encoding="utf-8")
        self.assertEqual(self.check().status,"WARN")
    def test_cli_json_and_strict(self):
        cmd=[sys.executable,str(SCRIPTS/"validate_light.py"),str(self.root),"--format","json"]
        outcome=subprocess.run(cmd,capture_output=True,text=True,check=False)
        self.assertEqual(outcome.returncode,0,outcome.stderr)
        self.assertEqual(json.loads(outcome.stdout)["status"],"PASS")
        authorized(self.root)
        outcome=subprocess.run(cmd+["--strict"],capture_output=True,text=True,check=False)
        self.assertEqual(outcome.returncode,1)
        self.assertEqual(json.loads(outcome.stdout)["status"],"WARN")
    def test_actual_stage_three_templates(self):
        minimal=REPO/"starter-kit"/"minimal"
        sprint_dir=REPO/"starter-kit"/"sprint-template"
        self.assertTrue(minimal.is_dir() and sprint_dir.is_dir(),"Stage 3 templates must be present in repository checkout")
        r=validator.validate(minimal,mode="template",sprint_template=sprint_dir)
        self.assertEqual(r.status,"PASS",r.findings)

if __name__=="__main__":
    unittest.main()
