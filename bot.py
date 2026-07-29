import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from strategy import get_signal

load_dotenv()

BOT_TOKEN = os.getenv("AAGP7bMHyjcCHzRsS34uV8VwlHFLzjy6R8g")

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN not found! Create a .env file.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Market Bot চালু হয়েছে!\n\n"
        "কমান্ড:\n"
        "/signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = get_signal()

        message = f"""
📊 AI Market Analysis

💰 Pair: BTCUSDT
💲 Price: {data['price']}
📈 Signal: {data['signal']}
🎯 Confidence: {data['confidence']}%
📉 RSI: {data['rsi']}

⚠️ এটি শুধুমাত্র শিক্ষামূলক বিশ্লেষণ।
"""

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"❌ Error:\n{e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("✅ Bot Started...")

    app.run_polling()

if __name__ == "__main__":
    main()
