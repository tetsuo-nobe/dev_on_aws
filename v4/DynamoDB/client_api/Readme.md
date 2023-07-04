## AWS SDK で DynamoDB を操作するサンプル (boto3 client API)

### ユーザーごとに各ゲームのスコアを格納するテーブルを操作する
---

* score_data.json
  - テーブルにロードするデータ
* myconfig.py
  - テーブル名の指定
* create_table.py
  - テーブルの作成
* put_item.py
  - テーブルへの項目の追加
* get_item.py
  - プライマリキーを指定した項目の取得
* query.py
  - query を使用しパーティションキーだけを指定した項目の取得
* pagenate.py
  - scan の結果をページ単位で表示
* partQL.py
  - partQL を使用した項目の取得
* upate_item.py
  - プライマリキーを指定した条件付きの項目の更新
* delete_item.py
  - プライマリキーを指定した項目の削除
* delete_table.py
  - テーブルの削除





