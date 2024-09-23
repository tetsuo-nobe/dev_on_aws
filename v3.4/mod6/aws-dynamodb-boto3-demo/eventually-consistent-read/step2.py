import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

table_name = 'profiles'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# デフォルト値 : りんご
response = table.put_item(
    Item = {
        'name': 'nobe',
        'fruits': 'apple'
    }
)

# イチゴに更新した直後に「結果整合性のある読み込み」を30回実行する
table.update_item(
    Key = {
        'name': 'nobe'
    },
    UpdateExpression = 'SET fruits = :fruits',
    ExpressionAttributeValues = {
        ':fruits': 'strawberry'
    }
)

for i in range(100):
        response = table.get_item(
            Key = {
                'name': 'nobe'
            }
        )
        print(response['Item'])