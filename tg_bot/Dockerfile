FROM python:3.10

USER root

ENV ROOT_DIR /app
WORKDIR $ROOT_DIR

COPY ./tg_bot/app/ $ROOT_DIR

RUN apt-get -y update && \
    pip install -r ./settings/requirements.txt

ENTRYPOINT python engine.py