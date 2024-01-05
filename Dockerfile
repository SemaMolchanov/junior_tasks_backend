FROM ala125050.kazincombank.kz:5000/projectoffice/ci_cd_containers/python:3.8-slim-buster

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

ARG GIT_CREDENTIALS
COPY requirements.txt /tmp
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt
RUN pip3 install gunicorn

WORKDIR /code
COPY . /code
