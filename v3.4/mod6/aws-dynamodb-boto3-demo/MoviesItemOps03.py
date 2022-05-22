# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Update Item 
  (項目の更新)
'''
from decimal import Decimal
from pprint import pprint
import boto3

def update_movie(title, year, rating, plot, actors, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')
    # update_itemの実行
    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a", # 更新値はプレースホルダにする
        ExpressionAttributeValues={                                          # 更新値をプレースホルダに埋め込み
            ':r': Decimal(rating),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_movie(
        "The Big New Movie", 2015, 5.5, "Everything happens all at once.",
        ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)
