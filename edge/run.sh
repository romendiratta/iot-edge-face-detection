#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: run.sh HOSTNAME PORT_NUMBER"
    echo "HOSTNAME: Hostname of the remote machine."
    echo "PORT_NUMBER: Port number that has been exposed on the host machine."
    exit
fi

# Deploy broker.
make deploy-broker
# Create broker service. This will allow the pods to connect to the broker.
make deploy-broker-service
# Deploy logger.
make deploy-logger
# Deploy forwarder.
echo | cat ./kubernetes/deployments/forwarder-deployment.yaml | sed "s/{{HOST}}/$1/g" | sed "s/{{PORT}}/$2/g" | kubectl apply -f -
# Deploy face-detector.
make deploy-face-detector


