import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

BUCKET = os.getenv('UploadBucket')

def lambda_handler(event, context):


    response = {"statusCode": 200, "body": json.dumps({
        "presigned": event
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response

