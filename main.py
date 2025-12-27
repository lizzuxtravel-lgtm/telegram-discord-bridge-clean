import os
import requests
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def telegram_webhook():
    data = request.json

    message = data.get("message", {})
    text = message.get("text", "[non-text]")
    user = message.get("from", {})

    payload = {
        "content": f"📩 **New Telegram Message**\n"
                   f"👤 Name: {user.get('first_name','')}\n"
                   f"🆔 Username: @{user.get('username','no_username')}\n"
                   f"💬 Message: {text}"
    }

    requests.post(DISCORD_WEBHOOK, json=payload)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
