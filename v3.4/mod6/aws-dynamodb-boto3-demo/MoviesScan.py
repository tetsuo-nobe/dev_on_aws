# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Scan 
  (テーブルのスキャン。
   Scanは常にテーブルから全項目を取出す。
   FilterExpressionがあればそこで指定した項目をピックアップして返す)
   このサンプルでは、yearが1950から1959まで項目をピックアップ
'''
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def scan_movies(year_range, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('Movies')
    # scanに指定するパラメータを定義
    scan_kwargs = {
        'FilterExpression': Key('year').between(*year_range),
        'ProjectionExpression': "#yr, title, info.rating",
        'ExpressionAttributeNames': {"#yr": "year"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        # scan実行
        response = table.scan(**scan_kwargs)
        display_movies(response.get('Items', []))
        # デフォルトで取得最大サイズは1MBなので、まだ残りのデータがあれば繰り返して取得する
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")
            pprint(movie['info'])

    query_range = (1950, 1959)
    print(f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    scan_movies(query_range, print_movies)
