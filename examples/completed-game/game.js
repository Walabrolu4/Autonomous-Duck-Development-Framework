/* Duck Dodge — ADDF Light Games Stage 5. No dependencies, telemetry or network calls. */
(function(root){
  "use strict";
  const W=720, H=420, R=17, SPEED=245, HAZARD_SPEED=185, SPAWN_EVERY=1.10;
  const clamp=(n,lo,hi)=>Math.max(lo,Math.min(hi,n));

  function createState(){
    return {phase:"ready",player:{x:98,y:H/2,r:R},hazards:[],seconds:0,spawnClock:0,passed:0};
  }
  function collision(circle,rect){
    const x=clamp(circle.x,rect.x,rect.x+rect.w);
    const y=clamp(circle.y,rect.y,rect.y+rect.h);
    return (circle.x-x)**2+(circle.y-y)**2 < circle.r**2;
  }
  function spawn(state,random=Math.random){
    const h=34+Math.floor(random()*27),w=29+Math.floor(random()*25);
    const y=12+random()*(H-h-24);
    state.hazards.push({x:W+8,y,w,h});
  }
  function step(state,keys,dt,random=Math.random){
    if(state.phase!=="running")return state;
    dt=clamp(Number.isFinite(dt)?dt:0,0,.05);
    const vx=(keys.right?1:0)-(keys.left?1:0);
    const vy=(keys.down?1:0)-(keys.up?1:0);
    const len=Math.hypot(vx,vy)||1;
    state.player.x=clamp(state.player.x+(vx/len)*SPEED*dt,R,W-R);
    state.player.y=clamp(state.player.y+(vy/len)*SPEED*dt,R,H-R);
    state.seconds+=dt;state.spawnClock+=dt;
    while(state.spawnClock>=SPAWN_EVERY){state.spawnClock-=SPAWN_EVERY;spawn(state,random);}
    for(const h of state.hazards)h.x-=HAZARD_SPEED*dt;
    state.hazards=state.hazards.filter(h=>{if(h.x+h.w<0){state.passed++;return false;}return true;});
    for(const h of state.hazards){if(collision(state.player,h)){state.phase="over";break;}}
    return state;
  }

  const api={createState,step,collision,constants:{W,H,R,SPEED,HAZARD_SPEED,SPAWN_EVERY}};
  if(typeof module!=="undefined"&&module.exports)module.exports=api;
  if(typeof document==="undefined")return;

  const canvas=document.getElementById("arena");
  const ctx=canvas.getContext("2d");
  const startBtn=document.getElementById("start"),pauseBtn=document.getElementById("pause");
  const scoreEl=document.getElementById("score"),bestEl=document.getElementById("best");
  const statusEl=document.getElementById("status"),announcer=document.getElementById("announcer");
  let state=createState(),best=0,last=0;
  const keys={left:false,right:false,up:false,down:false};
  const bindings={ArrowLeft:"left",KeyA:"left",ArrowRight:"right",KeyD:"right",ArrowUp:"up",KeyW:"up",ArrowDown:"down",KeyS:"down"};

  function changeMessage(message){announcer.textContent=message;}
  function resetKeys(){Object.keys(keys).forEach(k=>keys[k]=false);}
  function refreshHUD(){
    scoreEl.textContent=state.seconds.toFixed(1)+"s";
    bestEl.textContent=best.toFixed(1)+"s";
    statusEl.textContent={ready:"Ready",running:"Playing",paused:"Paused",over:"Game over"}[state.phase];
    startBtn.textContent=state.phase==="ready"?"Start game":"Play again";
    pauseBtn.disabled=state.phase==="ready"||state.phase==="over";
    pauseBtn.textContent=state.phase==="paused"?"Resume":"Pause";
  }
  function begin(){
    state=createState();state.phase="running";resetKeys();
    changeMessage("Playing. Dodge the red obstacles.");
    refreshHUD();
  }
  function togglePause(){
    if(state.phase==="running"){state.phase="paused";resetKeys();changeMessage("Paused.");}
    else if(state.phase==="paused"){state.phase="running";changeMessage("Playing.");}
    refreshHUD();
  }
  function draw(){
    ctx.fillStyle="#1b4d3e";ctx.fillRect(0,0,W,H);
    ctx.strokeStyle="rgba(246,241,228,.10)";ctx.lineWidth=1;
    for(let x=0;x<W;x+=45){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
    for(let y=0;y<H;y+=45){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
    ctx.fillStyle="#ef665b";
    for(const h of state.hazards){ctx.fillRect(h.x,h.y,h.w,h.h);ctx.strokeStyle="#14110d";ctx.lineWidth=3;ctx.strokeRect(h.x,h.y,h.w,h.h);}
    ctx.save();ctx.translate(state.player.x,state.player.y);
    ctx.fillStyle="#f5c518";ctx.beginPath();ctx.arc(0,0,R,0,Math.PI*2);ctx.fill();
    ctx.beginPath();ctx.arc(10,-9,8,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#14110d";ctx.beginPath();ctx.arc(12,-11,2.1,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#f6f1e4";ctx.beginPath();ctx.arc(-4,5,7,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#ef665b";ctx.beginPath();ctx.moveTo(17,-6);ctx.lineTo(27,-3);ctx.lineTo(17,1);ctx.closePath();ctx.fill();
    ctx.restore();
    if(state.phase!=="running"){
      ctx.fillStyle="rgba(20,17,13,.71)";ctx.fillRect(0,0,W,H);
      ctx.textAlign="center";ctx.fillStyle="#f6f1e4";ctx.font="700 32px system-ui";
      ctx.fillText(state.phase==="over"?"GAME OVER":state.phase==="paused"?"PAUSED":"DUCK DODGE",W/2,H/2-12);
      ctx.font="17px system-ui";ctx.fillText(state.phase==="over"?"Select Play again to retry":state.phase==="paused"?"Select Resume":"Select Start game to begin",W/2,H/2+24);
    }
  }
  function loop(now){
    const dt=last?(now-last)/1000:0;last=now;
    const old=state.phase;
    step(state,keys,dt);
    if(old==="running"&&state.phase==="over"){
      best=Math.max(best,state.seconds);
      resetKeys();
      changeMessage("Game over after "+state.seconds.toFixed(1)+" seconds. Select Play again.");
    }
    refreshHUD();draw();
    requestAnimationFrame(loop);
  }
  document.addEventListener("keydown",e=>{
    const dir=bindings[e.code];
    if(dir){e.preventDefault();keys[dir]=true;}
    if(e.code==="Space"&&state.phase!=="ready"&&state.phase!=="over"){e.preventDefault();togglePause();}
  });
  document.addEventListener("keyup",e=>{const dir=bindings[e.code];if(dir){e.preventDefault();keys[dir]=false;}});
  window.addEventListener("blur",()=>{resetKeys();if(state.phase==="running")togglePause();});
  startBtn.addEventListener("click",begin);
  pauseBtn.addEventListener("click",togglePause);
  document.querySelectorAll("[data-control]").forEach(btn=>{
    const dir=btn.getAttribute("data-control");
    btn.addEventListener("pointerdown",e=>{e.preventDefault();btn.setPointerCapture?.(e.pointerId);keys[dir]=true;});
    for(const event of ["pointerup","pointercancel","lostpointercapture"])btn.addEventListener(event,()=>keys[dir]=false);
  });
  // Read-only browser diagnostics for deterministic smoke tests; no mutation or approval hooks.
  root.DuckDodge={snapshot:()=>JSON.parse(JSON.stringify(state)),version:"stage-5-pilot-1"};
  refreshHUD();draw();requestAnimationFrame(loop);
})(typeof window!=="undefined"?window:globalThis);
