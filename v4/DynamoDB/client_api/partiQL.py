'''
  PartiQL を使用した項目の取得
  userId(パーティションキー)の値を指定して該当する項目を取得する
'''
import boto3
import botocore
from  myconfig import table_name
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer

# PartiQL のクエリーを実行する関数
def execute_partiQL(p_userId,p_gameId):
    
    ddbClient = boto3.client('dynamodb')
    # クエリー発行
    response = ddbClient.execute_statement(
        Statement="SELECT gameId,score,life FROM " + table_name + " WHERE userId = ? ",
        Parameters=[
           {"N": str(p_userId)}
        ]
    )
    return response["Items"]

## 項目の表示用のユーティリティ関数
def printScores(scores):
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
        items = execute_partiQL(3,"G001")
        printScores(items)
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  