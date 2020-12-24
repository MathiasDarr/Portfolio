#!/bin/bash

if [[ -z $2 ]]
then
  stackname=dakobed-blog-upload-api-stack
else
  stackname=$2
fi

aws cloudformation delete_stack --stack-name ${stackname}