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
RANK  = 3395

# query + 結果整合性
response = table.query(
    KeyConditionExpression = Key('year').eq(YEAR),
    ReturnConsumedCapacity = 'INDEXES',
)

print('---- query, ConsistentRead = False ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
print('※アイテムを10件表示')
for i, item in enumerate(response['Items']):
    print(item['title'])
    if i == 9:
        break
print(json.dumps(response['ConsumedCapacity'], indent=2))

# query + 強力な整合性
response = table.query(
    KeyConditionExpression = Key('year').eq(YEAR),
    ConsistentRead = True,
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- query, ConsistentRead = True ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
print('※アイテムを10件表示')
for i, item in enumerate(response['Items']):
    print(item['title'])
    if i == 9:
        break
print(json.dumps(response['ConsumedCapacity'], indent=2))

# query + filter + 結果整合性
response = table.query(
    KeyConditionExpression = Key('year').eq(YEAR),
    FilterExpression = Attr('info.rating').gt(8),
    ReturnConsumedCapacity = 'INDEXES',
)

print('---- query + filter ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
for i, item in enumerate(response['Items']):
    print(item['title'])
print(json.dumps(response['ConsumedCapacity'], indent=2))

# query (GSI) + 結果整合性
response = table.query(
    IndexName = 'title-index',
    KeyConditionExpression = Key('title').eq(TITLE),
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- query(GSI) ----')
print('Count : ' + json.dumps(response['Count'], indent=2))
print('※アイテムを10件表示')
for i, item in enumerate(response['Items']):
    print(item['title'])
    if i == 9:
        break
print(json.dumps(response['ConsumedCapacity'], indent=2))