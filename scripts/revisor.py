"""Revisor automático (ideia do "Agente Revisor" do timesmkt3, sem custo e sem chave de API).

Duas checagens:
1. Texto do post, ANTES de renderizar (revisar_post): regras de rótulo, OXXO, rodapé, tamanhos.
   Post reprovado é pulado e o próximo da fila sai no lugar; o aviso diz qual foi barrado e por quê.
2. Vídeo, DEPOIS de renderizar (python scripts/revisor.py --video out/<id>.mp4 site/<id>.jpg):
   duração, áudio e capa não vazia. Se reprovar, o workflow falha ANTES de publicar e chega o aviso de falha.

Uso manual: python scripts/revisor.py            -> revisa o banco inteiro (posts.json)
            python scripts/revisor.py --video out/x.mp4 site/x.jpg
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RODAPE = "CP Comercial | WhatsApp (11) 94764-6006"
SABORES_OXXO = {"morango", "tangerina"}
PROIBIDAS = ["distribuidor oficial", "emagrece", "emagrecer", "cura ", "detox", "queima gordura",
             "remédio", "medicamento", "milagre", "garantido"]
# Únicas alegações numéricas permitidas (rótulo): 6 g de fibra, 0 g de açúcar, 24% do VD, 400 ml, B3/B5/B6/B9.
NUM_OK = {"6 g", "0 g", "24%", "400 ml", "6g", "0g", "400ml"}
LIMITES = dict(tag=12, h1=12, h2=14, l2a=20, l2b=20, fim=30)

def revisar_post(p):
    """Devolve a lista de problemas (vazia = aprovado)."""
    erros = []
    texto = " ".join(str(p.get(k, "")) for k in ("tag", "h1", "h2", "l2a", "l2b", "fim", "legenda"))
    baixo = texto.lower()
    for w in PROIBIDAS:
        if w in baixo:
            erros.append(f"palavra proibida: '{w.strip()}'")
    for n in re.findall(r"\d+\s?(?:g|%|ml|kcal|cal)(?![a-zà-ú])", baixo):
        if n not in NUM_OK:
            erros.append(f"número fora do rótulo: '{n}'")
    tem_oxxo = "oxxo" in baixo or bool(p.get("oxxo"))
    if tem_oxxo and p.get("sabor") not in SABORES_OXXO:
        erros.append(f"OXXO citado para {p.get('sabor')} (só Morango e Tangerina)")
    if bool(p.get("oxxo")) != ("oxxo" in p.get("legenda", "").lower()):
        erros.append("campo oxxo e legenda não batem")
    if RODAPE not in p.get("legenda", ""):
        erros.append("legenda sem o rodapé da CP Comercial")
    for k, lim in LIMITES.items():
        if len(str(p.get(k, ""))) > lim:
            erros.append(f"{k} longo demais ({len(p[k])} > {lim} letras, a fonte fica pequena)")
    leg = p.get("legenda", "")
    if len(leg) > 2200:
        erros.append("legenda acima de 2.200 caracteres (limite do Instagram)")
    if len(re.findall(r"#\w+", leg)) > 30:
        erros.append("mais de 30 hashtags (limite do Instagram)")
    return erros

def revisar_video(mp4, capa=None):
    erros = []
    info = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type",
         "-of", "json", mp4], capture_output=True, text=True, check=True).stdout)
    dur = float(info["format"]["duration"])
    tipos = {s["codec_type"] for s in info.get("streams", [])}
    if not 10 <= dur <= 20:
        erros.append(f"duração estranha: {dur:.1f} s")
    if "audio" not in tipos:
        erros.append("vídeo sem áudio")
    if "video" not in tipos:
        erros.append("arquivo sem imagem")
    if capa and os.path.exists(capa):
        # capa "vazia" = quase sem variação de cor (só o fundo, sem título nem garrafa)
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", capa, "-vf", "scale=90:160,format=gray",
                              "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
        px = list(raw)
        media = sum(px) / len(px)
        desvio = (sum((x - media) ** 2 for x in px) / len(px)) ** 0.5
        if desvio < 12:
            erros.append(f"capa parece vazia (variação {desvio:.1f})")
    return erros

if __name__ == "__main__":
    if "--video" in sys.argv:
        i = sys.argv.index("--video")
        mp4 = sys.argv[i + 1]
        capa = sys.argv[i + 2] if len(sys.argv) > i + 2 else None
        e = revisar_video(mp4, capa)
        if e:
            sys.exit("REVISOR REPROVOU O VÍDEO: " + "; ".join(e))
        print("Revisor: vídeo aprovado")
    else:
        posts = json.load(open(os.path.join(ROOT, "content", "posts.json"), encoding="utf-8"))
        ruins = 0
        for p in posts:
            e = revisar_post(p)
            if e:
                ruins += 1
                print(f"✗ {p['id']}: " + "; ".join(e))
        print(f"Revisor: {len(posts) - ruins} aprovados, {ruins} reprovados de {len(posts)}")
        sys.exit(1 if ruins else 0)
