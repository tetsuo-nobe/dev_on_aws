# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Update Item 
  (項目の更新。条件に合致した場合のみ更新実行するケース)
　条件式
　https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

TABLE_NAME = 'Movies'

def remove_actors(title, year, actor_count, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')

    try:
        # 条件付きでupdate_item実行。条件を満たさない場合はClientErrorになる
        # (このサンプルで指定された項目の俳優数は3なので、3より多いという条件は満たさない)
        response = table.update_item(
            Key={
                'year': year,
                'title': title
            },
            UpdateExpression="remove info.actors[0]",
            ConditionExpression="size(info.actors) > :num", # ConditionExpressionで指定した条件が真の場合に更新実行
            ExpressionAttributeValues={':num': actor_count},
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print('!!! ClientError !!!')
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting conditional update (expecting failure)...")
    update_response = remove_actors("The Big New Movie", 2015, 3)
    if update_response:
        print("Update movie succeeded:")
        pprint(update_response)
        # pprint(update_response, sort_dicts=False)  # from Python 3.8
