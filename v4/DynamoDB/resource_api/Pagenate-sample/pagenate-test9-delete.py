# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  ページングのサンプルで使用したテーブル削除

'''
import boto3
from decimal import *
import json

tableName = 'pagenate-test'
loadFile  = 'testdata.json'

# テーブルを作成する関数
def delete_test_table():
    dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")
    # 既存のテーブル削除
    table = dynamodb.Table(tableName)
    table.delete()
    table.wait_until_not_exists()

if __name__ == '__main__':
    delete_test_table()
    print("Deleted")

