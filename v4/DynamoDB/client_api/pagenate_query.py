'''
  query の結果を ページ単位で表示

'''
import boto3
import botocore
from  myconfig import table_name
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer

# ページ単位で項目を表示する関数
def query_with_pagenate(pageSize,p_userId):
    
    ddbClient = boto3.client('dynamodb')
    # ページネーターの取得
    paginator = ddbClient.get_paginator('query')
    # イテレーターの取得
    page_iterator = paginator.paginate(
        TableName=table_name,
        KeyConditionExpression='userId = :userId',
        ExpressionAttributeValues={
            ':userId': {"N": str(p_userId)}
        },
        ProjectionExpression="gameId, score",
        PaginationConfig={
            'PageSize': pageSize
        }
    )
    # ページ単位で表示
    pageNumber = 0
    for page in page_iterator:
        if page["Count"] > 0:
            pageNumber += 1
            print("----- ページ " + str(pageNumber) + " 開始 -----")
            printScores(page['Items'])
            print("----- ページ " + str(pageNumber) + " 終了 -----\n")    
    
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
        items = query_with_pagenate(3,3)
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
