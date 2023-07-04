# Copyright 2021 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  AWS SDK for Python (boto3)で DynamoDBのQueryやScanを行うサンプル
'''
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import NoCredentialsError,ClientError

if __name__ == '__main__':
    try:
      # DynamoDBとのセッション開始
      dynamodb = boto3.resource('dynamodb')    
 
      # テーブル名
      table_name = "TrainingForQueryScan"   

      # テーブルの作成
      print("----- テーブル作成 開始" )
      table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'studentId',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'date',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'studentId',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
      )
      dynamodb.meta.client.get_waiter('table_exists').wait(TableName=table_name) # テーブル作成完了まで待機
      print("----- テーブル作成 完了" )

      # テーブルにアイテムを格納/上書き
      print("----- put_item 開始" )
      response = table.put_item(
        Item={
          'studentId': 1,
          'date': '2021/02/01',
          'cource': 'Developing on AWS',
          'trainerId': 'tnobe',
          'language': 'Python',
          'totalLabTime': 420,
          'audioIssue': True
        }
      )
      response = table.put_item(
        Item={
          'studentId': 1,
          'date': '2021/02/15',
          'cource': 'Architecting on AWS',
          'trainerId': 'gojos',
          'totalLabTime': 510,
          'audioIssue': False
        }
      )
      response = table.put_item(
        Item={
          'studentId': 2,
          'date': '2021/02/15',
          'cource': 'Developing on AWS',
          'trainerId': 'tnobe',
          'totalLabTime': 470,
          'audioIssue': False
        }
      )
      print("----- put_item 完了" )


      # テーブルへのQuery
      print("----- Query 開始" )
      response = table.query(
        ProjectionExpression="studentId, #dt, cource, trainerId",
        ExpressionAttributeNames={"#dt": "date"},
        KeyConditionExpression=
            Key('studentId').eq(1) & Key('date').between('2021/01/01', '2021/12/31')
      )
      print(response['Items'])
      print("----- Query 完了" )

      # テーブルへのScan
      print("----- Scan 開始" )
      # Scanのパラメータ設定
      scan_kwargs = {
        'FilterExpression': Key('cource').begins_with('Developing'), # コース名がDevelopingで始まる
        'ProjectionExpression': "studentId, cource, #dt",
        'ExpressionAttributeNames': {"#dt": "date"}
      }
      response = table.scan(**scan_kwargs)
      print(response['Items'])
      print("----- Scan 完了" )


      # テーブルの削除
      print("----- テーブル削除 開始" )
      table.delete()
      dynamodb.meta.client.get_waiter('table_not_exists').wait(TableName=table_name) # テーブル削除完了まで待機
      print("----- テーブル削除 完了" )
 

    except NoCredentialsError as nocrederr:
        print("!!!! InvalidCredentials !!!!")
        print(nocrederr)
    except ClientError as clienterr:
        print('!!!! ClientError !!!!')
        print(clienterr)
        error_code = clienterr.response['Error']['Code']
        print('error_code=',error_code)
    except Exception as ex:
        print('!!!! Exception !!!!')
        print(ex)

