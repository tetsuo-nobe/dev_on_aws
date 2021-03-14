# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  
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
    
    # メッセージを送信 (カスタム属性も設定)
    print('-- Send 開始 --')
    response = queue.send_message(MessageBody="Demo Message", MessageAttributes={'Author': {'StringValue': 'tnobe','DataType': 'String'}})
    print('-- Send 終了 --')

    # メッセージを受信
    print('-- Receive 開始 --')
    msg_list = queue.receive_messages(AttributeNames=['All'],MessageAttributeNames=['Author'],WaitTimeSeconds=20) # 標準属性は全て取得。カスタム属性も取得
    if msg_list:
      for message in msg_list:
        print('Message Body     : ' , message.body)         # メッセージの本文
        print('Message Attrbutes: ' , message.attributes  ) # メッセージの標準属性

        if message.message_attributes is not None: # カスタム属性の取得
          author_name = message.message_attributes.get('Author').get('StringValue')
          if author_name:
            author_text = ' ({0})'.format(author_name)
            # Print out the body and author (if set)
            print('Hello, {0}!{1}'.format(message.body, author_text))

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
    