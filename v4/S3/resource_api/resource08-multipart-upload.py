# Copyright 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  マルチパートアップロード
'''
import boto3
import time
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import NoCredentialsError,ClientError

def multipart_upload_by_upload_file():
    bucket =  "tnobe-s3-sample"                   # S3バケット指定
    file_path= "AWSIcons.zip"             # アップロードするオブジェクトのファイルパスを指定
    key = "AWSIcons.zip"                               # アップロードするオブジェクトのキーを指定
    MB = 1024 ** 2
    config = TransferConfig(multipart_threshold=100*MB, multipart_chunksize=10*MB)
    #
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    start = time.time()
    bucket.upload_file(file_path, key, Config=config)        # アップロード実行
    elapsed_time = time.time() - start
    print ("s3resource upload_file : elapsed_time:{0}".format(elapsed_time) + "[sec]")

def multipart_upload_by_upload_fileobj():
    bucket =  "tnobe-s3-sample"                   # S3バケット指定
    file_path= "AWSIcons.zip"             # アップロードするオブジェクトのファイルパスを指定
    key = "AWSIcons2.zip"                             # アップロードするオブジェクトのキーを指定
    #
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    start = time.time()
    with open(file_path, 'rb') as data:
      bucket.upload_fileobj(data, key)        # アップロード実行
    elapsed_time = time.time() - start
    print ("s3resource upload_fileobj: elapsed_time:{0}".format(elapsed_time) + "[sec]")
    



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


