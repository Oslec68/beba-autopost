<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pura Fibra $nome — VS</title>
<style>
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
  html,body{margin:0;padding:0;background:#000;}
  #root{position:relative;width:1080px;height:1920px;overflow:hidden;background:$dark;font-family:"MontF",Arial,sans-serif;font-weight:900;color:#fff;}
  .scene{position:absolute;inset:0;opacity:0;}
  #s1{opacity:1;}
  /* S1: tela dividida */
  #lhalf{position:absolute;left:0;top:0;width:540px;height:1920px;background:#3a3a3a;}
  #rhalf{position:absolute;left:540px;top:0;width:540px;height:1920px;background:$acc;}
  #tag1{position:absolute;left:0;right:0;margin:0 auto;top:290px;width:fit-content;padding:22px 54px;border-radius:999px;background:#fff;color:$dark;font-size:${tagfs}px;letter-spacing:2px;}
  #h1,#h2{position:absolute;left:40px;right:40px;text-align:center;line-height:1;letter-spacing:-5px;text-shadow:0 10px 30px rgba(0,0,0,.35);}
  #h1{top:470px;font-size:${h1fs}px;}
  #h2{top:660px;font-size:${h2fs}px;color:$bg2;}
  #can{position:absolute;left:120px;top:960px;width:300px;height:560px;border-radius:60px 60px 40px 40px;background:linear-gradient(90deg,#8a8a8a,#c9c9c9 45%,#7a7a7a);box-shadow:0 40px 60px rgba(0,0,0,.4);}
  #can:before{content:"";position:absolute;left:30px;right:30px;top:-26px;height:40px;border-radius:20px;background:#a8a8a8;}
  #can span{position:absolute;left:0;right:0;top:200px;text-align:center;color:#2b2b2b;font-size:46px;line-height:1.05;}
  #vsb{position:absolute;left:540px;top:1180px;width:220px;height:220px;margin:-110px 0 0 -110px;border-radius:50%;background:#fff;color:$dark;font-size:110px;line-height:220px;text-align:center;letter-spacing:-4px;box-shadow:0 20px 50px rgba(0,0,0,.35);}
  #b1{position:absolute;left:680px;top:880px;width:240px;}
  #b1 img{width:240px;display:block;filter:drop-shadow(0 40px 40px rgba(0,0,0,.35));}
  /* S2: tabela */
  #s2{background:$bg;color:$dark;}
  #th{position:absolute;left:60px;right:60px;top:190px;height:150px;display:flex;}
  #th div{flex:1;display:flex;align-items:center;justify-content:center;border-radius:30px;font-size:52px;text-align:center;line-height:1;}
  #th .a{background:#3a3a3a;color:#fff;margin-right:20px;}
  #th .b{background:$acc;color:#fff;}
  .row{position:absolute;left:60px;right:60px;height:250px;}
  .row .k{position:absolute;left:0;right:0;top:0;text-align:center;font-weight:700;font-size:44px;letter-spacing:4px;color:$dark;opacity:.75;}
  .row .a,.row .b{position:absolute;top:62px;width:470px;height:170px;border-radius:30px;display:flex;align-items:center;justify-content:center;font-size:88px;letter-spacing:-3px;}
  .row .a{left:0;background:#e3e3e3;color:#555;}
  .row .b{right:0;background:#fff;color:$acc;border:8px solid $acc;box-sizing:border-box;}
  #r1{top:400px;} #r2{top:690px;} #r3{top:980px;} #r4{top:1270px;}
  #s2 .b img{height:150px;}
  #verd{position:absolute;left:60px;right:60px;top:1600px;padding:34px 0;border-radius:999px;background:$dark;color:#fff;text-align:center;font-size:64px;}
  /* S3: final */
  #s3{background:$dark;}
  #b3{position:absolute;left:50%;top:170px;width:290px;margin-left:-145px;}
  #b3 img{width:290px;display:block;filter:drop-shadow(0 40px 50px rgba(0,0,0,.5));}
  #nm{position:absolute;left:0;right:0;top:1130px;text-align:center;font-size:100px;letter-spacing:-3px;line-height:1;}
  #nm small{display:block;color:$bg2;font-size:78px;margin-top:8px;letter-spacing:0;}
  #fim{position:absolute;left:60px;right:60px;top:1360px;text-align:center;font-weight:700;font-size:54px;}
  #ox{position:absolute;left:150px;right:150px;top:1470px;padding:22px 0;border-radius:999px;background:#fff;color:$dark;text-align:center;font-size:50px;}
  #hd{position:absolute;left:0;right:0;top:1620px;text-align:center;font-size:62px;color:$bg2;}
  #ft{position:absolute;left:0;right:0;top:1750px;text-align:center;font-weight:700;font-size:38px;}
  #flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
  <div class="scene" id="s1" data-layout-ignore>
    <div id="lhalf"></div><div id="rhalf"></div>
    <div id="can"><span>REFRI<br>COMUM</span></div>
    <div id="b1"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div id="vsb">VS</div>
    <div id="tag1">$tag</div>
    <div id="h1">$h1</div>
    <div id="h2">$h2</div>
  </div>

  <div class="scene" id="s2" data-layout-ignore>
    <div id="th"><div class="a">REFRI<br>COMUM</div><div class="b">PURA FIBRA<br>$nome</div></div>
    <div class="row" id="r1"><div class="k">AÇÚCAR</div><div class="a">TEM</div><div class="b">ZERO</div></div>
    <div class="row" id="r2"><div class="k">CALORIAS</div><div class="a">TEM</div><div class="b">ZERO</div></div>
    <div class="row" id="r3"><div class="k">FIBRA</div><div class="a">0 g</div><div class="b">6 g</div></div>
    <div class="row" id="r4"><div class="k">VITAMINAS DO COMPLEXO B</div><div class="a">—</div><div class="b">✓</div></div>
    <div id="verd">A troca que vale a pena.</div>
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
    // S1 (0–3.2)
    tl.fromTo("#lhalf", { x: -540 }, { x: 0, duration: .35, ease: "power4.out" }, 0);
    tl.fromTo("#rhalf", { x: 540 }, { x: 0, duration: .35, ease: "power4.out" }, 0);
    tl.fromTo("#tag1", { y: -300 }, { y: 0, duration: .45, ease: "back.out(1.8)" }, .2);
    tl.fromTo("#h1", { scale: 2.2, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, .45);
    tl.fromTo("#h2", { scale: 2.2, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, .75);
    tl.fromTo("#can", { y: 1000 }, { y: 0, duration: .6, ease: "back.out(1.3)" }, 1.0);
    tl.fromTo("#b1", { y: 1100 }, { y: 0, duration: .6, ease: "back.out(1.3)" }, 1.2);
    tl.fromTo("#vsb", { scale: 0, rotation: -90 }, { scale: 1, rotation: 0, duration: .5, ease: "back.out(2.2)" }, 1.6);
    tl.to("#vsb", { scale: 1.15, duration: .18, yoyo: true, repeat: 3 }, 2.2);
    tl.to("#can", { rotation: -6, duration: .25, yoyo: true, repeat: 3 }, 2.2);

    // S2 (3.2–10.6)
    cut("#s1", "#s2", 3.2);
    tl.fromTo("#th", { y: -250, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.6)" }, 3.25);
    ["#r1","#r2","#r3","#r4"].forEach((r, i) => {
      const t = 3.8 + i * 1.45;
      tl.fromTo(r + " .k", { opacity: 0 }, { opacity: .75, duration: .25 }, t);
      tl.fromTo(r + " .a", { x: -600 }, { x: 0, duration: .35, ease: "power3.out" }, t + .1);
      tl.fromTo(r + " .b", { x: 600 }, { x: 0, duration: .35, ease: "power3.out" }, t + .55);
      tl.to(r + " .b", { scale: 1.08, duration: .16, yoyo: true, repeat: 1 }, t + .95);
    });
    tl.fromTo("#verd", { scale: .4, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(2)" }, 9.7);

    // S3 (10.6–15)
    cut("#s2", "#s3", 10.6);
    tl.fromTo("#b3", { y: -900, rotation: -15 }, { y: 0, rotation: 0, duration: .7, ease: "bounce.out" }, 10.6);
    tl.fromTo("#nm", { y: 80, opacity: 0 }, { y: 0, opacity: 1, duration: .45, ease: "back.out(1.6)" }, 11.0);
    tl.fromTo("#fim", { opacity: 0 }, { opacity: 1, duration: .4 }, 11.5);
    $oxxo_js
    tl.fromTo("#hd", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, 12.5);
    tl.fromTo("#ft", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4 }, 12.8);
    tl.to("#b3", { y: -20, duration: 1, yoyo: true, repeat: 1, ease: "sine.inOut" }, 12.0);

    window.__timelines["main"] = tl;
  </script>
</div>
</body>
</html>
