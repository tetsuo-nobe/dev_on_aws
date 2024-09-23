import boto3
import pprint

# RCU = 1のテーブル
table_name = 'books-rcu-1'
print(table_name)

# Config クラスで再試行回数の設定を上書きする : 0回
from botocore.config import Config

config = Config(
    retries=dict(
        max_attempts=0
    )
)

# リソースクライアントを作成する（再試行回数なし）
dynamodb_no_retry = boto3.resource('dynamodb', config=config)
table_no_retry = dynamodb_no_retry.Table(table_name)

# 検索する ISBN 値
SEARCH_ISBN = '123456789-0'

# for 文で 100 回 get_item を実行する
# try-except で例外が発生した場合は詳細を出力する
count = 0
try:
    for i in range(100):
        count = i
        table_no_retry.get_item(
            Key = {
                'ISBN': SEARCH_ISBN
            }
        )
except dynamodb_no_retry.meta.client.exceptions.ProvisionedThroughputExceededException as e: 
    print('--- ProvisionedThroughputExceededException --- ' , count)
    print(e)

print('Finish! ',count)