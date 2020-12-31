
import boto3
import os
from datetime import datetime
import re
import json
from boto3.dynamodb.types import Decimal
import uuid


region = os.getenv('region')

dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Comments'
table = dynamo_resource.Table(TABLE_NAME)


def insert_comment(comment):
    return table.put_item(
        Item={
            'article_id':  comment['article_id'],
            'comment_id': comment['comment_id'],
            'commentor_name': comment['commentor_name'],
            'comment_time': comment['comment_time'],
            'content': comment['content']

        })


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

    article_id = event['body']['article_id']
    commentor_name = event['body']['commentor_name']
    content = event['body']['content']

    current_date = str(datetime.now())[:-7]
    current_date = re.sub(r"[ ,.;@#?!&$:-]+", '', current_date)
    comment = {'article_id': article_id, 'comment_id': str(uuid.uuid4()), 'commentor_name': commentor_name, 'content': content, 'comment_time': current_date}

    insert_comment(comment)

    response = {"statusCode": 200, "body": json.dumps({
        "comment": comment['comment_id']
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response
