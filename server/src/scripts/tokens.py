from requests import get
from uuid import uuid4
from datetime import datetime
from shutil import copyfileobj
from boto3 import client

from config import process

s3 = client('s3',
    aws_access_key_id=process.env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=process.env.AWS_SECRET_ACCESS_KEY,
    region_name=process.env.AWS_REGION_NAME
)

def nft():
    for i in range(1000000):
        text = get('https://api.smartpro.cloud/wp-admin').text
        tid = str(uuid4())
        ts = str(datetime.now().timestamp())
        key = f'nft/{i}_{tid}_{ts}.svg'
        print(s3.put_object(
            Bucket=process.env.AWS_BUCKET_NAME,
            Key=key,
            Body=text.encode('utf-8')
        ))

nft()