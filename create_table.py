import boto3
#localの場合は、access_key_id, secret_access_keyは適当でいい
dynamodb = boto3.resource(
    "dynamodb",
    region_name = "ap-northeast-1",
    endpoint_url = "http://localhost:8000",
    aws_access_key_id = "tekitou",
    aws_secret_access_key = "nandemoiiyo")

table = dynamodb.create_table(
    TableName = 'users',
    KeySchema = [
        {
            'AttributeName' : 'user_id',
            'KeyType' : 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName' : 'user_id',
            'AttributeType' : 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits' : 5,
        'WriteCapacityUnits' : 5
    }
)

#Active or not
print("Table status :", table.table_status)