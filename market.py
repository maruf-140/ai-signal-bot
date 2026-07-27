import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"

def get_klines(symbol="BTCUSDT", interval="1m", limit=200):
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": limit
    }

    r = requests.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()

    data = r.json()

    df = pd.DataFrame(data, columns=[
        "open_time","open","high","low","close","volume",
        "close_time","quote_asset_volume","trades",
        "taker_buy_base","taker_buy_quote","ignore"
    ])

    df["close"] = df["close"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["open"] = df["open"].astype(float)

    return df
