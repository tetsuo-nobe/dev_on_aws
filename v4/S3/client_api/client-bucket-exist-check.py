import boto3
from botocore.client import ClientError
from mybucket import bucket_name as bucket

try:
    s3client = boto3.client('s3')
    s3client.head_bucket(Bucket=bucket)
    print(f'bucket {bucket} exists')
except ClientError as clienterr:
    print('!!!! ClientError !!!!')
    print(clienterr)
    error_code = clienterr.response['Error']['Code']
    print('error_code=',error_code)