import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

AWS_REGION = os.getenv("AWS_REGION")
STREAM_NAME = os.getenv("STREAM_NAME")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")
BUCKET_NAME = os.getenv("BUCKET_NAME")
ARCHIVE_BUCKET = os.getenv("ARCHIVE_BUCKET")
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")