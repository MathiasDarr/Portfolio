"""
This script reads the customers csv file & populates the blog articles table & the comments table .
"""
# !/usr/bin/env python3


import boto3
import csv
import os
from time import sleep
import uuid


def insert_article(article, table):
    return table.put_item(
        Item={
            'article_id': article['article_id'],
            'title': article['title'],
            'category': article['category'],
            'article_date': article['article_date']
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

            ],
            KeySchema=[
                {
                    "AttributeName": "article_id",
                    "KeyType": "HASH"
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


def populate_articles_table():
    create_articles_table()
    sleep(15)
    table = dynamodb.Table('Articles')

    with open('data/articles.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_article(row, table)


def insert_comment(comment, table):
    return table.put_item(
        Item={
            'article_id':  comment['article_id'],
            'comment_id': comment['comment_id'],
            'commentor_name': comment['commentor_name'],
            'comment_time': comment['comment_time'],
            'content': comment['content']

        }
    )


def create_comments_table():
    try:
        resp = dynamodb.create_table(

            TableName="Comments",

            AttributeDefinitions=[
                {
                    "AttributeName": "article_id",
                    "AttributeType": "S"
                },

                {
                    "AttributeName": "comment_id",
                    "AttributeType": "S"
                },

            ],
            KeySchema=[
                {
                    "AttributeName": "article_id",
                    "KeyType": "HASH"
                },

                {
                    "AttributeName": "comment_id",
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


def populate_comments_table():
    create_comments_table()
    sleep(15)
    table = dynamodb.Table('Comments')

    with open('data/comments.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_comment(row, table)



if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb') #, endpoint_url="http://localhost:8000")
    # populate_articles_table()
    populate_comments_table()