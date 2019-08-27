FROM python:3.7-slim

LABEL maintainer="Tasimba Chirindo"

RUN apt-get update
# uWSGI is a C application, so you need a C compiler (like gcc or clang) and the Python development headers for deployments on Debian-based distros.
RUN apt-get install -y build-essential python3-dev nginx
RUN pip install uwsgi

RUN rm -v /etc/nginx/nginx.conf
ADD config/nginx.conf /etc/nginx/

COPY app ./app
WORKDIR /app

RUN pip install -r requirements.txt

COPY config/nginx.conf /etc/nginx/sites-enabled/default

CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app
