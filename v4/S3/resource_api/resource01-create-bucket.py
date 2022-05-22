# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットを作成
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def create_bucket():
    s3 = boto3.resource('s3')    # S3リソース取得
    bucket = "tnobe-s3-sample"   # バケット名
    create_bucket_config = {}    # バケットの構成を作成
    create_bucket_config["LocationConstraint"] = "ap-northeast-1"  # リージョンの指定
    s3.create_bucket(Bucket=bucket, CreateBucketConfiguration=create_bucket_config)  # バケットの作成
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
