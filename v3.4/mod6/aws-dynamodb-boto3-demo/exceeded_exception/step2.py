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

# for 文で 100 回 get_item を実行する
# try-except で例外が発生した場合は詳細を出力する
count = 0
try:
    for i in range(100):
        count = i
        table.get_item(
            Key = {
                'ISBN': SEARCH_ISBN
            }
        )
except dynamodb.meta.client.exceptions.ProvisionedThroughputExceededException as e:
    print('--- ProvisionedThroughputExceededException ---', count)
    print(e)

print('Finish! ',count)

