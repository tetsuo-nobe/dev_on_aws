# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  マルチパートダウンロード (Client API)
'''
import boto3
import time
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import NoCredentialsError,ClientError

def multipart_download_by_download_file():
    s3client = boto3.client('s3')                 # S3クライアント取得
    bucket =  "tnobe-s3-sample-client"            # S3バケット指定
    file_path= "C:\\temp\\Big-c1-downloaded.zip"  # ダウンロードするオブジェクトのファイルパスを指定
    key = "Big-c1.zip"                            # ダウンロードするオブジェクトのキーを指定
    MB = 1024 ** 2
    config = TransferConfig(multipart_threshold=100*MB, multipart_chunksize=10*MB)
    #
    start = time.time()
    s3client.download_file(bucket, key, file_path, Config=config)     # ダウンロード実行
    elapsed_time = time.time() - start
    print ("s3client download_file: elapsed_time:{0}".format(elapsed_time) + "[sec]")

def multipart_download_by_download_fileobj():
    s3client = boto3.client('s3')                 # S3クライアント取得
    bucket =  "tnobe-s3-sample-client"            # S3バケット指定
    file_path= "C:\\temp\\Big-c2-downloaded.zip"  # ダウンロードするオブジェクトのファイルパスを指定
    key = "Big-c2.zip"                            # ダウンロードするオブジェクトのキーを指定
    #
    start = time.time()
    with open(file_path, 'wb') as data:
      s3client.download_fileobj(bucket, key, data)   # ダウンロード実行
    elapsed_time = time.time() - start
    print ("s3client download_fileobj: elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    try:
        multipart_download_by_download_file()
        multipart_download_by_download_fileobj()
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


