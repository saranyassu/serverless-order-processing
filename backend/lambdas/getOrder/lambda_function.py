import json
import boto3

table = boto3.resource("dynamodb").Table("orders")

def lambda_handler(event, context):
    order_id = (event.get("pathParameters") or {}).get("id")
    item = table.get_item(Key={"OrderId": order_id}).get("Item")
    if not item:
        return {"statusCode": 404, "body": json.dumps({"message": "Not found"})}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(item, default=str)
    }