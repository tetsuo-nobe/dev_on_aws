'''
  バケット内のオブジェクトのリストを取得して表示  (Client API)
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def list_object():
  s3client = boto3.client('s3')                                     # S3クライアント取得
  prefix = ""                                                       # prefixの指定       
  response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix) # バケット内の該当オブジェクトのリストを取得
  for object in response['Contents']:                               # 取得したリストを表示
    print(object['Key'])

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
