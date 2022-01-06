# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  キューからメッセージを受信、キューへのメッセージ送信
'''
import boto3

qname = 'DemoQ1211'
sqs = boto3.resource('sqs')
try:
    # キューの名前を指定してインスタンスを取得
    queue = sqs.get_queue_by_name(QueueName=qname)
except:
    # 指定したキューがない場合はexceptionが返るので、キューを作成
    queue = sqs.create_queue(QueueName=qname)

# メッセージを受信
while True:
    # メッセージを取得
    msg_list = queue.receive_messages(MaxNumberOfMessages=10)
    # msg_list = queue.receive_messages(MaxNumberOfMessages=10, WaitTimeSeconds=20) # ロングポーリング
    # msg_list = queue.receive_messages(AttributeNames=['All'],MaxNumberOfMessages=10, WaitTimeSeconds=20) # 属性も全て取得
    if msg_list:
        for message in msg_list:
            print(message.body)         # メッセージの本文
            # print(message.attributes) # メッセージの属性
            # メッセージを削除
            message.delete()
        print('-- 次の Receive --')
    else:
        # メッセージがなくなったらbreak
        break
print('-- Receive 完了, Send 開始 --')
# 3つのメッセージをまとめたエントリをキューに送信
msg_num = 3
msg_list = [{'Id' : '{}'.format(i+1), 'MessageBody' : 'DemoMessage_{}'.format(i+1)} for i in range(msg_num)]
response = queue.send_messages(Entries=msg_list)
print('-- Send 終了 --')