"""Põe a chamada do cupom (content/cta.json) na legenda, antes da linha de revenda.
Não mexe na legenda se o cupom estiver desligado ou se ela já tiver o código do cupom.
Uso: from cta import aplicar_cta ; legenda = aplicar_cta(legenda)
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQ = os.path.join(ROOT, "content", "cta.json")

def carregar():
    try:
        return json.load(open(ARQ, encoding="utf-8"))
    except (OSError, ValueError):
        return {"ativo": False}

def aplicar_cta(legenda, cfg=None):
    cfg = cfg if cfg is not None else carregar()
    if not cfg.get("ativo") or not cfg.get("linhas"):
        return legenda
    if cfg.get("cupom") and cfg["cupom"] in legenda:
        return legenda
    bloco = "\n".join(cfg["linhas"])
    linhas = legenda.split("\n")
    # 1º lugar: antes da linha "Quer revender?" (rodapé da CP Comercial)
    for i, l in enumerate(linhas):
        if l.strip().startswith("Quer revender"):
            return "\n".join(linhas[:i] + [bloco, ""] + linhas[i:])
    # 2º: antes do bloco de hashtags (último parágrafo que começa com #)
    pars = legenda.rstrip().split("\n\n")
    if len(pars) > 1 and pars[-1].lstrip().startswith("#"):
        return "\n\n".join(pars[:-1] + [bloco, pars[-1]])
    return legenda.rstrip() + "\n\n" + bloco

if __name__ == "__main__":
    import sys
    print(aplicar_cta(sys.stdin.read()))
