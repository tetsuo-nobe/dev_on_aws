'''
  グローバルセカンダリインデックス作成
  ゲームのスコア情報を管理するテーブル。パーティションキー gameId, ソートキー score
'''
import boto3
import botocore
from  myconfig import table_name
from  myconfig import index_name

# テーブルを作成する関数
def create_gsi():
    ddbClient = boto3.client('dynamodb')
    # テーブル作成
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
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
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
    waiter = ddbClient.get_waiter('table_exists') # テーブル作成完了まで待機
    waiter.wait(TableName=table_name) 
    response = ddbClient.describe_table(
        TableName=table_name
    )
    return response

# ここから実行開始
if __name__ == '__main__':
    try:
        response = create_gsi()
        print("Table status:", response['Table']['TableStatus'])
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
