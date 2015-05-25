# Pop's SeaBar

Home of the Boardwalk Chicken


## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url


## How to Use

To use this project, follow these steps:

1. Create and enter a new project directory.
2. Create a working environment.
3. Create your new project using this template.


## Local Development

    $ createdb popsseabar

    $ pip install -r requirements.txt
    $ foreman run python manage.py collectstatic
    $ foreman run python manage.py migrate

    $ foreman start
    $ open http://localhost:5000


## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create foo
    $ heroku config:set ALLOWED_HOSTS=foo.herokuapp.com
    $ heroku config:set DEBUG=off
    $ heroku config:set SECRET_KEY=bar
    $ git push heroku master

    $ heroku run python manage.py migrate

You can replace ``foo`` with your desired Heroku app name and ``bar`` with your production secret key.


## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

