import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHA_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

AWS_REGION = os.getenv("AWS_REGION")
STREAM_NAME = os.getenv("STREAM_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")