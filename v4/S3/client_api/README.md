# ワーク: AWS SDK for Python (boto3) で Amazon S3 を操作してみよう

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示して 用意された環境を開いてください。
  - このサンプルでは Cloud9 の Managed temporary credentials を無効化する必要はありません。

3. Python のバージョンを 3.7 から 3.9 へアップグレードします。
  - Cloud9 の画面下部のターミナルで次のコマンドを実行します。
  ```
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  cat << 'EOT' >> ~/.bashrc
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  EOT
  source ~/.bashrc
  sudo yum -y update
  sudo yum -y install bzip2-devel
  sudo yum -y install xz-devel
  pyenv install 3.9.13
  pyenv global 3.9.13
  ```

  - 次に PATH を設定します。
  ```
  export PATH="$HOME/.pyenv/shims:$PATH"
  ```

  - Python のバージョンを確認して、AWS SDK for Python (boto3) をインストールします。
  ```
  python --version
  pip install boto3
  ```

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
  - バケット名はユニークにしてください。**アンダースコアは使用できません。**
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
- client11-presigned-url.py
  - 署名付きURLを生成するサンプル
- client12-delete-bucket.py
  - バケットの中の全てのオブジェクトとバケットを削除するサンプル