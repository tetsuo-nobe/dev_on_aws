# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットからオブジェクトを取得(get_objectを使用)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def get_object():
    s3 = boto3.resource('s3')       # S3リソース取得
    bucket = "tnobe-s3-sample"      # バケット名
    key = 'cat.jpg'                 # オブジェクトのキー(ファイル名)
    obj = s3.Object(bucket,key)     # バケット名とキーを指定してオブジェクト作成
    response = obj.get()
    body = response['Body'].read()
    output_file = open('c:\\temp\\cat_get.jpg','wb')
    output_file.write(body)
    output_file.close()
    print('END')

if __name__ == '__main__':
    try:
        get_object()
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
