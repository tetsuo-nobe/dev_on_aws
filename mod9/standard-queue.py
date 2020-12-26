# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  標準キューの作成と取出し順序の確認
'''
import boto3
sqs = boto3.resource('sqs')
qname = 'playground'

try:
    # キューの名前を指定してインスタンスを取得
    queue = sqs.get_queue_by_name(QueueName=qname)
    queue.purge()
except:
    # 指定したキューがない場合はexceptionが返るので、キューを作成
    queue = sqs.create_queue(QueueName=qname)

# メッセージの送信
for i in range(100):
    message = 'message_' + str(i)
    print(message)

    queue.send_message(
      MessageBody=message,
    )

# メッセージ数の表示
print('--- ApproximateNumberOfMessages ---')
print(queue.attributes['ApproximateNumberOfMessages'])

# メッセージの受信
messages = queue.receive_messages()

# メッセージの表示
print(messages[0].body)
print(messages[0].receipt_handle)

# メッセージの削除
messages[0].delete()

# メッセージの受信
messages = queue.receive_messages(
    MaxNumberOfMessages=10,    # 最大受信メッセージ数を10に限定
    WaitTimeSeconds=20
)

# メッセージの表示と削除
for message in messages:
    print(message.body)
    print(message.receipt_handle)
    message.delete()


