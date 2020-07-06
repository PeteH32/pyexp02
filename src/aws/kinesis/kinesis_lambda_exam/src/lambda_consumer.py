import base64
import datetime
import os
import random
import boto3
import json

########################################
def handler_consumer(event, context):
    print(f'handler_consumer(): Processing event: {event}')
    records = event["Records"]
    print(f'handler_consumer(): Number of records: {len(records)}')
    for record in records:
        data = record["kinesis"]["data"]
        payload = base64.b64decode(data)
        print(f"    Record: {payload}")

    print(f'================ DONE ==================')
