import requests

def get_signal(symbol="BTCUSDT"):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        price = float(response.json()["price"])

        signal = "BUY" if int(price) % 2 == 0 else "SELL"

        return {
            "price": round(price, 2),
            "signal": signal,
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
