# ワーク: AWS SAM を使って API Gateway の API と統合した Lambda 関数を作成してみよう

## このワーク環境は、ワーク実施時だけの一時的な環境になります。

---

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示してください。

3. IAM ユーザー毎に 1つの Cloud 9 IDE が用意されているので、[開く (Open)] をクリックします。

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

## AWS SAM を使用した API Gateway の API + Lambda 関数の作成

* SAM CLI を更新します。

        mkdir tmp && cd tmp
        wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
        unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
        sudo ./sam-installation/install --update
        cd ..
        rm -rf tmp

      
1. Cloud9 のターミナルで下記を実行して SAM のバージョンが `1.90.0` 以上であることを確認して下さい。

        
        sam --version
        

2. SAM のリソースを作成します。このワークでは Python の Lambda 関数を作成します。

        
        sam init --runtime python3.8
        

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
        
7. プロジェクト名を指定します。**`sam-app` の後にご自分の番号を付けて下さい。**
   
   - 下記は番号に `00` を付けた場合の例です。
   - **以後は `00` 部分はご自分の番号に置換えて下さい。**

        ```
        Project name [sam-app]: sam-app00
        ```

8. sam-app00 フォルダが作成されるので、下記の内容を確認・編集します。(**`00` 部分はご自分の番号に置換えて下さい。**)

    - SAM テンプレート
      - sam-app00/template.yaml 
        - 上記ファイルに HelloWorldFunction のプロパティに下記を追記して関数名を明示的に指定します。**`HelloWorldFunction` の後にご自分の番号を付けて下さい。**
        ```
        FunctionName: HelloWorldFunction00
        ```
        - 注意: インデントとして ` CodeUri: hello_world/` と同じ位置にしてください。

    - デプロイする Lambda 関数 (**`00` 部分はご自分の番号に置換えて下さい。**)
      - sam-app00/hello_world/app.py
        - デフォルトで **{message: hello world}** という JSON を返します。必要に応じて変更します。　
9. SAM でサーバーレスアプリケーションを構築してテストやデプロイする前準備を行います。
  -  **`00` 部分はご自分の番号に置換えて下さい。**

```
cd sam-app00
sam build
```        

10. SAM を使用しローカルでテストします。
  - (この操作には Docker が必要ですが Cloud9 は Docker を導入済ですので問題ありません。)
  ```
    sam local invoke 
  ```
  - 下記のように Lambda 関数で return している文字列が表示されることを確認します。
  ```
  {"statusCode": 200, "body": "{\"message\": \"hello world\"}`
  ```
11. sam deploy --guided を使用してデプロイを行います。
  - sam deploy --guidedを使うと、sam deploy のパラメータをファイルに保存し、以後、容易にデプロイできます。
        
        sam deploy --guided
        

  -  以後、対話的に進めていくと、指定した内容が sam deploy 実行時に必要パラメータとしてファイル（デフォルト: samconfig.toml）保存され、その後デプロイが実行されます。
  - `Stack Name [sam-app]` には、**`sam-app` にご自分の番号をつけた文字列を入力して下さい。**
  - `AWS Region` には、`ap-northeast-1` を入力して下さい。
  - その後は、**下記以外は、デフォルトのまま Enter キーを押下**して下さい。
  - `HelloWorldFunction may not have authorization defined, Is this okay? [y/N]:` には、**`y`** を入力して下さい。 
  - `Deploy this changeset? [y/N]:` にも、**y** を入力して下さい 


        
        Configuring SAM deploy
        ======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: sam-app99
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

        (以下略)
        

  -  **参考** : 1 回目のデプロイが完了後、2 回目の sam deploy を実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

        ```
        sam deploy 
        ```

12. デプロイの完了後、**Outputs** に下記のような API の URL が表示されることを確認して、ブラウザの新しいタブでアクセスします。

```
Key             HelloWorldApi
Description     API Gateway endpoint URL for Prod stage for Hello World function                                 
Value           https://in8gd5u2dk.execute-api.ap-northeast-1.amazonaws.com/Prod/hello/                                              
```
- ブラウザに `{"message": "hello world"}` と表示されることを確認して下さい。


13. SAM CLI を使用して デプロイされた Lambda 関数のテストをリモートで実行します。下記は番号に `00` を付けた場合の例です。**`00` 部分はご自分の番号に置換えて下さい。**

        sam remote invoke --stack-name sam-app00 --region ap-northeast-1

  - 下記のように Lambda 関数で return している文字列が表示されることを確認します。
  
        
        {"statusCode": 200, "body": "{\"message\": \"hello world\"}"}
        

14. SAM で作成したスタックを削除するには、`sam delete` を実行します。
  - 削除確認の入力が求められるので、`y` を入力して下さい。 
        
        sam delete

 
* 以上でワークは終了です。お疲れ様でした！

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





