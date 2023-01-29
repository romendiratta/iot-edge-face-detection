FROM ubuntu
# No interaction when updating the system.
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
# Update ubuntu dependencies.
RUN apt-get update
# Install python dependencies.
RUN apt install -y python3 python3-pip  python3-opencv vim-tiny  libopencv-dev
RUN pip3 install --no-cache Cython opencv-contrib-python numpy paho-mqtt boto3
# All code will be container in app directory. 
WORKDIR /app
# Copy processor code to docker container. 
COPY processor.py .
# Start python script. 
CMD ["python3", "processor.py"]
