# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Get Item 
  (項目の取得)
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

TABLE_NAME = 'Movies'

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    table = dynamodb.Table(TABLE_NAME)

    try:
        # 結果整合性
        response = table.get_item(Key={'year': year, 'title': title})
        # 強力な整合性
        #response = table.get_item(Key={'year': year, 'title': title},ConsistentRead=True)
    except ClientError as e:
        print('--- ClientError ---')
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)
        # pprint(movie, sort_dicts=False)  # from Python 3.8
