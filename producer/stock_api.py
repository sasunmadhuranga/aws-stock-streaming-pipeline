import requests
from datetime import datetime
from producer.config import FINNHUB_API_KEY, ALPHAVANTAGE_API_KEY


def get_finnhub(symbol):

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"

    try:
        r = requests.get(url).json()

        return {
            "symbol": symbol,
            "price": r["c"],
            "volume": 0,
            "timestamp": datetime.utcnow().isoformat(),
            "source": "finnhub"
        }

    except:
        return None


def get_alpha(symbol):

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

    try:
        r = requests.get(url).json()
        data = r["Global Quote"]

        return {
            "symbol": symbol,
            "price": float(data["05. price"]),
            "volume": int(data["06. volume"]),
            "timestamp": datetime.utcnow().isoformat(),
            "source": "alphavantage"
        }

    except:
        return None