import json
import uuid
import boto3
from datetime import datetime

table = boto3.resource("dynamodb").Table("orders")

def lambda_handler(event, context):
    body = json.loads(event.get("body") or "{}")
    order = {
        "OrderId": str(uuid.uuid4()),
        "item": body.get("item", "unknown"),
        "quantity": int(body.get("quantity", 1)),
        "status": "PLACED",
        "createdAt": datetime.utcnow().isoformat()
    }
    table.put_item(Item=order)
    return {
        "statusCode": 201,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(order)
    }