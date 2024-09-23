import json
import boto3

# テーブル purchase-histories2 (Hash=user,Range=date)
# LSI user-product-index (Hash=user,Range=product)
# LSI user-price-index (Hash=date,Range=price)
table_name = 'purchase-histories2'
print(table_name)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# 1アイテム追加（キーとproduct属性とprice属性）
response = table.put_item(
    Item = {
        'user': 'yoshida',
        'date': '2020-03-01',
        'product': 'aws-book-002',
        'price': 1000
    },
    ReturnConsumedCapacity = 'INDEXES'
)

print(json.dumps(response['ConsumedCapacity'], indent=2))
