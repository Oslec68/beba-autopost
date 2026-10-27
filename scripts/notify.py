"""Avisos opcionais por WhatsApp (Whapi) e/ou Telegram.
WhatsApp: secrets WHAPI_TOKEN e WHATSAPP_TO (DDI+DDD+número, ex.: 5511999998888).
Telegram: secrets TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID.
Sem os secrets de um canal, aquele canal é ignorado. Nunca derruba o workflow."""
import json, os, sys, urllib.request, urllib.parse

msg = " ".join(sys.argv[1:])

# WhatsApp via Whapi
w_tok, w_to = os.getenv("WHAPI_TOKEN"), os.getenv("WHATSAPP_TO")
if w_tok and w_to and msg:
    req = urllib.request.Request(
        "https://gate.whapi.cloud/messages/text",
        data=json.dumps({"to": w_to.strip(), "body": msg}).encode(),
        headers={"Authorization": f"Bearer {w_tok.strip()}", "Content-Type": "application/json",
                 "Accept": "application/json"},
        method="POST")
    try:
        urllib.request.urlopen(req, timeout=30)
        print("WhatsApp enviado")
    except Exception as e:
        print("WhatsApp falhou:", e)

# Telegram
t, chat = os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
if t and chat and msg:
    data = urllib.parse.urlencode({"chat_id": chat, "text": msg}).encode()
    try:
        urllib.request.urlopen(f"https://api.telegram.org/bot{t}/sendMessage", data=data, timeout=30)
    except Exception as e:
        print("Telegram falhou:", e)

print(msg)
