'''
  グローバルセカンダリインデックス(GSI)作成
  ゲームのスコア情報を管理するテーブル。パーティションキー gameId, ソートキー score
'''
import boto3
import botocore
import time
from  myconfig import table_name
from  myconfig import index_name

# GSI を作成する関数
def create_gsi():
    ddbClient = boto3.client('dynamodb')
    # GSI 作成
    table = ddbClient.update_table(
        TableName=table_name,
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": index_name,
                    "KeySchema": [
                        {
                            "AttributeName": "gameId",
                            "KeyType": "HASH"
                        },
                        {
                            "AttributeName": "score",
                            "KeyType": "RANGE"
                        },
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 2,
                        "WriteCapacityUnits": 2,
                    }
                }
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'gameId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'score',
                'AttributeType': 'N'
            }

        ]
    )
    # GSI 作成時は waiter が使えないのでステータスのチェックを繰り返して作成完了まで待機する
    index_status = ''
    while index_status != 'ACTIVE':
        time.sleep(30)
        response = ddbClient.describe_table(
            TableName=table_name
        )
        index_status = response['Table']['GlobalSecondaryIndexes'][0]['IndexStatus']
        print('GSI 作成中です。しばらくお待ちください... ' + index_status)
    return index_status

# ここから実行開始
if __name__ == '__main__':
    try:
        response = create_gsi()
        print("GSI status:", response)
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
