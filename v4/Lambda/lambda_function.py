from datetime import datetime

# ハンドラ関数の外側で日時データを取得
outside_handler = datetime.now()

def lambda_handler(event, context):
    # ハンドラ関数の内側で日時データを取得
    inside_handler = datetime.now()
    
    # 取得した日時データをログ出力
    print('outside_handler :' + str(outside_handler))
    print('inside_handler  :' + str(inside_handler))
    
    # context オブジェクトからいくつかの値をログ出力
    print("Lambda function ARN:", context.invoked_function_arn)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    
    # event オブジェクトから name の値を取得して return のペイロードに含める
    return {
        'statusCode': 200,
        'body': 'Hello! '  + event['name']
        }