# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  マルチパートアップロード構成を指定してアップロード
'''
import boto3
import time
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import NoCredentialsError,ClientError

def multipart_upload():
    s3client = boto3.client('s3')                 # S3クライアント取得
    bucket =  "tnobe-s3-sample"                   # S3バケット取得
    file_path= "C:\\temp\\Big.zip"                # アップロードするオブジェクトのファイルパスを指定
    key = "Big.zip"                               # アップロードするオブジェクトのキーを指定
    MB = 1024 ** 2
    config = TransferConfig(multipart_threshold=100*MB, multipart_chunksize=10*MB)
    #
    start = time.time()
    s3client.upload_file(file_path, bucket,key, Config=config)        # アップロード実行
    elapsed_time = time.time() - start
    print ("s3client Upload: elapsed_time:{0}".format(elapsed_time) + "[sec]")
    #
    s3 = boto3.resource('s3')                 # S3リソース取得
    bucket = s3.Bucket("tnobe-s3-sample")     # S3バケット取得
    key2 = "Big2.zip"                         # アップロードするオブジェクトのキーを指定
    start = time.time()
    bucket.upload_file(file_path, key2, Config=config)        # アップロード実行
    elapsed_time = time.time() - start
    print ("s3resourc Upload: elapsed_time:{0}".format(elapsed_time) + "[sec]")
    
    



if __name__ == '__main__':
    try:
        multipart_upload()
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


