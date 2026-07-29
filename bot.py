from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN
from strategy import get_signal

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Market Bot\n\nUse /signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_signal()

    msg = (
        f"📊 Pair: {data['pair']}\n"
        f"💰 Price: {data['price']}\n"
        f"📈 Trend: {data['trend']}\n\n"
        f"ℹ️ {data['note']}"
    )

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot Running...")
app.run_polling()
