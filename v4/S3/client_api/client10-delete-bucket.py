# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットを削除
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def delete_bucket():
    s3client = boto3.client('s3')               # S3クライアント取得
    bucket_name = "tnobe-s3-sample-client"      # バケット名指定
    response = s3client.list_objects_v2(Bucket=bucket_name)  # バケット内の全オブジェクトを削除
    keyCount = response['KeyCount']
    if keyCount > 0:
        s3client.delete_objects(
            Bucket = bucket_name,
            Delete={
                    'Objects': [{
                        'Key': object['Key']
                    } for object in response['Contents']]
                })
    s3client.delete_bucket(Bucket=bucket_name) # バケット削除
    print('Deleted bucket: ' + bucket_name)


if __name__ == '__main__':
    try:
        
        delete_bucket()
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
