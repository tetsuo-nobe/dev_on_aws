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

# バナナに更新した直後に「強力な整合性のある読み込み」を30回実行する
table.update_item(
    Key = {
        'name': 'nobe'
    },
    UpdateExpression = 'SET fruits = :fruits',
    ExpressionAttributeValues = {
        ':fruits': 'banana'
    }
)

for i in range(30):
        response = table.get_item(
            Key = {
                'name': 'nobe'
            },
            ConsistentRead = True
        )
        print(response['Item'])
