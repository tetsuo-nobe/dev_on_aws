'''
  バケットからオブジェクトを取得：download_fileobjbを使用 (Client API)
'''
import boto3
import io
import csv
import json
from botocore.exceptions import NoCredentialsError,ClientError
from mybucket import bucket_name as bucket

key = 'item.csv'
s3client = boto3.client('s3')   # S3クライアント取得

# ローカルの csv ファイルを読み込んで Upload
def upload_fileobjb():
    with open(key, 'rb') as data:   
      s3client.upload_fileobj(data, bucket, key)                     
    print('File Uploaded: ' + key)

# csv ファイルをダウンロードして変数に保持
def download_fileobjb():
    bytes_buffer = io.BytesIO()
    s3client.download_fileobj(bucket, key, bytes_buffer)  
    
    print('File Downloaded: ' + key)
    byte_value = bytes_buffer.getvalue()
    return byte_value.decode('utf-8')

# csv フォーマットを json フォーマットに変換
def convertCSVtoJSON(input):
    jsonList = []
    keys = []
    csvReader = csv.reader(input.split('\n'), delimiter=",")

    for i, row in enumerate(csvReader):
        if i == 0:
            keys = row
        else:
            obj = {}
            for x, val in enumerate(keys):
                obj[val] = row[x]
            jsonList.append(obj)
    return json.dumps(jsonList, indent=4)

if __name__ == '__main__':
    try:
        upload_fileobjb()
        csvData = download_fileobjb()
        jsonData  = convertCSVtoJSON(csvData)
        print(jsonData)
        
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
