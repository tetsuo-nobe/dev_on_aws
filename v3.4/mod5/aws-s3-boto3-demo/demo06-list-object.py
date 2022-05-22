# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケット内のオブジェクトのリストを取得して表示
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def list_object():
  s3 = boto3.resource('s3')          # S3リソース取得
  bucket = "tnobe-s3-sample"         # バケット名
  prefix = ""                        # prefixの指定       
  list = s3.Bucket(bucket).objects.filter(Prefix=prefix) # バケット内の該当オブジェクトのリストを取得
  for object in list:                                    # 取得したリストを表示
    print(object.key)

if __name__ == '__main__':
    try:
        list_object()
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
