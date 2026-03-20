import time
import time
from producer.stock_api import get_finnhub, get_alpha
from producer.s3_producer import send_to_s3

stocks = ["AAPL", "TSLA", "AMZN", "GOOGL"]

def run_producer():
    while True:  # run continuously
        for symbol in stocks:

            data = get_finnhub(symbol)

            if not data:
                print("Finnhub failed → switching to AlphaVantage")
                data = get_alpha(symbol)

            if data:
                send_to_s3(data)
                print("Uploaded:", data)

            time.sleep(20)



