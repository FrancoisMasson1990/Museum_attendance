FROM tiangolo/uvicorn-gunicorn:python3.10-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app

ADD requirements.txt .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache

COPY . .