import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "口座に入金しました。"
    }
