FROM python:3.8-alpine

MAINTAINER bharatmca@gmail.com

WORKDIR /app

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY . /app

RUN adduser -D myuser
USER myuser
