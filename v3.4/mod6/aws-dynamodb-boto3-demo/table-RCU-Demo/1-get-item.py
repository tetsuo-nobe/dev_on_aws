import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

table_name = 'Movies'
print(table_name)

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(table_name)


# 検索する値
YEAR = 1985
TITLE = 'Mask'

# get_item + 結果整合性
response = table.get_item(
    Key = {
        'year': YEAR,
        'title': TITLE
    },
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- get_item, ConsistentRead = False ----')
print(response['Item'])
print(json.dumps(response['ConsumedCapacity'], indent=2))

# get_item + 強力な整合性
response = table.get_item(
    Key = {
        'year': YEAR,
        'title': TITLE
    },
    ConsistentRead = True,
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- get_item, ConsistentRead = True ----')
print(response['Item'])
print(json.dumps(response['ConsumedCapacity'], indent=2))


