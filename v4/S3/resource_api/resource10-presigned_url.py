# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  署名付きURLを生成
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name

def presigned_url():
    KEY = 'cat.jpg'                                     # オブジェクトのキー
    s3 = boto3.resource('s3')                           # S3クライアント取得
    url =  s3.meta.client.generate_presigned_url(       # 署名付きURL生成
            ClientMethod = 'get_object',
            Params = {'Bucket' : bucket_name, 'Key' : KEY},
            ExpiresIn = 30,
            HttpMethod = 'GET')
    print('Presigned URL: ', url)

if __name__ == '__main__':
    try:
        presigned_url()
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