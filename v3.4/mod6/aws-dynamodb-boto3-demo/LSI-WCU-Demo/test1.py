import json
import boto3
from boto3.dynamodb.conditions import Key

table_name = 'AttributeNameTest'
print(table_name)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

'''
response = table.query(
        KeyConditionExpression=Key('customerId').eq("1")
    )
'''
response = table.query(
        KeyConditionExpression=Key('customerID').eq("1")
    )

print(response['Items'])