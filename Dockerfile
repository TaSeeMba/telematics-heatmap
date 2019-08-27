FROM python:3.7-slim

COPY app /app

WORKDIR /app

RUN ls -l

RUN pip install -r requirements.txt

CMD python main.py