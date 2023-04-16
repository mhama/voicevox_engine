#!/bin/bash
# build docker container and upload to AWS ECR
# usage:
# ./build_docker_awslambda.sh "new-tag-name"
#
set -eu

export imagetag="$1"
export ecrurl="393863632510.dkr.ecr.ap-northeast-1.amazonaws.com/vvengine-lambda2023"

docker buildx build -t vvengine:${imagetag} --target aws-lambda-runtime-env . 
docker tag vvengine:${imagetag} ${ecrurl}:${imagetag}
docker push ${ecrurl}:${imagetag}

