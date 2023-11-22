# ワーク: AWS SDK for Python (boto3) で Amazon DynamoDB を操作してみよう

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示して 用意された環境を開いてください。
  - このサンプルでは Cloud9 の Managed temporary credentials を無効化する必要はありません。

3. Cloud9 の画面下部のターミナルで次のコマンドを実行し、Python のバージョンが 3.8 以上であることを確認します。
  
  ```
  python --version
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
  cd  dev_on_aws/v4/DynamoDB/client_api
  ```

3. 以後、講師の解説をききながらサンプルを実行して下さい。


## クライアント API を使用するサンプル

### ユーザーごとに各ゲームのスコアを格納するテーブルを操作する
---

* score_data.json
  - テーブルにロードするデータ
* myconfig.py
  - テーブル名やセカンダリインデックス名の指定
* create_table.py
  - テーブルの作成
* put_item.py
  - テーブルへの項目の追加
* get_item.py
  - プライマリキーを指定した項目の取得
* query.py
  - query を使用しパーティションキーだけを指定した項目の取得
* pagenate_scan.py
  - scan の結果をページ単位で表示
* pagenate_query.py
  - query の結果をページ単位で表示
* partQL.py
  - partQL を使用した項目の取得
* upate_item.py
  - プライマリキーを指定した条件付きの項目の更新
  - ReturnValues パラメータに指定できる値は、[こちら](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_item.html)
* add_gsi.py
  - グローバルセカンダリインデックスの作成
* query_gsi.py
  - グローバルセカンダリインデックスへのクエリー実行
* delete_item.py
  - プライマリキーを指定した項目の削除  
* delete_table.py
  - テーブルの削除





