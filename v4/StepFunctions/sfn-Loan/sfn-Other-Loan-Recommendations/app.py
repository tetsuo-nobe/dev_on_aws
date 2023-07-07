import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "お薦めの他のローンの情報を取得しました。"
    }
