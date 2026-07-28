from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from strategy import get_signal

# এখানে তোমার BotFather থেকে পাওয়া নতুন Token বসাও
BOT_TOKEN = "AAGP7bMHyjcCHzRsS34uV8VwlHFLzjy6R8g"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Signal Bot চালু হয়েছে!\n\n"
        "কমান্ড:\n"
        "/signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = get_signal("BTCUSDT")

        message = f"""
📊 AI Market Analysis

🪙 Pair: BTCUSDT
💰 Price: {data['price']}
📈 Signal: {data['signal']}
🎯 Confidence: {data['confidence']}%
📉 RSI: {data['rsi']}

⚠️ এটি শুধুমাত্র মার্কেট বিশ্লেষণ।
"""
        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("✅ Bot Started...")
app.run_polling()
