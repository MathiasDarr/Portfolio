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
            'article_category': article['article_category'],
            'article_name': article['article_name'],

        }
    )


def create_portfolio_articles_table():
    try:
        resp = dynamodb.create_table(

            TableName="PortfolioArticles",
            AttributeDefinitions=[
                {
                    "AttributeName": "article_category",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "article_name",
                    "AttributeType": "S"
                },
            ],
            KeySchema=[
                {
                    "AttributeName": "article_category",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "article_name",
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
    dynamodb = boto3.resource('dynamodb') #, endpoint_url="http://localhost:8000")
    # create_portfolio_articles_table()
    # sleep(15)
    table = dynamodb.Table('PortfolioArticles')

    with open('data/portfolio_articles.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_article(row)