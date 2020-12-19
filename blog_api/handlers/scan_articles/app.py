import json
import boto3
import os


dynamo_endpoint = os.getenv('dynamo_endpoint')

if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb',endpoint_url=dynamo_endpoint)



def scan_articles():
    table = dynamo_resource.Table('Articles')
    scan_results = table.scan()
    return scan_results['Items']


def lambda_handler(event, context):
    """

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    articles = scan_articles()

    response = {"statusCode": 200, "body": json.dumps({
        "articles": articles
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}

    return response
