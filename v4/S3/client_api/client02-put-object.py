# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットにオブジェクトを格納:put_objectを使用  (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def put_object():
    s3client = boto3.client('s3')          # S3クライアント取得
    key = 'cat.jpg'                        # オブジェクトのキー(ファイル名)
    localfile =  open('cat.jpg','rb')
    s3client.put_object(Body=localfile, Bucket=bucket, Key=key) # バケット名とキーを指定してオブジェクト作成
    print('Put Object: ' + key)

if __name__ == '__main__':
    try:
        put_object()
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
