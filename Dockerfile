FROM ubuntu:latest
COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get install -y ffmpeg
RUN apt-get install -y alsa-utils
RUN apt-get install -y python3-pip
RUN apt install -y libjpeg-dev zlib1g-dev
RUN pip3 install Pillow
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /
CMD [ "python3","main.py"]