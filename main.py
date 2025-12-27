import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import requests

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

async def forward_to_discord(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text
        username = update.message.from_user.username or update.message.from_user.first_name

        payload = {
            "content": f"📩 **Telegram Message**\n👤 {username}\n💬 {text}"
        }

        requests.post(DISCORD_WEBHOOK, json=payload)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_discord))
    app.run_polling()

if __name__ == "__main__":
    main()
