# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットからオブジェクトを削除 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def delete_object():
    s3client = boto3.client('s3')       # S3クライアント取得
    bucket = "tnobe-s3-sample-client"      
    key = 'Eiffel.jpg'                  # オブジェクトのキー(ファイル名)
    s3client.delete_object(             # オブジェクトの削除
      Bucket=bucket,
      Key=key
    )
    print("Deleted :" + key)

if __name__ == '__main__':
    try:
        delete_object()
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
