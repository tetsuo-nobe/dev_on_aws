# ワーク: AWS Cloud9 をさわってみよう

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示して 用意された環境を開いてください。

## Cloud9 でシンプルな Python プログラムを動かしてみよう

1. Cloud9 の画面下部のターミナルで次のコマンドを実行します。
  - `git clone` コマンドで GitHub リポジトリから Python のサンプルプログラムを取得します。
  - `git` コマンドは Cloud9 に組み込まれています。
  ```
  git clone https://github.com/tetsuo-nobe/dev_on_aws
  ```

2. Python のサンプルプログラムが存在するフォルダに移動します。

  ```
  cd  dev_on_aws/v4/Cloud9
  ```

3. Cloud9 の画面左側のエクスプローラーから `dev_on_aws/v4/Cloud9/basic.py` をダブルクリックして開きます。
   - Python のコードが表示されたことを確認します。
   - Cloud9 でコードを編集して実行できます。

4. Cloud9 画面下部のターミナルで次のコマンドを実行します。
    
  ```
  python basic.py 
  ```
5. basic.py が実行されて次の例のように表示されます。
  - 最初に表示されるのは Python のコードで出力している実行日時です。
```
2023-06-25 04:52:40.315054
呼出し結果:Hello!Alex
10
apple の価格:200
```

## AWS CLI をさわってみよう

1. Cloud9 画面下部のターミナルで次のコマンドを実行して AWS CLI が使用できることを確認します。
   - Cloud9 には AWS CLI が組み込まれています。
  ```
  aws --version
  ```
   - 次のように AWS CLI のバージョンが表示されます。(バージョン番号が異なっても問題ありません。） 
  ```
  aws-cli/2.12.3 Python/3.11.4 Linux/4.14.314-238.539.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off
  ```
2. AWS CLI を使用して Amazon EC2 インスタンスの情報を表示します。 

  ```
  aws ec2 describe-instances 
  ```
   - 多くの情報が表示されることを確認します。
   - 確認後、ターミナルにプロンプトが戻らない場合は `q` キーを押下して下さい。
     
3. AWS CLI の `query` オプションを使用して Amazon EC2 インスタンスの情報の一部だけを表示します。 
   - 次の例ではインスタンス ID だけを表示しています。
  ```
  aws ec2 describe-instances  --query 'Reservations[*].Instances[*].InstanceId' 
  ```

4. AWS CLI の `query` オプションを使用して Amazon EC2 インスタンスの情報の一部だけを表示します。 
   - 次の例ではインスタンス ID と インスタンスタイプを表示しています。
  ```
  aws ec2 describe-instances  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType]' 
  ```

5. AWS CLI の `output` オプションを使用して Amazon EC2 インスタンスの情報の表示形式を指定します。 
   - 次の例では出力形式をテキストに指定しています。他にも `yaml` や `table` を試してみましょう。
  ```
  aws ec2 describe-instances  --query 'Reservations[*].Instances[*].InstanceId' --output text
  ```

---
## AWS IDE Toolkit for Cloud9 の AWS Explorer をさわってみよう

1. Cloud9 画面左側から AWS アイコンまたは AWS タブをクリックします。
   - AWS IDE Toolkit の AWS Explorer が表示されます。
   - ![s1](https://dev.nobelabo.net/images/github/s1.png)
2. Cloud9 画面左下側から `AWS:profile:default` をクリックします。
   - 接続に使用するプロファイルやロールの一覧を表示して、`profile:default` をクリックします。
   - ![s2](https://dev.nobelabo.net/images/github/s2.png)
   - ![s3](https://dev.nobelabo.net/images/github/s3.png)
3. (もし下図のようになった場合) AWS Explorer で `Add regions to AWS Explorer...` をクリックします。
   - ![s4](https://dev.nobelabo.net/images/github/s4.png)
4. (もし下図のようになった場合) AWS Explorer で現在使用しているリージョンをチェックして Enter キーを押下します。
   - ![s5](https://dev.nobelabo.net/images/github/s5.png)
6. AWS Explorer で表示されたリージョン名を展開表示します。
   - これにより、AWS リソース名の一覧が表示されます。ここから各リソースを参照できます。
   - ![s6](https://dev.nobelabo.net/images/github/s6.png)
7. AWS Explorer で表示された S3 を展開表示して 1 つ以上のバケット名が表示されることを確認します。
   - ![s7](https://dev.nobelabo.net/images/github/s7.png)
---
## ワークは以上で終了です。この環境はそのまま残しておいて下さい。後でラボ 1 でも使用します。
