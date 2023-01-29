import paho.mqtt.client as mqtt
import logging
import sys
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set local MQTT variables.
LOCAL_MQTT_HOST="broker-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

# Set cloud MQTT variables.
CLOUD_MQTT_HOST=os.environ["CLOUD_MQTT_HOST"].strip()
CLOUD_MQTT_PORT=int(os.environ["CLOUD_MQTT_PORT"].strip())
CLOUD_MQTT_TOPIC="faces-cloud"

def on_connect_local(client, userdata, flags, rc):
        logger.info(f"Connected to local broker with RC: {str(rc)}")
        client.subscribe(LOCAL_MQTT_TOPIC)
        
def on_connect_cloud(client, userdata, flags, rc):
        logger.info(f"Connected to cloud broker with RC: {str(rc)}")
	
def on_message_local(client,userdata, msg):
  try:
    # Rebroadcast message to remote MQTT broker.
    cloud_mqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg.payload, retain=False)
  except:
    logger.info(f"Unexpected error: {sys.exc_info()[0]}")

# Setup local MQTT client.
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message_local

# Setup cloud MQTT client.
cloud_mqttclient = mqtt.Client()
cloud_mqttclient.on_connect = on_connect_cloud
cloud_mqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)

# Listen until stopped.
local_mqttclient.loop_forever()
