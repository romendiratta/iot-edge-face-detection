import paho.mqtt.client as mqtt
import logging
import sys
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set MQTT variables.
LOCAL_MQTT_HOST="broker-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc):
        logger.info(f"Connected to local broker with RC: {str(rc)}")
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    logger.info(f"Message received at: {datetime.now()} ")
  except:
    logger.info(f"Unexpected error: {sys.exc_info()[0]}")

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# Listen until stopped.
local_mqttclient.loop_forever()
