"""Ciclo de feedback: mede cada Reel publicado e ensina o sistema a usar mais o que funciona.

Lê state/posted.json, busca as métricas de cada Reel na API do Instagram e grava state/desempenho.json com:
- nota de cada post  (views + 2x curtidas/comentários + 5x salvamentos/compartilhamentos)
- média por formato e por sabor
- "pesos" por formato, que o render_next.py usa para escolher o próximo formato
  (formato que rende mais sai com mais frequência; nenhum formato some, só muda o ritmo)

Uso: python scripts/desempenho.py   (precisa de IG_TOKEN)
Sem a permissão instagram_manage_insights no token, usa só curtidas e comentários (avisa no resumo).
"""
import datetime, json, os, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = f"https://graph.facebook.com/{os.getenv('IG_API_VERSION', 'v23.0')}"
TOKEN = os.environ["IG_TOKEN"]
METRICAS = ["views", "reach", "likes", "comments", "shares", "saved"]

def get(path, **params):
    params["access_token"] = TOKEN
    url = f"{BASE}/{path}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read())

def medir(media_id):
    """Devolve (métricas, completo?)."""
    try:
        d = get(f"{media_id}/insights", metric=",".join(METRICAS))
        m = {x["name"]: (x.get("values") or [{}])[0].get("value", 0) or 0 for x in d.get("data", [])}
        return m, True
    except urllib.error.HTTPError:
        pass
    try:
        d = get(media_id, fields="like_count,comments_count")
        return {"likes": d.get("like_count", 0), "comments": d.get("comments_count", 0)}, False
    except urllib.error.HTTPError as e:
        print("sem dados para", media_id, e.code)
        return None, False

def nota(m):
    return (m.get("views", 0) + 2 * (m.get("likes", 0) + m.get("comments", 0))
            + 5 * (m.get("shares", 0) + m.get("saved", 0)))

def media_por(posts, chave):
    g = {}
    for p in posts:
        g.setdefault(p[chave], []).append(p["nota"])
    return {k: dict(n=len(v), media=round(sum(v) / len(v), 1)) for k, v in g.items()}

def main():
    posted = json.load(open(os.path.join(ROOT, "state", "posted.json"), encoding="utf-8"))
    linhas, completo = [], True
    for x in posted:
        if not x.get("media_id"):
            continue
        m, ok = medir(x["media_id"])
        if m is None:
            continue
        completo = completo and ok
        linhas.append(dict(id=x["id"], sabor=x["id"].split("_", 1)[-1], formato=x.get("formato", "rotina"),
                           permalink=x.get("permalink", ""), quando=x.get("quando", ""), nota=nota(m), **m))
    if not linhas:
        raise SystemExit("Nenhum Reel com métricas.")
    geral = sum(p["nota"] for p in linhas) / len(linhas) or 1
    por_formato = media_por(linhas, "formato")
    # peso só vale com pelo menos 3 Reels do formato; limitado entre 0,6 e 1,6 para nenhum formato sumir
    pesos = {f: round(min(1.6, max(0.6, v["media"] / geral)), 2) if v["n"] >= 3 else 1.0
             for f, v in por_formato.items()}
    out = dict(atualizado=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
               metricas_completas=completo, nota_media=round(geral, 1), pesos=pesos,
               por_formato=por_formato, por_sabor=media_por(linhas, "sabor"),
               posts=sorted(linhas, key=lambda p: -p["nota"]))
    json.dump(out, open(os.path.join(ROOT, "state", "desempenho.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    top = out["posts"][:3]
    fmt = sorted(por_formato.items(), key=lambda kv: -kv[1]["media"])
    sab = sorted(out["por_sabor"].items(), key=lambda kv: -kv[1]["media"])
    msg = ["📊 @beba.wellness — desempenho dos Reels (" + str(len(linhas)) + " medidos)",
           "Top 3: " + " | ".join(f"{p['id']} ({p['nota']})" for p in top),
           "Melhor formato: " + f"{fmt[0][0]} ({fmt[0][1]['media']})" + " · pior: " + f"{fmt[-1][0]} ({fmt[-1][1]['media']})",
           "Melhor sabor: " + f"{sab[0][0]}" + " · pior: " + f"{sab[-1][0]}",
           "Pesos usados daqui pra frente: " + ", ".join(f"{k} {v}" for k, v in sorted(pesos.items()))]
    if not completo:
        msg.append("⚠️ Token sem a permissão instagram_manage_insights: medindo só curtidas e comentários.")
    texto = "\n".join(msg)
    open(os.path.join(ROOT, "state", "desempenho_resumo.txt"), "w", encoding="utf-8").write(texto)
    print(texto)

if __name__ == "__main__":
    main()
