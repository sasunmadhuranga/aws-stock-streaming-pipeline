import json
import boto3
import base64
from anomaly_detection import detect_anomaly

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("stock_table")

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET = "stock-raw-data-bucket"
TOPIC = "SNS_TOPIC_ARN"


def lambda_handler(event, context):

    for record in event["Records"]:

        payload = base64.b64decode(record["kinesis"]["data"])
        data = json.loads(payload)

        symbol = data["symbol"]
        price = data["price"]

        if detect_anomaly(price):

            sns.publish(
                TopicArn=TOPIC,
                Message=f"Anomaly detected for {symbol} price {price}"
            )

        table.put_item(Item=data)

        s3.put_object(
            Bucket=BUCKET,
            Key=f"{symbol}/{data['timestamp']}.json",
            Body=json.dumps(data)
        )