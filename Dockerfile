FROM python:3.7-alpine

MAINTAINER EveryThingIsData

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache  postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual ./temp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt

RUN apk del ./temp-build-deps

COPY . /app
WORKDIR /app

RUN adduser -D dockuser
RUN chown dockuser:dockuser -R /app/
USER dockuser