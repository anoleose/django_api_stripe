FROM python:3.10

RUN python -m venv venv
RUN pip install --upgrade pip
WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
  	build-essential \
  	libpq-dev \
  	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /project/


