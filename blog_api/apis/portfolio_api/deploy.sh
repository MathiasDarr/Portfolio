#!/bin/bash

if [[ -z $2 ]]
then
  stackname=portfolio-api-stack
else
  stackname=$2
fi

echo ${stackname}

rm -rf package.yaml

sam package \
  --template-file template.yaml \
  --s3-bucket "dakobed-serverless-apis" \
  --output-template-file package.yaml


#  awslocal api create-rest-api --region ${REGION} --name ${API_NAME}

aws cloudformation deploy \
    --template-file package.yaml \
    --stack-name ${stackname} \
    --capabilities CAPABILITY_NAMED_IAM

