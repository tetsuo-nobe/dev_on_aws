# ワーク: AWS SDK で Amazon S3 を操作する

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示して 用意された環境を開いてください。
  - このサンプルでは Cloud9 の Managed temporary credentials を無効化する必要はありません。

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

4. 以後、講師の解説をききながらサンプルを実行して下さい。


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
- client06-list-object.py
  - バケットのオブジェ句のリストを取得して表示するサンプル
- client07-delete-object.py
  - バケットのオブジェクトを削除するサンプル
- client08-multipart-upload.py
  - マルチパートアップロードのサンプル
- client09-multipart-download.py
  - マルチパートダウンロードのサンプル
- client10-presigned-url.py
  - 署名付きURLを生成するサンプル
- client11-delete-bucket.py
  - バケットの中の全てのオブジェクトとバケットを削除するサンプル