import datetime
import random
import boto3
import json

print(f'========================================')

# Helpers


def my_json_convertor(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


################################################################################
# S3
s3_resource = boto3.resource('s3')
for bucket in s3_resource.buckets.all():
    print(f'Bucket: {bucket.name}\n    {bucket}')


print(f'====================\n')
################################################################################
# Kinesis

########################################
# Describe a stream


def describe_stream(stream_name):
    resp = kinesis_client.describe_stream(StreamName=stream_name)
    num_shards = len(resp["StreamDescription"]["Shards"])
    print(
        f'{stream_name}: num_shards={num_shards}, arn={resp["StreamDescription"]["StreamARN"]}')
    for shard in resp["StreamDescription"]["Shards"]:
        print(f'    ShardId: {shard["ShardId"]}')
        print(
            f'      HashKeyRange.StartingHashKey: {shard["HashKeyRange"]["StartingHashKey"]}')
        print(
            f'      HashKeyRange.EndingHashKey: {shard["HashKeyRange"]["EndingHashKey"]}')
        print(
            f'      SequenceNumberRange.StartingSequenceNumber: {shard["SequenceNumberRange"]["StartingSequenceNumber"]}')
    print()


# List streams
kinesis_client = boto3.client('kinesis')
response = kinesis_client.list_streams()
my_stream_names = response["StreamNames"]
print(f'Number of streams: {len(my_stream_names)} ')
for stream_name in my_stream_names:
    resp = kinesis_client.describe_stream(StreamName=stream_name)
    describe_stream(stream_name)
print()

########################################
# Put/Get records

# For producer/consumer (put/get), see my examples here:
#   src/aws/kinesis/kinesis_exp01
#   src/aws/kinesis/kinesis_example_01

################################################################################
print(f'================ DONE ==================')
