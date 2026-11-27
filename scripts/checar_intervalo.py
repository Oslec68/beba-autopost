"""Trava contra post duplicado nos horários automáticos.

Uso: python scripts/checar_intervalo.py state/posted.json 120
Grava ok=sim ou ok=nao em $GITHUB_OUTPUT. Dá "nao" quando o último post
registrado no arquivo saiu há menos de N minutos (ex.: o disparo externo e um
agendamento atrasado do GitHub chegando juntos).
"""
import datetime, json, os, sys

arq, minutos = sys.argv[1], int(sys.argv[2])
ok = "sim"
try:
    posted = json.load(open(arq, encoding="utf-8"))
except (FileNotFoundError, ValueError):
    posted = []
if posted and posted[-1].get("quando"):
    ultimo = datetime.datetime.fromisoformat(posted[-1]["quando"])
    agora = datetime.datetime.now(datetime.timezone.utc)
    passou = (agora - ultimo).total_seconds() / 60
    print(f"Último post: {posted[-1]['id']} há {passou:.0f} min (mínimo {minutos})")
    if passou < minutos:
        ok = "nao"
        print("PULANDO: post recente demais, este disparo não publica nada")
saida = os.environ.get("GITHUB_OUTPUT")
if saida:
    with open(saida, "a") as f:
        f.write(f"ok={ok}\n")
else:
    print("ok=" + ok)
