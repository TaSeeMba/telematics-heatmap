FROM ubuntu:18.10

LABEL maintainer="Tasimba Chirindo"

RUN apt-get update
RUN apt-get install -y python3 python3-pip nginx
RUN pip3 install uwsgi

RUN rm -v /etc/nginx/nginx.conf
ADD config/nginx.conf /etc/nginx/

COPY app ./app
WORKDIR /app

RUN ls -l

RUN pip3 install -r requirements.txt

COPY config/nginx.conf /etc/nginx/sites-enabled/default

CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app
