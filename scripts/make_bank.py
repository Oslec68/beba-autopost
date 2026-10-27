# Gera content/posts.json (banco de conteúdo). Rode de novo após editar a lista.
import json, os

# sabor, tag, h1, h2, l2a, l2b, fim, gancho_da_legenda
P = [
 ("limao","SEG","SEGUNDA","DE NOVO?","Começa a semana","no leve.","Semana nova, hábito novo.","Segunda de novo? 🍋"),
 ("tangerina","10:00","REUNIÃO","LONGA?","Leva junto","na bolsa.","Fibra que cabe na rotina.","Reunião longa? Leva junto. 🍊"),
 ("morango","06:30","TREINO","CEDO?","Água com fibra","antes de sair.","Seu treino começa aqui.","Treino cedo? 🍓"),
 ("pessego","12:00","ALMOÇO","NA RUA?","Troca o refri","por Pura Fibra.","Almoço mais leve.","Almoço na rua? Troca o refri. 🍑"),
 ("limao","LIMÃO","0 G DE","AÇÚCAR","Sabor de limão","e zero açúcar.","Refresca sem pesar.","Zero grama de açúcar. 🍋"),
 ("tangerina","DICA","6 G DE","FIBRA","Em uma garrafa","de 400 ml.","Praticidade na mão.","6 g de fibra em uma garrafa. 🍊"),
 ("morango","18:00","SAIU DO","TRABALHO?","Bora pro treino","com fibra.","Seu fim de tarde ativo.","Saiu do trabalho? Bora! 🍓"),
 ("pessego","DOM","DOMINGO","EM CASA?","Gelada, leve","e sem açúcar.","Domingo com sabor.","Domingo em casa? 🍑"),
 ("limao","CALOR","SOL","FORTE?","Gelada fica","ainda melhor.","Hidratação com sabor.","Sol forte pede algo gelado. 🍋"),
 ("tangerina","16:00","FOME DE","LANCHE?","Uma garrafa","e segue o dia.","Lanche da tarde leve.","Bateu a fome do meio da tarde? 🍊"),
 ("morango","TER","TREINO","DE PERNA?","Hidrata e soma","6 g de fibra.","Pós-treino completo.","Dia de perna? 🍓"),
 ("pessego","21:00","SÉRIE À","NOITE?","Troca o refri","da maratona.","Sua noite sem açúcar.","Maratona de série hoje? 🍑"),
 ("limao","08:00","NO","CARRO?","Garrafa de","400 ml na mão.","Leva para onde for.","Indo de carro? Leva junto. 🍋"),
 ("tangerina","QUA","MEIO DA","SEMANA","Mantém o ritmo","com fibra.","Quarta mais leve.","Meio da semana, ritmo mantido. 🍊"),
 ("morango","CORRIDA","5 KM","HOJE?","Na volta,","Pura Fibra.","Corrida com recompensa.","5 km hoje? 🍓"),
 ("pessego","14:00","SONO PÓS","ALMOÇO?","Algo leve","e saboroso.","Tarde sem peso.","Aquele sono pós-almoço? 🍑"),
 ("limao","ZERO","ZERO","CALORIA","Sabor limão","sem culpa.","Leve de verdade.","Zero caloria, todo o sabor. 🍋"),
 ("tangerina","17:00","TRÂNSITO","PARADO?","Uma garrafa","e paciência.","Fim de tarde mais leve.","Trânsito parado? 🍊"),
 ("morango","SEX","SEXTOU","NO LEVE","Morango gelado","zero açúcar.","Sexta com sabor.","Sextou no leve. 🍓"),
 ("pessego","VIAGEM","PÉ NA","ESTRADA?","Leva na","mochila.","Viagem com fibra.","Pé na estrada? 🍑"),
 ("limao","PAUSA","PAUSA","NO ESTUDO","Uma pausa com","sabor de limão.","Estudo com sabor.","Pausa no estudo? 🍋"),
 ("tangerina","QUI","QUINTA","CORRIDA?","6 g de fibra","em cada garrafa.","Quinta mais leve.","Quinta corrida? 🍊"),
 ("morango","ACADEMIA","BOLSA DA","ACADEMIA","Tem espaço","pra fibra?","Treino completo.","O que vai na sua bolsa da academia? 🍓"),
 ("pessego","19:30","JANTAR","LEVE?","Combina com","Pura Fibra.","Noite mais leve.","Jantar leve hoje? 🍑"),
 ("limao","HOME","HOME","OFFICE?","Do lado do","notebook.","Trabalho com sabor.","Home office hoje? 🍋"),
 ("tangerina","SÁB","FEIRA DE","SÁBADO","Volta pra casa","com fibra.","Sábado mais leve.","Feira de sábado? 🍊"),
 ("morango","YOGA","AULA DE","YOGA?","Depois da aula,","Pura Fibra.","Rotina leve.","Saiu da aula de yoga? 🍓"),
 ("pessego","4 SABORES","QUAL É","O SEU?","Limão, tangerina,","morango, pêssego.","Pêssego é o meu.","Qual é o seu sabor? Conta aqui. 🍑"),
 ("limao","REFRI?","TROCA","O REFRI","Mesmo gelado,","zero açúcar.","Troca que vale.","Troca o refri. 🍋"),
 ("tangerina","24%","24% DA","FIBRA","do dia em","uma garrafa.","Fácil assim.","24% da fibra do dia em uma garrafa. 🍊"),
 ("morango","VITAMINAS","COMPLEXO","B","B3, B5, B6 e B9","na garrafa.","Vitaminas na rotina.","Vitaminas do complexo B na garrafa. 🍓"),
 ("pessego","PRAIA","DIA DE","PRAIA?","Gelada na","bolsa térmica.","Verão com sabor.","Dia de praia? 🍑"),
 ("limao","09:00","PAUSA","DO CAFÉ","Troca por","algo gelado.","Pausa refrescante.","Pausa do café? Troca por algo gelado. 🍋"),
 ("tangerina","PASSEIO","PASSEIO","COM O DOG?","Hidrata você","no caminho.","Passeio mais leve.","Passeio com o dog? 🍊"),
 ("morango","BIKE","PEDAL DE","DOMINGO?","Garrafa no","suporte.","Pedal com fibra.","Pedal de domingo? 🍓"),
 ("pessego","15:30","CAFÉ DA","TARDE?","Troca o doce","por Pura Fibra.","Tarde sem açúcar.","Café da tarde sem açúcar. 🍑"),
 ("limao","ROTINA","BEBER","ÁGUA?","Com sabor","fica mais fácil.","Hidratação com sabor.","Difícil beber água? 🍋"),
 ("tangerina","OXXO","PASSOU","NO OXXO?","Tem Pura Fibra","tangerina.","Achou, levou.","Passou no OXXO? 🍊"),
 ("morango","OXXO","TÁ NO","OXXO","Morango gelado","te esperando.","580 lojas em SP.","Tá no OXXO. 🍓"),
 ("pessego","FÉRIAS","MODO","FÉRIAS","Leve, gelado","e zero açúcar.","Férias com sabor.","Modo férias. 🍑"),
 ("limao","DOM","DOMINGO","DE SOL","Limão gelado","combina.","Domingo leve.","Domingo de sol. 🍋"),
 ("tangerina","NOITE","SEDE","À NOITE?","Zero açúcar,","zero caloria.","Noite mais leve.","Sede à noite? 🍊"),
]
NOME = {"limao":"Limão","tangerina":"Tangerina","morango":"Morango","pessego":"Pêssego"}
OXXO = {"tangerina","morango"}
TAGS = ["#purafibra #zeroaçucar #zerocaloria #fibras #bebawellness",
        "#purafibra #rotinasaudavel #zeroaçucar #hidratacao #bebawellness",
        "#purafibra #bemestar #zerocaloria #fibras #bebawellness",
        "#purafibra #vidasaudavel #zeroaçucar #bebidafuncional #bebawellness"]
out = []
for i, (s, tag, h1, h2, a, b, fim, hook) in enumerate(P, 1):
    cap = f"{hook}\n\nPura Fibra {NOME[s]}: 6 g de fibra, zero açúcar, zero caloria e vitaminas do complexo B.\n{fim}\n"
    if s in OXXO:
        cap += "📍 Você encontra no OXXO.\n"
    cap += f"\nQuer revender? CP Comercial | WhatsApp (11) 94764-6006\n\n{TAGS[i % 4]}"
    out.append(dict(id=f"pf{i:03d}_{s}", sabor=s, tag=tag, h1=h1, h2=h2, l2a=a, l2b=b, fim=fim, oxxo=s in OXXO, legenda=cap))
p = os.path.join(os.path.dirname(__file__), "..", "content", "posts.json")
json.dump(out, open(p, "w"), ensure_ascii=False, indent=1)
print(len(out), "posts")
