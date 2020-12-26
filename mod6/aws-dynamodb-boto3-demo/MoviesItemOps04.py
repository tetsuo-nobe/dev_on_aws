# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Update Item 
  (項目の更新。既存の値をもとに算出した値を更新値とするケース)
'''
from decimal import Decimal
from pprint import pprint
import boto3


def increase_rating(title, year, rating_increase, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')
    # update_itemの実行
    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating = info.rating + :val", # 既存の値に加算した値を更新値とする
        ExpressionAttributeValues={
            ':val': Decimal(rating_increase)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = increase_rating("The Big New Movie", 2015, 1)
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)
