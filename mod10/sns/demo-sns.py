# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  AWS SDK for Python (boto3)で SNSの基本的な操作を行うサンプル
  SNS Topic作成、Lambda関数のサブスクリプション設定、フィルターポリシー設定、メッセージ発行
  (Lambda関数側に、SNS Topicからのinvokeを許可するリソースベースのポリシーを事前に設定済)
'''
import boto3
import json
from botocore.exceptions import NoCredentialsError,ClientError

if __name__ == '__main__':
  try:
    sns = boto3.resource('sns')
    topic_name = 'ShoppingEvents'

    # トピックの作成
    topic = sns.create_topic(Name=topic_name)

    # サブスクライブの設定 (SQSやLambdaの場合は、SQSやLambda側にリソースベースのポリシーでSNSからのアクセスの許可が必要)
    lambda_subscription  = topic.subscribe(Protocol='lambda',Endpoint='arn:aws:lambda:ap-northeast-1:000000000000:function:SNSSDKFunction')
    # フィルターポリシー設定 (メッセージ属性で、"event_type"が"product_page_visited"のものを対象とする)
    lambda_subscription.set_attributes(
         AttributeName='FilterPolicy',
         AttributeValue=json.dumps({"event_type": ["product_page_visited"]})
    )

    # メッセージを発行
    print('-- Publish 開始 --')
    message = '{"product": {"id": 1251, "status": "in_stock"}, "buyer": {"id":4454}}'
    topic.publish(
	    Subject = 'Product Visited #1251',
	    Message = message,	
	    MessageAttributes = {
		    'event_type': {
			  'DataType': 'String',
			  'StringValue': 'product_page_visited'
		    }  
	    }
    )
    print('-- Publish 終了 --')

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
    
