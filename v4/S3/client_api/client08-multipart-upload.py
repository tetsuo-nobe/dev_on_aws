# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  マルチパートアップロード (Client API)
'''
import boto3
import time
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import NoCredentialsError,ClientError

def multipart_upload_by_upload_file():
    s3client = boto3.client('s3')                 # S3クライアント取得
    bucket =  "tnobe-s3-sample-client"            # S3バケット指定
    file_path= "C:\\temp\\Big-c1.zip"             # アップロードするオブジェクトのファイルパスを指定
    key = "Big-c1.zip"                            # アップロードするオブジェクトのキーを指定
    MB = 1024 ** 2
    config = TransferConfig(multipart_threshold=100*MB, multipart_chunksize=10*MB)
    #
    start = time.time()
    s3client.upload_file(file_path, bucket,key, Config=config)     # アップロード実行
    elapsed_time = time.time() - start
    print ("s3client upload_file: elapsed_time:{0}".format(elapsed_time) + "[sec]")

def multipart_upload_by_upload_fileobj():
    s3client = boto3.client('s3')                 # S3クライアント取得
    bucket =  "tnobe-s3-sample-client"            # S3バケット指定
    file_path= "C:\\temp\\Big-c2.zip"             # アップロードするオブジェクトのファイルパスを指定
    key = "Big-c2.zip"                            # アップロードするオブジェクトのキーを指定
    #
    start = time.time()
    with open(file_path, 'rb') as data:
      s3client.upload_fileobj(data, bucket, key)   # アップロード実行
    elapsed_time = time.time() - start
    print ("s3client upload_fileobj: elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    try:
        multipart_upload_by_upload_file()
        multipart_upload_by_upload_fileobj()
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

