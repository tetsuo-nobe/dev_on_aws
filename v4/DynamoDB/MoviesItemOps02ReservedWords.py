# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Get Item 
  (項目の取得。取得する属性も指定。ただし属性名が予約語の場合はプレースホルダ使用)
  DynamoDBの予約語
  https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/ReservedWords.html
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title},
                                ProjectionExpression='#yr, title',        # 属性名 yearは予約語なのでプレースホルダにする
                                ExpressionAttributeNames={'#yr': 'year'}) # プレースホルダに属性名を設定
    except ClientError as e:
        print('--- ClientError ---')
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)
