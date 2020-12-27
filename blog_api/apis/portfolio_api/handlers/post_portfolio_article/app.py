import boto3
import os

from datetime import datetime
import re
import json
import uuid


dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)

TABLE_NAME = 'PortfolioArticles'
table = dynamo_resource.Table(TABLE_NAME)


def insert_order(article):

    table.put_item(
        Item={
            'article_category': article['article_category'],
            'article_name': article['article_name'],
            'content': article['content']
        }
    )


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

    article_category = event['body']['article_category']
    article_name = event['body']['article_name']

    content = event['body']['content']

    portfolio_article = {'article_category': article_category, 'content': content, 'article_name':article_name, 'preview':content[:450]}

    insert_order(portfolio_article)

    response = {"statusCode": 200, "body": json.dumps({
        "article": "success"
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response

