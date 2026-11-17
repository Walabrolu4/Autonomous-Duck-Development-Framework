/* Executable, dependency-free tests for the actual Duck Dodge game logic. */
"use strict";
const assert=require("node:assert/strict");
const test=require("node:test");
const game=require("../game.js");
const {W,H,R,SPEED,SPAWN_EVERY}=game.constants;

test("ready state is non-playing and has no hazards",()=>{
  const s=game.createState();
  assert.equal(s.phase,"ready");assert.equal(s.seconds,0);assert.equal(s.hazards.length,0);
});
test("step is inert until a game is running",()=>{
  const s=game.createState();game.step(s,{right:true},.05,()=>.5);
  assert.equal(s.player.x,98);assert.equal(s.seconds,0);
});
test("keyboard movement changes position and clamps to arena",()=>{
  const s=game.createState();s.phase="running";
  for(let i=0;i<250;i++)game.step(s,{right:true,down:true},.05,()=>.5);
  assert.ok(s.player.x>=R&&s.player.x<=W-R);
  assert.ok(s.player.y>=R&&s.player.y<=H-R);
  const beforeX=s.player.x;game.step(s,{left:true},.05,()=>.5);
  assert.ok(s.player.x<beforeX);
});
test("diagonal speed is normalized",()=>{
  const a=game.createState();a.phase="running";
  const b=game.createState();b.phase="running";
  game.step(a,{right:true},.05,()=>.5);
  game.step(b,{right:true,up:true},.05,()=>.5);
  assert.ok(Math.abs((a.player.x-98)-SPEED*.05)<1e-9);
  const diag=Math.hypot(b.player.x-98,b.player.y-H/2);
  assert.ok(Math.abs(diag-SPEED*.05)<1e-9);
});
test("hazards spawn after the documented interval",()=>{
  const s=game.createState();s.phase="running";
  for(let i=0;i<23;i++)game.step(s,{},.05,()=>.5);
  assert.ok(s.hazards.length>=1);
  assert.ok(s.seconds>=SPAWN_EVERY);
});
test("non-finite delta cannot corrupt the state",()=>{
  const s=game.createState();s.phase="running";
  game.step(s,{},NaN,()=>.5);
  assert.equal(s.seconds,0);assert.equal(s.player.x,98);
});
test("hazard overlaps trigger game over",()=>{
  const s=game.createState();s.phase="running";
  s.hazards=[{x:s.player.x-12,y:s.player.y-12,w:24,h:24}];
  game.step(s,{},.01,()=>.5);
  assert.equal(s.phase,"over");
});
test("non-overlapping rectangle does not collide",()=>{
  assert.equal(game.collision({x:10,y:10,r:5},{x:100,y:100,w:10,h:10}),false);
});
test("over state freezes simulation; a fresh createState resets",()=>{
  const s=game.createState();s.phase="over";s.seconds=10;
  game.step(s,{right:true},.04);
  assert.equal(s.seconds,10);
  const next=game.createState();assert.equal(next.phase,"ready");assert.equal(next.seconds,0);
});
test("paused state does not advance or spawn",()=>{
  const s=game.createState();s.phase="paused";
  game.step(s,{right:true},.05,()=>.5);assert.equal(s.seconds,0);assert.equal(s.hazards.length,0);
});
