"""Publica o mesmo vídeo do Reel também como Reel na Página do Facebook.
Uso: python scripts/publish_fb_reel.py <video_url_publica>
Lê a legenda de out/next.json. Variáveis: IG_TOKEN (o mesmo token da Página, obrigatório),
FB_PAGE_ID (opcional: sem ele, a Página é descoberta pelo próprio token), IG_API_VERSION (opcional).
O token precisa da permissão pages_manage_posts (além das que já usa para o Instagram).
Falha aqui nunca derruba o Reel do Instagram: o workflow roda este passo com continue-on-error.
Fluxo da API de Reels do Facebook: start -> upload por URL (rupload) -> finish -> espera ficar pronto.
"""
import json, os, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from publish_ig import call, TOKEN, VER, ROOT, _transiente  # mesmo token e mesma chamada da API


def upload_por_url(video_id, video_url, tentativas=3):
    """O Facebook baixa o vídeo direto do link público (GitHub Pages)."""
    req = urllib.request.Request(
        f"https://rupload.facebook.com/video-upload/{VER}/{video_id}", data=b"", method="POST",
        headers={"Authorization": f"OAuth {TOKEN}", "file_url": video_url})
    for n in range(1, tentativas + 1):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                resp = json.loads(r.read())
            if resp.get("success"):
                return
            raise SystemExit(f"ERRO upload: {resp}")
        except urllib.error.HTTPError as e:
            corpo = e.read().decode()[:500]
            if n < tentativas and _transiente(e.code, corpo):
                print(f"AVISO: falha passageira no upload (tentativa {n}/{tentativas}), repetindo...")
                time.sleep(20 * n)
                continue
            raise SystemExit(f"ERRO upload: {e.code} {corpo}")
        except (urllib.error.URLError, TimeoutError) as e:
            if n < tentativas:
                time.sleep(20 * n)
                continue
            raise SystemExit(f"ERRO upload: rede {e}")


def main():
    video_url = sys.argv[1]
    nxt = json.load(open(os.path.join(ROOT, "out", "next.json"), encoding="utf-8"))
    page_id = os.getenv("FB_PAGE_ID")
    if not page_id:
        me = call("GET", "me", fields="id,name")  # com token de Página, /me é a própria Página
        page_id = me["id"]
        print("Página:", me.get("name"), page_id)

    vid = call("POST", f"{page_id}/video_reels", upload_phase="start")["video_id"]
    upload_por_url(vid, video_url)
    call("POST", f"{page_id}/video_reels", upload_phase="finish", video_id=vid,
         video_state="PUBLISHED", description=nxt["legenda"])

    for _ in range(60):  # até ~10 min
        st = call("GET", vid, fields="status").get("status", {})
        video = st.get("video_status")
        fase = (st.get("publishing_phase") or {}).get("status")
        print("status fb:", video, "| publicação:", fase)
        if video == "error" or fase == "error":
            raise SystemExit(f"ERRO no processamento do Reel do Facebook: {st}")
        if fase == "complete":
            break
        time.sleep(10)
    else:
        raise SystemExit("ERRO: tempo esgotado esperando o Facebook publicar o Reel")

    link = call("GET", vid, fields="permalink_url").get("permalink_url", "")
    if link.startswith("/"):
        link = "https://www.facebook.com" + link
    print("FACEBOOK PUBLICADO", nxt["id"], link)
    with open(os.getenv("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"fb_link={link}\n")


if __name__ == "__main__":
    main()
