"""Publica um post de imagem ou um carrossel no Instagram (API com login do Facebook).
Uso: python scripts/publish_feed.py <url_base_publica_da_pasta>   (ex.: https://x.github.io/repo/fc001/)
Lê out/feed_next.json. Variáveis: IG_TOKEN (token da Página), IG_USER_ID e IG_API_VERSION (opcionais).
Ao publicar, registra em state/posted_feed.json.
"""
import json, os, re, sys, time, datetime, urllib.request, urllib.parse, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.getenv("IG_API_VERSION", "v23.0")
BASE = f"https://graph.facebook.com/{VER}"
UID = os.getenv("IG_USER_ID") or "17841441162584913"  # @beba.wellness
TOKEN = os.environ["IG_TOKEN"]

def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{BASE}/{path}"
    req = urllib.request.Request(url + "?" + data.decode()) if method == "GET" else \
        urllib.request.Request(url, data=data, method="POST")
    tentativas = 1 if path.endswith("media_publish") else 3
    for n in range(1, tentativas + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            corpo = e.read().decode()[:500]
            if n < tentativas and _transiente(e.code, corpo):
                print(f"AVISO: falha passageira em {path} (tentativa {n}/{tentativas}), repetindo...")
                time.sleep(20 * n)
                continue
            raise SystemExit(f"ERRO API {path}: {e.code} {corpo}")
        except (urllib.error.URLError, TimeoutError) as e:
            if n < tentativas:
                print(f"AVISO: rede falhou em {path} (tentativa {n}/{tentativas}), repetindo...")
                time.sleep(20 * n)
                continue
            raise SystemExit(f"ERRO API {path}: rede {e}")

def _transiente(code, corpo):
    """Falha passageira do Instagram/Meta: erro 5xx ou resposta marcada como is_transient."""
    return code >= 500 or '"is_transient":true' in corpo.replace(" ", "")

def publicar_com_retentativa(uid, cid, tentativas=3):
    """media_publish com nova tentativa em falha passageira.
    Antes de repetir, confere se o post JÁ saiu (status PUBLISHED), para nunca publicar em dobro."""
    ultimo = None
    for n in range(1, tentativas + 1):
        try:
            return call("POST", f"{uid}/media_publish", creation_id=cid)["id"]
        except SystemExit as e:
            ultimo = e
            m = re.search(r": (\d{3}) ", str(e))
            if not _transiente(int(m.group(1)) if m else 0, str(e)):
                raise   # erro definitivo (token, permissão, bloqueio): não adianta repetir
            print(f"AVISO: falha passageira ao publicar (tentativa {n}/{tentativas}): {e}")
            time.sleep(30 * n)
            try:
                st = call("GET", cid, fields="status_code")
            except SystemExit:
                st = {}
            if st.get("status_code") == "PUBLISHED":
                rec = call("GET", f"{uid}/media", fields="id", limit="1").get("data", [])
                if rec:
                    print("Post já estava publicado apesar do erro; seguindo sem repetir.")
                    return rec[0]["id"]
    raise ultimo

def wait(cid):
    for _ in range(60):
        st = call("GET", cid, fields="status_code")
        code = st.get("status_code")
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            raise SystemExit(f"ERRO no processamento: {st}")
        time.sleep(5)
    raise SystemExit("ERRO: tempo esgotado esperando o Instagram processar")

def main():
    base = sys.argv[1].rstrip("/") + "/"
    nxt = json.load(open(os.path.join(ROOT, "out", "feed_next.json"), encoding="utf-8"))
    urls = [base + f for f in nxt["arquivos"]]
    print("Conta:", call("GET", UID, fields="username").get("username"), "|", nxt["id"], nxt["tipo"])
    if len(urls) == 1:
        cid = call("POST", f"{UID}/media", image_url=urls[0], caption=nxt["legenda"])["id"]
    else:
        kids = []
        for u in urls[:10]:  # limite do Instagram: 10 itens por carrossel
            k = call("POST", f"{UID}/media", image_url=u, is_carousel_item="true")["id"]
            wait(k); kids.append(k)
        cid = call("POST", f"{UID}/media", media_type="CAROUSEL", children=",".join(kids),
                   caption=nxt["legenda"])["id"]
    wait(cid)
    media_id = publicar_com_retentativa(UID, cid)
    link = call("GET", media_id, fields="permalink").get("permalink", "")
    state_p = os.path.join(ROOT, "state", "posted_feed.json")
    posted = json.load(open(state_p, encoding="utf-8")) if os.path.exists(state_p) else []
    posted = [x for x in posted if x["id"] != nxt["id"]]
    posted.append({"id": nxt["id"], "tipo": nxt["tipo"], "media_id": media_id, "permalink": link,
                   "quando": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")})
    json.dump(posted, open(state_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("PUBLICADO", nxt["id"], link)
    with open(os.getenv("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"permalink={link}\n")

if __name__ == "__main__":
    main()
