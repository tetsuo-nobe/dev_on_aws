import boto3
import pprint

# RCU = 1のテーブル
table_name = 'books-rcu-1'
print(table_name)

# リソースクライアントを作成する
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# 検索する ISBN 値
SEARCH_ISBN = '123456789-0'

# get_item で 1 item を取得する
response = table.get_item(
    Key = {
        'ISBN': SEARCH_ISBN
    }
)
print(response['Item'])

