'''
   バッチサンプル
'''
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name='ap-northeast-1')

userid1 = "1"
userid2 = "2"

try:
    # LimitTestテーブルに入っている2つの項目をbatch_get_itemで取得する
    # （指定したキーで実際に存在するものだけ取得する）
    response = dynamodb.batch_get_item(
        RequestItems={
            'LimitTest': {
                'Keys': [
                    {
                        'userid': userid1
                    },
                    {
                        'userid': userid2
                    },
                ],            
                'ConsistentRead': True            
            }
        },
        ReturnConsumedCapacity='TOTAL'
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Responses']
    print("BatchGetItem succeeded:")
    print(item)
    print(response)
    
