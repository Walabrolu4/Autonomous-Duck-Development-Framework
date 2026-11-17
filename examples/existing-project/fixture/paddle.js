/* Legacy Paddle: tiny pre-existing demonstration source; do not overwrite during audit. */
(function(root){
  "use strict";
  const clamp=(n,min,max)=>Math.min(max,Math.max(min,n));
  function createPaddle(){return {x:120,width:60,arenaWidth:320};}
  function move(state,direction,distance=8){
    return {...state,x:clamp(state.x+direction*distance,0,state.arenaWidth-state.width)};
  }
  const api={createPaddle,move};
  if(typeof module!=="undefined"&&module.exports)module.exports=api;
  else root.LegacyPaddle=api;
})(typeof window!=="undefined"?window:globalThis);
