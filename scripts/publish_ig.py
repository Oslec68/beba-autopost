"""Publica um Reel no Instagram pela API oficial (Instagram API com login do Facebook).
Uso: python scripts/publish_ig.py <video_url_publica>
Lê a legenda de out/next.json. Variáveis: IG_TOKEN (token da Página, obrigatório),
IG_USER_ID (opcional, padrão @beba.wellness), IG_API_VERSION (opcional).
Ao publicar, registra em state/posted.json.
"""
import json, os, sys, time, datetime, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.getenv("IG_API_VERSION", "v23.0")
BASE = f"https://graph.facebook.com/{VER}"
UID = os.getenv("IG_USER_ID") or "17841441162584913"  # @beba.wellness
TOKEN = os.environ["IG_TOKEN"]

def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{BASE}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ERRO API {path}: {e.code} {e.read().decode()[:500]}")

def main():
    video_url = sys.argv[1]
    nxt = json.load(open(os.path.join(ROOT, "out", "next.json"), encoding="utf-8"))
    uid = UID
    me = call("GET", uid, fields="username")
    print("Conta:", me.get("username"))
    c = call("POST", f"{uid}/media", media_type="REELS", video_url=video_url,
             caption=nxt["legenda"], share_to_feed="true")
    cid = c["id"]
    for _ in range(60):  # até ~10 min
        st = call("GET", cid, fields="status_code,status")
        code = st.get("status_code")
        print("status:", code)
        if code == "FINISHED":
            break
        if code in ("ERROR", "EXPIRED"):
            raise SystemExit(f"ERRO no processamento do vídeo: {st}")
        time.sleep(10)
    else:
        raise SystemExit("ERRO: tempo esgotado esperando o Instagram processar o vídeo")
    pub = call("POST", f"{uid}/media_publish", creation_id=cid)
    media_id = pub["id"]
    link = call("GET", media_id, fields="permalink").get("permalink", "")
    state_p = os.path.join(ROOT, "state", "posted.json")
    posted = json.load(open(state_p, encoding="utf-8")) if os.path.exists(state_p) else []
    posted = [x for x in posted if x["id"] != nxt["id"]]
    posted.append({"id": nxt["id"], "media_id": media_id, "permalink": link,
                   "quando": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")})
    json.dump(posted, open(state_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("PUBLICADO", nxt["id"], link)
    with open(os.getenv("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"permalink={link}\n")

if __name__ == "__main__":
    main()
