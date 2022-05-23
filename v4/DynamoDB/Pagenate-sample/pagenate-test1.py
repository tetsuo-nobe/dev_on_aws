# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Scan + ページングのサンプル 1

'''
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def scan_items(id_range, display_items, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    # ソートキー seq 1 から12 までの項目をもつテーブル
    table = dynamodb.Table('pagenate-test')

    # Scanに指定するパラメータを定義

    # 10件取得する条件 -> 'Count': 10, 'ScannedCount': 12になる。LastEvaluatedKeyは無し
    scan_kwargs_range10 = {
        'FilterExpression': Key('seq').between(*id_range)
    }

    # Scan実行
    response = table.scan(**scan_kwargs_range10)
    display_items(response.get('Items', []))
    # 
    start_key = response.get('LastEvaluatedKey', None)
    print(response)

    # 10件取得する条件でLimit 3 -> -> 'Count': 3, 'ScannedCount': 3になる。LastEvaluatedKeyに3つ目のItemが設定される
    
    scan_kwargs_range10_limit3 = {
        'FilterExpression': Key('seq').between(*id_range),
        'Limit' : 3
    }

    # Scan実行
    response = table.scan(**scan_kwargs_range10_limit3)
    display_items(response.get('Items', []))
    # 
    start_key = response.get('LastEvaluatedKey', None)
    print(response)


if __name__ == '__main__':
    def print_items(items):
        for item in items:
            print(f"\n{item['id']} : {item['seq']}")
            print("------------------")

    query_range = (1, 10)
    print(f"Scanning for id from {query_range[0]} to {query_range[1]}...")
    scan_items(query_range, print_items)
