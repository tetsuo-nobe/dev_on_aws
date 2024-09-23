import time
import boto3

# 前処理。まず検証用にテーブルを作成する
table_name = 'Accounts_{}'.format(time.time())
client = boto3.client('dynamodb', region_name='ap-northeast-1')
response = client.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
    ],
    BillingMode='PAY_PER_REQUEST'
)
print('create_table: TableName = {}'.format(response['TableDescription']['TableName']))

# テーブルの初期化作業の完了待ち
table_exists_waiter = client.get_waiter('table_exists')
table_exists_waiter.wait(TableName=table_name)

# 次にアイテムを2件登録する
# Dynamoさんの口座の残高を 100 に、DBさんの口座の残高を 50 に設定するイメージ
response = client.put_item(
    TableName=table_name,
    Item={
        'name': {'S': 'Dynamo'},
        'balance': {'N': '100'}
    },
    ReturnConsumedCapacity='INDEXES'
)
print('put_item: ConsumedCapacity = {}'.format(response['ConsumedCapacity']))
response = client.put_item(
    TableName=table_name,
    Item={
        'name': {'S': 'DB'},
        'balance': {'N': '50'}
    },
    ReturnConsumedCapacity='INDEXES'
)
print('put_item: ConsumedCapacity = {}'.format(response['ConsumedCapacity']))

# 1件だけ更新する
# Dynamoさんの口座から 20 引き出されたイメージ
response = client.update_item(
    TableName=table_name,
    Key={
        'name': {'S': 'Dynamo'}
    },
    AttributeUpdates={
        'balance': {
            'Action': 'PUT',
            'Value': {'N': '80'}
        }
    },
    ReturnConsumedCapacity='INDEXES'
)
print('update_item: ConsumedCapacity = {}'.format(response['ConsumedCapacity']))

# 2件まとめて更新して両方共エラーになることを確認する
# Dynamoさんの口座からDBさんの口座に 10 振り込む処理の裏側で同時に先程のDynamoさんの口座の引き落としが発生していたイメージ
try:
    client.transact_write_items(
        ReturnConsumedCapacity='INDEXES',
        TransactItems=[
            {
                'Update': {
                    'TableName': table_name,
                    'Key': {
                        'name': {'S': 'Dynamo'}
                    },
                    'ConditionExpression': 'balance = :bc',
                    'UpdateExpression': 'SET balance = :bu',
                    'ExpressionAttributeValues': {
                        ':bc': {'N': '100'},  # 元々は 100 の想定
                        ':bu': {'N': '90'},  # 100 - 10 = 90
                    }
                }
            },
            {
                'Update': {
                    'TableName': table_name,
                    'Key': {
                        'name': {'S': 'DB'}
                    },
                    'ConditionExpression': 'balance = :bc',
                    'UpdateExpression': 'SET balance = :bu',
                    'ExpressionAttributeValues': {
                        ':bc': {'N': '50'},  # 元々は 50 の想定
                        ':bu': {'N': '60'},  # 50 + 10 = 60
                    }
                }
            }
        ]
    )
except Exception as e:
    print('transact_write_items: {}'.format(e))

# エラーになったため再度最新の値を取得して振り込み処理をやり直すイメージ
response = client.transact_get_items(
    TransactItems=[
        {
            'Get': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'Dynamo'}
                }
            }
        },
        {
            'Get': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'DB'}
                }
            }
        }
    ]
)
print('transact_get_items: Responses = {}'.format(response['Responses']))

# 再度振込処理を実行するイメージ
response = client.transact_write_items(
    ReturnConsumedCapacity='INDEXES',
    TransactItems=[
        {
            'Update': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'Dynamo'}
                },
                'ConditionExpression': 'balance = :bc',
                'UpdateExpression': 'SET balance = :bu',
                'ExpressionAttributeValues': {
                    ':bc': {'N': '80'},  # 80 に修正
                    ':bu': {'N': '70'},  # 80 - 10 = 70
                }
            }
        },
        {
            'Update': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'DB'}
                },
                'ConditionExpression': 'balance = :bc',
                'UpdateExpression': 'SET balance = :bu',
                'ExpressionAttributeValues': {
                    ':bc': {'N': '50'},  # 変更なし
                    ':bu': {'N': '60'},  # 50 + 10 = 60
                }
            }
        }
    ]
)
print('transact_write_items: ConsumedCapacity = {}'.format(response['ConsumedCapacity']))

# 両方のアイテムが想定通り更新されていることを確認する
response = client.transact_get_items(
    TransactItems=[
        {
            'Get': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'Dynamo'}
                }
            }
        },
        {
            'Get': {
                'TableName': table_name,
                'Key': {
                    'name': {'S': 'DB'}
                }
            }
        }
    ]
)
print('transact_get_items: Responses = {}'.format(response['Responses']))

# 後処理。テーブルを削除する
response = client.delete_table(TableName=table_name)
print('delete_table: TableName = {}'.format(response['TableDescription']['TableName']))