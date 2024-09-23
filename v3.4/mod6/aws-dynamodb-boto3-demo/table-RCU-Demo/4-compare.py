import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

# 同じアイテムをget_item,query,scanで取得した時の消費するRCUの比較

table_name = 'Movies'
print(table_name)

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(table_name)

# 検索する値
YEAR = 1986
TITLE = 'Top Gun'

# get_item + 結果整合性
response = table.get_item(
    Key = {
        'year': YEAR,
        'title': TITLE
    },
    ReturnConsumedCapacity = 'INDEXES'
)
print('---- get_item, ConsistentRead = False ----')
print('Year=',response['Item']['year'],'Title=',response['Item']['title'])
print(json.dumps(response['ConsumedCapacity'], indent=2))

# query + 結果整合性
response = table.query(
    KeyConditionExpression = Key('year').eq(YEAR) & Key('title').eq(TITLE),
    ReturnConsumedCapacity = 'INDEXES',
)

print('---- query, ConsistentRead = False ----')
print('Year=',response['Items'][0]['year'],'Title=',response['Items'][0]['title'])
print(json.dumps(response['ConsumedCapacity'], indent=2))

# scan + 結果整合性
response = table.scan(
    FilterExpression = Key('year').eq(YEAR) & Key('title').eq(TITLE),
    ReturnConsumedCapacity = 'INDEXES'
)

print('---- scan, ConsistentRead = False ----')
print('Year=',response['Items'][0]['year'],'Title=',response['Items'][0]['title'])
print(json.dumps(response['ConsumedCapacity'], indent=2))