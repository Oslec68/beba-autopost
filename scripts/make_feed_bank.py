# Gera content/feed.json (banco de carrosséis e posts de imagem). Rode de novo após editar.
# Cada item: id, tipo ("carrossel" ou "imagem"), slides (lista) e legenda.
# Tipos de slide: capa, produto, lista, numero, vs, lineup, cta (ver scripts/render_feed.py).
# Regras: só alegações do rótulo; OXXO só em Morango e Tangerina; nunca "Distribuidor Oficial".
import json, os

NOME = {"limao": "Limão", "tangerina": "Tangerina", "morango": "Morango", "pessego": "Pêssego"}
RODAPE = "Quer revender? CP Comercial | WhatsApp (11) 94764-6006"
TAGS = ["#purafibra #zeroaçucar #zerocaloria #fibras #bebawellness",
        "#purafibra #rotinasaudavel #zeroaçucar #bebidafuncional #bebawellness",
        "#purafibra #bemestar #zerocaloria #vidasaudavel #bebawellness"]
CTA = lambda s: {"t": "cta", "sabor": s, "titulo": "Salva e manda pra quem precisa.",
                 "texto": "Pura Fibra: 6 g de fibra, zero açúcar, zero caloria."}

ITENS = [
 ("carrossel", "Qual é o seu sabor? Conta aqui nos comentários 👇", [
   {"t": "capa", "sabor": "pessego", "kicker": "4 SABORES", "h1": "QUAL É", "h2": "O SEU?"},
   {"t": "produto", "sabor": "limao", "titulo": "Limão", "chips": ["Refrescante", "Zero açúcar", "6 g de fibra"]},
   {"t": "produto", "sabor": "tangerina", "titulo": "Tangerina", "chips": ["Cítrico", "Zero caloria", "Tem no OXXO"]},
   {"t": "produto", "sabor": "morango", "titulo": "Morango", "chips": ["Docinho na medida", "Zero açúcar", "Tem no OXXO"]},
   {"t": "produto", "sabor": "pessego", "titulo": "Pêssego", "chips": ["Suave", "Zero caloria", "Complexo B"]},
   {"t": "cta", "sabor": "pessego", "titulo": "Comenta o seu sabor.", "texto": "Limão, tangerina, morango ou pêssego?"}]),
 ("imagem", "4 sabores, zero açúcar. Qual você leva hoje?", [
   {"t": "lineup", "sabor": "limao", "titulo": "4 SABORES. ZERO AÇÚCAR.", "texto": "6 g de fibra em cada garrafa de 400 ml."}]),
 ("carrossel", "Troca o refri sem perder o gelado. Arrasta pro lado 👉", [
   {"t": "capa", "sabor": "tangerina", "kicker": "TROCA INTELIGENTE", "h1": "TROCA", "h2": "O REFRI"},
   {"t": "vs", "sabor": "tangerina", "titulo": "Na hora da sede",
    "esq": ["Refri comum", "Costuma ter açúcar", "Sem fibra"],
    "dir": ["Pura Fibra", "0 g de açúcar", "6 g de fibra", "Complexo B"]},
   {"t": "numero", "sabor": "tangerina", "big": "0 g", "label": "DE AÇÚCAR", "texto": "Sabor de verdade, sem açúcar."},
   {"t": "numero", "sabor": "tangerina", "big": "0", "label": "CALORIA", "texto": "Leve para qualquer hora do dia."},
   {"t": "cta", "sabor": "tangerina", "titulo": "Troca que vale.", "texto": "Gelada, leve e com 6 g de fibra."}]),
 ("imagem", "6 g de fibra em uma garrafa. 🍋", [
   {"t": "numero", "sabor": "limao", "big": "6 g", "label": "DE FIBRA", "texto": "24% do valor diário em uma garrafa de 400 ml."}]),
 ("carrossel", "O que tem dentro de uma Pura Fibra? Arrasta 👉", [
   {"t": "capa", "sabor": "morango", "kicker": "POR DENTRO", "h1": "O QUE TEM", "h2": "NA GARRAFA?"},
   {"t": "numero", "sabor": "morango", "big": "6 g", "label": "DE FIBRA", "texto": "24% do valor diário em cada garrafa."},
   {"t": "lista", "sabor": "morango", "num": "B", "titulo": "Vitaminas do complexo B", "texto": "B3, B5, B6 e B9 na mesma garrafa."},
   {"t": "numero", "sabor": "morango", "big": "0", "label": "AÇÚCAR E CALORIA", "texto": "Zero açúcar, zero caloria."},
   {"t": "numero", "sabor": "morango", "big": "400", "label": "ML", "texto": "Tamanho certo para levar na bolsa."},
   CTA("morango")]),
 ("imagem", "Pêssego: suave, gelado e zero açúcar. 🍑", [
   {"t": "produto", "sabor": "pessego", "titulo": "Pêssego", "chips": ["Zero açúcar", "Zero caloria", "6 g de fibra"]}]),
 ("carrossel", "5 momentos para ter uma Pura Fibra por perto. Qual é o seu? 👇", [
   {"t": "capa", "sabor": "limao", "kicker": "ROTINA", "h1": "5 MOMENTOS", "h2": "PRA LEVAR"},
   {"t": "lista", "sabor": "limao", "num": "1", "titulo": "Antes do treino", "texto": "Hidrata e já soma 6 g de fibra."},
   {"t": "lista", "sabor": "tangerina", "num": "2", "titulo": "Na mesa de trabalho", "texto": "Do lado do notebook, sem açúcar."},
   {"t": "lista", "sabor": "morango", "num": "3", "titulo": "No almoço", "texto": "Troca o refri por algo leve."},
   {"t": "lista", "sabor": "pessego", "num": "4", "titulo": "Na viagem", "texto": "Garrafa de 400 ml cabe na mochila."},
   {"t": "lista", "sabor": "limao", "num": "5", "titulo": "No fim de tarde", "texto": "Gelada, zero caloria."},
   CTA("limao")]),
 ("imagem", "Troca o refri. 🍊", [
   {"t": "capa", "sabor": "tangerina", "kicker": "DICA DO DIA", "h1": "TROCA", "h2": "O REFRI", "sem_seta": True}]),
 ("carrossel", "Pura Fibra no OXXO: Morango e Tangerina te esperando. 📍", [
   {"t": "capa", "sabor": "morango", "kicker": "ONDE ENCONTRAR", "h1": "TÁ NO", "h2": "OXXO"},
   {"t": "produto", "sabor": "morango", "titulo": "Morango", "chips": ["Você encontra no OXXO", "Zero açúcar", "6 g de fibra"]},
   {"t": "produto", "sabor": "tangerina", "titulo": "Tangerina", "chips": ["Você encontra no OXXO", "Zero caloria", "6 g de fibra"]},
   {"t": "cta", "sabor": "tangerina", "titulo": "Passou no OXXO? Leva.", "texto": "Morango e Tangerina na geladeira."}]),
 ("imagem", "Zero caloria, todo o sabor. 🍑", [
   {"t": "numero", "sabor": "pessego", "big": "0", "label": "CALORIA", "texto": "Pêssego gelado, leve de verdade."}]),
 ("carrossel", "Sua semana com sabor: um Pura Fibra para cada dia. 🗓️", [
   {"t": "capa", "sabor": "limao", "kicker": "PLANEJA AÍ", "h1": "SUA SEMANA", "h2": "COM SABOR"},
   {"t": "lista", "sabor": "limao", "num": "SEG", "titulo": "Limão", "texto": "Começa a semana no leve."},
   {"t": "lista", "sabor": "tangerina", "num": "QUA", "titulo": "Tangerina", "texto": "Meio da semana, ritmo mantido."},
   {"t": "lista", "sabor": "morango", "num": "SEX", "titulo": "Morango", "texto": "Sextou sem açúcar."},
   {"t": "lista", "sabor": "pessego", "num": "DOM", "titulo": "Pêssego", "texto": "Domingo gelado e leve."},
   CTA("pessego")]),
 ("imagem", "Morango gelado no OXXO. 🍓", [
   {"t": "produto", "sabor": "morango", "titulo": "Morango", "chips": ["Você encontra no OXXO", "Zero açúcar", "Complexo B"]}]),
 ("carrossel", "Quer revender Pura Fibra? Fala com a CP Comercial. 📲", [
   {"t": "capa", "sabor": "tangerina", "kicker": "PARA LOJISTAS", "h1": "QUER", "h2": "REVENDER?"},
   {"t": "lista", "sabor": "limao", "num": "1", "titulo": "4 sabores no mix", "texto": "Limão, tangerina, morango e pêssego."},
   {"t": "lista", "sabor": "tangerina", "num": "2", "titulo": "Zero açúcar com fibra", "texto": "6 g de fibra e zero caloria."},
   {"t": "lista", "sabor": "morango", "num": "3", "titulo": "Garrafa de 400 ml", "texto": "Prática para geladeira e balcão."},
   {"t": "lista", "sabor": "pessego", "num": "4", "titulo": "Marca já no OXXO", "texto": "O consumidor já encontra na rua."},
   {"t": "cta", "sabor": "tangerina", "titulo": "Chama no WhatsApp.", "texto": "(11) 94764-6006", "revenda": True}]),
 ("imagem", "Pausa com sabor. 🍋", [
   {"t": "lineup", "sabor": "pessego", "titulo": "QUAL VOCÊ LEVA HOJE?", "texto": "Limão, tangerina, morango ou pêssego."}]),
 ("carrossel", "Dica: Pura Fibra fica ainda melhor gelada. 🧊", [
   {"t": "capa", "sabor": "limao", "kicker": "DICA", "h1": "SIRVA", "h2": "GELADA"},
   {"t": "lista", "sabor": "limao", "num": "1", "titulo": "Geladeira", "texto": "Deixa umas garrafas sempre prontas."},
   {"t": "lista", "sabor": "limao", "num": "2", "titulo": "Bolsa térmica", "texto": "Leva gelada para a praia ou o parque."},
   {"t": "lista", "sabor": "limao", "num": "3", "titulo": "Com gelo", "texto": "Copo, gelo e uma rodela de limão."},
   CTA("limao")]),
 ("imagem", "Quer revender? Fala com a CP Comercial. 📲", [
   {"t": "cta", "sabor": "morango", "titulo": "Quer revender Pura Fibra?", "texto": "(11) 94764-6006", "revenda": True}]),
 ("carrossel", "Pura Fibra combina com o quê? Arrasta 👉", [
   {"t": "capa", "sabor": "pessego", "kicker": "COMBINAÇÕES", "h1": "COMBINA", "h2": "COM..."},
   {"t": "produto", "sabor": "limao", "titulo": "Almoço", "chips": ["Limão", "Leve", "Sem açúcar"]},
   {"t": "produto", "sabor": "tangerina", "titulo": "Café da tarde", "chips": ["Tangerina", "Zero caloria", "6 g de fibra"]},
   {"t": "produto", "sabor": "morango", "titulo": "Pós-treino", "chips": ["Morango", "6 g de fibra", "Complexo B"]},
   {"t": "produto", "sabor": "pessego", "titulo": "Noite de série", "chips": ["Pêssego", "Zero açúcar", "Gelado"]},
   CTA("pessego")]),
 ("imagem", "Vitaminas do complexo B na garrafa. 🍊", [
   {"t": "lista", "sabor": "tangerina", "num": "B", "titulo": "Vitaminas do complexo B", "texto": "B3, B5, B6 e B9. Zero açúcar."}]),
]

out = []
for i, (tipo, gancho, slides) in enumerate(ITENS, 1):
    sabores = [s["sabor"] for s in slides]
    oxxo = any("OXXO" in json.dumps(s, ensure_ascii=False) for s in slides)
    cap = f"{gancho}\n\nPura Fibra: 6 g de fibra, zero açúcar, zero caloria e vitaminas do complexo B.\n"
    if oxxo:
        cap += "📍 Morango e Tangerina você encontra no OXXO.\n"
    cap += f"\n{RODAPE}\n\n{TAGS[i % 3]}"
    pref = "fc" if tipo == "carrossel" else "fi"
    out.append(dict(id=f"{pref}{i:03d}_{sabores[0]}", tipo=tipo, slides=slides, legenda=cap))

p = os.path.join(os.path.dirname(__file__), "..", "content", "feed.json")
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "itens:", sum(x["tipo"] == "carrossel" for x in out), "carrosséis,",
      sum(x["tipo"] == "imagem" for x in out), "imagens")
