"""ADDF Light Games Stage 6: normative, dependency-free schema (Python 3.10+).

Kept separate from runtime validation to make exact contracts reviewable.
Source: spec/PROJECT_FILE_CONTRACTS.md and spec/SPRINT_FILE_CONTRACTS.md.
"""
CORE = {
 "AGENTS.md": ("ADDF Light — Agent Operating Contract", "Edition and scope|Session startup|Lifecycle and roles|Read and write boundaries|Approval gates|Plan and scope change|Testing, review and handoff|Safe defaults and stopping rules"),
 "SECURITY.md": ("Security and Context Boundaries", "Never read or transmit|Permitted project context|Execution environment|External effects requiring separate approval|Emergency stop and recovery"),
 "GAME.md": ("Game Vision", "Project identity|Player and experience|Core loop and mechanics|Design pillars|Constraints and non-goals|Current playable hypothesis|Unknowns and provisional assumptions|References"),
 "STATE.md": ("Current Project State", "Identity and state|Gate evidence|Active authorization|Blockers and unknowns|Latest verified evidence|Next action|Session handoff"),
 "DECISIONS.md": ("Decision Log", "Decision index|Active decisions|Deferred questions|Superseded and rejected decisions"),
 "planning/BACKLOG.md": ("Project Backlog", "Current direction|Candidate slices|Research spikes|Deferred and discarded"),
}
SPRINT = {
 "SPRINT.md": "Sprint metadata|Why this sprint|Player-facing outcome|Scope|Research and evidence|Design alternatives and learning checkpoint|Selected design and decisions|Acceptance criteria|Constraints, risks and assumptions|Design approval — Gate D",
 "PLAN.md": "Sprint metadata|Inputs and assumptions|Exact file operations|Commands and external side effects|Dependencies and assets|Implementation sequence|Verification plan|Risks, rollback and stop conditions|Open ambiguities|Implementation approval — Gate I|Execution record",
 "REVIEW.md": "Sprint metadata|Build and test evidence|Acceptance criteria results|Playtest instructions|Human observations|Refinement rounds|Known limitations and deferred work|Human acceptance — Gate A|Sprint retrospective and handoff",
}
FIELDS = {
 "AGENTS.md": {"Edition and scope": "framework_edition contract_version project_name"},
 "SECURITY.md": {"Execution environment": "execution_mode network_access secret_handling"},
 "GAME.md": {"Project identity": "project_id working_title project_origin game_target", "Current playable hypothesis": "prototype_goal player_action observable_result"},
 "STATE.md": {"Identity and state": "project_id active_sprint lifecycle_stage sprint_status last_verified_at", "Gate evidence": "gate_d gate_i gate_a", "Active authorization": "plan_revision scope_reference authorized authorized_by", "Next action": "actor action"},
 "SPRINT.md": {"Sprint metadata": "sprint_id sprint_kind project_id file_revision status", "Design approval — Gate D": "gate_d_status decision_references human_response recorded_from approved_sprint_revision conditions"},
 "PLAN.md": {"Sprint metadata": "sprint_id sprint_kind project_id file_revision status", "Implementation approval — Gate I": "plan_revision linked_sprint_revision gate_i_status authorized_operations authorized_commands dependency_approvals separate_special_approvals human_response recorded_from conditions"},
 "REVIEW.md": {"Sprint metadata": "sprint_id sprint_kind project_id file_revision status", "Human acceptance — Gate A": "review_round gate_a_status human_response recorded_from conditions outstanding_release_blockers next_action"},
}
ENUMS = {
 "framework_edition": "addf-light",
 "execution_mode": "manual local-agent remote-agent unknown",
 "network_access": "disabled allowlisted human-approved-only unknown",
 "secret_handling": "never-load",
 "project_origin": "no-idea idea existing-project",
 "game_target": "web-2d web-3d desktop mobile other undecided",
 "lifecycle_stage": "research design implement refine acceptance",
 "sprint_status": "discovering designing awaiting_approval implementing refining awaiting_acceptance accepted rejected paused",
 "authorized": "yes no",
 "actor": "human agent external",
 "sprint_kind": "playable-slice research-spike maintenance",
 "status": "draft in_review approved active closed",
 "gate_d_status": "pending approved rejected not_required",
 "gate_i_status": "pending authorized rejected withdrawn stale",
 "gate_a_status": "pending accepted accepted_with_conditions needs_refinement rejected paused",
}
ID_FIELDS = {
 "D": "status tier sprint context options evidence ai_recommendation human_choice rationale implications supersedes revisit_when",
 "B": "id title outcome priority status depends_on sprint reason",
}
EXPECTED_STAGES = {
 "discovering":"research", "designing":"design", "awaiting_approval":"design",
 "implementing":"implement", "refining":"refine",
 "awaiting_acceptance":"acceptance", "accepted":"acceptance", "rejected":"acceptance",
}
ADVANCED = set("awaiting_approval implementing refining awaiting_acceptance accepted rejected".split())
REVIEW_READY = set("awaiting_acceptance accepted rejected".split())
PENDING = set(("", "pending", "unknown", "none", "not_recorded", "not_verified"))
