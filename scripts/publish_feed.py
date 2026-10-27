"""Publica um post de imagem ou um carrossel no Instagram (API com login do Facebook).
Uso: python scripts/publish_feed.py <url_base_publica_da_pasta>   (ex.: https://x.github.io/repo/fc001/)
Lê out/feed_next.json. Variáveis: IG_TOKEN (token da Página), IG_USER_ID e IG_API_VERSION (opcionais).
Ao publicar, registra em state/posted_feed.json.
"""
import json, os, sys, time, datetime, urllib.request, urllib.parse, urllib.error

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
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ERRO API {path}: {e.code} {e.read().decode()[:500]}")

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
    media_id = call("POST", f"{UID}/media_publish", creation_id=cid)["id"]
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
