import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "審査不合格を通知しました。"
    }
