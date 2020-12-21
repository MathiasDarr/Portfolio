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

TABLE_NAME = 'Articles'
table = dynamo_resource.Table(TABLE_NAME)


def insert_order(article):
    article_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'article_id': article_id,
            'title': article['title'],
            'category': article['category'],
            'content': article['content'],
            'article_date': article['article_date']
        }
    )
    return article_id


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

    title = event['body']['title']
    category = event['body']['category']
    content = event['body']['content']
    article_date = event['body']['article_date']
    article = {'title': title, 'category': category, 'content': content, 'article_date': article_date}

    article_id = insert_order(article)

    response = {"statusCode": 200, "body": json.dumps({
        "article": article_id
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response
