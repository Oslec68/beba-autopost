"""Verifica se o token da Página (IG_TOKEN) ainda funciona.
Com login do Facebook, o token da Página gerado a partir de um token de longa duração não vence;
este script só confere e falha (gerando aviso) se ele tiver sido revogado."""
import json, os, sys, urllib.request, urllib.error

tok = os.environ["IG_TOKEN"]
uid = os.getenv("IG_USER_ID") or "17841441162584913"
url = f"https://graph.facebook.com/v23.0/{uid}?fields=username&access_token={tok}"
try:
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.loads(r.read())
except urllib.error.HTTPError as e:
    sys.exit(f"ERRO: token inválido ou revogado: {e.code} {e.read().decode()[:300]}")
print("Token OK para @" + d.get("username", "?"))
