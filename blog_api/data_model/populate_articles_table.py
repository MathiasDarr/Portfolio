"""
This script reads the customers csv file & populates the customers table.
dynamoDB table.
"""
# !/usr/bin/env python3


import boto3
import csv
import os
from time import sleep
import uuid


def insert_article(article):
    return table.put_item(
        Item={
            'article_id': str(uuid.uuid4()),
            'title': article['title'],
            'category': article['category'],
            'article_date':article['article_date']
        }
    )


def create_articles_table():
    try:
        resp = dynamodb.create_table(

            TableName="Articles",

            AttributeDefinitions=[
                {
                    "AttributeName": "article_id",
                    "AttributeType": "S"
                },

                {
                    "AttributeName": "article_date",
                    "AttributeType": "S"
                },

            ],
            KeySchema=[
                {
                    "AttributeName": "article_id",
                    "KeyType": "HASH"
                },

                {
                    "AttributeName": "article_date",
                    "KeyType": "RANGE"
                },

            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            },
        )
        return resp
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:4566")
    dynamodb = boto3.resource('dynamodb') #, endpoint_url="http://localhost:8000")
    create_articles_table()
    sleep(15)
    table = dynamodb.Table('Articles')

    with open('data/articles.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_article(row)
