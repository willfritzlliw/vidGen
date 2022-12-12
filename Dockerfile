FROM nvidia/cuda:10.2-base
COPY ./requirements.txt /requirements.txt
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y ffmpeg
RUN apt-get install -y alsa-utils
RUN apt-get install -y python3-pip
RUN apt install -y libjpeg-dev zlib1g-dev
RUN pip3 install Pillow
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /
CMD [ "python","videoGen.py"]