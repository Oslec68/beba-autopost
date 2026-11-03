"""Publica o mesmo vídeo do Reel também como Story no @beba.wellness.
Uso: python scripts/publish_story.py <video_url_publica>
Variáveis: IG_TOKEN (obrigatório), IG_USER_ID e IG_API_VERSION (opcionais).
Falha aqui nunca derruba o Reel: o workflow roda este passo com continue-on-error.
"""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from publish_ig import call, UID  # mesma conta, token e chamada da API


def main():
    video_url = sys.argv[1]
    c = call("POST", f"{UID}/media", media_type="STORIES", video_url=video_url)
    cid = c["id"]
    for _ in range(60):  # até ~10 min
        st = call("GET", cid, fields="status_code,status")
        code = st.get("status_code")
        print("status story:", code)
        if code == "FINISHED":
            break
        if code in ("ERROR", "EXPIRED"):
            raise SystemExit(f"ERRO no processamento do Story: {st}")
        time.sleep(10)
    else:
        raise SystemExit("ERRO: tempo esgotado esperando o Instagram processar o Story")
    pub = call("POST", f"{UID}/media_publish", creation_id=cid)
    print("STORY PUBLICADO", pub.get("id"))


if __name__ == "__main__":
    main()
