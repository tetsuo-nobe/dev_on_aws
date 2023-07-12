'''
  バケットを削除
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

def delete_bucket():
    s3client = boto3.client('s3')               # S3クライアント取得
    response = s3client.list_objects_v2(Bucket=bucket)  # バケット内の全オブジェクトを削除
    keyCount = response['KeyCount']
    if keyCount > 0:
        s3client.delete_objects(
            Bucket = bucket,
            Delete={
                    'Objects': [{
                        'Key': object['Key']
                    } for object in response['Contents']]
                })
    s3client.delete_bucket(Bucket=bucket) # バケット削除
    waiter = s3client.get_waiter('bucket_not_exists')
    waiter.wait(Bucket=bucket)
    print('Deleted bucket: ' + bucket)


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
