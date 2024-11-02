'''
  テーブル削除
'''
import boto3
import botocore
from  myconfig import table_name

# テーブルを削除する関数
def delete_table():
    ddbClient = boto3.client('dynamodb')
    # テーブル削除
    table = ddbClient.delete_table(
        TableName=table_name
    )
    waiter = ddbClient.get_waiter('table_not_exists') # テーブル削除完了まで待機
    waiter.wait(TableName=table_name) 


# ここから実行開始
if __name__ == '__main__':
    try:
        response = delete_table()
        print("Table Deleted")
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
