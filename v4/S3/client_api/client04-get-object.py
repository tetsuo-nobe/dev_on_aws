'''
  バケットからオブジェクトを取得:get_objectを使用 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def get_object():
    s3client = boto3.client('s3')                  # S3クライアント取得
    key = 'cat.jpg'                                # オブジェクトのキー(ファイル名)
    response = s3client.get_object(Bucket=bucket,Key=key)     # バケット名とキーを指定してオブジェクト作成
    body = response['Body'].read()
    output_file = open('cat_get.jpg','wb')
    output_file.write(body)
    output_file.close()
    print('END')

if __name__ == '__main__':
    try:
        get_object()
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
