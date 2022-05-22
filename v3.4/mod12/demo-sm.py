import json
import boto3
import sys
import os
import logging
import base64
from botocore.exceptions import ClientError
import pymysql
from datetime import date, datetime

# レスポンスヘッダー
HEADERS = {
    'Content-Type': 'application/json; charset=utf-8'
}

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# SQL
query = """
SELECT name, price, created_at
FROM items
WHERE deleted_at IS NULL
ORDER BY created_at DESC
"""

def get_secret():

    secret_name = "dbsecrets"
    region_name = "ap-northeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        print("GetSecretValue")
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            print("DecryptionFailureException")
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            print("InternalServiceErrorException")
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            print("InvalidParameterException")
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            print("InvalidRequestException")
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            print("ResourceNotFoundException")
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
            print("return secret")
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            print("return binary")
            return decoded_binary_secret
            

def lambda_handler(event, context):
    # DBへ接続
    try:

        print("Call get_secret")
        secret = get_secret()
        #print(secret['host'])
        print("START CONNECT")
        conn = pymysql.connect(
            secret['host'],
            user=secret['username'],
            passwd=secret['password'],
            db=secret['dbname'],
            connect_timeout=20
        )

        # queryの実行
        with conn.cursor() as cur:
            cur.execute(query)
            logger.info(cur._executed)

            item_list = cur.fetchall()

        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'headers': HEADERS,
            'body': json.dumps(item_list, default=str)
        }

    except:
        logger.error('ERROR: DB Connection error')
        return {
            'isBase64Encoded': False,
            'statusCode': 500,
            'headers': HEADERS,
            'body': []
        }
