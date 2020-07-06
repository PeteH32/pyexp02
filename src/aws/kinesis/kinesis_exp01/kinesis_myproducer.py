import datetime
import random
import boto3
import json

print(f'========================================')

# Helpers

def my_json_convertor(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    else:
        return f"my_json_convertor(): Couldn't deserialize."

########################################
# Put a few records

kinesis_client = boto3.client('kinesis')

def put_stuff(stream_name):
    print(f'Putting stuff:')
    for i in range(0, 5):
        acctid = random.randint(1, 1000)
        dataObj = {
            'account': str(acctid),
            'message_id': str(i),
            'message': f'For account {acctid}, here is a message with id: {i}.'
        }
        dataStr = json.dumps(dataObj)
        resp = kinesis_client.put_record(
            StreamName=stream_name, PartitionKey=str(acctid), Data=dataStr)
        print(
            f'    ShardId:{resp["ShardId"]}, SequenceNumber:{resp["SequenceNumber"]}, dataStr:{dataStr}')
    print()


my_strm = 'Foo2'
print(f'Going to do put stuff on stream: {my_strm}')

put_stuff(my_strm)

print()

################################################################################
print(f'================ DONE ==================')
