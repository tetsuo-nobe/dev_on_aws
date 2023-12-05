# ワーク: AWS SDK for Python (boto3) で Amazon S3 を操作してみよう

## 準備

1. ラボ用 URL にアクセスして、サインインして下さい。

1. **ラボ 2 (Python)** の **起動** ボタンをクリックして下さい。

1. ページ上部にある **ラボを開始する** ボタンをクリックして下さい。
   
1. ページ上部にある **コンソールを開く** のボタンをクリックして、AWS マネジメントコンソールにサインインしてください。

1. AWS マネジメントコンソールで、ページ上部の検索窓で `Cloud9` と入力し、表示されるメニューから **Cloud9** の部分をクリックして下さい。  

1. Cloud9 のページで、**Lab2** という環境を開いてください。

## Cloud9 でサンプルのプログラムを動かしてみよう

1. Cloud9 の画面下部のターミナルで次のコマンドを実行します。
  - `git clone` コマンドで GitHub リポジトリから AWS SDK for Python (boto3) のサンプルを取得します。
  - `git` コマンドは Cloud9 に組み込まれています。
  ```
  git clone https://github.com/tetsuo-nobe/dev_on_aws
  ```

2. AWS SDK for Python (boto3) のサンプルが存在するフォルダに移動します。
  - **サンプルは必ずこのフォルダから実行します。**
  ```
  cd  dev_on_aws/v4/S3/client_api
  ```

3. Cloud9 の左側のナビゲーターより、**dev_on_aws/v4/S3/client_api/mybucket.py** を開きます。
  - bucket_name に、このワーク用のバケット名を指定します。
  - バケット名はユニークにしてください。(下記は例です。) **アンダースコアは使用できません。**
  ```
  bucket_name = 'tnobe-s3-sample'
  ```

4. 以後、講師の解説をききながらサンプルを実行して下さい。
  - 例: client-bucket-exist-check.py を実行する場合
  ```
  python  client-bucket-exist-check.py
  ```

## クライアント API を使用するサンプル

***
- mybucket.py
  - サンプルで使用するバケット名を指定するファイル
- AWSIcons.zip
  - サンプルで使用するデータ
- cat.jpg
  - サンプルで使用する画像
- Eiffel.jpg
  - サンプルで使用する画像
- client-bucket-exist-check.py
  - バケットの存在チェックを行うサンプル
- client00-list-bucket.py
  - バケットのリストを取得して表示するサンプル
- client01-create-bucket.py
  - バケットを作成するサンプル
- client02-put-object.py
  - バケットにオブジェクトを格納するサンプル
- client03-upload-file.py
  - バケットにファイルをアップロードするサンプル
- client04-get-object.py
  - バケットからオブジェクトを取得するサンプル
- client05-download-file.py
  - バケットからファイルとしてダウンロードするサンプル
- client06-upload-download-fileobjb.py
  - 変数データのアップロードとダウンロードして変数に保持するサンプル
- client07-list-object.py
  - バケットのオブジェ句のリストを取得して表示するサンプル
- client08-delete-object.py
  - バケットのオブジェクトを削除するサンプル
- client09-multipart-upload.py
  - マルチパートアップロードのサンプル
- client10-multipart-download.py
  - マルチパートダウンロードのサンプル
- client11-presigned_url.py
  - 署名付きURLを生成するサンプル
- client12-delete-bucket.py
  - バケットの中の全てのオブジェクトとバケットを削除するサンプル
