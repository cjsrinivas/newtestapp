import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('This is another try of the latest Hello World without Abel yet again!')
    }
