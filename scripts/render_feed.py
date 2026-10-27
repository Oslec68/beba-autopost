"""Escolhe o próximo item de content/feed.json (carrossel ou imagem) e gera os JPEGs 1080x1350.
Saída: out/feed/<id>/01.jpg, 02.jpg... e out/feed_next.json (id, tipo, arquivos, legenda).
Uso: python scripts/render_feed.py [--id fc001_pessego] [--todos]   (--todos renderiza o banco inteiro, para revisão)
"""
import html, json, os, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "template", "assets")
W, H = 1080, 1350
CORES = {
    "limao":     dict(nome="LIMÃO",     bg="#eef7d2", bg2="#c9e58c", dark="#26400c", acc="#5f9e12"),
    "tangerina": dict(nome="TANGERINA", bg="#ffe6cc", bg2="#ffbf80", dark="#5c2404", acc="#e8660c"),
    "morango":   dict(nome="MORANGO",   bg="#fde0dc", bg2="#f5a39a", dark="#4a1410", acc="#c2271d"),
    "pessego":   dict(nome="PÊSSEGO",   bg="#ffe9dc", bg2="#f8bf9c", dark="#5a2a14", acc="#e0773f"),
}
RODAPE = "CP Comercial | WhatsApp (11) 94764-6006"

CSS = """
@font-face{font-family:"MontF";src:url(fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
@font-face{font-family:"MontF";src:url(fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
html,body{margin:0;padding:0;}
#root{position:relative;width:1080px;height:1350px;overflow:hidden;background:__BG__;font-family:"MontF",Arial,sans-serif;font-weight:900;color:__DARK__;}
#root.dk{background:__DARK__;color:#fff;}
#stripe{position:absolute;left:-400px;top:560px;width:1900px;height:420px;background:__BG2__;transform:rotate(-14deg);}
#root.dk #stripe{background:rgba(255,255,255,.06);}
#dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.55) 3px,transparent 4px);background-size:54px 54px;opacity:.5;}
#root.dk #dots{opacity:.08;}
.handle{position:absolute;left:70px;top:60px;font-weight:700;font-size:34px;letter-spacing:1px;opacity:.75;}
.count{position:absolute;right:70px;top:56px;font-size:34px;padding:8px 22px;border-radius:999px;background:__DARK__;color:#fff;}
#root.dk .count{background:#fff;color:__DARK__;}
.bottle{position:absolute;filter:drop-shadow(0 40px 40px rgba(0,0,0,.28));}
.bottle img{display:block;width:100%;}
.pill{display:inline-block;padding:20px 48px;border-radius:999px;background:__DARK__;color:#fff;}
.foot{position:absolute;left:0;right:0;bottom:56px;text-align:center;}
.foot span{display:inline-block;padding:18px 40px;border-radius:999px;background:__DARK__;color:#fff;font-weight:700;font-size:34px;}
#root.dk .foot span{background:#fff;color:__DARK__;}
.c{position:absolute;left:0;right:0;text-align:center;line-height:1;}
"""

def fit(text, maxpx, width, k):
    return int(min(maxpx, width / (k * max(len(text), 1))))

def esc(s):
    return html.escape(str(s))

MAXB = [10**6]  # limite inferior da garrafa (posts de imagem: acima do rodapé)

def bottle(s, left, top, h):
    if top + h > MAXB[0]:
        nh = MAXB[0] - top
        left += int((h - nh) * 372 / 1200 / 2); h = nh
    w = int(h * 372 / 1200)
    return f'<div class="bottle" style="left:{left}px;top:{top}px;width:{w}px"><img src="garrafas/{s}.png"></div>'

def slide_html(sl, idx, total, single):
    s = sl["sabor"]; c = CORES[s]; t = sl["t"]
    dark = t in ("lista", "cta")
    MAXB[0] = 1195 if single else 10**6
    body = []
    if t == "capa":
        body.append(f'<div class="c" style="top:200px;font-size:{fit(sl["kicker"],56,800,.72)}px"><span class="pill">{esc(sl["kicker"])}</span></div>')
        body.append(f'<div class="c" style="top:360px;font-size:{fit(sl["h1"],190,980,.80)}px;letter-spacing:-5px">{esc(sl["h1"])}</div>')
        body.append(f'<div class="c" style="top:560px;font-size:{fit(sl["h2"],190,980,.80)}px;letter-spacing:-5px;color:{c["acc"]}">{esc(sl["h2"])}</div>')
        body.append(bottle(s, 540 - 95, 790, 610))
        if not single and not sl.get("sem_seta"):
            body.append(f'<div style="position:absolute;right:70px;bottom:90px;font-size:40px"><span class="pill" style="background:{c["acc"]}">ARRASTA →</span></div>')
    elif t == "produto":
        body.append(bottle(s, 110, 250, 1000))
        tfs = 116 if len(sl["titulo"]) <= 9 else 80
        body.append(f'<div style="position:absolute;left:500px;top:250px;font-weight:700;font-size:36px;color:{c["acc"]};letter-spacing:2px">PURA FIBRA {esc(c["nome"])}</div>')
        body.append(f'<div style="position:absolute;left:500px;right:50px;top:305px;font-size:{tfs}px;line-height:1;letter-spacing:-3px">{esc(sl["titulo"])}</div>')
        for k, ch in enumerate(sl["chips"]):
            fs = 50 if len(ch) <= 14 else 42
            body.append(f'<div style="position:absolute;left:500px;width:500px;top:{560 + k * 190}px;box-sizing:border-box;padding:34px 30px;border-radius:32px;background:{"#fff" if k % 2 == 0 else c["dark"]};color:{c["dark"] if k % 2 == 0 else "#fff"};border:7px solid {c["dark"]};font-size:{fs}px;text-align:center">{esc(ch)}</div>')
    elif t == "lista":
        n = sl["num"]
        body.append(f'<div style="position:absolute;left:80px;top:220px;width:260px;height:260px;border-radius:50%;background:{c["acc"]};color:#fff;text-align:center;line-height:260px;font-size:{fit(n,140,230,.78)}px">{esc(n)}</div>')
        body.append(f'<div style="position:absolute;left:80px;right:80px;top:560px;font-size:{fit(sl["titulo"],120,1500,.62)}px;line-height:1.02;letter-spacing:-3px">{esc(sl["titulo"])}</div>')
        body.append(f'<div style="position:absolute;left:80px;right:400px;top:900px;font-weight:700;font-size:52px;line-height:1.2;color:{c["bg2"]}">{esc(sl["texto"])}</div>')
        body.append(bottle(s, 760, 760, 760))
    elif t == "numero":
        big = sl["big"]
        body.append(f'<div class="c" style="top:200px;font-size:{fit(big,420,900,.72)}px;letter-spacing:-12px;color:{c["acc"]}">{esc(big)}</div>')
        body.append(f'<div class="c" style="top:640px;font-size:{fit(sl["label"],110,940,.76)}px;letter-spacing:-2px">{esc(sl["label"])}</div>')
        body.append(f'<div style="position:absolute;left:80px;right:420px;top:860px;font-weight:700;font-size:52px;line-height:1.2">{esc(sl["texto"])}</div>')
        body.append(bottle(s, 740, 780, 720))
    elif t == "vs":
        body.append(f'<div class="c" style="top:190px;font-size:{fit(sl["titulo"],96,960,.66)}px;letter-spacing:-2px">{esc(sl["titulo"])}</div>')
        for col, items in (("esq", sl["esq"]), ("dir", sl["dir"])):
            x = 70 if col == "esq" else 560
            bgc, fg = ("#ffffff", "#8a8a8a") if col == "esq" else (c["dark"], "#fff")
            rows = "".join(f'<div style="padding:22px 0;border-top:3px solid {"#ddd" if col=="esq" else "rgba(255,255,255,.2)"};font-weight:700;font-size:42px;line-height:1.15">{"✕ " if col=="esq" else "✓ "}{esc(it)}</div>' for it in items[1:])
            body.append(f'<div style="position:absolute;left:{x}px;top:380px;width:450px;box-sizing:border-box;padding:40px 34px;border-radius:40px;background:{bgc};color:{fg}"><div style="font-size:{fit(items[0],62,380,.68)}px;margin-bottom:24px;{"color:"+c["bg2"] if col=="dir" else ""}">{esc(items[0])}</div>{rows}</div>')
        body.append(bottle(s, 470, 860, 520))
    elif t == "lineup":
        body.append(f'<div class="c" style="top:180px;font-size:{fit(sl["titulo"],100,980,.70)}px;letter-spacing:-3px;padding:0 50px">{esc(sl["titulo"])}</div>')
        for k, sb in enumerate(["limao", "tangerina", "morango", "pessego"]):
            x = 70 + k * 245
            body.append(bottle(sb, x + 22, 360, 660))
            body.append(f'<div style="position:absolute;left:{x}px;width:245px;top:1040px;text-align:center;font-size:34px;color:{CORES[sb]["acc"]}">{esc(CORES[sb]["nome"])}</div>')
        body.append(f'<div class="c" style="top:1110px;font-weight:700;font-size:{fit(sl["texto"],44,960,.56)}px;padding:0 60px">{esc(sl["texto"])}</div>')
    elif t == "cta":
        rev = sl.get("revenda")
        body.append(f'<div style="position:absolute;left:80px;right:80px;top:230px;font-size:{fit(sl["titulo"],120,1700,.62)}px;line-height:1.02;letter-spacing:-3px">{esc(sl["titulo"])}</div>')
        if rev:
            body.append(f'<div style="position:absolute;left:80px;top:640px;white-space:nowrap;font-size:96px;letter-spacing:-2px;color:{c["bg2"]}">{esc(sl["texto"])}</div>')
            body.append(bottle(s, 780, 790, 520))
        else:
            body.append(f'<div style="position:absolute;left:80px;right:420px;top:720px;font-weight:700;font-size:52px;line-height:1.15;color:{c["bg2"]}">{esc(sl["texto"])}</div>')
            body.append(bottle(s, 760, 560, 660))
    else:
        raise ValueError("tipo de slide desconhecido: " + t)
    if t == "cta" or single:
        body.append(f'<div class="foot"><span>{esc(RODAPE)}</span></div>')
    head = '<div class="handle">@beba.wellness</div>'
    if total > 1:
        head += f'<div class="count">{idx}/{total}</div>'
    css = CSS.replace("__BG__", c["bg"]).replace("__BG2__", c["bg2"]).replace("__DARK__", c["dark"])
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'<div id="root" class="{"dk" if dark else ""}"><div id="stripe"></div><div id="dots"></div>'
            f'{head}{"".join(body)}</div></body></html>')

def render_item(item, page, outdir):
    from PIL import Image
    shutil.rmtree(outdir, ignore_errors=True); os.makedirs(outdir)
    slides = item["slides"]; files = []
    for i, sl in enumerate(slides, 1):
        h = slide_html(sl, i, len(slides), item["tipo"] == "imagem")
        hp = os.path.join(ASSETS, f"_slide_{os.getpid()}.html")  # dentro de assets para achar fontes e garrafas
        open(hp, "w", encoding="utf-8").write(h)
        page.goto("file://" + hp); page.wait_for_timeout(150)
        page.evaluate("document.fonts.ready")
        png = os.path.join(outdir, f"{i:02d}.png")
        page.locator("#root").screenshot(path=png)
        os.remove(hp)
        jpg = os.path.join(outdir, f"{i:02d}.jpg")
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=92)
        os.remove(png); files.append(jpg)
    return files

def load(p, default):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default

def main():
    from playwright.sync_api import sync_playwright
    feed = load(os.path.join(ROOT, "content", "feed.json"), [])
    posted = load(os.path.join(ROOT, "state", "posted_feed.json"), [])
    done = {x["id"] for x in posted}
    if "--todos" in sys.argv:
        itens = feed
    elif "--id" in sys.argv:
        want = sys.argv[sys.argv.index("--id") + 1]
        itens = [next(x for x in feed if x["id"] == want)]
    else:
        pend = [x for x in feed if x["id"] not in done]
        if not pend:
            first = posted[0]["id"]
            pend = [next(x for x in feed if x["id"] == first)]
            print("AVISO: banco do feed esgotado, repetindo", first)
        itens = pend[:1]
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": W, "height": H})
        for it in itens:
            files = render_item(it, page, os.path.join(ROOT, "out", "feed", it["id"]))
            print("OK", it["id"], it["tipo"], len(files), "imagem(ns)")
        b.close()
    if len(itens) == 1:
        it = itens[0]
        json.dump({"id": it["id"], "tipo": it["tipo"], "legenda": it["legenda"],
                   "arquivos": [f"{i:02d}.jpg" for i in range(1, len(it["slides"]) + 1)]},
                  open(os.path.join(ROOT, "out", "feed_next.json"), "w", encoding="utf-8"), ensure_ascii=False)

if __name__ == "__main__":
    main()
