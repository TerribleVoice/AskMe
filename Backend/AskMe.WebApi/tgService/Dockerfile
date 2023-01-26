FROM python:3.8

USER root

COPY ./tgService /app

RUN cd /app && \
    apt-get -y update && \
    apt-get -y install gunicorn && \
    pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT python main.py