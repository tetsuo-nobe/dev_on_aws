import boto3
from botocore.client import ClientError
from mybucket import bucket_name as bucket

try:
    s3 = boto3.resource('s3')
    s3.meta.client.head_bucket(Bucket=bucket)
    print(f'bucket {bucket} exists')
except ClientError as clienterr:
    print('!!!! ClientError !!!!')
    print(clienterr)
    error_code = clienterr.response['Error']['Code']
    print('error_code=',error_code)