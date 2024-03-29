# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Put Item 
  (項目の追加/置換え)
'''
from pprint import pprint
import boto3

TABLE_NAME = 'Movies'

def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
    table = dynamodb.Table(TABLE_NAME)
    # put_item実行
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", 2015,
                           "Nothing happens at all.", 0)
    print("Put movie succeeded:")
    pprint(movie_resp)
    # pprint(movie_resp, sort_dicts=False)  # from Python 3.8
