'''
  get_item を使用した項目の取得
  プライマリキーの値を指定して該当する項目を取得する
'''
import boto3
import botocore
from  myconfig import table_name
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer

# get_item で全ての属性を取得する関数(結果整合性)
def get_all_attributes(p_userId,p_gameId):
    
    ddbClient = boto3.client('dynamodb')
    # get_item 発行
    response = ddbClient.get_item(
            TableName = table_name,
            Key       = {
                         'userId': {'N': str(p_userId)},
                         'gameId': {'S': p_gameId},
            }
    )
    return response["Item"]

# get_item で全ての属性を取得する関数(強力な整合性)
def get_all_attributes_consistent_read(p_userId,p_gameId):
    
    ddbClient = boto3.client('dynamodb')
    # get_item 発行
    response = ddbClient.get_item(
            TableName = table_name,
            Key       = {
                         'userId': {'N': str(p_userId)},
                         'gameId': {'S': p_gameId},
            },
            ConsistentRead=True
    )
    return response["Item"]

def get_selected_attributes(p_userId,p_gameId):
    
    ddbClient = boto3.client('dynamodb')
    # get_item 発行
    response = ddbClient.get_item(
            TableName = table_name,
            Key       = {
                         'userId': {'N': str(p_userId)},
                         'gameId': {'S': p_gameId},
            },
            ProjectionExpression='score,life'
    )
    return response["Item"]



## 単一項目の表示用のユーティリティ関数
def printScores(score):
    scores = [score]
    if isinstance(scores, list):
        for score in scores:
            print(
                json.dumps(
                    {key: TypeDeserializer().deserialize(value) for key, value in score.items()},
                    cls=DecimalEncoder
                )
            )

# 項目を JSON に変換するためのヘルパークラス
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  # <---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)

# ここから実行開始
if __name__ == '__main__':
    try:
        item = get_all_attributes(3,"G001")
        printScores(item)
        item = get_all_attributes_consistent_read(3,"G001")
        printScores(item)
        item = get_selected_attributes(3,"G001")
        printScores(item)
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
