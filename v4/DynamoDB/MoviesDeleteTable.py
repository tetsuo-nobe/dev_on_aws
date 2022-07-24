# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  テーブル削除
'''
import boto3

TABLE_NAME = 'Movies'

def delete_movie_table(dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
        # dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    table.delete()
    dynamodb.meta.client.get_waiter('table_not_exists').wait(TableName=TABLE_NAME) # テーブル削除完了まで待機


if __name__ == '__main__':
    delete_movie_table()
    print("Movies table deleted.")
