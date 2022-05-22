# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Get Item 
  (項目の取得。取得する属性も指定するケース)
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table('Movies')

    try:
        # ProjectionExpressionの指定により、title属性だけを取得
        response = table.get_item(Key={'year': year, 'title': title},
                                ProjectionExpression='title')
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
