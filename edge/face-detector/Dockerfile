# Using ubuntu base image.
FROM ubuntu
# No interaction when updating the system.
ENV DEBIAN_FRONTEND noninteractive
# Update ubuntu dependencies.
RUN apt-get update
# Install python dependencies.
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev
RUN pip3 install --no-cache Cython opencv-contrib-python numpy paho-mqtt
# All code will be container in app directory. 
WORKDIR /app
# Copy face detector code to docker container. 
COPY face-detector.py .
# Start python script. 
CMD ["python3", "face-detector.py"]
