FROM alpine:latest
# Add mosquitto broker.
RUN apk add --no-cache mosquitto
# Configure to allow remote access.
RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf
# Start the broker.
CMD ["mosquitto","-v","-c","/etc/mosquitto/mosquitto.conf"]
