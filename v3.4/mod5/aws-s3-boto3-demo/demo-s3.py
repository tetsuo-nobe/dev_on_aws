# Copyright 2021 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  AWS SDK for Python (boto3)で S3の基本的な操作を行うサンプル
'''
import boto3
from botocore.exceptions import NoCredentialsError,ClientError

if __name__ == '__main__':
    try:
      # S3とのセッション開始
      s3 = boto3.resource('s3')    # S3リソース取得

      # バケット名
      bucket_name = "tnobe-s3-sample-0313"   # バケット名

      # バケットの作成
      create_bucket_config = {}    # バケットの構成を作成
      create_bucket_config["LocationConstraint"] = "ap-northeast-1"  # リージョンの指定
      s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=create_bucket_config)  # バケットの作成
      print('Created bucket: ' + bucket_name)
    
      # バケットにオブジェクトを格納
      file_path= "C:\\temp\\Eiffel.jpg"     # アップロードするオブジェクトのファイルパスを指定
      key = "Eiffel.jpg"                    # アップロードするオブジェクトのキーを指定
      bucket = s3.Bucket(bucket_name)
      bucket.upload_file(file_path, key)    # アップロード実行
      print('File Upload: ' + file_path) 

      # バケット内のオブジェクトのリストを取得して表示
      prefix = "Ei"                        # prefixの指定       
      list = s3.Bucket(bucket_name).objects.filter(Prefix=prefix) # バケット内の該当オブジェクトのリストを取得
      for object in list:                                    # 取得したリストを表示
        print('Matched: ' + object.key)

      # バケットからオブジェクトを取得
      file_path= "C:\\temp\\Eiffel_downloaded.jpg"    # ダウンロードするオブジェクトのファイルパスを指定
      key = "Eiffel.jpg"                              # ダウンロードするオブジェクトのキーを指定
      bucket.download_file(key, file_path)            # ダウンロード実行
      print('File Downloaded: ' + file_path)

      # バケットからオブジェクトを削除
      key = 'Eiffel.jpg'                     # オブジェクトのキー(ファイル名)
      s3obj = s3.Object(bucket_name,key)     # バケット名とキーを指定してオブジェクト作成
      s3obj.delete()                         # 削除実行
      s3obj.wait_until_not_exists()          # 削除完了を確認
      print("Deleted :" + key)

      # バケットの削除
      bucket = s3.Bucket(bucket_name)         # S3バケット取得
      for object in bucket.objects.all():     # バケット内の全オブジェクトを削除
        object.delete()
      bucket.delete()                         # バケット削除
      print('Deleted bucket: ' + bucket_name)

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

