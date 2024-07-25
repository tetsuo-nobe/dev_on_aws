# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
import boto3
from boto3.session import Session
from botocore.exceptions import NoCredentialsError,ClientError

def s3_resource():
    # デフォルトのプロファイルのアクセスキーIDを使用 
    # (環境変数AWS_ACCESS_KEY_IDとAWS_SECRET_ACCESS_KEYがある場合は、環境変数の値が優先される)
    s3client = boto3.client('s3')
    response = s3client.list_buckets()     # S3クライアントから全てのバケットを取得
    for bucket in response['Buckets']:     # バケットの表示   
        print(f'bucket={bucket["Name"]}')

    print('------------------------------------------')

    # コードで指定したアクセスキーIDを使用（推奨しません）
    session = Session(aws_access_key_id='<Your ACCESS KEY ID>',
                      aws_secret_access_key='<Your SECRET ACCESS KEY>',
                      region_name='ap-northeast-1')
    s3client = session.client('s3')
    response = s3client.list_buckets()     # S3クライアントから全てのバケットを取得
    for bucket in response['Buckets']:     # バケットの表示   
        print(f'bucket={bucket["Name"]}')
    
    print('------------------------------------------')

    # デフォルト以外のプロファイルを使用
    profile = '<Your Profile Name>'
    session = Session(profile_name=profile)

    s3client = session.client('s3')
    response = s3client.list_buckets()     # S3クライアントから全てのバケットを取得
    for bucket in response['Buckets']:     # バケットの表示   
        print(f'bucket={bucket["Name"]}')

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
