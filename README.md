# django_api_stripe

## Test this repository

```
git clone https://github.com/anoleose/django_api_stripe.git
cd django_api_stripe 
python -m venv venv
linux os: source venv/bin/activate
windows os: venv\Scripts\activate 
pip install django 
pip install -r requirements.txt
```

## Run the server locally 

```
python manage.py makemigrations
python migrate
python createsuperuser
python manage.py runserver 
```
Go to [localhost](http://127.0.0.1:8000)


## Docker

 ###### create Dockerfile file
```
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
```
###### create docker-compose.yml file
```
version: "3.10"

services:

  app:
    build: 
      context: .
    volumes:
      - .:/project
    ports:
      - "8000:8000"
    env_file: .env
    image: app:django
    container_name: django_api_stripe
    command: 
      sh -c 
      "python manage.py migrate && 
        python manage.py runserver 0.0.0.0:8000"
    
```
Go to [localhost](http://127.0.0.1:8000)



