# ワーク: AWS SAM を使って API Gateway の API と統合した Lambda 関数を作成してみよう

## このワーク環境は、ワーク実施時だけの一時的な環境になります。

---

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. **東京リージョン**で、`Cloud9` のページを表示してください。

3. IAM ユーザー毎に 1つの Cloud 9 IDE が用意されているので、[開く (Open)] をクリックします

4. Notification のダイアログが表示された場合は [OK] をクリックします。

---

## Cloud9 の一時認証情報の無効化
1. Cloud9 画面の右上にある**歯車アイコン**をクリックします。
1. Preferences タブ の左側で **AWS Settings** をクリックします。
1. 右側の **Credentials** にある **AWS managed temporary credentials** トグルを OFFにします。
  ![codepipeline-demo-img](https://eks.nobelabo.net/images/mod7-cloud9.png)
1. Preferences のタブを閉じます。

---

## 現在の IAM ロールの確認

1. Cloud9 のターミナルで次のコマンドを実行します。 
   ```
   aws sts get-caller-identity
   ```
1. 出力された Arn に、**my-SAM-Work-Role** という文字が含まれていることを確認します。

---

## Cloud9 のディスク容量の拡張

- SAM のビルド時に Docker イメージを使用するため、ディスク容量が不足する場合があります。以下の手順でディスク容量を拡張してください。

1. Cloud9 のターミナルで、リサイズ用のスクリプトをダウンロードします。
   ```
   wget https://tnobep-work-public.s3.ap-northeast-1.amazonaws.com/sam-work/resize.sh
   ```

2. スクリプトに実行権限を付与し、実行します（下記の例では 30 GiB に拡張）。
   ```
   chmod +x resize.sh
   ./resize.sh 30
   ```

---

## AWS SAM を使用した API Gateway の API + Lambda 関数の作成
      
1. Cloud9 のターミナルで下記を実行して SAM のバージョンが `1.90.0` 以上であることを確認してください。

        
        sam --version
        

2. SAM のリソースを作成します。このワークでは Python の Lambda 関数を作成します。

        
        sam init --runtime python3.14
        

3. テンプレートを選択します。このワークでは、1 の AWS Quick Start Templatesを選択します。

        
        Which template source would you like to use?
               1 - AWS Quick Start Templates
               2 - Custom Template Location
        Choice: 1
        

4. アプリケーションのテンプレートを選択します。このワークでは、1 の Hello World Example を選択します。

        Choose an AWS Quick Start application template
                1 - Hello World Example
                2 - Hello World Example with Powertools for AWS Lambda
                3 - Infrastructure event management
                4 - Multi-step workflow
                5 - Lambda EFS example
                6 - Serverless Connector Hello World Example
                7 - Multi-step workflow with Connectors
        Template: 1
        
5. AWS X-Ray によるトレース取得の有効化または無効化を指定します。このワークでは、そのまま Enter キーを押下して N (無効化)を選択します。

        
        Based on your selections, the only Package type available is Zip.
        We will proceed to selecting the Package type as Zip.

        Based on your selections, the only dependency manager available is pip.
        We will proceed copying the template using pip.

        Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: 
        
6. Amazon CloudWatch Application Insights によるモニタリングを指定します。このワークでは、そのまま Enter キーを押下して N (無効化)を選択します。  
        
        Would you like to enable monitoring using CloudWatch Application Insights?
        For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]:

7. Lambda 関数で構造化された JSON フォーマットのログの出力を指定します。このワークでは、そのまま Enter キーを押下して N (無効化)を選択します。  

        Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]:
   
        
8. プロジェクト名を指定します。**`sam-app` の後にご自分の番号を付けてください。**
   
   - 下記は番号に `00` を付けた場合の例です。
   - **以後は `00` 部分はご自分の番号に置換えてください。**

        ```
        sam-app00
        ```

9. sam-app00 フォルダが作成されるので、下記の内容を確認・編集します。(**`00` 部分はご自分の番号に置換えてください。**)

    - SAM テンプレート
      - sam-app00/template.yaml 
        - 上記ファイルに HelloWorldFunction のプロパティに下記を追記して関数名を明示的に指定します。**`HelloWorldFunction` の後にご自分の番号を付けてください。**
        ```
        FunctionName: HelloWorldFunction00
        ```
        - 注意: インデントとして ` CodeUri: hello_world/` と同じ位置にしてください。
        - 注意: ファイル編集後は、Ctrl + s キーまたは [File] メニューから [Save] を選択して編集内容を保存してください。

    - デプロイする Lambda 関数 (**`00` 部分はご自分の番号に置換えてください。**)
      - sam-app00/hello_world/app.py
        - デフォルトでは **{message: hello world}** という JSON を返すコードになっています。
        - このワークでは、API Gateway の GET メソッドのクエリパラメータ `name` の値を取得して、`hello <name の値>` を返すようにコードを変更します。
        - `app.py` を開き、`lambda_handler` 関数の内容を以下のように書き換えてください:
        ```python
        import json

        def lambda_handler(event, context):
            # クエリパラメータから name の値を取得
            params = event.get("queryStringParameters")
            if params and "name" in params:
                name = params["name"]
            else:
                name = "world"

            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": f"hello {name}",
                }),
            }
        ```

        - 注意: ファイル編集後は、Ctrl + s キーまたは [File] メニューから [Save] を選択して編集内容を保存してください。
        - これにより、`/hello?name=SAM` のようにアクセスすると `{"message": "hello SAM"}` が返されます。
        - クエリパラメータ `name` を省略した場合は、デフォルトで `{"message": "hello world"}` が返されます。

10. sam-app00/hello_world/requirements.txt を開きます。
    - `request` の記載を `pymysql` に書き換えます。
    - **これにより、SAM のビルド時に pymysql パッケージが関数に取り込まれ、デプロイ時に関数コードと一緒にまとめてデプロイできます。**
    - (今回のコードでは実際は pymysql を使用しませんが、**SAM によりパッケージと取込みが容易に行えることを確認して下さい。**）
    - 注意: ファイル編集後は、Ctrl + s キーまたは [File] メニューから [Save] を選択して編集内容を保存してください。

11. SAM でサーバーレスアプリケーションのビルドを行い、依存性を解決し、テストやデプロイする前準備を行います。
  -  **`00` 部分はご自分の番号に置換えてください。**

```
cd sam-app00
```

  -  ビルド前にテンプレートの検証を行います。
```
sam validate
```



  - ( sam build で --use-container オプションを使用する場合 Docker が必要ですが Cloud9 は Docker を導入済ですので問題ありません。)
```
sam build  --use-container
```        

12. SAM を使用しローカルでテストします。
  - (この操作には Docker が必要ですが Cloud9 は Docker を導入済ですので問題ありません。)
  ```
    sam local invoke 
  ```
  - 下記のように Lambda 関数で return している文字列が表示されることを確認します。
  ```
  {"statusCode": 200, "body": "{\"message\": \"hello world\"}"}
  ```

### event.json を使用したローカルテスト

  - Lambda 関数に渡すイベントデータを JSON ファイルとして作成し、ローカルテストに使用できます。
  - これにより、API Gateway からのリクエスト（クエリパラメータ付き）をシミュレートしたテストが可能になります。

  **ステップ 1: SAM CLI でサンプルイベントを生成する**
  
  - SAM CLI には、各種 AWS サービスのサンプルイベントを生成する機能があります。API Gateway の GET メソッドのイベントを生成してファイルに保存します。

  ```
  sam local generate-event apigateway aws-proxy --method GET > events/event.json
  ```

  **ステップ 2: event.json を編集してクエリパラメータを設定する**

  - 生成された `events/event.json` を開き、`queryStringParameters` フィールドを探して以下のように編集します:
  ```json
  "queryStringParameters": {
    "name": "SAM"
  },
  ```
  - 注意: ファイル編集後は、Ctrl + s キーまたは [File] メニューから [Save] を選択して編集内容を保存してください。
  - これにより、`/hello?name=SAM` でアクセスした場合と同じイベントをシミュレートできます。

  **ステップ 3: event.json を使用してローカルで Lambda 関数をテストする**

  - `--event` (または `-e`) オプションでイベントファイルを指定して、Lambda 関数をローカルで呼び出します。
  ```
  sam local invoke --event events/event.json
  ```

  - 下記のように、クエリパラメータ `name` の値が反映された結果が表示されることを確認します:
  ```
  {"statusCode": 200, "body": "{\"message\": \"hello SAM\"}"}
  ```

---

### デプロイ

13. sam deploy --guided を使用してデプロイを行います。
  - sam deploy --guidedを使うと、sam deploy のパラメータをファイルに保存し、以後、容易にデプロイできます。
        
        sam deploy --guided
        

  -  以後、対話的に進めていくと、指定した内容が sam deploy 実行時に必要パラメータとしてファイル（デフォルト: samconfig.toml）保存され、その後デプロイが実行されます。
  - `Stack Name [sam-app]` には、**`sam-app` にご自分の番号をつけた文字列を入力してください。**
  - `AWS Region` には、`ap-northeast-1` を入力してください。
  - その後は、**下記以外は、デフォルトのまま Enter キーを押下**してください。
  - `HelloWorldFunction may not have authorization defined, Is this okay? [y/N]:` には、**`y`** を入力してください。 
  - `Deploy this changeset? [y/N]:` にも、**y** を入力してください 


        
        Configuring SAM deploy
        ======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app99]: 
        AWS Region [us-east-1]: ap-northeast-1
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: 
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: 
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: 
        HelloWorldFunction has no authentication. Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: 
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 


        (以下略)
        

  -  **参考** : 1 回目のデプロイが完了後、2 回目の sam deploy を実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

        ```
        sam deploy 
        ```

14. デプロイの完了後、**Outputs** に下記のような API の URL が表示されることを確認して、ブラウザの新しいタブでアクセスします。

```
Key             HelloWorldApi
Description     API Gateway endpoint URL for Prod stage for Hello World function                                 
Value           https://in8gd5u2dk.execute-api.ap-northeast-1.amazonaws.com/Prod/hello/                                              
```
- ブラウザに `{"message": "hello world"}` と表示されることを確認してください。
- マネジメントコンソールで、Lambda 関数がデプロイされ、API Gateway の API と統合されていることを確認してください。

- 次に、ブラウザで API の URL にクエリパラメータ `name` を付けてアクセスしてみましょう。手順 14 で確認した API の URL の末尾に `?name=あなたの名前` を追加します。
    - 例: `https://in8gd5u2dk.execute-api.ap-northeast-1.amazonaws.com/Prod/hello/?name=Taro`
- ブラウザに `{"message": "hello Taro"}` のように、指定した名前が表示されることを確認してください。

---

### デプロイ後のリモートテスト

15. SAM CLI を使用して デプロイされた Lambda 関数のテストをリモートで実行します。下記は番号に `00` を付けた場合の例です。**`00` 部分はご自分の番号に置換えてください。**

        sam remote invoke --stack-name sam-app00 --region ap-northeast-1

  - 下記のように Lambda 関数で return している文字列が表示されることを確認します。
  
        
        {"statusCode": 200, "body": "{\"message\": \"hello world\"}"}


16. (応用) リモートテストでもイベントを使用する

  - デプロイ後の Lambda 関数に対しても、イベントファイルを指定してリモートテストを実行できます。**`00` 部分はご自分の番号に置換えてください。**
  ```
  sam remote invoke --stack-name sam-app00 --region ap-northeast-1 --event-file events/event.json
  ```

  - これにより、デプロイ済みの関数に対して特定のイベントデータを送信し、動作を確認できます。


17. sam-app00/hello_world/app.py を開き、Lambda 関数が return する message の文字列（例: `f"hello {name}"` の `hello` 部分）を他の文字列に変更して保存します。**`00` 部分はご自分の番号に置換えてください。**　その後、下記のコマンドで再度デプロイして API でアクセスし、表示される文字列が変更されていることを確認してください。また、前の手順と同じように`sam remote invoke` も実行してください。

        sam build --use-container

        sam deploy 


    * イメージを取得するための Disk space が無くてエラーになった場合は、次のコマンドを実行してみてください

      ```
      docker image prune -a
      ```
---

### スタックの削除

18. SAM で作成したスタックを削除するには、`sam delete` を実行します。
  - 削除確認の入力が 2 回求められるので、`y` を入力してください。
  - (参考) y の応答なしで削除する場合は、`--no-prompts` オプションをつけます。
        
        sam delete

* 以上でワークは終了です。お疲れ様でした！

## このワーク環境は、ワーク実施時だけの一時的な環境になります。
 <br />
 <br />
 <br />

---

## 参考: その他のローカルテスト用のコマンド 

- Amazon API Gateway

  1. SAM CLI でテスト用の API エンドポイントを起動 (停止する時は Ctrl + c)
  
  ```
  sam local start-api
  ```

  2. 新しいターミナルを開き、curl コマンドでテスト実行   

  ```
  curl http://127.0.0.1:3000/hello
  ```

---

## 参考: sam local generate-event で生成できるイベントの種類

- SAM CLI では、さまざまな AWS サービスのイベントをシミュレートできます。利用可能なサービス一覧を確認するには:
  ```
  sam local generate-event --help
  ```

- 代表的なイベントソース:
  | サービス | コマンド例 | 説明 |
  |---------|-----------|------|
  | API Gateway | `sam local generate-event apigateway aws-proxy` | REST API プロキシ統合イベント |
  | S3 | `sam local generate-event s3 put` | S3 オブジェクト作成イベント |
  | DynamoDB | `sam local generate-event dynamodb update` | DynamoDB ストリームイベント |
  | SNS | `sam local generate-event sns notification` | SNS 通知イベント |
  | SQS | `sam local generate-event sqs receive-message` | SQS メッセージ受信イベント |
  | CloudWatch Events | `sam local generate-event cloudwatch scheduled-event` | スケジュールイベント |

- 各イベントで指定できるオプションの確認方法:
  ```
  sam local generate-event apigateway aws-proxy --help
  ```





