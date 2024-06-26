# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Query 
  (テーブルの検索。パーティションキーの等価条件だけ指定するケース)
  このサンプルでは、year=1985の項目を抽出
'''
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = 'Movies'

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")  
    table = dynamodb.Table(TABLE_NAME)
    # Query実行
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1985
    print(f"Movies from {query_year}")
    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title'])
