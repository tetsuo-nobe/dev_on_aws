'''
  テーブル作成
  ゲームのスコア情報を管理するテーブル。パーティションキー userId, ソートキー gameId
'''
import boto3
import botocore
from  myconfig import table_name

# テーブルを削除する関数
def delete_table():
    ddbClient = boto3.client('dynamodb')
    # テーブル作成
    table = ddbClient.delete_table(
        TableName=table_name
    )
    waiter = ddbClient.get_waiter('table_not_exists') # テーブル削除完了まで待機
    waiter.wait(TableName=table_name) 
    response = ddbClient.describe_table(
        TableName=table_name
    )
    return response

# ここから実行開始
if __name__ == '__main__':
    try:
        response = delete_table()
        print("Table status:", response['Table']['TableStatus'])
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
