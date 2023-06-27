# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットからオブジェクトを取得：download_fileを使用 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def download_file():
    s3client = boto3.client('s3')                   # S3クライアント取得
    file_path= "Eiffel_downloaded.jpg"    # ダウンロードするオブジェクトのファイルパスを指定
    key = "Eiffel.jpg"                              # ダウンロードするオブジェクトのキーを指定
    s3client.download_file(bucket, key, file_path)  # ダウンロード実行
    print('File Downloaded: ' + file_path)

if __name__ == '__main__':
    try:
        download_file()
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
