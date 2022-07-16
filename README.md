# dbsiproject

Youtube Link: https://youtu.be/T_yEXAxunes

Guide to integrate Django with Redis: (Mac)


Commands to run on terminal:

## Install redis:
1. brew intall redis
2. brew services start redis
3. To check if the redis server is running use command- 
redis-cli 
Send PING and you will see a PONG response back. "exit" once checked. 
or
telnet 127.0.0.1 6379

## Installing Django:
pipenv install django

## Installing django-redis plugin
django-redis 5.0.0

## Running the server
python3 manage.py runserver


Information about the project:

* Open the project with visual studio

* Our app name - RedisApp inside Django Project

* Using Open API -  
- Access the JSON API directly from here: https://data.cityofnewyork.us/resource/s3k6-
pzi2.json
- API Docs: https://dev.socrata.com/foundry/data.cityofnewyork.us/s3k6-pzi2

* Model SchoolItem Created to store the response in the database.

* URLS created:
- http://127.0.0.1:8000/highschooldirectory
- http://127.0.0.1:8000/q1Data
- http://127.0.0.1:8000/q2Data
- http://127.0.0.1:8000/q3Data
- http://127.0.0.1:8000/q4Data
- http://127.0.0.1:8000/database

* Most important files:
- views.py
- models.py
- config.py
- templates package


* cache setup in settings.py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

* 