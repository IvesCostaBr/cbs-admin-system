FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY . .




