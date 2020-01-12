FROM python:latest

MAINTAINER InnovativeInventor

WORKDIR /usr/src/app

RUN pip install requests dropbox

COPY . /usr/src/app/

ENTRYPOINT [ "python", "client.py" ]
