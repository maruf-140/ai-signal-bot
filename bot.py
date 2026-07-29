import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from strategy import get_signal

# Load .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise Exception("BOT_TOKEN not found in .env")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Signal Bot Started!\n\n"
        "Commands:\n"
        "/signal - Get BTCUSDT Signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = get_signal()

        text = (
            f"📊 AI Signal\n\n"
            f"💰 Pair: BTCUSDT\n"
            f"💵 Price: {data['price']}\n"
            f"📈 Signal: {data['signal']}\n"
            f"🎯 Confidence: {data['confidence']}%\n"
            f"📉 RSI: {data['rsi']}"
        )

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
