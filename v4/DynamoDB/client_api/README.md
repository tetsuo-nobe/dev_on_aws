# ワーク: AWS SDK for Python (boto3) で Amazon DynamoDB を操作してみよう

## 準備

1. ラボ用 URL にアクセスして、サインインして、コースのパネルの [Open] を選択して下さい。

1. **ラボ 3 (Python)** の **起動** ボタンをクリックして下さい。

1. ページ上部にある **ラボを開始する** (オレンジのボタン）をクリックして下さい。
   
1. ページ上部にある **コンソールを開く** (オレンジのボタン）をクリックして、AWS マネジメントコンソールにサインインしてください。

1. ラボのガイドに基づき、VS Code Server 環境を開いてください。
   
## サンプルのプログラムを動かしてみよう

1. VS Code Server の画面下部のターミナルで次のコマンドを実行します。
  - `git clone` コマンドで GitHub リポジトリから AWS SDK for Python (boto3) のサンプルを取得します。
  - `git` コマンドは VS Code Server に組み込まれています。
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





