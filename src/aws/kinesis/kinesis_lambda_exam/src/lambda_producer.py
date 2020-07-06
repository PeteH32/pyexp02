import datetime
import os
import random
import boto3
import json

########################################
# Put a few records

kinesis_client = boto3.client('kinesis')


def put_some_records(stream_name):
    print(f'put_some_records(): Stream name: {stream_name}')
    for i in range(0, 5):
        acctid = random.randint(1, 1000)
        dataObj = {
            'account': str(acctid),
            'message_id': str(i),
            'message': f'For account {acctid}, here is a message with id: {i}.'
        }
        dataStr = json.dumps(dataObj)
        resp = kinesis_client.put_record(
            StreamName=stream_name,
            PartitionKey=str(acctid),
            Data=dataStr)
        print(
            f'    ShardId:{resp["ShardId"]}, SequenceNumber:{resp["SequenceNumber"]}, dataStr:{dataStr}')
    print()


def handler_producer(event, context):
    my_strm = os.environ.get('stream_name', 'peteh01')

    print(f'handler_producer(): Going to do put records into stream: {my_strm}')

    put_some_records(my_strm)

    print(f'================ DONE ==================')
