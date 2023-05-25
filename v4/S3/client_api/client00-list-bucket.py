# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットのリストを取得して表示 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

# Before running the code, check that the ~/.aws/credentials file contains your credentials.

def get_bucket_name():
    s3client = boto3.client('s3')          # S3クライアント取得
    response = s3client.list_buckets()     # S3クライアントから全てのバケットを取得
    for bucket in response['Buckets']:     # バケットの表示   
        print(f'bucket={bucket["Name"]}')

    # for bucket in response['Buckets']:     # バケットとリージョンの表示   
    #     region=s3client.head_bucket(Bucket=bucket['Name'])['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']
    #     print(f'bucket={bucket["Name"]},region={region}')
    
if __name__ == '__main__':
    try:
        get_bucket_name()
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
