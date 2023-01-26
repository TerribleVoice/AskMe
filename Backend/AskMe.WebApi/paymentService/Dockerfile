FROM python:3.8

USER root

COPY ./paymentService /app

RUN cd /app && \
    apt-get -y update && \
    apt-get -y install gunicorn && \
    pip install -r requirements.txt

WORKDIR /app

ENV HOST 0.0.0.0
ENV PORT 4554

EXPOSE 4554

ENTRYPOINT python main.py