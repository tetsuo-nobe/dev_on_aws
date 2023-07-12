'''
  バケットを作成 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def create_bucket():
    s3client = boto3.client('s3')       # S3クライアント取得
    create_bucket_config = {}           # バケットの構成を作成
    create_bucket_config["LocationConstraint"] = "ap-northeast-1"  # リージョンの指定
    s3client.create_bucket(Bucket=bucket, CreateBucketConfiguration=create_bucket_config)  # バケットの作成
    waiter = s3client.get_waiter('bucket_exists')
    waiter.wait(Bucket=bucket)
    print('Created bucket: ' + bucket)


if __name__ == '__main__':
    try:
        create_bucket()
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
