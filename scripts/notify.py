"""Aviso opcional no Telegram. Sem TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID, não faz nada."""
import os, sys, urllib.request, urllib.parse

t, chat = os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
msg = " ".join(sys.argv[1:])
if t and chat and msg:
    data = urllib.parse.urlencode({"chat_id": chat, "text": msg}).encode()
    try:
        urllib.request.urlopen(f"https://api.telegram.org/bot{t}/sendMessage", data=data, timeout=30)
    except Exception as e:
        print("Telegram falhou:", e)
print(msg)
