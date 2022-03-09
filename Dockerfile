# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirenments.txt requirenments.txt

RUN apt update && apt install -y build-essential && apt install default-libmysqlclient-dev -y

RUN pip3 install -r requirenments.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "falcon1.app", "--timeout", "600" ]