'''
  https://gist.github.com/reedobrien/cbbe6d728e802874940a
'''
import boto3
from boto3.dynamodb.types import STRING

table = boto3.resource("dynamodb", region_name="us-east-1").Table("UserAssets")

## Attrs for GSI
attrdef = [
            {"AttributeName": "state", "AttributeType": STRING},
            {"AttributeName": "userId", "AttributeType": STRING},
            {"AttributeName": "assetId", "AttributeType": STRING}
            ]
            
## Asset ID index definition
assetIdIdx = [
    {"Create": {
            "IndexName": "assetId-index",
            "KeySchema": [{
                "AttributeName": "assetId",
                "KeyType": "HASH"
                }],
            'Projection': {
                'ProjectionType': "ALL",

                },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    },
]

## State index definition
stateIdx = [        
    {"Create": {
            "IndexName": "state-index",
            "KeySchema": [{
                "AttributeName": "state",
                "KeyType": "HASH"
                }],
            'Projection': {
                'ProjectionType': "ALL",

                },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            }},
    ]

## User ID index definition
userIdIdx =[
    {"Create": {
            "IndexName": "userId-index",
            "KeySchema": [{
                "AttributeName": "userId",
                "KeyType": "HASH"
                }],
            'Projection': {
                'ProjectionType': "ALL",

                },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            }},
    ]

# for each index 
table.update(AttributeDefinitions=attrdef, GlobalSecondaryIndexUpdates=assetIdIdx)
table.update(AttributeDefinitions=attrdef, GlobalSecondaryIndexUpdates=userIdIdx)
table.update(AttributeDefinitions=attrdef, GlobalSecondaryIndexUpdates=stateIdx)
print("GSI Added")