# Copyright 2021 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  AWS SDK for Python (boto3)で DynamoDBの基本的な操作を行うサンプル
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

if __name__ == '__main__':
    try:
      # DynamoDBとのセッション開始
      dynamodb = boto3.resource('dynamodb')    
      # dynamodb = boto3.resource('dynamodb', region_name="ap-northeast-1") # リージョンを明示的に指定する方法

      # テーブル名
      table_name = "Training"   

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
      print("----- put_item 完了" )


      # テーブルからアイテムを取得
      print("----- get_item 開始" )
      response = table.get_item(Key={'studentId': 1, 'date': '2021/02/01'})    # 結果整合性
      # response = table.get_item(Key={'studentId': 1, 'date': '2021/02/01'},ConsistentRead=True) # 強力な整合性
      print(response['Item'])  
      print("----- get_item 完了" )


      # テーブルからアイテムを取得 (ProjectionExpressionを使用しcource属性とlanguage属性だけを取得)
      print("----- get_item + projection expression 開始" )
      response = table.get_item(Key={'studentId': 1, 'date': '2021/02/01'},
                                ProjectionExpression='cource,trainerId')   
      print(response['Item'])  
      print("----- get_item + projection expression 完了" )


      # テーブルからアイテムを取得(ProjectionExpressionを使用。ただし予約語がある場合はプレースホルダ使用)
      print("----- get_item + projection expression + プレースホルダ 開始" )
      response = table.get_item(Key={'studentId': 1, 'date': '2021/02/01'},
                                ProjectionExpression='cource, #lang',           # 属性名 languageは予約語なのでプレースホルダにする
                                ExpressionAttributeNames={'#lang': 'language'}) # プレースホルダに属性名を設定

      print(response['Item'])  
      print("----- get_item + projection expression + プレースホルダ 完了" )


      # アイテムを更新
      print("----- update_item 開始" )
      response = table.update_item(
        Key={
            'studentId': 1,
            'date': '2021/02/01'
        },
        UpdateExpression="set totalLabTime = totalLabTime + :val", # 既存の値に加算した値を更新値とする
        ExpressionAttributeValues={
            ':val': 30
        },
        ReturnValues="UPDATED_NEW"
      )
      print("----- update_item 完了" )

      # アイテムを更新（条件付き）
      response = table.update_item(
            Key={
                'studentId': 1,
                'date': '2021/02/01'
            },
            UpdateExpression="add #pin :pinNo",
            ConditionExpression="audioIssue = :bool", # ConditionExpressionで指定した条件が真の場合に更新実行
            ExpressionAttributeNames={'#pin': 'audioPIN'},
            ExpressionAttributeValues={':pinNo': 1234, ':bool': True},
            ReturnValues="UPDATED_NEW"
      )

      # テーブルからアイテムを取得(更新内容の確認のため)
      print("----- get_item 開始" )
      response = table.get_item(Key={'studentId': 1, 'date': '2021/02/01'},ConsistentRead=True) # 強力な整合性
      print(response['Item'])  
      print("----- get_item 完了" )

      # アイテムの削除
      response = table.delete_item(
            Key={
                'studentId': 1,
                'date': '2021/02/01'
            }
      )

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

