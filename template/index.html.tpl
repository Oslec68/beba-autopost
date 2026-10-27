<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pura Fibra $nome — Rotina</title>
<style>
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
  html,body{margin:0;padding:0;background:#000;}
  #root{position:relative;width:1080px;height:1920px;overflow:hidden;background:$bg;font-family:"MontF",Arial,sans-serif;font-weight:900;color:$dark;}
  .scene{position:absolute;inset:0;opacity:0;}
  #stripe{position:absolute;left:-400px;top:700px;width:1900px;height:520px;background:$bg2;transform:rotate(-14deg);}
  #dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.55) 3px,transparent 4px);background-size:54px 54px;opacity:.5;}
  /* S1 */
  #s1{opacity:1;}
  #clock{position:absolute;left:0;right:0;margin:0 auto;top:190px;width:fit-content;padding:26px 60px;border-radius:999px;background:$dark;color:#fff;text-align:center;font-size:${tagfs}px;letter-spacing:2px;}
  #h1,#h2{position:absolute;left:0;right:0;text-align:center;line-height:1;letter-spacing:-5px;}
  #h1{top:450px;font-size:${h1fs}px;}
  #h2{top:650px;font-size:${h2fs}px;color:$acc;}
  #peek{position:absolute;left:50%;top:960px;width:330px;margin-left:-165px;}
  #peek img{width:330px;display:block;filter:drop-shadow(0 40px 40px rgba(0,0,0,.25));}
  /* S2 */
  #s2{background:$dark;color:#fff;}
  #s2 .l{position:absolute;left:80px;right:80px;text-align:left;font-size:${lfs}px;line-height:1.02;letter-spacing:-3px;}
  #l2a{top:330px;} #l2b{top:620px;color:$bg2;}
  #b2{position:absolute;left:600px;top:880px;width:340px;}
  #b2 img{width:340px;display:block;filter:drop-shadow(0 50px 60px rgba(0,0,0,.5));}
  /* S3 */
  #b3{position:absolute;left:90px;top:420px;width:400px;}
  #b3 img{width:400px;display:block;filter:drop-shadow(0 50px 50px rgba(0,0,0,.28));}
  #halo{position:absolute;left:290px;top:1000px;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;background:radial-gradient(circle,#fff 0%,rgba(255,255,255,0) 62%);}
  .chip{position:absolute;left:540px;width:480px;text-align:center;border-radius:36px;padding:26px 0;background:#fff;color:$dark;border:7px solid $dark;font-size:58px;line-height:1.05;}
  .chip small{display:block;font-weight:700;font-size:32px;letter-spacing:1px;}
  .chip.dk{background:$dark;color:#fff;}
  #fib{top:470px;padding:30px 0;}
  #fib b{display:block;font-size:170px;line-height:.95;letter-spacing:-6px;color:$acc;}
  #zero{top:900px;} #vitB{top:1100px;} #ml{top:1330px;}
  /* S4 */
  #s4{background:$bg;}
  #b4{position:absolute;left:50%;top:150px;width:300px;margin-left:-150px;}
  #b4 img{width:300px;display:block;filter:drop-shadow(0 40px 40px rgba(0,0,0,.25));}
  #nm{position:absolute;left:0;right:0;top:1150px;text-align:center;font-size:100px;letter-spacing:-3px;line-height:1;}
  #nm small{display:block;color:$acc;font-size:78px;margin-top:8px;letter-spacing:0;}
  #fim{position:absolute;left:60px;right:60px;top:1380px;text-align:center;font-weight:700;font-size:56px;}
  #ox{position:absolute;left:150px;right:150px;top:1490px;padding:22px 0;border-radius:999px;background:$dark;color:#fff;text-align:center;font-size:50px;}
  #hd{position:absolute;left:0;right:0;top:1630px;text-align:center;font-size:62px;color:$acc;}
  #ft{position:absolute;left:0;right:0;top:1760px;text-align:center;font-weight:700;font-size:38px;}
  #flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
  <div id="stripe" data-layout-ignore></div>
  <div id="dots" data-layout-ignore></div>

  <div class="scene" id="s1" data-layout-ignore>
    <div id="clock">$tag</div>
    <div id="h1">$h1</div>
    <div id="h2">$h2</div>
    <div id="peek"><img src="assets/garrafas/$slug.png" alt=""></div>
  </div>

  <div class="scene" id="s2" data-layout-ignore>
    <div class="l" id="l2a">$l2a</div>
    <div class="l" id="l2b">$l2b</div>
    <div id="b2"><img src="assets/garrafas/$slug.png" alt=""></div>
  </div>

  <div class="scene" id="s3" data-layout-ignore>
    <div id="halo"></div>
    <div id="b3"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div class="chip" id="fib"><b><span id="n">0</span> g</b>de fibra</div>
    <div class="chip dk" id="zero">ZERO AÇÚCAR</div>
    <div class="chip" id="vitB"><small>vitaminas do</small>COMPLEXO B</div>
    <div class="chip dk" id="ml">ZERO CALORIA</div>
  </div>

  <div class="scene" id="s4" data-layout-ignore>
    <div id="b4"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div id="nm">PURA FIBRA<small>$nome</small></div>
    <div id="fim">$fim</div>
    $oxxo_html
    <div id="hd">@beba.wellness</div>
    <div id="ft">CP Comercial | WhatsApp (11) 94764-6006</div>
  </div>
  <div id="flash" data-layout-ignore></div>

  <audio id="trilha" data-start="0" data-duration="15" data-track-index="20" src="assets/music.wav"></audio>

  <script src="assets/gsap.min.js"></script>
  <script>
    window.__timelines = window.__timelines || {};
    const tl = gsap.timeline({ paused: true });
    const cut = (from, to, t) => {
      tl.to("#flash", { opacity: .85, duration: .07 }, t - .07); tl.to("#flash", { opacity: 0, duration: .28 }, t);
      tl.set(from, { opacity: 0 }, t); tl.set(to, { opacity: 1 }, t);
    };
    tl.to("#stripe", { x: 120, duration: 15, ease: "none" }, 0);

    // S1 (0–3.0)
    tl.fromTo("#clock", { y: -400, rotation: -8 }, { y: 0, rotation: 0, duration: .55, ease: "back.out(1.8)" }, .05);
    tl.fromTo("#h1", { x: -1100 }, { x: 0, duration: .4, ease: "power4.out" }, .45);
    tl.fromTo("#h2", { x: 1100 }, { x: 0, duration: .4, ease: "power4.out" }, .75);
    tl.fromTo("#peek", { y: 1100 }, { y: 0, duration: .8, ease: "back.out(1.3)" }, 1.3);
    tl.to("#clock", { scale: 1.08, duration: .2, yoyo: true, repeat: 3 }, 1.1);
    tl.to("#peek", { y: -22, rotation: 3, duration: .55, yoyo: true, repeat: 1, ease: "sine.inOut" }, 2.0);

    // S2 (3.0–6.5)
    cut("#s1", "#s2", 3.0);
    tl.fromTo("#l2a", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 3.15);
    tl.fromTo("#l2b", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 3.75);
    tl.fromTo("#b2", { x: 700, rotation: 20 }, { x: 0, rotation: 8, duration: .8, ease: "power3.out" }, 4.1);
    tl.to("#b2", { y: -30, duration: .9, yoyo: true, repeat: 1, ease: "sine.inOut" }, 4.9);

    // S3 (6.5–11.5)
    cut("#s2", "#s3", 6.5);
    tl.fromTo("#b3", { y: 1300 }, { y: 0, duration: .7, ease: "back.out(1.2)" }, 6.5);
    tl.fromTo("#halo", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .8 }, 6.5);
    tl.fromTo("#fib", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .45, ease: "back.out(2)" }, 7.0);
    const c = { v: 0 };
    tl.to(c, { v: 6, duration: .9, ease: "power2.out", onUpdate: () => { document.getElementById("n").textContent = Math.round(c.v); } }, 7.0);
    tl.fromTo("#zero", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: .4, ease: "power3.out" }, 8.1);
    tl.to("#zero", { scale: 1.08, duration: .22, yoyo: true, repeat: 1 }, 8.55);
    tl.fromTo("#vitB", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: .4, ease: "power3.out" }, 9.0);
    tl.fromTo("#ml", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: .4, ease: "power3.out" }, 9.9);
    tl.to("#b3", { y: -24, duration: 1.2, yoyo: true, repeat: 3, ease: "sine.inOut" }, 7.3);

    // S4 (11.5–15)
    cut("#s3", "#s4", 11.5);
    tl.fromTo("#b4", { scale: .5, opacity: 0 }, { scale: 1, opacity: 1, duration: .55, ease: "back.out(1.6)" }, 11.5);
    tl.fromTo("#nm", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 11.75);
    tl.fromTo("#fim", { opacity: 0 }, { opacity: 1, duration: .4 }, 12.2);
    $oxxo_js
    tl.fromTo("#hd", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, 13.0);
    tl.fromTo("#ft", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4 }, 13.3);
    tl.to("#hd", { scale: 1.06, duration: .4, yoyo: true, repeat: 1, ease: "sine.inOut" }, 13.8);

    window.__timelines["main"] = tl;
  </script>
</div>
</body>
</html>
