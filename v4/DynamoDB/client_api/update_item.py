'''
  query を使用した項目の取得
  userId(パーティションキー)の値を指定して該当する項目を取得する
'''
import boto3
import botocore
from  myconfig import table_name
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer

# 項目を更新する関数
def update_left(p_userId,p_gameId,p_life):
    
    ddbClient = boto3.client('dynamodb')
    # update_item 発行
    try:
        response = ddbClient.update_item(
            TableName=table_name,
            Key={
                "userId": {"N": str(p_userId)},
                "gameId": {"S": p_gameId }
            },
            ReturnValues='ALL_NEW',
            UpdateExpression='SET life = life + :add_life',
            ConditionExpression='score >= :score',
            ExpressionAttributeValues={
                ':add_life': {'N': str(p_life)},
                ':score': {'N': "3000"},
            }
        )
        
        return response['Attributes']
    except botocore.exceptions.ClientError as err:
        if err.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return "Sorry, your update is invalid mate!"
        else:
            return err.response['Error']['Message']


# ここから実行開始
if __name__ == '__main__':
    try:
        item = update_left(3,"G001",1)
        print(item) 
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
