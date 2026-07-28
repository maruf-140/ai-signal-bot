import pandas_ta as ta
from market import get_klines

def get_signal(symbol="BTCUSDT"):
    df = get_klines(symbol)

    # Indicators
    df["EMA9"] = ta.ema(df["close"], length=9)
    df["EMA21"] = ta.ema(df["close"], length=21)
    df["RSI"] = ta.rsi(df["close"], length=14)

    macd = ta.macd(df["close"])
    df["MACD"] = macd["MACD_12_26_9"]
    df["SIGNAL"] = macd["MACDs_12_26_9"]

    last = df.iloc[-1]

    signal = "WAIT"
    confidence = 50

    if (
        last["EMA9"] > last["EMA21"]
        and last["MACD"] > last["SIGNAL"]
        and last["RSI"] < 70
    ):
        signal = "BUY"
        confidence = 78

    elif (
        last["EMA9"] < last["EMA21"]
        and last["MACD"] < last["SIGNAL"]
        and last["RSI"] > 30
    ):
        signal = "SELL"
        confidence = 78

    return {
    "signal": signal,
    "confidence": confidence,
    "price": round(last["close"], 2),
    "rsi": round(last["RSI"], 2),
        }
