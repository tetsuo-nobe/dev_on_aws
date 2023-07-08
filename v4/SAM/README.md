# ワーク: AWS SAM を使って API Gateway の API と統合した Lambda 関数を作成してみよう

## このワーク環境は、ワーク実施時だけの一時的な環境になります。

---

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示してください。

3. IAM ユーザー毎に 1つの Cloud 9 IDE が用意されているので、[開く (Open)] をクリックします。

---

## 手順
* 以降の手順を実施して AWS SAM で API Gateway の API + Lambda 関数を作成して下さい。
      
1. Cloud9 のターミナルで下記を実行して SAM のバージョンを確認します。

        
        sam --version
        

1. SAM のリソースを作成します。デモでは Python の Lambda 関数を作成します。

        
        sam init --runtime python3.7
        

1. テンプレートを選択します。このデモでは、1のAWS Quick Start Templatesを選択します。

        
        Choose an AWS Quick Start application template
              1 - Hello World Example
              2 - Infrastructure event management
              3 - Multi-step workflow
              4 - Serverless Connector Hello World Example
              5 - Multi-step workflow with Connectors
        Choice: 1
        

1. アプリケーションのテンプレートを選択します。このデモでは、1 の Hello World Example を選択します。

        
        Choose an AWS Quick Start application template
                1 - Hello World Example
                2 - Infrastructure event management
                3 - Multi-step workflow
        Template: 1
        

1. AWS X-Ray によるトレース取得の有効化または無効化を指定します。このデモでは、そのまま Enter キーを押下して N (無効化)を選択します。

        
        Based on your selections, the only Package type available is Zip.
        We will proceed to selecting the Package type as Zip.

        Based on your selections, the only dependency manager available is pip.
        We will proceed copying the template using pip.

        Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: 

1. Amazon CloudWatch Application Insights によるモニタリングを指定します。このデモでは、そのまま Enter キーを押下して N (無効化)を選択します。  

        Would you like to enable monitoring using CloudWatch Application Insights?
        For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: 

1. プロジェクト名を指定します。**`sam-app` の後にご自分の番号を付けて下さい。**
  1. 下記は番号に `00` を付けた場合の例です。

        
        Project name [sam-app]: sam-app00
        
1. sam-app00 フォルダが作成されるので、下記の内容を確認・編集します。
  1. **以後は `00` 部分はご自分の番号に置換えて下さい。**

  1. SAM テンプレート
    1. sam-app00/template.yaml 
      1. 上記ファイルに HelloWorldFunction のプロパティに下記を追記して関数名を明示的に指定します。**`HelloWorldFunction` の後にご自分の番号を付けて下さい。**
        1.  `FunctionName: HelloWorldFunction00`
        1. 注意: インデントとして ` CodeUri: hello_world/` と同じ位置にしてください。
    1. デプロイする Lambda 関数
      1. sam-app00/hello_world/app.py
      1. デフォルトで {message: hello world}という JSON を返します。必要に応じて変更します。　

1. SAM でサーバーレスアプリケーションを構築してテストやデプロイする前準備を行います。
  1. **`00` 部分はご自分の番号に置換えて下さい。**
        
        cd sam-app00
        sam build
        

1. SAM を使用しローカルでテストします。
  1. (この操作には Docker が必要ですが Cloud9 は Docker を導入済ですので問題ありません。)

        
        sam local invoke 
        
  1. 下記のように Lambda 関数で return している文字列が表示されることを確認します。
    1. `{"statusCode": 200, "body": "{\"message\": \"hello world\"}`

1. sam deploy --guided を使用してデプロイを行います。
  1. sam deploy --guidedを使うと、sam deploy のパラメータをファイルに保存し、以後、容易にデプロイできます。
        
        sam deploy --guided
        

  1. 以後、対話的に進めていくと、指定した内容が sam deploy 実行時に必要パラメータとしてファイル（デフォルト: samconfig.toml）保存され、その後デプロイが実行されます。

        
        Configuring SAM deploy
        ======================

                Looking for config file [samconfig.toml] :  Not found

                Setting default arguments for 'sam deploy'
                =========================================
                Stack Name [sam-app]: aws-sam-demo-app
                AWS Region [ap-northeast-1]: 
                #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
                Confirm changes before deploy [y/N]: 
                #SAM needs permission to be able to create roles to connect to the resources in your template
                Allow SAM CLI IAM role creation [Y/n]: 
                #Preserves the state of previously provisioned resources when an operation fails
                Disable rollback [y/N]: 
                HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
                Save arguments to configuration file [Y/n]: 
                SAM configuration file [samconfig.toml]: 
                SAM configuration environment [default]: 

                Looking for resources needed for deployment:
                Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-31392rxojqwi
                A different default S3 bucket can be set in samconfig.toml
        (以下略)
        
  1. 以上でデプロイは完了です！

  1. **参考** : 1 回目のデプロイが完了後、2 回目の sam deploy を実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

        
        sam deploy 
        
1. SAM で作成したスタックを削除するには、`sam delete` を実行します。

        
        sam delete

  - 削除確認の入力が求められるので、`y` を入力して下さい。 
 <br />
 <br />
 <br />


## その他のローカルテスト用のコマンド 

Lambda 関数
        
        sam local start-lambda
        

        
        aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
        

API Gateway
        
        sam local start-api
        

        
        curl http://127.0.0.1:3000/hello
        





