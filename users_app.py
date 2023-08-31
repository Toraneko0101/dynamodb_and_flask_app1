from flask import Flask, request, jsonify, render_template, redirect, url_for
import boto3
from botocore.exceptions import NoCredentialsError
from operator import itemgetter

app = Flask(__name__)
#localの場合は、access_key_id, secret_access_keyは適当でいい
dynamodb = boto3.resource(
    "dynamodb",
    region_name = "ap-northeast-1",
    endpoint_url = "http://localhost:8000",
    aws_access_key_id = "tekitou",
    aws_secret_access_key = "nandemoiiyo")

table_name = "users"
table = dynamodb.Table(table_name)

@app.route("/")
def index():
    scan = table.scan()["Items"]
    items = sorted(scan, key=itemgetter("user_id")) #sort
    return render_template("index.html", items = items)

@app.route("/create_item", methods=["POST"])
def create_item():
    user_id = int(request.form["user_id"])
    user_age = int(request.form["user_age"])
    user_name = request.form["user_name"]
    
    table.put_item(
        Item = {
            'user_id' : user_id,
            'user_age' : user_age,
            'user_name' : user_name
        }
    )
    item = table.get_item(Key={"user_id" : user_id})
    print(item["Item"])
    
    return redirect(url_for("index", status="add"))

@app.route("/update_item", methods=["POST"])
def update_item():
    user_id = int(request.form["user_id"])
    user_age = int(request.form["user_age"])
    user_name = request.form["user_name"]
    
    table.update_item(
        Key = {
            'user_id' : user_id
        },
        ExpressionAttributeNames = {
            '#age' : 'user_age',
            '#name' : 'user_name'
        },
        ExpressionAttributeValues = {
            ':col1' : user_age,
            ':col2' : user_name
        },
        UpdateExpression = 'set #age = :col1, #name = :col2',
        ReturnValues = 'UPDATED_NEW'
    )
    
    item = table.get_item(Key= {'user_id' : user_id})
    print(item["Item"])
    
    return redirect(url_for("index", status="update"))

@app.route("/delete_item", methods=["POST"])
def delete_item():
    user_id = int(request.form["user_id"])
    table.delete_item(Key={"user_id": user_id})
    #url_forは該当の関数名のrender_templateへ戻る    
    return redirect(url_for("index", status="delete"))
    
if __name__ == "__main__":
    app.run(debug=True)
    




