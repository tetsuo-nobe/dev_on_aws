# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  バケットにオブジェクトを格納(put_objectを使用)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def put_object():
    s3 = boto3.resource('s3')          # S3リソース取得
    bucket = "tnobe-s3-sample"         # バケット名
    key = 'cat.jpg'                    # オブジェクトのキー(ファイル名)
    localfile =  open('c:\\temp\\cat.jpg','rb')
    obj = s3.Object(bucket,key)        # バケット名とキーを指定してオブジェクト作成
    obj.put( Body=localfile )          # オブジェクトをバケットにPUT Bodyにはbyte,file,stringを指定可能
    obj.wait_until_exists()            # PUT完了を確認
    print('Put Object: ' + key)


if __name__ == '__main__':
    try:
        put_object()
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
