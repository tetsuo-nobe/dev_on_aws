# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  Scan + ページングのサンプル 2

'''
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def scan_items(query_range, display_items, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1")

    # ソートキー seq 1 から12 までの項目をもつテーブル
    table = dynamodb.Table('pagenate-test')

    # Scanに指定するパラメータを定義
    # seq 1から10の範囲を条件に指定。ただし Limit 3アイテムとする。
    scan_kwargs = {
        'FilterExpression': Key('seq').between(*query_range),
        'Limit' : 3
    }
    # Limit 3で区切りながら条件にマッチする10件の項目を取得
    print(f"Scanning for id from {query_range[0]} to {query_range[1]}...")
    done = False
    start_key = None
    page = 0
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        # Scan実行
        response = table.scan(**scan_kwargs)
        # まだ残りのデータがあれば繰り返して取得する
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
        if (done != True):
            page = page + 1
            display_items(response.get('Items', []),page)
        #
        


if __name__ == '__main__':
    def print_items(items,page):
        print(f"-- page {page}---------------------")
        for item in items:
            print(f"\n{item['id']} : {item['seq']}")

    query_range = (1, 10)
    scan_items(query_range, print_items)
