import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

table_name = 'Movies'
print(table_name)

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(table_name)

# scan + 結果整合性
response = table.scan(
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- scan, ConsistentRead = False ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
print(json.dumps(response['ConsumedCapacity'], indent=2))

# scan + 強力な整合性
response = table.scan(
    ConsistentRead = True,
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- scan, ConsistentRead = True ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
print(json.dumps(response['ConsumedCapacity'], indent=2))




