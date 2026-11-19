"""Carrossel de matéria (formato aprovado pelo Celso em 19/11/2026):
  1. Gancho: a manchete da matéria/estudo.
  2. Explicação: o que o estudo mostra, com a fonte.
  3. Produto: "Um jeito gostoso de repor as fibras do dia" + os 4 sabores.
A legenda termina com "E você, conhece um jeito fácil e gostoso de repor suas fibras?".

Uso: python scripts/render_materia.py content/materias/<id>.json
Saída: out/materias/<id>/01.jpg, 02.jpg, 03.jpg

Formato do JSON:
{
  "id": "m2026-11-21_antibiotico",
  "kicker": "SAÚDE INTESTINAL",
  "manchete": "Tomou antibiótico?",
  "sub": "Seu intestino pode sentir por até 8 anos",
  "fonte_curta": "Estudo publicado na Nature Medicine",
  "pontos": ["...", "...", "..."],          # 3 ou 4 frases curtas
  "fonte": "Baldanzi et al., Nature Medicine, 2026",
  "aviso": "Use antibióticos só com orientação médica.",   # opcional
  "legenda": "..."
}
"""
import html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "template", "assets")
W, H = 1080, 1350
RODAPE = "CP Comercial | WhatsApp (11) 94764-6006"
VERDE, LIMA, CREME, ESCURO = "#0f2a17", "#a6cc3a", "#f7f3e6", "#123d22"

FONTES = """
@font-face{font-family:"MontF";src:url(fonts/montserrat-latin-900-normal.woff2) format("woff2");font-weight:900;}
@font-face{font-family:"MontF";src:url(fonts/montserrat-latin-700-normal.woff2) format("woff2");font-weight:700;}
html,body{margin:0;padding:0;}
#root{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:"MontF",Arial,sans-serif;}
.handle{position:absolute;left:70px;top:60px;font-weight:700;font-size:32px;letter-spacing:1px;opacity:.7;}
.count{position:absolute;right:70px;top:56px;font-weight:900;font-size:32px;padding:8px 22px;border-radius:999px;}
.pill{display:inline-block;padding:16px 36px;border-radius:999px;font-weight:700;font-size:34px;letter-spacing:5px;}
"""


def esc(s):
    return html.escape(str(s))


def fit(text, maxpx, width, k):
    return int(min(maxpx, width / (k * max(len(text), 1))))


def capa(m, total):
    t1 = m["manchete"]
    fs = fit(max(t1.split(), key=len), 170, 940, .62)
    return f"""<div id="root" style="background:radial-gradient(circle at 85% 75%,#1f5a2e 0%,{VERDE} 55%);color:#fff">
<div class="handle">@beba.wellness</div><div class="count" style="background:#fff;color:{VERDE}">1/{total}</div>
<div style="position:absolute;left:70px;top:190px"><span class="pill" style="border:3px solid {LIMA};color:#fff">{esc(m["kicker"])}</span></div>
<div style="position:absolute;left:70px;right:70px;top:320px;font-weight:900;font-size:{fs}px;line-height:1.0;letter-spacing:-4px">{esc(t1)}</div>
<div style="position:absolute;left:70px;right:140px;top:{340 + int(fs * 2.15)}px;font-weight:900;font-size:76px;line-height:1.08;color:{LIMA}">{esc(m["sub"])}</div>
<div style="position:absolute;left:70px;width:560px;top:1080px;border-top:4px solid {LIMA}"></div>
<div style="position:absolute;left:70px;top:1110px;font-weight:700;font-size:38px">{esc(m["fonte_curta"])}</div>
<div style="position:absolute;right:70px;bottom:70px;font-weight:700;font-size:38px;color:{LIMA}">Arraste para o lado →</div>
</div>"""


def estudo(m, total):
    pts = m["pontos"][:4]
    fs = 40 if max(len(p) for p in pts) < 60 else 36
    cards = "".join(
        f'<div style="display:flex;gap:30px;align-items:center;margin-bottom:22px;padding:24px 32px;border-radius:30px;'
        f'background:#fff;border:3px solid #dfe8cf"><div style="flex:0 0 76px;height:76px;border-radius:50%;background:{ESCURO};'
        f'color:#fff;font-weight:900;font-size:42px;text-align:center;line-height:76px">{i}</div>'
        f'<div style="font-weight:700;font-size:{fs}px;line-height:1.22;color:{ESCURO}">{esc(p)}</div></div>'
        for i, p in enumerate(pts, 1))
    aviso = (f'<div style="margin-top:14px;font-weight:700;font-size:32px;color:{ESCURO}">✚ {esc(m["aviso"])}</div>'
             if m.get("aviso") else "")
    return f"""<div id="root" style="background:{CREME};color:{ESCURO}">
<div class="handle">@beba.wellness</div><div class="count" style="background:{ESCURO};color:#fff">2/{total}</div>
<div style="position:absolute;left:70px;top:150px"><span class="pill" style="border:3px solid #9cbf63;color:{ESCURO}">O QUE O ESTUDO MOSTRA</span></div>
<div style="position:absolute;left:70px;right:70px;top:255px">{cards}</div>
<div style="position:absolute;left:70px;right:70px;bottom:70px;font-size:30px;line-height:1.3">
<div style="font-weight:700;opacity:.8">Fonte: {esc(m["fonte"])}</div>{aviso}</div>
</div>"""


def produto(m, total):
    gar = "".join(
        f'<div style="position:absolute;left:{95 + k * 230}px;top:330px;width:200px;filter:drop-shadow(0 30px 30px rgba(0,0,0,.25))">'
        f'<img src="garrafas/{s}.png" style="display:block;width:100%"></div>'
        for k, s in enumerate(["limao", "tangerina", "morango", "pessego"]))
    return f"""<div id="root" style="background:linear-gradient(#f8efe4,#efe0cf);color:#3b1d10">
<div class="handle">@beba.wellness</div><div class="count" style="background:#3b1d10;color:#fff">3/{total}</div>
<div style="position:absolute;left:60px;right:60px;top:140px;text-align:center;font-weight:900;font-size:68px;line-height:1.1;letter-spacing:-1px">Um jeito gostoso de repor as fibras do dia</div>
{gar}
<div style="position:absolute;left:0;right:0;top:1030px;text-align:center;font-weight:700;font-size:40px">6 g de fibra • zero açúcar • zero caloria</div>
<div style="position:absolute;left:0;right:0;top:1095px;text-align:center;font-weight:700;font-size:34px;opacity:.8">📍 Morango e Tangerina você encontra no OXXO</div>
<div style="position:absolute;left:0;right:0;bottom:56px;text-align:center"><span style="display:inline-block;padding:18px 40px;border-radius:999px;background:#3b1d10;color:#fff;font-weight:700;font-size:34px">{esc(RODAPE)}</span></div>
</div>"""


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    m = json.load(open(sys.argv[1], encoding="utf-8"))
    out = os.path.join(ROOT, "out", "materias", m["id"])
    os.makedirs(out, exist_ok=True)
    slides = [capa(m, 3), estudo(m, 3), produto(m, 3)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": W, "height": H})
        for i, body in enumerate(slides, 1):
            hp = os.path.join(ASSETS, f"_materia_{os.getpid()}.html")
            open(hp, "w", encoding="utf-8").write(
                f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTES}</style></head><body>{body}</body></html>')
            page.goto("file://" + hp)
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(200)
            png = os.path.join(out, f"{i:02d}.png")
            page.locator("#root").screenshot(path=png)
            os.remove(hp)
            Image.open(png).convert("RGB").save(os.path.join(out, f"{i:02d}.jpg"), "JPEG", quality=92)
            os.remove(png)
    print("OK", out)


if __name__ == "__main__":
    main()
