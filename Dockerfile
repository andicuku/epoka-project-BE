FROM python:3.11-slim-buster
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt ./
RUN pip install pip --upgrade
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

COPY . .