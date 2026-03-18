import boto3
import json
from producer.config import AWS_REGION, BUCKET_NAME

s3 = boto3.client("s3", region_name=AWS_REGION)

def send_to_s3(data):

    key = f"incoming/{data['symbol']}_{data['timestamp']}.json"
    print("BUCKET_NAME:", BUCKET_NAME, type(BUCKET_NAME))
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(data)
    )

    return True