import requests

def get_signal(symbol="BTCUSDT"):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        price = float(r.json()["price"])

        return {
            "price": round(price, 2),
            "signal": "BUY" if int(price) % 2 == 0 else "SELL",
            "confidence": 75,
            "rsi": "N/A"
        }

    except Exception:
        return {
            "price": "N/A",
            "signal": "NO SIGNAL",
            "confidence": 0,
            "rsi": "N/A"
        }
