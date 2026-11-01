<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pura Fibra $nome — Checklist</title>
<style>
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
  html,body{margin:0;padding:0;background:#000;}
  #root{position:relative;width:1080px;height:1920px;overflow:hidden;background:$dark;font-family:"MontF",Arial,sans-serif;font-weight:900;color:#fff;}
  .scene{position:absolute;inset:0;opacity:0;}
  #s1{opacity:1;}
  #blob{position:absolute;left:520px;top:700px;width:900px;height:900px;border-radius:50%;background:$acc;}
  #tag1{position:absolute;left:80px;top:290px;font-size:${tagfs}px;letter-spacing:4px;color:$bg2;border-bottom:10px solid $bg2;padding-bottom:6px;}
  #h1,#h2{position:absolute;left:80px;right:60px;text-align:left;line-height:.98;letter-spacing:-6px;}
  #h1{top:470px;font-size:${h1fs}px;}
  #h2{top:660px;font-size:${h2fs}px;color:$bg2;}
  #b1{position:absolute;left:560px;top:880px;width:330px;transform:rotate(-10deg);}
  #b1 img{width:330px;display:block;filter:drop-shadow(0 50px 60px rgba(0,0,0,.45));}
  #arrow{position:absolute;left:90px;top:1040px;font-size:260px;line-height:1;color:#fff;}
  /* S2: checklist */
  #s2{background:$bg;color:$dark;}
  #t2{position:absolute;left:70px;right:70px;top:190px;font-size:84px;letter-spacing:-3px;line-height:1.02;}
  #t2 span{color:$acc;}
  #b2{position:absolute;left:60px;top:560px;width:300px;}
  #b2 img{width:300px;display:block;filter:drop-shadow(0 40px 40px rgba(0,0,0,.25));}
  .it{position:absolute;left:400px;right:50px;height:200px;display:flex;align-items:center;font-size:60px;line-height:1.02;letter-spacing:-2px;}
  .bx{flex:none;width:110px;height:110px;margin-right:30px;border-radius:24px;border:9px solid $dark;box-sizing:border-box;position:relative;background:#fff;}
  .ck{position:absolute;left:4px;top:-34px;font-size:120px;line-height:1;color:$acc;}
  #i0{top:560px;} #i1{top:790px;} #i2{top:1020px;} #i3{top:1250px;}
  #sum{position:absolute;left:60px;right:60px;top:1590px;padding:32px 0;border-radius:30px;background:$dark;color:#fff;text-align:center;font-size:62px;}
  /* S3: final */
  #s3{background:$acc;}
  #b3{position:absolute;left:50%;top:180px;width:290px;margin-left:-145px;}
  #b3 img{width:290px;display:block;filter:drop-shadow(0 40px 50px rgba(0,0,0,.4));}
  #nm{position:absolute;left:0;right:0;top:1130px;text-align:center;font-size:100px;letter-spacing:-3px;line-height:1;}
  #nm small{display:block;color:$dark;font-size:78px;margin-top:8px;letter-spacing:0;}
  #fim{position:absolute;left:60px;right:60px;top:1360px;text-align:center;font-weight:700;font-size:54px;}
  #ox{position:absolute;left:150px;right:150px;top:1470px;padding:22px 0;border-radius:999px;background:$dark;color:#fff;text-align:center;font-size:50px;}
  #hd{position:absolute;left:0;right:0;top:1620px;text-align:center;font-size:62px;color:$dark;}
  #ft{position:absolute;left:0;right:0;top:1750px;text-align:center;font-weight:700;font-size:38px;}
  #flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
  <div class="scene" id="s1" data-layout-ignore>
    <div id="blob"></div>
    <div id="tag1">$tag</div>
    <div id="h1">$h1</div>
    <div id="h2">$h2</div>
    <div id="arrow">↘</div>
    <div id="b1"><img src="assets/garrafas/$slug.png" alt=""></div>
  </div>

  <div class="scene" id="s2" data-layout-ignore>
    <div id="t2">Checklist da<br><span>garrafinha certa:</span></div>
    <div id="b2"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div class="it" id="i0"><div class="bx"><div class="ck">✓</div></div>6 g de fibra</div>
    <div class="it" id="i1"><div class="bx"><div class="ck">✓</div></div>Zero açúcar</div>
    <div class="it" id="i2"><div class="bx"><div class="ck">✓</div></div>Zero caloria</div>
    <div class="it" id="i3"><div class="bx"><div class="ck">✓</div></div>Vitaminas do complexo B</div>
    <div id="sum">4 de 4. Aprovada.</div>
  </div>

  <div class="scene" id="s3" data-layout-ignore>
    <div id="b3"><img src="assets/garrafas/$slug.png" alt=""></div>
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
    // S1 (0–3.0)
    tl.fromTo("#blob", { scale: 0 }, { scale: 1, duration: .6, ease: "back.out(1.3)" }, 0);
    tl.fromTo("#tag1", { opacity: 0, x: -200 }, { opacity: 1, x: 0, duration: .35, ease: "power3.out" }, .15);
    tl.fromTo("#h1", { x: -1100 }, { x: 0, duration: .4, ease: "power4.out" }, .4);
    tl.fromTo("#h2", { x: -1100 }, { x: 0, duration: .4, ease: "power4.out" }, .7);
    tl.fromTo("#b1", { y: 1200, rotation: 30 }, { y: 0, rotation: -10, duration: .7, ease: "back.out(1.3)" }, 1.0);
    tl.fromTo("#arrow", { scale: 0 }, { scale: 1, duration: .35, ease: "back.out(2.5)" }, 1.5);
    tl.to("#arrow", { x: 30, y: 30, duration: .25, yoyo: true, repeat: 3 }, 1.9);
    tl.to("#b1", { rotation: -4, duration: .5, yoyo: true, repeat: 1, ease: "sine.inOut" }, 2.0);

    // S2 (3.0–10.4)
    cut("#s1", "#s2", 3.0);
    tl.fromTo("#t2", { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.6)" }, 3.05);
    tl.fromTo("#b2", { x: -500 }, { x: 0, duration: .5, ease: "power3.out" }, 3.3);
    ["#i0","#i1","#i2","#i3"].forEach((it, i) => {
      const t = 3.9 + i * 1.3;
      tl.fromTo(it, { x: 800, opacity: 0 }, { x: 0, opacity: 1, duration: .35, ease: "power3.out" }, t);
      tl.fromTo(it + " .ck", { scale: 0, rotation: -40 }, { scale: 1, rotation: 0, duration: .3, ease: "back.out(3)" }, t + .55);
      tl.to("#b2", { y: -18, duration: .15, yoyo: true, repeat: 1 }, t + .55);
    });
    tl.fromTo("#sum", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(2)" }, 9.3);
    tl.to("#sum", { scale: 1.06, duration: .2, yoyo: true, repeat: 1 }, 9.8);

    // S3 (10.4–15)
    cut("#s2", "#s3", 10.4);
    tl.fromTo("#b3", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .5, ease: "power3.out" }, 10.4);
    tl.fromTo("#nm", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 10.8);
    tl.fromTo("#fim", { opacity: 0 }, { opacity: 1, duration: .4 }, 11.3);
    $oxxo_js
    tl.fromTo("#hd", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, 12.4);
    tl.fromTo("#ft", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4 }, 12.7);
    tl.to("#b3", { y: -20, duration: 1, yoyo: true, repeat: 1, ease: "sine.inOut" }, 11.8);

    window.__timelines["main"] = tl;
  </script>
</div>
</body>
</html>
