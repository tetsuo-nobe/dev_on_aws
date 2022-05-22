# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
import boto3
from boto3.session import Session
from botocore.exceptions import NoCredentialsError,ClientError

def s3_resource():
    # デフォルトのプロファイルのアクセスキーIDを使用 
    # (環境変数AWS_ACCESS_KEY_IDとAWS_SECRET_ACCESS_KEYがある場合は、環境変数の値が優先される)
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    print('------------------------------------------')

    # コードで指定したアクセスキーIDを使用（推奨しません）
    session = Session(aws_access_key_id='<YOUR ACCESS KEY ID>',
                      aws_secret_access_key='<YOUR SECRET ACCESS KEY>',
                      region_name='<REGION_NAME')
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
    
    print('------------------------------------------')

    # デフォルト以外のプロファイルを使用
    profile = '<YOUR PROFILE NAME>'
    session = Session(profile_name=profile)

    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    print('------------------------------------------')

if __name__ == '__main__':
    try:
        s3_resource()
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
