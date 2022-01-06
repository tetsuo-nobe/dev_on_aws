# Copyright 2021 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  AWS SDK for Python (boto3)で SQSの基本的な操作を行うサンプル
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

if __name__ == '__main__':
  try:
    sqs = boto3.resource('sqs')
    qname = 'DemoQ0313'

    # キューの作成
    queue = sqs.create_queue(QueueName=qname)
    
    # キューの名前を指定してインスタンスを取得
    # queue = sqs.get_queue_by_name(QueueName=qname)  
    
    # メッセージを送信 
    print('-- Send 開始 --')
    response = queue.send_message(MessageBody="Demo Message")
    print('-- Send 終了 --')

    # メッセージを受信
    print('-- Receive 開始 --')
    # msg_list = queue.receive_messages()     # ショートポーリング
    msg_list = queue.receive_messages(WaitTimeSeconds=20)   # ロングポーリング
    if msg_list:
      for message in msg_list:
        print('Message Body: ' , message.body)         # メッセージの本文を表示
        # メッセージを削除
        message.delete()
    print('-- Receive 完了 --')

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
    