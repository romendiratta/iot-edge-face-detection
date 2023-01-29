import logging
import cv2
import paho.mqtt.client as mqtt
import boto3

# Set up logger.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up MQTT variables
LOCAL_MQTT_HOST="broker-cloud"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces-cloud"

# Define behavior on connect.
def on_connect_local(client, userdata, flags, rc):
    logger.info(f"Connected to local broker with RC: {str(rc)}")
    client.subscribe(LOCAL_MQTT_TOPIC)
# Define behavior on received msg. 
def on_message_local(client, userdata, msg):
    logger.info(f"{msg}")

# Setup connection to MQTT broker. 
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message_local

local_mqttclient.loop_forever()
