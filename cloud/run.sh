#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: run.sh PORT_NUMBER S3_BUCKET_NAME"
    echo "PORT_NUMBER: Port that has been exposed on the host machine."
    echo "S3_BUCKET_NAME: Name of bucket where images will be saved."
    exit
fi

# Build broker docker image.
make build-broker
# Create docker network.
docker network create --driver=bridge cloud-network
# Start the broker.
docker run -d -p $1:1883 --network=cloud-network --name=broker-cloud broker-cloud:latest
# Build the processor docker image.
make build-processor
# Start the image processor.
docker run -d --network=cloud-network --env S3_BUCKET_NAME=$2 processor:latest
