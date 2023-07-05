# ワーク: AWS Lambda 関数を作成してテスト実行してみよう

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. AWS Lambda のページを表示してください。

3. 以降の手順を実施して Lambda 関数を作成、テスト事項して下さい。

4. Lambda 関数の作成
  - 関数名: `work-function`
  - ランタイム: **Python 3.9**
  - デフォルトの実行ロールの変更
    - **既存のロールを使用する**
    - **LambdaPollyRole**
  - - [**関数の作成**] をクリック
5. Lambda 関数のコードの作成
  - コード: このフォルダにある lambda_function.py の内容に置換える
    - コード変更後は [**Deploy**] をクリックする
6. Lambda 関数のテスト実行
  - [**テスト**] タブをクリック
  - イベント名: `work-event`
  - イベント JSON:このフォルダにある event.json の内容に置換える
  - [**保存**] をクリック
  - [**テスト**] をクリック
  - 緑色の [**実行中の関数: 成功 (ログ)**] が表示されることを確認して
  - [**詳細**]をクリックして展開表示
  - 下記が表示されていることを確認
     ```
     {
       "statusCode": 200,
       "body": "Hello! Alex"
     }
     ```
  - [**ログ出力**]部分を確認
  - [**テスト**] をクリックする毎に、[**ログ出力**] の [**outside_handler**] と [**inside_handler**] の値はどうなるかを確認
---

* lambda_function.py
  - Lambda 関数のコード
* event.json
  - Lambda 関数のテストで使用する event オブジェクト用の JSON





