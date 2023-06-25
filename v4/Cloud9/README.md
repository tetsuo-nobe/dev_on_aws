This is README.md

```
cd  dev_on_aws/v4/PythonBasic
```

```
python basic.py 
```

```
2023-06-25 04:52:40.315054
呼出し結果:Hello!Alex
10
apple の価格:200
```

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

```
aws ec2 describe-instances --instance-ids 
```



