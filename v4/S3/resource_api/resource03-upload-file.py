# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットにオブジェクトを格納(upload_fileを使用)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def upload_file():
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    file_path= "C:\\temp\\Eiffel.jpg"         # アップロードするオブジェクトのファイルパスを指定
    key = "Eiffel.jpg"                        # アップロードするオブジェクトのキーを指定
    bucket.upload_file(file_path, key)        # アップロード実行
    print('File Upload: ' + file_path)


if __name__ == '__main__':
    try:
        upload_file()
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
