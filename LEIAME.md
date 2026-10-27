# beba-autopost — 3 Reels por dia no @beba.wellness, grátis

O GitHub gera o vídeo, publica no Instagram pela API oficial e guarda o histórico. Não precisa de PC ligado nem de Metricool.

## Como funciona
1. Às **09:10, 13:10 e 19:10** (horário de Brasília), o GitHub Actions pega o próximo post de `content/posts.json`.
2. Ele renderiza o vídeo de 15 s com HyperFrames (template em `template/`) e uma música gerada na hora, diferente para cada post.
3. O vídeo vai para um link público temporário (GitHub Pages) e é publicado como Reel pela API do Instagram.
4. O post entra em `state/posted.json` e chega um aviso no Telegram (opcional).
5. Toda segunda-feira o token do Instagram é renovado sozinho.

Custo: **R$ 0**. Em repositório público, o GitHub Actions é gratuito e sem limite de minutos. O banco tem 42 posts, que dão 14 dias a 3 por dia.

## Instalação (uma vez só, uns 20 minutos)

### 1. Repositório
1. Em github.com, clique em **New repository** e use o nome `beba-autopost`, como **Public**. O GitHub Pages grátis exige repositório público. Os tokens ficam em Secrets e não aparecem para ninguém.
2. Clique em **Add file → Upload files** e arraste **todo o conteúdo** desta pasta, incluindo a pasta `.github`.
3. Vá em **Settings → Pages → Build and deployment → Source: GitHub Actions**.

### 2. Token do Instagram (Meta)
1. Entre em **developers.facebook.com → Meus apps → Criar app** e escolha o tipo **Outro → Empresa**.
2. No app, adicione o produto **Instagram** e escolha **"Configuração da API com login do Instagram"**.
3. Em **"Gerar tokens de acesso"**, clique em **Adicionar conta** e entre com a **@beba.wellness**.
4. Autorize as permissões **instagram_business_basic** e **instagram_business_content_publish**.
5. Clique em **Gerar token** e copie o token.
   Normalmente não é preciso revisão da Meta para publicar na sua própria conta (como administrador ou testador do app).

### 3. Secrets do GitHub
Vá em **Settings → Secrets and variables → Actions → New repository secret**:
| Nome | Valor |
|---|---|
| `IG_TOKEN` | o token do passo 2 |
| `GH_PAT` | token do GitHub (Settings → Developer settings → Fine-grained tokens) com acesso só a este repositório e permissão **Secrets: Read and write**. Serve para renovar o IG_TOKEN sozinho |
| `TELEGRAM_BOT_TOKEN` | (opcional) o mesmo bot do Radar Saudável |
| `TELEGRAM_CHAT_ID` | (opcional) o seu chat |

### 4. Teste
1. Vá em **Actions → Publicar Reel @beba.wellness → Run workflow**, com **teste = true**. O vídeo é renderizado e publicado no link, mas não vai para o Instagram.
2. Se der certo, rode de novo com **teste = false**. O primeiro Reel sai na hora.
3. **Ligar o automático:** vá em Settings → Secrets and variables → Actions → aba **Variables** → **New repository variable**, com nome `AUTOPOST_ATIVO` e valor `sim`. A partir daí, os 3 horários rodam sozinhos. Para pausar, troque o valor para `nao`.

## Uso no dia a dia
- **Mais conteúdo:** edite a lista em `scripts/make_bank.py`, rode `python scripts/make_bank.py` e suba o `content/posts.json`.
- **Banco esgotado:** o sistema volta a publicar a partir do post mais antigo e avisa.
- **Pausar:** em Actions → Publicar Reel, clique em **⋯ → Disable workflow**.
- **Publicar um post específico:** use Run workflow com `post_id` preenchido (ex.: `pf028_pessego`).

## Regras de conteúdo (já aplicadas no banco)
- As alegações usadas são as do rótulo: 6 g de fibra (24% do VD), zero açúcar, zero caloria, vitaminas do complexo B, 400 ml.
- "Você encontra no OXXO" aparece só em **Morango e Tangerina**.
- Nunca aparece "Distribuidor Oficial". O rodapé é sempre "CP Comercial | WhatsApp (11) 94764-6006".
