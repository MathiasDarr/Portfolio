### Portfolio ###
* This repository contains my portfolio/blog project developed using Vue JS & AWS Severless Application Model SAM
* Deployed as a static website to S3 & AWS Route 53 at www.dalinar-mir.com 

### Technologies Used ### 
* Vue JS, Vuex state store, Vuetify 
* AWS S3, AWS Route 53
* AWS SAM serverless API developed using API Gateway, Lambda & DynamoDB 

### Projects Showcased ###
* Snotel Data Pipeline & Query API
    * Dockerized Data Pipeline scrapes data from USDA & Pushes data to DynamoDB
    * Serverless API allows for querying snowpack data
      
* Spring Ecommerce Microservices
    * Kafka message broker
    * DynamoDB backend
    * Scrape product detail data from Rei.com
* Spring RideShare Microservices
    * Data Model using Apache Cassandra & PostgreSQL 

* Music Information Retrieval Deep Learning Project
    * Neural network developed using Keras & trained on AWS GPU instance

* Twitter Airflow Pipeline
    * Stream tweets using Java twitter4j library pushing data into elastic search & kafka
    * Apache Airflow DAG writes data to S3 using parquet format every hour
    
* Twitter Spark Analysis
    * Apply language identification model using Spark Streaming which ingests data from Kafka  
    * Spark ML pipeline applies transformations
    * Stanford Core NLP used for dependency parsing & applying a sentiment analysis model
    
* Serverless ECommerce FullStack Application
    * API Gateway Developed using AWS SAM 
    * Front end developed using Vue JS, Vuex, Vuetify, 
    * AWS cognito for issuing JWT tokens to authenticated users

* Serverless Data Processing Applications
    * Move data using AWS Kinesis, Firehose, SQS for moving data into DynamoDB & AWS s3
    * CloudFormation templates for deploying 

* Serverless Upload Application
    * AWS Cognito for issuing JWT tokens to authenticated users
    * Serverless API issues presigned URLs to allow users to upload files to S3
    * Upload files are pushed to SQS queue for further processing
    * Python script running on EC2 instance polls the SQS queue for files to process and runs Librosa transforms
    
    