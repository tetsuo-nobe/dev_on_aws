# モジュールのインポート
from datetime import datetime as dt 

# 現在日時を取得して print 関数で表示
print(dt.now())

# 文字列の変数定義
message = "Hello!"

# 関数定義
def sayHello(name):
    return message + name

# 関数 sayHello を呼出し結果を表示
result = sayHello("Alex")
print("呼出し結果:" + result)

# 数値の変数定義
num1 = 4
num2 = 6
num3 = num1 + num2

# if を使用した条件分岐
if num3 == 10:
    print("10")
elif num3 < 10:
    print(" < 10")
else:
    print(" > 10")
    
# 辞書型の使用    
price = {"apple": 200, "banana" : 300}
apple_price = price["apple"]
print("apple の価格:" + str(apple_price))


