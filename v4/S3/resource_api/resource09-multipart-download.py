# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  マルチパートダウンロード
'''
import boto3
import time
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import NoCredentialsError,ClientError

def multipart_download_by_download_file():
    bucket =  "tnobe-s3-sample"                   # S3バケット指定
    file_path= "C:\\temp\\Big-r1-downloaded.zip"  # ダウンロードするオブジェクトのファイルパスを指定
    key = "Big-r1.zip"                            # ダウンロードするオブジェクトのキーを指定
    MB = 1024 ** 2
    config = TransferConfig(multipart_threshold=100*MB, multipart_chunksize=10*MB)
    #
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    start = time.time()
    bucket.download_file(key, file_path, Config=config)        # ダウンロード実行
    elapsed_time = time.time() - start
    print ("s3resource download_file : elapsed_time:{0}".format(elapsed_time) + "[sec]")

def multipart_download_by_download_fileobj():
    bucket =  "tnobe-s3-sample"                    # S3バケット指定
    file_path= "C:\\temp\\Big-r2-downloaded.zip"   # ダウンロードするオブジェクトのファイルパスを指定
    key = "Big-r2.zip"                             # ダウンロードするオブジェクトのキーを指定
    #
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    start = time.time()
    with open(file_path, 'wb') as data:
      bucket.download_fileobj(key,data)        # ダウンロード実行
    elapsed_time = time.time() - start
    print ("s3resource download_fileobj: elapsed_time:{0}".format(elapsed_time) + "[sec]")
    



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


