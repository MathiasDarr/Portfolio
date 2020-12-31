import boto3
import os
from boto3.dynamodb.conditions import Key
import json


dynamo_endpoint = os.getenv('dynamo_endpoint')
if dynamo_endpoint == 'cloud':
    dynamo_resource = boto3.resource('dynamodb')
else:
    dynamo_resource = boto3.resource('dynamodb', endpoint_url=dynamo_endpoint)

TABLE_NAME = 'Comments'
table = dynamo_resource.Table(TABLE_NAME)


def query_comments_by_article_id(article_id):
    comments = table.query(
        KeyConditionExpression=Key('article_id').eq(article_id)
    )
    comments = comments['Items']
    return comments


def lambda_handler(event, context):

    article_id = event['pathParameters']['article_id']
    comments = query_comments_by_article_id(article_id)
    response = {"statusCode": 200, "body": json.dumps({
        "orders": comments
    }), 'headers': {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}}
    return response
