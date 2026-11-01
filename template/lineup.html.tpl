<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pura Fibra $nome — Sabores</title>
<style>
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
  html,body{margin:0;padding:0;background:#000;}
  #root{position:relative;width:1080px;height:1920px;overflow:hidden;background:#fffaf3;font-family:"MontF",Arial,sans-serif;font-weight:900;color:$dark;}
  .scene{position:absolute;inset:0;opacity:0;}
  #s1{opacity:1;}
  .st{position:absolute;top:0;width:270px;height:1920px;}
  #st0{left:0;background:#c9e58c;} #st1{left:270px;background:#ffbf80;} #st2{left:540px;background:#f5a39a;} #st3{left:810px;background:#f8bf9c;}
  #card{position:absolute;left:70px;right:70px;top:280px;height:620px;border-radius:50px;background:#fff;box-shadow:0 30px 60px rgba(0,0,0,.18);}
  #tag1{position:absolute;left:0;right:0;margin:0 auto;top:330px;width:fit-content;padding:18px 50px;border-radius:999px;background:$acc;color:#fff;font-size:${tagfs}px;letter-spacing:2px;}
  #h1,#h2{position:absolute;left:90px;right:90px;text-align:center;line-height:1;letter-spacing:-5px;}
  #h1{top:520px;font-size:${h1fs}px;}
  #h2{top:700px;font-size:${h2fs}px;color:$acc;}
  .bt{position:absolute;top:1000px;width:210px;}
  .bt img{width:210px;display:block;filter:drop-shadow(0 30px 30px rgba(0,0,0,.25));}
  #p0{left:30px;} #p1{left:300px;} #p2{left:570px;} #p3{left:840px;}
  /* S2: line-up */
  #s2{background:#fffaf3;}
  #t2{position:absolute;left:0;right:0;top:220px;text-align:center;font-size:120px;letter-spacing:-4px;line-height:1;}
  #t2 small{display:block;font-size:60px;color:$acc;letter-spacing:0;margin-top:14px;}
  .lb{position:absolute;top:620px;width:240px;text-align:center;}
  .lb img{width:190px;display:block;margin:0 auto;filter:drop-shadow(0 30px 30px rgba(0,0,0,.25));}
  .lb span{display:block;margin-top:24px;font-size:38px;letter-spacing:-1px;}
  #q0{left:15px;} #q1{left:285px;} #q2{left:555px;} #q3{left:825px;}
  #q0 span{color:#5f9e12;} #q1 span{color:#e8660c;} #q2 span{color:#c2271d;} #q3 span{color:#e0773f;}
  #pick{position:absolute;left:120px;right:120px;top:1460px;padding:30px 0;border-radius:999px;background:$dark;color:#fff;text-align:center;font-size:64px;}
  /* S3: destaque */
  #s3{background:$bg;}
  #ring{position:absolute;left:540px;top:820px;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;border:40px solid $bg2;box-sizing:border-box;}
  #b3{position:absolute;left:50%;top:260px;width:340px;margin-left:-170px;}
  #b3 img{width:340px;display:block;filter:drop-shadow(0 50px 60px rgba(0,0,0,.3));}
  #nm{position:absolute;left:0;right:0;top:1380px;text-align:center;font-size:96px;letter-spacing:-3px;line-height:1;}
  #nm small{display:block;color:$acc;font-size:120px;margin-top:6px;letter-spacing:-3px;}
  #inf{position:absolute;left:0;right:0;top:1660px;text-align:center;font-weight:700;font-size:48px;}
  /* S4: final */
  #s4{background:$dark;color:#fff;}
  #fim{position:absolute;left:70px;right:70px;top:420px;text-align:center;font-size:96px;line-height:1.05;letter-spacing:-3px;}
  .mini{position:absolute;top:900px;width:150px;}
  .mini img{width:150px;display:block;}
  #m0{left:150px;} #m1{left:345px;} #m2{left:540px;} #m3{left:735px;}
  #ox{position:absolute;left:150px;right:150px;top:1440px;padding:22px 0;border-radius:999px;background:$acc;color:#fff;text-align:center;font-size:50px;}
  #hd{position:absolute;left:0;right:0;top:1590px;text-align:center;font-size:62px;color:$bg2;}
  #ft{position:absolute;left:0;right:0;top:1720px;text-align:center;font-weight:700;font-size:38px;}
  #flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
  <div class="scene" id="s1" data-layout-ignore>
    <div class="st" id="st0"></div><div class="st" id="st1"></div><div class="st" id="st2"></div><div class="st" id="st3"></div>
    <div id="card"></div>
    <div id="tag1">$tag</div>
    <div id="h1">$h1</div>
    <div id="h2">$h2</div>
    <div class="bt" id="p0"><img src="assets/garrafas/limao.png" alt=""></div>
    <div class="bt" id="p1"><img src="assets/garrafas/tangerina.png" alt=""></div>
    <div class="bt" id="p2"><img src="assets/garrafas/morango.png" alt=""></div>
    <div class="bt" id="p3"><img src="assets/garrafas/pessego.png" alt=""></div>
  </div>

  <div class="scene" id="s2" data-layout-ignore>
    <div id="t2">4 SABORES<small>qual é o seu?</small></div>
    <div class="lb" id="q0"><img src="assets/garrafas/limao.png" alt=""><span>LIMÃO</span></div>
    <div class="lb" id="q1"><img src="assets/garrafas/tangerina.png" alt=""><span>TANGERINA</span></div>
    <div class="lb" id="q2"><img src="assets/garrafas/morango.png" alt=""><span>MORANGO</span></div>
    <div class="lb" id="q3"><img src="assets/garrafas/pessego.png" alt=""><span>PÊSSEGO</span></div>
    <div id="pick">Hoje é dia de...</div>
  </div>

  <div class="scene" id="s3" data-layout-ignore>
    <div id="ring"></div>
    <div id="b3"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div id="nm">PURA FIBRA<small>$nome</small></div>
    <div id="inf">6 g de fibra · zero açúcar · zero caloria</div>
  </div>

  <div class="scene" id="s4" data-layout-ignore>
    <div id="fim">$fim</div>
    <div class="mini" id="m0"><img src="assets/garrafas/limao.png" alt=""></div>
    <div class="mini" id="m1"><img src="assets/garrafas/tangerina.png" alt=""></div>
    <div class="mini" id="m2"><img src="assets/garrafas/morango.png" alt=""></div>
    <div class="mini" id="m3"><img src="assets/garrafas/pessego.png" alt=""></div>
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
    ["#st0","#st1","#st2","#st3"].forEach((s, i) => tl.fromTo(s, { y: i % 2 ? 1920 : -1920 }, { y: 0, duration: .45, ease: "power4.out" }, i * .07));
    tl.fromTo("#card", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(1.6)" }, .35);
    tl.fromTo("#tag1", { y: -200, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.8)" }, .55);
    tl.fromTo("#h1", { opacity: 0, scale: .7 }, { opacity: 1, scale: 1, duration: .35, ease: "back.out(1.8)" }, .75);
    tl.fromTo("#h2", { opacity: 0, scale: .7 }, { opacity: 1, scale: 1, duration: .35, ease: "back.out(1.8)" }, 1.0);
    ["#p0","#p1","#p2","#p3"].forEach((p, i) => tl.fromTo(p, { y: 1000 }, { y: 0, duration: .55, ease: "back.out(1.4)" }, 1.2 + i * .12));
    ["#p0","#p1","#p2","#p3"].forEach((p, i) => tl.to(p, { y: -30, duration: .3, yoyo: true, repeat: 1, ease: "sine.inOut" }, 2.1 + i * .12));

    // S2 (3.0–7.8)
    cut("#s1", "#s2", 3.0);
    tl.fromTo("#t2", { scale: 1.8, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "power4.out" }, 3.05);
    ["#q0","#q1","#q2","#q3"].forEach((q, i) => tl.fromTo(q, { y: -1100 }, { y: 0, duration: .6, ease: "bounce.out" }, 3.5 + i * .25));
    ["#q0","#q1","#q2","#q3"].forEach((q, i) => tl.to(q, { scale: 1.12, duration: .15, yoyo: true, repeat: 1 }, 5.3 + i * .3));
    tl.fromTo("#pick", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.6)" }, 6.6);
    tl.to("$outros", { opacity: .2, scale: .85, duration: .3 }, 7.2);
    tl.to("#q$idx", { scale: 1.2, duration: .3, ease: "back.out(2)" }, 7.2);

    // S3 (7.8–11.4)
    cut("#s2", "#s3", 7.8);
    tl.fromTo("#ring", { scale: .2, opacity: 0 }, { scale: 1, opacity: 1, duration: .6, ease: "back.out(1.4)" }, 7.8);
    tl.fromTo("#b3", { scale: .3, rotation: -25 }, { scale: 1, rotation: 0, duration: .6, ease: "back.out(1.6)" }, 7.85);
    tl.fromTo("#nm", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 8.3);
    tl.fromTo("#inf", { opacity: 0 }, { opacity: 1, duration: .4 }, 8.9);
    tl.to("#ring", { rotation: 90, scale: 1.05, duration: 3, ease: "sine.inOut" }, 8.4);
    tl.to("#b3", { y: -26, duration: 1, yoyo: true, repeat: 1, ease: "sine.inOut" }, 9.0);

    // S4 (11.4–15)
    cut("#s3", "#s4", 11.4);
    tl.fromTo("#fim", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 11.45);
    ["#m0","#m1","#m2","#m3"].forEach((m, i) => tl.fromTo(m, { y: 700, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 11.8 + i * .1));
    $oxxo_js
    tl.fromTo("#hd", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, 12.8);
    tl.fromTo("#ft", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4 }, 13.1);

    window.__timelines["main"] = tl;
  </script>
</div>
</body>
</html>
