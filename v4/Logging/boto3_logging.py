"""
* Pythonのloggingモジュールのログレベル
* 数値が小さいほど詳細なメッセージが出力される
  - logging.DEBUG (10) - 詳細な診断情報
  - logging.INFO (20) - 一般的な情報メッセージ
  - logging.WARNING (30) - 警告メッセージ（デフォルトレベル）
  - logging.ERROR (40) - エラーメッセージ
  - logging.CRITICAL (50) - 重大なエラーメッセージ
"""

import logging
import boto3

# boto3のデバッグログを有効化
logging.basicConfig(level=logging.DEBUG)
boto3.set_stream_logger('boto3', logging.DEBUG)
boto3.set_stream_logger('botocore', logging.DEBUG)


# S3クライアントを作成してテスト
def get_bucket_count():
    print("============================================");
    print("Welcome to the AWS Boto3 SDK! Ready, Set, Go!");
    print("============================================");

    try:
        s3 = boto3.resource('s3')
    except NoCredentialsError:
        print("InvalidCredentials")
        sys.exit()

    try:
        no_of_buckets = len(list(s3.buckets.all()))
        print("You have", str(no_of_buckets), "Amazon S3 buckets.")
        return no_of_buckets

    except ClientError as ex:
        print(ex)
        return 0


if __name__ == '__main__':
    get_bucket_count()