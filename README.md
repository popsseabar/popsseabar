# Pop's SeaBar

Home of the Boardwalk Chicken

## Requirements

- [Foreman](https://github.com/ddollar/foreman)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)
- [Postgres](http://postgresapp.com/)
- [Redis](http://redis.io/)
- [Sass](http://sass-lang.com/libsass)

## Setup Local Environment

    $ mkvirtualenv --python=$(which python3) popsseabar

    $ createdb popsseabar

    $ pip install -r requirements-dev.txt

    $ echo "DATABASE_URL=postgres://localhost/popsseabar" >> .env
    $ echo "DEBUG=True" >> .env
    $ echo "DJANGO_LOG_LEVEL=DEBUG" >> .env
    $ echo "DJANGO_SETTINGS_MODULE=popsseabar.settings.development" >> .env
    $ echo "PORT=5000"
    $ echo "REDIS_URL=redis://127.0.0.1:6379/0" >> .env
    $ echo "SECRET_KEY=foobar" >> .env
    $ echo "SERVER_EMAIL=no-reply@popsseabar.com" >> .env

    $ foreman run python manage.py collectstatic --noinput
    $ foreman run python manage.py migrate

## Local Development

    $ redis-server
    $ foreman start
    $ sass --watch popsseabar/static/sass:popsseabar/static/css --style compressed

    $ open http://localhost:5000

## Deployment to Heroku

    $ git push

    $ heroku run python manage.py migrate

