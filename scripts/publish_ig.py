"""Publica um Reel no Instagram pela API oficial (Instagram API com login do Facebook).
Uso: python scripts/publish_ig.py <video_url_publica>
Lê a legenda de out/next.json. Variáveis: IG_TOKEN (token da Página, obrigatório),
IG_USER_ID (opcional, padrão @beba.wellness), IG_API_VERSION (opcional).
Ao publicar, registra em state/posted.json.
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
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    # Nova tentativa em falha passageira (menos no media_publish, que tem conferência própria contra post em dobro)
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

def main():
    video_url = sys.argv[1]
    nxt = json.load(open(os.path.join(ROOT, "out", "next.json"), encoding="utf-8"))
    uid = UID
    me = call("GET", uid, fields="username")
    print("Conta:", me.get("username"))
    # Capa: sem thumb_offset/cover_url o Instagram usa o quadro 0 (só o fundo, antes das animações).
    extra = {}
    if len(sys.argv) > 2 and sys.argv[2]:
        extra["cover_url"] = sys.argv[2]
    else:
        extra["thumb_offset"] = str(nxt.get("capa_ms", 2800))
    try:
        c = call("POST", f"{uid}/media", media_type="REELS", video_url=video_url,
                 caption=nxt["legenda"], share_to_feed="true", **extra)
    except SystemExit as e:
        if "cover_url" not in extra:
            raise
        print("AVISO: cover_url recusada, usando thumb_offset.", e)
        c = call("POST", f"{uid}/media", media_type="REELS", video_url=video_url, caption=nxt["legenda"],
                 share_to_feed="true", thumb_offset=str(nxt.get("capa_ms", 2800)))
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
    media_id = publicar_com_retentativa(uid, cid)
    link = call("GET", media_id, fields="permalink").get("permalink", "")
    state_p = os.path.join(ROOT, "state", "posted.json")
    posted = json.load(open(state_p, encoding="utf-8")) if os.path.exists(state_p) else []
    posted = [x for x in posted if x["id"] != nxt["id"]]
    posted.append({"id": nxt["id"], "formato": nxt.get("formato", "rotina"), "media_id": media_id, "permalink": link,
                   "quando": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")})
    json.dump(posted, open(state_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("PUBLICADO", nxt["id"], link)
    with open(os.getenv("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"permalink={link}\n")

if __name__ == "__main__":
    main()
