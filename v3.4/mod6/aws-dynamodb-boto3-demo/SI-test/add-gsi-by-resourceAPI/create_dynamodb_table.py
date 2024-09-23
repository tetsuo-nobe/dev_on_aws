import boto3

TABLE_NAME='UserAssets'

def drop_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
        # dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    table.delete()
    dynamodb.meta.client.get_waiter('table_not_exists').wait(TableName=TABLE_NAME, WaiterConfig={'Delay': 2})

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
        #dynamodb = boto3.resource('dynamodb')
    # テーブル作成
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'userId',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'assetId',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'userId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'assetId',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    dynamodb.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
    return table

def put_userAsset(userId, assetId, state, table):
    # put_item実行
    response = table.put_item(
       Item={
            'userId': userId,
            'assetId': assetId,
            'state': state
        }
    )
    return response

if __name__ == '__main__':
    drop_table()
    print("Table dropped")
    table = create_table()
    print("Table status:", table.table_status)
    put_userAsset('U001','A001','S1',table)
    put_userAsset('U001','A002','S2',table)
    put_userAsset('U002','A003','S1',table)
    put_userAsset('U002','A004','S2',table)
    print("-- Finished --")


