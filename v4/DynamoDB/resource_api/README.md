## AWS SDK で DynamoDB を操作するサンプル (boto3 resource API)
### 下記のドキュメントの内容をベースにいくつかのサンプルを追加
#### https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/GettingStarted.html

***

- demo-dynamodb-basic.py
  - DynamoDBに対する基本操作を実行する
- demo-dynamodb-query-scam.py
  - DynamoDBテーブルにQueryやScanを実行する
- moviedata.json
  - サンプルデータ
- MoviesCreateTable.py
  - Moviesテーブルの作成
    - パーティションキーはyear、ソートキーはtitle
    - ReadCapacityUnitとWriteCapacityUnitは10
- MoviesDeleteTable.py
  - Moviesテーブルの削除
- MoviesItemOps01.py
  - put_itemを使用した項目の追加/置換え
- MoviesItemOps02.py
  - get_itemを使用した項目の取得
- MoviesItemOps02ProjectionExpression.py
  - get_itemを使用した項目の取得。対象属性も指定する
- MoviesItemOps02ReservedWords.py
  - get_itemを使用した項目の取得。対象属性も指定する。ただし属性名が予約語の場合はプレースホルダ使用
- MoviesItemOps03.py
  - update_itemを使用した項目の更新
- MoviesItemOps04.py
  - update_itemを使用した項目の更新。既存の値をもとに算出した値を更新値とする
- MoviesItemOps05.py
  - update_itemを使用した項目の更新。条件に合致した場合のみ更新実行する
- MoviesItemOps06.py
  - delete_itemを使用した項目の削除。条件に合致した場合のみ削除実行する
- MoviesLoadData.py
  - サンプルデータのロード用
- MoviesQuery01.py
  - queryを使用した検索。パーティションキーの等価条件だけ指定する
- MoviesQuery02.py
  - queryを使用した検索。パーティションキーの等価条件とソートキーの値の範囲を指定するケース
- MoviesScan.py
  - delete_itemをテーブルのスキャン。
    - Scanは常にテーブルから全項目を取出す。
    - FilterExpressionがあればそこで指定した項目をピックアップして返す
- Pagenate-sample
  - ページングしながら複数の項目を取得するサンプル
    - pagenate-test0.py
      - サンプル用のテーブルの作成とサンプル用の項目の作成
    - pagenate-test1.py
      - Scanと Limitの基本的な使い方やレスポンスを確認する
    - pagenate-test2.py
      - Scan実行時に Limitを指定して区切りながらに項目を取得する。
    - pagenate-test9-delete.py
      - サンプル用のテーブルの削除  
    - testdata.json
      - サンプル用のデータ






