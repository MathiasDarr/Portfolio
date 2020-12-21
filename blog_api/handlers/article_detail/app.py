"""
The lambda function defined here queries the category GSI

"""

import json
import boto3
from boto3.dynamodb.conditions import Key
import os


dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud' or dynamo_endpoint =='':
    dynamo = boto3.client('dynamodb')
else:
    dynamo = boto3.client('dynamodb',endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Articles'


def get_article_detail(article_id, article_date):
    response = dynamo.get_item(
        TableName=TABLE_NAME,
        Key={
            'article_id': {'S': article_id},
            'article_date': {'S': article_date}
        }
    )
    item = response['Item']
    keys = list(item.keys())
    article = {key: list(item[key].values())[0] for key in keys}

    return article


# product_name = 'Heeled Boots'
# vendor ="Blundstone"
# response = get_product_detail(vendor, product_name)


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

    # article_id = event['pathParameters']['article_id']
    # article_date = event['pathParameters']['article_date']
    article_id ="184eb13c-0b8e-475c-8c21-f331af51757b"
    article_date="12-20-2020"
    article = get_article_detail(article_id, article_date)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "article": article,
            'headers': {"Access-Control-Allow-Origin": "*"}
        }),
    }
