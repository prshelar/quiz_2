setInterval(()=>{
 let h=document.createElement("div");
 h.innerText="💖";
 h.style.position="fixed";
 h.style.left=Math.random()*100+"vw";
 h.style.top="100vh";
 document.body.appendChild(h);
 let y=100;
 let t=setInterval(()=>{
  y-=2; h.style.top=y+"vh";
  if(y<-5){clearInterval(t);h.remove();}
 },30);
},700);