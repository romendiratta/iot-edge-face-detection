#!/bin/bash

# Deploy broker.
make deploy-broker
# Create broker service. This will allow the pods to connect to the broker.
make broker-service
# Deploy logger.
make deploy-logger
# Create secrets needed for forwarder. This will allow the forwarder to connect to the remote host. 
# make deploy-secrets
# Deploy forwarder.
# make deploy-forwarder
# Deploy face-detector.
make deploy-face-detector


