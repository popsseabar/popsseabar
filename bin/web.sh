#!/bin/sh

if [ $DJANGO_SETTINGS_MODULE = "settings.development" ]; then
    PYTHONUNBUFFERED=True python manage.py runserver
else
    gunicorn wsgi --log-file -
fi
