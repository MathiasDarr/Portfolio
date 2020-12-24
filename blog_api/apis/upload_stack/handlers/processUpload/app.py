import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

BUCKET = os.getenv('UploadBucket')
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    key = body['key']

    object_acl = s3.ObjectAcl(BUCKET, key)
    response = object_acl.put(ACL='public-read')

    response = {"statusCode": 200, "body": json.dumps({
        "presigned": response
    }), 'headers': {"Access-Control-Allow-Origin": "*"}}
    return response

