from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from strategy import get_signal

load_dotenv()
TOKEN = os.getenv("8862576397:AAF0GsWwt5wNGgjh5INtQpiQs-5k3eFY6OM")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Signal Bot Ready!\n\nUse /signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_signal()

    await update.message.reply_text(
        f"""📊 AI Signal

💰 Price: {data['price']}
📈 Signal: {data['signal']}
🎯 Confidence: {data['confidence']}%
📉 RSI: {data['rsi']}
"""
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
