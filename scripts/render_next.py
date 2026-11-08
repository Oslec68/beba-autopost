"""Escolhe o próximo post do banco, monta o projeto HyperFrames e renderiza o MP4.
Saída: out/<id>.mp4, out/<id>.txt (legenda) e out/next.json.
Uso: python scripts/render_next.py [--id pf001_limao] [--no-render]
"""
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revisor import revisar_post
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

# Formatos de vídeo. "capa" = momento (ms) usado como capa do Reel: o quadro em que
# título, gancho e garrafa já estão na tela (sem isso o Instagram usa o quadro 0, que é só o fundo).
FORMATOS = {
    "vs":        dict(tpl="vs.html.tpl",        capa=2900),
    "quiz":      dict(tpl="quiz.html.tpl",      capa=2900),
    "lineup":    dict(tpl="lineup.html.tpl",    capa=2700),
    "checklist": dict(tpl="checklist.html.tpl", capa=2900),
    "rotina":    dict(tpl="index.html.tpl",     capa=2800),
}
ORDEM = ["vs", "quiz", "lineup", "checklist", "rotina"]
SABORES = ["limao", "tangerina", "morango", "pessego"]

# Perguntas do quiz: só informações do rótulo.
QUIZ = [
    dict(perg="Quantos gramas de fibra tem uma Pura Fibra?", ops=["2 g", "6 g", "0 g"], certo=1),
    dict(perg="Quanto açúcar tem uma Pura Fibra?", ops=["Bastante", "Um pouco", "Zero"], certo=2),
    dict(perg="Quantas calorias tem uma Pura Fibra?", ops=["Zero", "Umas 60", "Umas 120"], certo=0),
    dict(perg="A Pura Fibra traz vitaminas do...", ops=["Complexo A", "Complexo B", "Complexo Z"], certo=1),
]

def escolher_formato(post, posted):
    """Formato fixo no post (campo "formato") ou o formato usado há mais tempo,
    para nunca sair dois vídeos seguidos com a mesma cara."""
    if post.get("formato") in FORMATOS:
        return post["formato"]
    ultimo = {f: -1 for f in ORDEM}
    for i, x in enumerate(posted):
        ultimo[x.get("formato", "rotina")] = i
    # Ciclo de feedback: state/desempenho.json (gerado toda semana pelo desempenho.py) dá um peso a
    # cada formato. Quem rende mais volta mais rápido; sem dados, peso 1 = rodízio igual ao original.
    pesos = load(os.path.join(ROOT, "state", "desempenho.json"), {}).get("pesos", {})
    n = len(posted)
    def prioridade(f):
        espera = n - ultimo[f]  # posts desde a última vez que o formato saiu
        if espera <= 1:
            return (-1, ORDEM.index(f))  # nunca dois seguidos
        return (-(espera * pesos.get(f, 1.0)), ORDEM.index(f))
    return min(ORDEM, key=prioridade)

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
    # Revisor automático: post com problema de texto/regra é pulado e avisado.
    bloqueados = {}
    for p in posts:
        e = revisar_post(p)
        if e:
            bloqueados[p["id"]] = e
            print(f"REVISOR barrou {p['id']}: " + "; ".join(e))
    if want:
        post = next(p for p in posts if p["id"] == want)
        if want in bloqueados and "--forcar" not in sys.argv:
            raise SystemExit(f"REVISOR reprovou {want}: " + "; ".join(bloqueados[want]) + " (use --forcar para ignorar)")
    else:
        posts = [p for p in posts if p["id"] not in bloqueados]
        pend = [p for p in posts if p["id"] not in done]
        if not pend:
            # banco esgotado: recomeça o ciclo pelo post publicado há mais tempo
            order = [x["id"] for x in posted]
            ids = {p["id"]: p for p in posts}
            post = next(ids[i] for i in order if i in ids)
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
    formato = sys.argv[sys.argv.index("--formato") + 1] if "--formato" in sys.argv else escolher_formato(post, posted)
    F = FORMATOS[formato]
    if post["oxxo"]:
        oh = '<div id="ox">Você encontra no OXXO</div>'
        oj = 'tl.fromTo("#ox", { scale: .6, opacity: 0 }, { scale: 1, opacity: 1, duration: .4, ease: "back.out(2)" }, 12.6);'
    elif formato == "rotina":
        oh, oj = '<style>#hd{top:1530px!important}#ft{top:1660px!important}</style>', ""
    else:
        oh, oj = "", ""
    q = QUIZ[seed % len(QUIZ)]
    idx = SABORES.index(s)
    extra = dict(
        perg=q["perg"], pfs=fit(q["perg"], 92, 2300, 0.62), op0=q["ops"][0], op1=q["ops"][1], op2=q["ops"][2],
        certo=q["certo"], errados=",".join(f"#o{i}" for i in range(3) if i != q["certo"]),
        idx=idx, outros=",".join(f"#q{i}" for i in range(4) if i != idx))
    tpl = Template(open(os.path.join(ROOT, "template", F["tpl"]), encoding="utf-8").read())
    html = tpl.substitute(
        slug=s, nome=c["nome"], bg=c["bg"], bg2=c["bg2"], dark=c["dark"], acc=c["acc"],
        tag=post["tag"], h1=post["h1"], h2=post["h2"], l2a=post["l2a"], l2b=post["l2b"], fim=post["fim"],
        h1fs=fit(post["h1"], 190, 1000, 0.80), h2fs=fit(post["h2"], 170, 1000, 0.80),
        tagfs=fit(post["tag"], 110, 900, 0.78), lfs=fit(max(post["l2a"], post["l2b"], key=len), 108, 920, 0.60),
        oxxo_html=oh, oxxo_js=oj, **extra)
    open(os.path.join(proj, "index.html"), "w", encoding="utf-8").write(html)
    out = os.path.join(ROOT, "out"); os.makedirs(out, exist_ok=True)
    mp4 = os.path.join(out, post["id"] + ".mp4")
    open(os.path.join(out, post["id"] + ".txt"), "w", encoding="utf-8").write(post["legenda"])
    json.dump({"id": post["id"], "mp4": mp4, "legenda": post["legenda"], "formato": formato, "capa_ms": F["capa"],
               "bloqueados": sorted(bloqueados)},
              open(os.path.join(out, "next.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("Formato:", formato, "| capa em", F["capa"], "ms")
    if "--no-render" not in sys.argv:
        subprocess.run(["npx", "-y", "hyperframes@0.8.198", "render", "--quality", "high", "--output", mp4],
                       cwd=proj, check=True)
    print("OK", post["id"], mp4)

if __name__ == "__main__":
    main()
