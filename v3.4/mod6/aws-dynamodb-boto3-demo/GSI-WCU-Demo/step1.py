import json
import boto3

# テーブル purchase-histories2 (Hash=user,Range=date)
# LSI user-product-index (Hash=user,Range=product)
# LSI user-price-index (Hash=date,Range=price)
table_name = 'purchase-histories2'
print(table_name)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# 1アイテム追加（キーのみ）
response = table.put_item(
    Item = {
        'user': 'yoshida',
        'date': '2020-01-01'
    },
    ReturnConsumedCapacity = 'INDEXES'
)

print(json.dumps(response['ConsumedCapacity'], indent=2))