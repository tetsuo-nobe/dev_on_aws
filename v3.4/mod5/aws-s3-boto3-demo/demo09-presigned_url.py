# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  署名付きURLを生成
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

def presigned_url():
    BUCKET = 'tnobe-presign'                            # バケット名
    KEY = 'cat.jpg'                                     # オブジェクトのキー
    s3client = boto3.client('s3')                       # S3クライアント取得
    url =  s3client.generate_presigned_url(             # 署名付きURL生成
            ClientMethod = 'get_object',
            Params = {'Bucket' : BUCKET, 'Key' : KEY},
            ExpiresIn = 35,
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