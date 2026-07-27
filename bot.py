from strategy import get_async def signal(update, context):
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
