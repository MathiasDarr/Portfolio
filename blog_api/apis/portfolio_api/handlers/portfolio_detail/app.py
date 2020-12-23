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

TABLE_NAME = 'PortfolioArticles'


def get_article_detail(article_category, article_name):
    response = dynamo.get_item(
        TableName=TABLE_NAME,
        Key={
            'article_category': {'S': article_category},
            'article_name': {'S': article_name}
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

    article_category = event['pathParameters']['article_category']
    article_name = event['pathParameters']['article_name']
    article = get_article_detail(article_category, article_name)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "article": article,
            'headers': {"Access-Control-Allow-Origin": "*"}
        }),
    }
