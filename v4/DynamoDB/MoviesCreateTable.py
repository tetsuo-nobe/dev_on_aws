# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  テーブル作成
  映画の情報を管理するテーブル。パーティションキー year, ソートキー title
'''
import boto3

TABLE_NAME = 'Movies'

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
        #dynamodb = boto3.resource('dynamodb')
    # テーブル作成
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    dynamodb.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME) # テーブル作成完了まで待機
    table = dynamodb.Table(TABLE_NAME)
    return table


if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)
    
