# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Query 
  (テーブルの検索。パーティションキーの等価条件とソートキーの値の範囲を指定するケース)
  このサンプルでは、year=1992, titleが、A* から Lまで(L*は範囲外)の項目を抽出 
'''
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = 'Movies'

def query_and_project_movies(year, title_range, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table(TABLE_NAME)
    print(f"Get year, title, genres, and lead actor")

    # Query実行
    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=
            Key('year').eq(year) & Key('title').between(title_range[0], title_range[1])
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1992
    query_range = ('A', 'L')
    print(f"Get movies from {query_year} with titles from "
          f"{query_range[0]} to {query_range[1]}")
    movies = query_and_project_movies(query_year, query_range)
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")
        pprint(movie)
        # pprint(movie, sort_dicts=False)  # from Python 3.8
