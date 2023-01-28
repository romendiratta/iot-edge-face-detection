#!/bin/bash

# Deploy broker.
make deploy-broker
# Create broker service. This will allow the pods to connect to the broker.
make deploy-broker-service
# Deploy logger.
make deploy-logger
# Deploy forwarder.
# make deploy-forwarder
# Deploy face-detector.
make deploy-face-detector


