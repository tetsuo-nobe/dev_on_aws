# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Scan + ページングのサンプル (準備）

'''
import boto3
from decimal import *
import json

tableName = 'pagenate-test'
loadFile  = 'testdata.json'

# テーブルを作成する関数
def create_test_table():
    dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
    # 既存のテーブル削除
    table = dynamodb.Table(tableName)
    table.delete()
    table.wait_until_not_exists()
     # テーブル作成
    table = dynamodb.create_table(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'seq',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'seq',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    )
    table.wait_until_exists()
    return table

# JSONファイルの内容をアイテムとしてテーブルに追加する関数
def load_test_items():
   with open(loadFile) as json_file:
        test_list = json.load(json_file, parse_float=Decimal)
   dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
   table = dynamodb.Table(tableName)
   for test_item in test_list:
       id =  test_item['id']
       seq = test_item['seq']
       print("Adding item:", id, seq)
       table.put_item(Item=test_item)

if __name__ == '__main__':
    test_table = create_test_table()
    print("Table status:", test_table.table_status)
    load_test_items()
    print("--- Loaded ----")
