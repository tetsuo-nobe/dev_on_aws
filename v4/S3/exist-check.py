import boto3
from botocore.client import ClientError

try:
    s3 = boto3.resource('s3')
    bucket_name = "tnobe-presign"
    s3.meta.client.head_bucket(Bucket=bucket_name)
    print(f'bucket {bucket_name} exists')
except ClientError as clienterr:
    print('!!!! ClientError !!!!')
    print(clienterr)
    error_code = clienterr.response['Error']['Code']
    print('error_code=',error_code)