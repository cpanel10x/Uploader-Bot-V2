FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN mkdir /Uploader-Bot-V2
WORKDIR /Uploader-Bot-V2
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
