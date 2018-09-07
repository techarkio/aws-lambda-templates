import json


def lambda_handler(event, context):
    # TODO: add your code to here
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
