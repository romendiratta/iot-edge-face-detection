FROM alpine:latest
# Make sure that the output is not buffered.
ENV PYTHONUNBUFFERED=1
# Add python and pip.
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
# Install MQTT python package.
RUN pip3 install --no-cache paho-mqtt
# Copy logger file into the container.
WORKDIR /app
COPY logger.py .
# Execute python scipt. 
CMD ["python3", "logger.py"]
