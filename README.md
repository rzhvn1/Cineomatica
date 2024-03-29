# Cinematica API

Cinematica API is an website, where you can book and buy tickets for the movies you want to see.  This project is heavily inspired by the [Cinematica](https://cinematica.kg) website. It's very easy to use and I hope you enjoy it!

Click here to open Heroku ---> [Cinematica API](https://neo-cinema.herokuapp.com)


## Getting Started

Follow the instructions and enjoy API!

### Prerequisites	

First clone this repository with following instruction:
```
git clone "this repository"
```
Then you need to build containers with the following command:
```
docker-compose up --build
```

### Create database and user
```
docker exec -it cinema_db bash
su postgres
psql
CREATE DATABASE cinema;
CREATE USER cinema_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE cinema TO cinema_admin;
```

### Running the migrations
```
docker-compose run --rm cinema python manage.py migrate
```

### Creating a superuser
```
docker-compose run --rm cinema python manage.py createsuperuser
```

### Running 
```
docker-compose up
```

### Built With

* [Python](https://www.python.org) - is an interpreted high-level general-purpose programming language.
* [Postman](https://www.postman.com) - s an API platform for building and using APIs
* [Django](https://docs.djangoproject.com/en/4.0/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs used
* [PostgreSQL](https://www.postgresql.org) - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
* [Docker](https://www.docker.com) - Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

### Postman Collections

* [Click Here](https://www.getpostman.com/collections/bc6119ae05fb84bc6eb8) to open the project's Postman collections

## Authors

* Erzhan Muratov

## Acknowledgments

* Карина (My Mentor)
* Адиль Дуйшеналиев
* Медет Мусаев
* Имамидинов Агахан