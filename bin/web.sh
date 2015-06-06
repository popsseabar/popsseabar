#!/bin/sh

if [ $DJANGO_SETTINGS_MODULE = "popsseabar.settings.development" ]; then
    PYTHONUNBUFFERED=True python manage.py runserver
    # PYTHONUNBUFFERED=True python -m pdb manage.py runserver
else
    gunicorn popsseabar.wsgi --log-file -
fi
