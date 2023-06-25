# モジュール 3 : Cloud9 のワーク

## 準備

1. 講師のガイドにもとづき、AWS マネジメントコンソールにサインインしてください。

2. Cloud9 のページを表示して 用意された環境を開いてください。

## Cloud9　でシンプルな Python プログラムを動かしてみよう

1. Cloud9 の画面下部のターミナルで次のコマンドを実行します。
  - `git clone` コマンドで GitHub リポジトリから Python のサンプルプログラムを取得します。
  - `git` は Cloud9 に組み込まれています。
```
git clone https://github.com/tetsuo-nobe/dev_on_aws
```

1. Python のサンプルプログラムが存在するフォルダに移動します。

```
cd  dev_on_aws/v4/Cloud9
```
1. Cloud9 の画面左側のエクスプローラーから `dev_on_aws/v4/Cloud9/basic.py` をダブルクリックして開きます。
   * 

```
python basic.py 
```

```
2023-06-25 04:52:40.315054
呼出し結果:Hello!Alex
10
apple の価格:200
```

## AWS CLI をさわってみよう


```
aws --version
```

```
aws-cli/2.12.3 Python/3.11.4 Linux/4.14.314-238.539.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off
```

```
aws ec2 describe-instances 
```

q を押す

```
aws ec2 describe-instances  --query 'Reservations[*].Instances[*].InstanceId' 
```

```
aws ec2 describe-instances  --query 'Reservations[*].Instances[*].InstanceId' --output text
```

```
aws ec2 describe-instances  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType]' 
```

---
## AWS IDE Toolkit for Cloud9 の AWS Explorer をさわってみよう


