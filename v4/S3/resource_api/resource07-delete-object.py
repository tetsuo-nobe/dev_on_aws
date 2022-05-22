# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットからオブジェクトを削除
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def delete_object():
    s3 = boto3.resource('s3')
    bucket = "tnobe-s3-sample"      # バケット名
    key = 'Eiffel.jpg'              # オブジェクトのキー(ファイル名)
    obj = s3.Object(bucket,key)     # バケット名とキーを指定してオブジェクト作成
    obj.delete()                    # 削除実行
    obj.wait_until_not_exists()     # 削除完了を確認
    print("Deleted :" + key)

if __name__ == '__main__':
    try:
        delete_object()
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
