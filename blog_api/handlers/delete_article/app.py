"""
The lambda function defined here queries the category GSI

"""

import json
import boto3
from boto3.dynamodb.conditions import Key
import os


dynamo_endpoint = os.getenv('dynamo_endpoint')
# if dynamo_endpoint == 'cloud' or dynamo_endpoint =='':
#     dynamodb = boto3.resource('dynamodb')
# else:
#     dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")#,endpoint_url=dynamo_endpoint)

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Articles'
table = dynamodb.Table(TABLE_NAME)

def delete_article(article_id, article_date):
    response = table.delete_item(
        Key={
            'article_id':  article_id,
            'article_date': article_date
        }
    )
    return response

# article_id='9eefada5-e655-4410-9fb4-db62dcce243d'
# article_date ='12-17-2020'
#
# delete_article(article_id, article_date)


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

    article_id = event['pathParameters']['article_id']
    article_date = event['pathParameters']['article_date']
    # article_id ="1184eb13c-0b8e-475c-8c21-f331af51757b"
    # article_date="12-20-2020"
    response = delete_article(article_id, article_date)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "article": response,
            'headers': {"Access-Control-Allow-Origin": "*"}
        }),
    }
