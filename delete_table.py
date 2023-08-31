import boto3
dynamodb = boto3.resource(
    "dynamodb",
    region_name = "ap-northeast-1",
    endpoint_url = "http://localhost:8000",
    aws_access_key_id = "tekitou",
    aws_secret_access_key = "nandemoiiyo")

table = dynamodb.Table("users")

table.delete()

dynamodb = boto3.client(
    "dynamodb",
    region_name = "ap-northeast-1",
    endpoint_url = "http://localhost:8000",
    aws_access_key_id = "watasihanekoinudesu",
    aws_secret_access_key = "anatahanyankodesu")

tables = dynamodb.list_tables()
print("Table Lists: ", tables["TableNames"])