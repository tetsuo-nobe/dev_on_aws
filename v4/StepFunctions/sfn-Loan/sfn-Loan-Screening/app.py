import json
import random

def lambda_handler(event, context):
    outcome = ['Passed','Failed']
    result = random.sample(outcome, 1)
    return {
        "statusCode": 200,
        "body": result[0]
    }
