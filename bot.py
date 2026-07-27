from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from strategy import get_signal

TOKEN = "AAHmiU0DBoEdgghIZ-Y0q5VFigIlcfB-irE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Signal Bot Ready!\n\n"
        "কমান্ড:\n"
        "/signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_signal("BTCUSDT")

    await update.message.reply_text(
        f"""📊 AI Market Analysis

🪙 Pair: BTCUSDT
💰 Price: {data['price']}
📈 Signal: {data['signal']}
🎯 Confidence: {data['confidence']}%
📉 RSI: {data['rsi']}

⚠️ Analysis only. No signal can guarantee profit."""
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot Started...")
app.run_polling()
