# iot-edge-face-detector
### Author: Rohan Mendiratta

### Introduction
The purpose of the this repository is to demonstrate how processing can be performed between cloud and edge devices. 

### Architecture:
![](./docs/architecure.png)
In the above image, we can see how the architecure is constructed between the edge and cloud devices.

QoS(Quality Of Service): Please note that we are using the default QoS level of 0. This means that a message will be published at most once. Since this data is not vital, we are not worried losing some messages. 

On the edge device, there are 4 main processes that are running in containers. The orchestation of these containers is managed via Kubernetes. First the MQTT broker is deployed. Then a K8's sevice is created to allow other pods to access the broker. The logger is deployed next, this logger will subscribe to a topic on the MQTT broker and log each time a message is receieved on the topic. Next the face detector is deployed. This is the source of our messages. The pod accesses the camera on the edge device and scans the image for faces. If a face is detected, the image will be encoded and published to the topic. Finally the forwarder is deployed, this listens to the topic and forwards any messages to the MQTT broker in the cloud. 

On the cloud VM, there are 2 main processes that are running within containers. First the MQTT broker is created, which will receive messages from the forwarder running on the edge device. Finally there is an image processer which subscibes to a topic on the broker. When the processor receives a message, it decodes it back into an image and saves it into an S3 bucket. In this case there is no orchestration tool and the containers are run directly via docker. A Docker newtork bridge has been created to allow the processor to connect to the broker. 

### Setup
#### Cloud VM
The cloud VM must be created first. In this case we will be using an EC2 instance. You may use whatever base image, but ensure that Docker has been installed. It is also necessary that a Security Group is attached to this instance that allows a TCP connection on a port of your choosing. To access the S3 bucket without credentials, it is also neccessary that you assign a role to your EC2 instance with S3 permissions. This will allow you EC2 instance to write to the S3 bucket without credentials.

To start the container in the cloud, you will run the `run.sh OPEN_PORT S3_BUCKET_NAME` script in the cloud folder. This will take care of building the docker images locally, setting up the network bridge, and starting the services. Two arguments must be passed to this script. The first is the port that you have opened on the instance. This will allow traffic that flows to the port on the host machine to be correctly routed to the MQTT broker. The second is the S3 bucket name where the images will be stored.

#### Edge Device
The pods on the edge device can now be created. You must have a version of Kubernetes installed on your edge device (K3's is recommended). To start the pods you will run the `run.sh HOSTNAME PORT_NUMBER` script in the edge folder. This will take care of deploying all of the pods and setting up the service to allow the pods to interact with the broker. Two arguments must be passed to this script. The first is the hostname of your cloud VM. The second is the port that you have opened on your cloud VM. This will allow the forwarder to connect to the remote broker running on your cloud VM. 

NOTE: If you edge device is not using an ARM architecure, you will need to use the Dockerfiles to rebuild the images for the correct architecure. 
