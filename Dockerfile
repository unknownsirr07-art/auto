#!/usr/bin/env bash

FROM python:3.10.8-slim-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install --upgrade -r /requirements.txt

RUN mkdir /NewAuto
WORKDIR /NewAuto

COPY . /NewAuto

CMD ["/bin/bash", "start.sh"]