# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットのリストを取得して表示
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

# Before running the code, check that the ~/.aws/credentials file contains your credentials.

def get_bucket_name():
    s3 = boto3.resource('s3')         # S3リソース取得
    for bucket in s3.buckets.all():   # S3リソースから全てのバケットを取得して表示
        region=s3.meta.client.head_bucket(Bucket=bucket.name)['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']
        print(f'bucket={bucket.name},region={region}')
    
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
