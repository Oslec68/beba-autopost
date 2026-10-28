"""Escolhe o próximo post do banco, monta o projeto HyperFrames e renderiza o MP4.
Saída: out/<id>.mp4, out/<id>.txt (legenda) e out/next.json.
Uso: python scripts/render_next.py [--id pf001_limao] [--no-render]
"""
import json, os, shutil, subprocess, sys
from string import Template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORES = {
    "limao":     dict(nome="LIMÃO",     bg="#eef7d2", bg2="#c9e58c", dark="#26400c", acc="#5f9e12"),
    "tangerina": dict(nome="TANGERINA", bg="#ffe6cc", bg2="#ffbf80", dark="#5c2404", acc="#e8660c"),
    "morango":   dict(nome="MORANGO",   bg="#fde0dc", bg2="#f5a39a", dark="#4a1410", acc="#c2271d"),
    "pessego":   dict(nome="PÊSSEGO",   bg="#ffe9dc", bg2="#f8bf9c", dark="#5a2a14", acc="#e0773f"),
}

def fit(text, maxpx, width, k):
    """Tamanho de fonte para caber em `width` px (k = largura média por caractere em em)."""
    return int(min(maxpx, width / (k * max(len(text), 1))))

def load(p, default):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default

def escolher(pend):
    """Primeiro post pendente que combina com o dia/hora reais (Brasília).
    Evita "Segunda de novo?" numa terça ou "Almoço na rua?" às 22h.
    O GitHub costuma atrasar o cron em horas, por isso vale a hora real, não a do agendamento."""
    import datetime
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    dia, hora = agora.weekday(), agora.hour
    regras = load(os.path.join(ROOT, "content", "regras.json"), {})
    def cabe(p):
        r = regras.get(p["id"])
        if not r:
            return True
        if "dias" in r and dia not in r["dias"]:
            return False
        if "horas" in r and not (r["horas"][0] <= hora < r["horas"][1]):
            return False
        return True
    for p in pend:
        if cabe(p):
            print(f"Escolhido {p['id']} (dia {dia}, {hora}h)")
            return p
    livres = [p for p in pend if p["id"] not in regras]
    print("AVISO: nenhum post combina com agora; usando o primeiro sem restrição")
    return livres[0] if livres else pend[0]

def main():
    posts = load(os.path.join(ROOT, "content", "posts.json"), [])
    state_p = os.path.join(ROOT, "state", "posted.json")
    posted = load(state_p, [])
    done = {x["id"] for x in posted}
    want = sys.argv[sys.argv.index("--id") + 1] if "--id" in sys.argv else None
    if want:
        post = next(p for p in posts if p["id"] == want)
    else:
        pend = [p for p in posts if p["id"] not in done]
        if not pend:
            # banco esgotado: recomeça o ciclo pelo post publicado há mais tempo
            order = [x["id"] for x in posted]
            post = next(p for p in posts if p["id"] == order[0])
            print("AVISO: banco esgotado, repetindo", post["id"])
        else:
            post = escolher(pend)
    s = post["sabor"]; c = CORES[s]
    proj = os.path.join(ROOT, "build", post["id"])
    shutil.rmtree(proj, ignore_errors=True)
    shutil.copytree(os.path.join(ROOT, "template", "assets"), os.path.join(proj, "assets"))
    seed = sum(map(ord, post["id"]))
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "music.py"), str(seed),
                    os.path.join(proj, "assets", "music.wav")], check=True)
    if post["oxxo"]:
        oh = '<div id="ox">Você encontra no OXXO</div>'
        oj = 'tl.fromTo("#ox", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(2)" }, 12.6);'
    else:
        oh, oj = '<style>#hd{top:1530px!important}#ft{top:1660px!important}</style>', ""
    tpl = Template(open(os.path.join(ROOT, "template", "index.html.tpl"), encoding="utf-8").read())
    html = tpl.substitute(
        slug=s, nome=c["nome"], bg=c["bg"], bg2=c["bg2"], dark=c["dark"], acc=c["acc"],
        tag=post["tag"], h1=post["h1"], h2=post["h2"], l2a=post["l2a"], l2b=post["l2b"], fim=post["fim"],
        h1fs=fit(post["h1"], 190, 1000, 0.80), h2fs=fit(post["h2"], 170, 1000, 0.80),
        tagfs=fit(post["tag"], 110, 900, 0.78), lfs=fit(max(post["l2a"], post["l2b"], key=len), 108, 920, 0.60),
        oxxo_html=oh, oxxo_js=oj)
    open(os.path.join(proj, "index.html"), "w", encoding="utf-8").write(html)
    out = os.path.join(ROOT, "out"); os.makedirs(out, exist_ok=True)
    mp4 = os.path.join(out, post["id"] + ".mp4")
    open(os.path.join(out, post["id"] + ".txt"), "w", encoding="utf-8").write(post["legenda"])
    json.dump({"id": post["id"], "mp4": mp4, "legenda": post["legenda"]},
              open(os.path.join(out, "next.json"), "w", encoding="utf-8"), ensure_ascii=False)
    if "--no-render" not in sys.argv:
        subprocess.run(["npx", "-y", "hyperframes@0.8.198", "render", "--quality", "high", "--output", mp4],
                       cwd=proj, check=True)
    print("OK", post["id"], mp4)

if __name__ == "__main__":
    main()
