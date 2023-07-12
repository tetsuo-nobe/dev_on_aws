'''
  バケットにオブジェクトを格納:upload_fileを使用 (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def upload_file():
    s3client = boto3.client('s3')             # S3クライアント取得
    file_path= "Eiffel.jpg"         # アップロードするオブジェクトのファイルパスを指定
    key = "Eiffel.jpg"                        # アップロードするオブジェクトのキーを指定
    s3client.upload_file(file_path, bucket, key)
    print('File Upload: ' + file_path)

if __name__ == '__main__':
    try:
        upload_file()
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
