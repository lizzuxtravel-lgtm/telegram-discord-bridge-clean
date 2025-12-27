import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text if update.message.text else "[Non-text message]"

    payload = {
        "content": f"📩 **New Telegram Message**\n"
                   f"👤 Name: {user.full_name}\n"
                   f"🆔 Username: @{user.username}\n"
                   f"💬 Message: {text}"
    }

    requests.post(DISCORD_WEBHOOK, json=payload)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    print("Bot is running...")
    app.run_polling()
