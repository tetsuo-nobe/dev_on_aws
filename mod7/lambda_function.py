# Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  ���s�R���e�L�X�g�̍ė��p�̃T���v��
'''
from datetime import datetime

outside_handler = datetime.now()

def lambda_handler(event, context):

    inside_handler = datetime.now()

    print('outside_handler :' + str(outside_handler))
    print('inside_handler  :' + str(inside_handler))