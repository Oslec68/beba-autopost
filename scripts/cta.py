"""Ajusta a legenda antes de publicar na @beba.wellness:
1. Tira a linha "Quer revender? ..." (revenda é do perfil de empresas, não desta conta).
2. Põe a chamada do cupom (content/cta.json) logo antes das hashtags, trocando qualquer versão antiga dela.
Uso: from cta import aplicar_cta ; legenda = aplicar_cta(legenda)
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQ = os.path.join(ROOT, "content", "cta.json")

def carregar():
    try:
        return json.load(open(ARQ, encoding="utf-8"))
    except (OSError, ValueError):
        return {"ativo": False}

def tirar_revenda(legenda):
    linhas = [l for l in legenda.split("\n") if not l.strip().startswith("Quer revender")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()

def aplicar_cta(legenda, cfg=None):
    cfg = cfg if cfg is not None else carregar()
    legenda = tirar_revenda(legenda)
    if not cfg.get("ativo") or not cfg.get("linhas"):
        return legenda
    cupom = cfg.get("cupom", "")
    linhas = [l for l in legenda.split("\n")
              if not (cupom and cupom in l) and l.strip() != "👉 Segue a @beba.wellness"]
    legenda = re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()
    bloco = "\n".join(cfg["linhas"])
    pars = legenda.split("\n\n")
    if len(pars) > 1 and pars[-1].lstrip().startswith("#"):
        return "\n\n".join(pars[:-1] + [bloco, pars[-1]])
    return legenda + "\n\n" + bloco

if __name__ == "__main__":
    import sys
    print(aplicar_cta(sys.stdin.read()))
