import json
import boto3
import urllib.parse
import os
import copy
from decimal import Decimal
from anomaly_detection import detect_anomaly

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

s3 = boto3.client("s3")
sns = boto3.client("sns")

ARCHIVE_BUCKET = os.getenv("ARCHIVE_BUCKET")
TOPIC = os.getenv("SNS_TOPIC_ARN")


def lambda_handler(event, context):

    for record in event["Records"]:

        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

        print("Processing file:", key)

        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read()

        try:
            data = json.loads(file_content)
        except json.JSONDecodeError as e:
            print("JSON decode failed:", e)
            continue

        print("Data:", data)

        symbol = data.get("symbol")
        price = data.get("price")

        data["price"] = Decimal(str(price))

        if not symbol or price is None:
            print("Invalid data:", data)
            continue

        if detect_anomaly(price):
            sns.publish(
                TopicArn=TOPIC,
                Message=f"Anomaly detected for {symbol} price {price}"
            )

        print("Writing to DynamoDB:", data)

        table.put_item(Item=data)

        archive_data = copy.deepcopy(data)
        archive_data["price"] = float(archive_data["price"])

        s3.put_object(
            Bucket=ARCHIVE_BUCKET,
            Key=f"{symbol}/{data['timestamp']}.json",
            Body=json.dumps(archive_data)
        )