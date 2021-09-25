## Lambda関数 (Python)でSecrets Managerからシークレットを取得する
- demo-sm.py
  - Secrets Managerからデータベース接続情報を取得
    - シークレット名 dbsecretsは、このデモではハードコードしているが本来は環境変数で渡す
    - シークレットにアクセスするためのコードは、Secrets Managerが提供するサンプルを流用
  - データベースに接続してSQL発行、データをリターン



