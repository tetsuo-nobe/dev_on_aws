# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  実行コンテキストの再利用のサンプル
'''
from datetime import datetime

outside_handler = datetime.now()

def lambda_handler(event, context):

    inside_handler = datetime.now()

    print('outside_handler :' + str(outside_handler))
    print('inside_handler  :' + str(inside_handler))