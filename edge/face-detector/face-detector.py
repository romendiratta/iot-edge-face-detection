import logging
import cv2
import paho.mqtt.client as mqtt
import time


# Set up logger.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up MQTT variables
LOCAL_MQTT_HOST="broker-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

# Setup connection to MQTT broker. 
def on_connect_local(client, userdata, flags, rc):
        logger.info(f"Connected to local broker with RC: {str(rc)}")
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# Load Haar feature face capture.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

logger.info("Beginning camera capture.")
cap = cv2.VideoCapture(0) 

while(True):
    # Capture frame-by-frame.
    ret, frame = cap.read()

    # Convert frame to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in image. 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Only process if face has been detected.
        if x and y and w and h:
            # Cut out face from the frame.
            roi_gray = gray[y:y+h, x:x+w]
            # Encode image for publishing.
            rc,png = cv2.imencode('.png', roi_gray)
            # Convert face to bytes.
            msg = png.tobytes()
            # Publish message to topic. 
            local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg)  
	    # Sleep so image can only be sent every 3 seconds. 

