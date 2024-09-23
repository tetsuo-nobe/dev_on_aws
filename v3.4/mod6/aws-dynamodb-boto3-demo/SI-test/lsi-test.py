'''
  テーブル作成時にLSIを作成し、LSIに対してQueryとScanを行う
'''
import boto3
import time
from boto3.dynamodb.conditions import Key


TABLE_NAME = "TravelerSurvey"
HTTP_STATUS_SUCCESS = 200
LSI_NAME = 'TravelerSurveyByRepAndDate'


def remove_table():
    # Name of the table
    table_name = TABLE_NAME

    # Removes the table_name from the region given as input
    try:
        rval = False
        dynamoDB = boto3.resource('dynamodb')
        table = dynamoDB.Table(table_name)
        resp = table.delete()
        #time.sleep(15)
        dynamoDB.meta.client.get_waiter('table_not_exists').wait(TableName=table_name, WaiterConfig={'Delay': 2})
        if resp['ResponseMetadata'][
                'HTTPStatusCode'] == HTTP_STATUS_SUCCESS:
            print("{0} Table has been deleted.".format(table_name))
    except Exception as err:
        print("--- Exception ---")
        print(
            "Existing table deletion failed: {0} Table".format(table_name))
        print("Error Message: {0}".format(err))
        


def create_table_wrapper():
    # Name of the table
    table_name = TABLE_NAME

    # Attributes for partition keys and sort key
    rep_id_attr_name = 'RepId'
    traveler_id_attr_name = 'TravelerId'
    contact_date_attr_name = 'ContactDate'

    # Name of the global secondary index
    lsi_name = LSI_NAME

    # Create a DynamoDB table and global secondary index
    create_table(
        table_name,
        lsi_name,
        rep_id_attr_name,
        traveler_id_attr_name,
        contact_date_attr_name)


def create_table(
        ddb_table_name,
        ddb_lsi_name,
        rep_id_attr_name,
        traveler_id_attr_name,
        contact_date_attr_name):

    dynamodb = boto3.resource('dynamodb')

    # The variables below transform the arguments into the parameters expected by dynamodb.create_table.

    table_name = ddb_table_name
    key_schema = [{'AttributeName': rep_id_attr_name, 'KeyType': 'HASH'},
                  {'AttributeName': traveler_id_attr_name, 'KeyType': 'RANGE'}]
                
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}

    local_secondary_indexes = [{
            'IndexName': ddb_lsi_name,
            'KeySchema': [
                {'AttributeName': rep_id_attr_name, 'KeyType': 'HASH'},
                {'AttributeName': contact_date_attr_name, 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'ALL'},
    }]
    attribute_definitions = [
        {'AttributeName': rep_id_attr_name, 'AttributeType': 'S'},
        {'AttributeName': traveler_id_attr_name, 'AttributeType': 'S'},
        {'AttributeName': contact_date_attr_name, 'AttributeType': 'S'}
    ]

    try:
        # Create a DynamoDB table with the parameters provided

        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      LocalSecondaryIndexes=local_secondary_indexes,
                                      )

    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))

    # Wait until the table is created before returning
    dynamodb.meta.client.get_waiter('table_exists').wait(TableName=table_name)

def  put_item_to_table(rep_id, traverler_id, contactdate):
    dynamoDB = boto3.resource('dynamodb')
    reservations_table = dynamoDB.Table(TABLE_NAME) 
    reservations_table.put_item(
        Item={
            'RepId': rep_id,
            'TravelerId': traverler_id,
            'ContactDate': contactdate})


def query_to_lsi(rep_id):
    dynamoDB = boto3.resource('dynamodb')
    table = dynamoDB.Table(TABLE_NAME)
    recs = table.query(
        IndexName=LSI_NAME,
        KeyConditionExpression=Key('RepId').eq(rep_id)
    )
    print(recs['Items'])  

def scan_to_lsi(rep_id,contactdate):
    dynamoDB = boto3.resource('dynamodb')
    table = dynamoDB.Table(TABLE_NAME)
    recs = table.scan(
        IndexName=LSI_NAME,
        FilterExpression=Key('RepId').eq(rep_id) & Key('ContactDate').begins_with(contactdate)
    )
    print(recs['Items'])  

def get_item_from_lsi(rep_id,contactdate):
   print('セカンダリインデックス(GSI/LSI)にはQuery,Scanしか操作できない。get_itemは不可')

if __name__ == '__main__':
    print('===============================================================')
    print('DynamoDB - Table creation')
    print('===============================================================')
    remove_table()
    create_table_wrapper()
    print(TABLE_NAME + " Table created")
    print("put item")
    put_item_to_table("S001","T001","2020/12/01")
    print("query to LSI")
    query_to_lsi(rep_id="S001")
    print("scan to LSI")
    scan_to_lsi(rep_id="S001",contactdate="2020/12")
    print("get item from LSI")
    get_item_from_lsi(rep_id="S001",contactdate="2020/12/01")
    print('--- END ---')

