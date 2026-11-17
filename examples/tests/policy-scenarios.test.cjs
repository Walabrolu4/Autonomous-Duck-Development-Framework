/* Stage 5 synthetic policy cases. Test data never constitutes real user approval. */
"use strict";
const test=require("node:test");
const assert=require("node:assert/strict");
const {gateIValid,canWrite,canCloseAccepted,canResumeImplementation}=require("./policy-model.cjs");
function scenario(){
 const plan={sprintId:"sprint-001",revision:"r1",riskTier:"low",operations:["create:game.js","create:index.html"],commands:["node --test"],dependencies:[],unknownRisk:false,unapprovedSpecialEffect:false};
 const humanApproval={actor:"human",kind:"Gate-I",evidence:"SYNTHETIC_FIXTURE_ONLY",sprintId:plan.sprintId,planRevision:plan.revision,riskTier:plan.riskTier,operations:[...plan.operations],commands:[...plan.commands],dependencies:[]};
 return {gateD:"approved",plan,humanApproval,status:"implementing",planMatchesWorktree:true};
}
test("positive control: exact synthetic Gate I matches one plan",()=>assert.equal(gateIValid(scenario()),true));
test("no Gate D blocks implementation",()=>{const s=scenario();s.gateD="pending";assert.equal(gateIValid(s),false);});
test("no human evidence blocks implementation",()=>{const s=scenario();s.humanApproval.evidence="";assert.equal(gateIValid(s),false);});
test("agent cannot impersonate human",()=>{const s=scenario();s.humanApproval.actor="agent";assert.equal(gateIValid(s),false);});
test("stale plan revision blocks implementation",()=>{const s=scenario();s.plan.revision="r2";assert.equal(gateIValid(s),false);});
test("extra file operation blocks implementation",()=>{const s=scenario();s.plan.operations.push("create:assets/duck.png");assert.equal(gateIValid(s),false);});
test("unapproved install command blocks implementation",()=>{const s=scenario();s.plan.commands.push("npm install");assert.equal(gateIValid(s),false);});
test("new dependency blocks implementation",()=>{const s=scenario();s.plan.dependencies.push("phaser");assert.equal(gateIValid(s),false);});
test("changed risk tier blocks implementation",()=>{const s=scenario();s.plan.riskTier="high";assert.equal(gateIValid(s),false);});
test("special deployment effect blocks implementation",()=>{const s=scenario();s.plan.unapprovedSpecialEffect=true;assert.equal(gateIValid(s),false);});
test("approved plan only allows its exact operation",()=>{const s=scenario();assert.equal(canWrite(s,"create:index.html"),true);assert.equal(canWrite(s,"delete:README.md"),false);});
test("build success alone cannot close acceptance",()=>{const s={criteriaComplete:true,releaseBlockers:0};assert.equal(canCloseAccepted(s),false);});
test("human verdict with incomplete criteria cannot close",()=>{const s={criteriaComplete:false,releaseBlockers:0,review:{actor:"human",kind:"Gate-A",verdict:"accepted",evidence:"SYNTHETIC"}};assert.equal(canCloseAccepted(s),false);});
test("human rejection does not count as accepted",()=>{const s={criteriaComplete:true,releaseBlockers:0,review:{actor:"human",kind:"Gate-A",verdict:"rejected",evidence:"SYNTHETIC"}};assert.equal(canCloseAccepted(s),false);});
test("clean synthetic acceptance control",()=>{const s={criteriaComplete:true,releaseBlockers:0,review:{actor:"human",kind:"Gate-A",verdict:"accepted",evidence:"SYNTHETIC"}};assert.equal(canCloseAccepted(s),true);});
test("resumption without matched source state fails closed",()=>{const s=scenario();s.planMatchesWorktree=false;assert.equal(canResumeImplementation(s),false);});
test("resumption with missing approval fails closed",()=>{const s=scenario();s.humanApproval=null;assert.equal(canResumeImplementation(s),false);});
test("resumption exact scope positive control",()=>assert.equal(canResumeImplementation(scenario()),true));
