import json
import boto3
import os
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
        key = record["s3"]["object"]["key"]

        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response["Body"].read()

        try:
            data = json.loads(file_content)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON for {key}: {e}")
            continue  # skip to next record

        symbol = data.get("symbol")
        price = data.get("price")

        if not symbol or price is None:
            print(f"Invalid data in {key}: {data}")
            continue

        # anomaly detection
        if detect_anomaly(price):

            sns.publish(
                TopicArn=TOPIC,
                Message=f"Anomaly detected for {symbol} price {price}"
            )

        # store processed data
        table.put_item(Item=data)

        # archive raw data
        s3.put_object(
            Bucket=ARCHIVE_BUCKET,
            Key=f"{symbol}/{data['timestamp']}.json",
            Body=json.dumps(data)
        )