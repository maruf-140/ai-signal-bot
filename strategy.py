from market import get_price

def get_signal():
    price = get_price()

    return {
        "pair": "BTCUSDT",
        "price": price,
        "trend": "Market Data",
        "note": "This is market information, not a guaranteed trading signal."
    }
