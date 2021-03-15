FROM python:3
# send python output straight to terminal
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt

ENV FLASK_APP=flask_server

COPY . /code/

