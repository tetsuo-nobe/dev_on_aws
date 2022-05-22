'''
  Delete Item 
  (項目の削除。条件に合致した場合のみ削除実行するケース)
　条件式
　https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html
'''
from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_underrated_movie(title, year, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')

    try:
        # 条件付きでdelete_item実行
        # (このサンプルで指定された項目のratingは6.5なので、6以下という条件は満たさない)
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            },
            ConditionExpression="info.rating <= :val",
            ExpressionAttributeValues={
                ":val": Decimal(rating)
            }
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
    print("Attempting a conditional delete...")
    delete_response = delete_underrated_movie("The Big New Movie", 2015, 6)
    if delete_response:
        print("Delete movie succeeded:")
        pprint(delete_response, sort_dicts=False)
