import boto3

client = boto3.client('dynamodb')

try:
    resp = client.delete_table(
        TableName="Books",
    )
    print("Table deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)
