'''
  テーブル作成時にGSIを作成し、GSIに対してQueryとScanを行う
'''
import boto3
import time
from boto3.dynamodb.conditions import Key


RESERVATIONS_TABLE_NAME = "Reservations"
HTTP_STATUS_SUCCESS = 200
GSI_NAME = 'ReservationsByCityDate'


def remove_reservations_table():
    # Name of the table
    table_name = RESERVATIONS_TABLE_NAME

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
        


def create_reservations_table_wrapper():
    # Name of the table
    table_name = RESERVATIONS_TABLE_NAME

    # Attributes for partition keys and sort key
    customer_id_attr_name = 'CustomerId'
    city_attr_name = 'City'
    date_attr_name = 'Date'

    # Name of the global secondary index
    gsi_name = GSI_NAME

    # Create a DynamoDB table and global secondary index
    create_reservations_table(
        table_name,
        gsi_name,
        customer_id_attr_name,
        city_attr_name,
        date_attr_name)


def create_reservations_table(
        ddb_table_name,
        ddb_gsi_name,
        customer_id_attr_name,
        city_attr_name,
        date_attr_name):

    dynamodb = boto3.resource('dynamodb')

    # The variables below transform the arguments into the parameters expected by dynamodb.create_table.

    table_name = ddb_table_name
    key_schema = [{'AttributeName': customer_id_attr_name, 'KeyType': 'HASH'}]
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}

    global_secondary_indexes = [{
            'IndexName': ddb_gsi_name,
            'KeySchema': [
                {'AttributeName': city_attr_name, 'KeyType': 'HASH'},
                {'AttributeName': date_attr_name, 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'ALL'},
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    }]
    attribute_definitions = [
        {'AttributeName': customer_id_attr_name, 'AttributeType': 'S'},
        {'AttributeName': city_attr_name, 'AttributeType': 'S'},
        {'AttributeName': date_attr_name, 'AttributeType': 'S'}
    ]

    try:
        # Create a DynamoDB table with the parameters provided

        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      GlobalSecondaryIndexes=global_secondary_indexes,
                                      )

    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))

    # Wait until the table is created before returning
    dynamodb.meta.client.get_waiter('table_exists').wait(TableName=table_name)

def  put_item_to_table(customer_id, city, date):
    dynamoDB = boto3.resource('dynamodb')
    reservations_table = dynamoDB.Table(RESERVATIONS_TABLE_NAME) 
    reservations_table.put_item(
        Item={
            'CustomerId': customer_id,
            'City': city,
            'Date': date})


def query_to_gsi(city):
    dynamoDB = boto3.resource('dynamodb')
    reservations_table = dynamoDB.Table(RESERVATIONS_TABLE_NAME)
    recs = reservations_table.query(
        IndexName=GSI_NAME,
        KeyConditionExpression=Key('City').eq(city)
    )
    print(recs['Items'])  

def scan_to_gsi(city):
    dynamoDB = boto3.resource('dynamodb')
    reservations_table = dynamoDB.Table(RESERVATIONS_TABLE_NAME)
    recs = reservations_table.scan(
        IndexName=GSI_NAME,
        FilterExpression=Key('City').eq(city)
    )
    print(recs['Items'])  

def get_item_from_gsi(city,date):
   print('セカンダリインデックス(GSI/LSI)にはQuery,Scanしか操作できない。get_itemは不可')

if __name__ == '__main__':
    print('===============================================================')
    print('DynamoDB - Reservations Table creation')
    print('===============================================================')
    remove_reservations_table()
    create_reservations_table_wrapper()
    print(RESERVATIONS_TABLE_NAME + " Table created")
    print("put item")
    put_item_to_table("C001","Reno","2020/12/01")
    
    print("query to gsi")
    query_to_gsi(city="Reno")
    print("scan to gsi")
    scan_to_gsi(city="Reno")
    print("get item from gsi")
    get_item_from_gsi(city="Reno",date="2020/12/01") # 'セカンダリインデックス(GSI/LSI)にはQuery,Scanしか操作できない。get_itemは不可'
    print('--- END ---')

