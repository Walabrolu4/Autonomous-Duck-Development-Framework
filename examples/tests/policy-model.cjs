/* Stage 5 EXERCISE ONLY. This deterministic reference model is not wired into any AI host.
   It tests what "should be allowed" under the spec; it cannot prove LLM compliance
   or authenticate whether a human really consented. */
"use strict";
function sameList(a,b){
  return Array.isArray(a)&&Array.isArray(b)&&a.length===b.length&&
    [...a].sort().every((x,i)=>x===[...b].sort()[i]);
}
function gateIValid(s){
  if(!s||!s.plan||!s.humanApproval)return false;
  const {plan,humanApproval:g}=s;
  return (
    (s.gateD==="approved"||s.gateD==="not_required") &&
    g.actor==="human" && g.kind==="Gate-I" && Boolean(g.evidence) &&
    g.sprintId===plan.sprintId && g.planRevision===plan.revision &&
    g.riskTier===plan.riskTier &&
    sameList(g.operations,plan.operations)&&sameList(g.commands,plan.commands)&&
    sameList(g.dependencies,plan.dependencies)&&
    !plan.unknownRisk && !plan.unapprovedSpecialEffect
  );
}
function canWrite(s,operation){
  return gateIValid(s)&&s.plan.operations.includes(operation);
}
function canCloseAccepted(s){
  return Boolean(
    s&&s.review&&s.review.actor==="human"&&s.review.kind==="Gate-A"&&
    s.review.verdict==="accepted"&&s.review.evidence&&
    s.criteriaComplete===true&&s.releaseBlockers===0
  );
}
function canResumeImplementation(s){
  return s?.status==="implementing"&&gateIValid(s)&&s.planMatchesWorktree===true;
}
module.exports={gateIValid,canWrite,canCloseAccepted,canResumeImplementation};
