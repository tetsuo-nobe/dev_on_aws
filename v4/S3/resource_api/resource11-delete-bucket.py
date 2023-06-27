# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットを削除
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name

def delete_bucket():
    s3 = boto3.resource('s3')               # S3リソース取得
    bucket = s3.Bucket(bucket_name)         # S3バケット取得
    for object in bucket.objects.all():     # バケット内の全オブジェクトを削除
      object.delete()
    bucket.delete()                         # バケット削除
    print('Deleted bucket: ' + bucket_name)


if __name__ == '__main__':
    try:
        
        delete_bucket()
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
