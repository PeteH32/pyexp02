import datetime
from time import sleep, time
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
# Watch stream and get records


kinesis_client = boto3.client('kinesis')


def keep_getting_records(stream_name, shard_id, limit):
    print(
        f"keep_getting_records(): Getting all records from stream: {stream_name} shardId={shard_id}, limit={limit}")
    all_records = []
    resp = kinesis_client.get_shard_iterator(
        StreamName=stream_name, ShardId=shard_id, ShardIteratorType="LATEST")
    shard_itr = resp["ShardIterator"]
    while shard_itr:
        resp = kinesis_client.get_records(ShardIterator=shard_itr, Limit=limit)
        records = resp["Records"]
        print(
            f"keep_getting_records(): Number records from get_records()={len(records)}")
        if (len(records) > 0):
            print(records)
        all_records.append(records)

        # Get next shard iterator
        shard_itr = resp["NextShardIterator"]

        # Sleep a bit
        time, sleep(2)

    print(f"    keep_getting_records(): Total records={len(all_records)}")


my_strm = 'Foo2'
print(f'Going to do get stuff on stream: {my_strm}')

print(f'Getting stuff:')
keep_getting_records(my_strm, "shardId-000000000000", 2)
print()

################################################################################
print(f'================ DONE ==================')
