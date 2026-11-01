<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pura Fibra $nome — Quiz</title>
<style>
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
  @font-face{font-family:"MontF";src:url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
  html,body{margin:0;padding:0;background:#000;}
  #root{position:relative;width:1080px;height:1920px;overflow:hidden;background:$acc;font-family:"MontF",Arial,sans-serif;font-weight:900;color:#fff;}
  .scene{position:absolute;inset:0;opacity:0;}
  #s1{opacity:1;}
  #qbig{position:absolute;right:-120px;top:120px;font-size:1500px;line-height:1;color:rgba(255,255,255,.14);}
  #tag1{position:absolute;left:80px;top:300px;padding:20px 48px;border-radius:24px;background:$dark;color:#fff;font-size:${tagfs}px;letter-spacing:2px;transform:rotate(-4deg);}
  #h1,#h2{position:absolute;left:80px;right:60px;text-align:left;line-height:1;letter-spacing:-5px;}
  #h1{top:500px;font-size:${h1fs}px;}
  #h2{top:690px;font-size:${h2fs}px;color:$dark;}
  #b1{position:absolute;left:620px;top:930px;width:300px;transform:rotate(12deg);}
  #b1 img{width:300px;display:block;filter:drop-shadow(0 40px 50px rgba(0,0,0,.35));}
  #sab{position:absolute;left:80px;top:1100px;width:460px;padding:30px 36px;border-radius:36px;background:#fff;color:$dark;font-size:64px;line-height:1.05;}
  #sab small{display:block;font-weight:700;font-size:34px;color:$acc;letter-spacing:2px;margin-bottom:8px;}
  /* S2: pergunta */
  #s2{background:$bg;color:$dark;}
  #qt{position:absolute;left:0;right:0;margin:0 auto;top:200px;width:fit-content;padding:20px 50px;border-radius:999px;background:$dark;color:#fff;font-size:54px;letter-spacing:3px;}
  #perg{position:absolute;left:70px;right:70px;top:360px;text-align:center;font-size:${pfs}px;line-height:1.08;letter-spacing:-2px;}
  .op{position:absolute;left:110px;right:110px;height:180px;border-radius:40px;background:#fff;border:8px solid $dark;box-sizing:border-box;display:flex;align-items:center;font-size:72px;letter-spacing:-2px;}
  .op b{display:inline-block;width:120px;height:120px;margin:0 40px 0 22px;border-radius:50%;background:$dark;color:#fff;text-align:center;line-height:120px;font-size:64px;}
  #o0{top:860px;} #o1{top:1080px;} #o2{top:1300px;}
  .op.ok{background:$acc;color:#fff;border-color:$acc;}
  #bar{position:absolute;left:110px;right:110px;top:1560px;height:30px;border-radius:15px;background:rgba(0,0,0,.12);overflow:hidden;}
  #barf{width:100%;height:100%;background:$dark;transform-origin:left center;}
  #cert{position:absolute;left:0;right:0;top:1650px;text-align:center;font-size:76px;color:$acc;}
  /* S3: final */
  #s3{background:$dark;}
  #b3{position:absolute;left:90px;top:300px;width:330px;}
  #b3 img{width:330px;display:block;filter:drop-shadow(0 40px 50px rgba(0,0,0,.5));}
  #nm{position:absolute;left:480px;right:40px;top:470px;font-size:96px;letter-spacing:-3px;line-height:1;}
  #nm small{display:block;color:$bg2;font-size:74px;margin-top:10px;letter-spacing:0;}
  #lst{position:absolute;left:480px;right:40px;top:760px;font-weight:700;font-size:46px;line-height:1.55;}
  #fim{position:absolute;left:60px;right:60px;top:1390px;text-align:center;font-weight:700;font-size:54px;}
  #ox{position:absolute;left:150px;right:150px;top:1490px;padding:22px 0;border-radius:999px;background:$acc;color:#fff;text-align:center;font-size:50px;}
  #hd{position:absolute;left:0;right:0;top:1630px;text-align:center;font-size:62px;color:$bg2;}
  #ft{position:absolute;left:0;right:0;top:1760px;text-align:center;font-weight:700;font-size:38px;}
  #flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1080" data-height="1920">
  <div class="scene" id="s1" data-layout-ignore>
    <div id="qbig">?</div>
    <div id="tag1">$tag</div>
    <div id="h1">$h1</div>
    <div id="h2">$h2</div>
    <div id="sab"><small>QUIZ RÁPIDO</small>Acerta essa?</div>
    <div id="b1"><img src="assets/garrafas/$slug.png" alt=""></div>
  </div>

  <div class="scene" id="s2" data-layout-ignore>
    <div id="qt">VOCÊ SABIA?</div>
    <div id="perg">$perg</div>
    <div class="op" id="o0"><b>A</b>$op0</div>
    <div class="op" id="o1"><b>B</b>$op1</div>
    <div class="op" id="o2"><b>C</b>$op2</div>
    <div id="bar"><div id="barf"></div></div>
    <div id="cert">Acertou?</div>
  </div>

  <div class="scene" id="s3" data-layout-ignore>
    <div id="b3"><img src="assets/garrafas/$slug.png" alt=""></div>
    <div id="nm">PURA FIBRA<small>$nome</small></div>
    <div id="lst">✓ 6 g de fibra<br>✓ zero açúcar<br>✓ zero caloria<br>✓ complexo B</div>
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
    tl.fromTo("#qbig", { rotation: -30, opacity: 0 }, { rotation: 0, opacity: 1, duration: .6, ease: "back.out(1.5)" }, 0);
    tl.fromTo("#tag1", { x: -700 }, { x: 0, duration: .4, ease: "power4.out" }, .15);
    tl.fromTo("#h1", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.6)" }, .45);
    tl.fromTo("#h2", { y: 120, opacity: 0 }, { y: 0, opacity: 1, duration: .4, ease: "back.out(1.6)" }, .75);
    tl.fromTo("#b1", { x: 700, rotation: 40 }, { x: 0, rotation: 12, duration: .7, ease: "back.out(1.4)" }, 1.1);
    tl.fromTo("#sab", { scale: 0 }, { scale: 1, duration: .45, ease: "back.out(2)" }, 1.5);
    tl.to("#b1", { rotation: 4, duration: .5, yoyo: true, repeat: 2, ease: "sine.inOut" }, 2.0);

    // S2 (3.2–10.2)
    cut("#s1", "#s2", 3.2);
    tl.fromTo("#qt", { y: -200 }, { y: 0, duration: .4, ease: "back.out(1.8)" }, 3.25);
    tl.fromTo("#perg", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: .45 }, 3.5);
    ["#o0","#o1","#o2"].forEach((o, i) => tl.fromTo(o, { x: i % 2 ? 900 : -900 }, { x: 0, duration: .4, ease: "power3.out" }, 4.1 + i * .3));
    tl.fromTo("#barf", { scaleX: 1 }, { scaleX: 0, duration: 3.0, ease: "none" }, 5.2);
    tl.to("#o$certo", { backgroundColor: "$acc", borderColor: "$acc", color: "#fff", duration: .15 }, 8.2);
    tl.fromTo("#o$certo", { scale: 1 }, { scale: 1.08, duration: .2, yoyo: true, repeat: 3 }, 8.2);
    tl.to("$errados", { opacity: .25, duration: .3 }, 8.2);
    tl.fromTo("#cert", { scale: .3, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(2)" }, 8.6);

    // S3 (10.2–15)
    cut("#s2", "#s3", 10.2);
    tl.fromTo("#b3", { x: -600, rotation: -20 }, { x: 0, rotation: -4, duration: .6, ease: "back.out(1.4)" }, 10.2);
    tl.fromTo("#nm", { x: 600, opacity: 0 }, { x: 0, opacity: 1, duration: .45, ease: "power3.out" }, 10.5);
    tl.fromTo("#lst", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: .5 }, 10.9);
    tl.fromTo("#fim", { opacity: 0 }, { opacity: 1, duration: .4 }, 11.6);
    $oxxo_js
    tl.fromTo("#hd", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: .35, ease: "power4.out" }, 12.6);
    tl.fromTo("#ft", { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .4 }, 12.9);

    window.__timelines["main"] = tl;
  </script>
</div>
</body>
</html>
