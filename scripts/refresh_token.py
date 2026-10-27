"""Renova o token de longa duração do Instagram (vale 60 dias; renovar com frequência).
Imprime o novo token em stdout (o workflow grava no secret IG_TOKEN) e a validade em stderr."""
import json, os, sys, urllib.request

tok = os.environ["IG_TOKEN"]
url = "https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=" + tok
try:
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.loads(r.read())
except urllib.error.HTTPError as e:
    sys.exit(f"ERRO ao renovar token: {e.code} {e.read().decode()[:300]}")
print(f"Token renovado. Expira em {int(d.get('expires_in', 0)) // 86400} dias.", file=sys.stderr)
print(d["access_token"])
