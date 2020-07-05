# Example from:

- https://www.arundhaj.com/blog/getting-started-kinesis-python.html


## First create a Kinesis stream using the following aws-cli command

- `aws kinesis create-stream --stream-name python-stream --shard-count 1`


## kinesis_producer.py

```
import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'python-stream'

kinesis_client = boto3.client('kinesis')

def put_to_stream(thing_id, property_value, property_timestamp):
    payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'thing_id': thing_id
              }

    print(payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=thing_id)

while True:
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    thing_id = 'aa-bb'

    put_to_stream(thing_id, property_value, property_timestamp)

    # wait for 5 second
    time.sleep(5)

```

## kinesis_consumer.py

```
import boto3
import json
from datetime import datetime
import time

my_stream_name = 'python-stream'

kinesis_client = boto3.client('kinesis')

response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=2)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=2)

    print(record_response)

    # wait for 5 seconds
    time.sleep(5)

```
