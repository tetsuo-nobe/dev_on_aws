'''
   Limitサンプル
'''
import boto3
import time

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')

table = dynamodb.Table('LimitTest')
last_key = None

# LimitTestテーブルの全項目うち3項目づつ取り出す
while True:
  params = {'Limit':3}
  if last_key:
    params['ExclusiveStartKey'] = last_key

  response = table.scan(**params)

  #response = table.query(
  #      KeyConditionExpression=Key('place').eq('room1') & Key('time').between('2016-06-23 12:00:00', '2016-06-23 13:00:00'), 
  #      FilterExpression=Attr('count').gte(1),
  #      Limit=3)
  if 'LastEvaluatedKey' not in response:
    print('====================LAST ITEMS====================')
    print('Items', response['Items'], sep='=')
    break

  last_key = response['LastEvaluatedKey']
  print('====================ITEMS====================')
  print('Items', response['Items'], sep='=')
  print('LastEvaluatedKey', last_key, sep='=')
  time.sleep(1)