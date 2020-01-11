FROM python:latest

MAINTAINER InnovativeInventor

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install requests dropbox

COPY . /usr/src/app/

ENTRYPOINT [ "python", "client.py" ]
