#!/bin/bash
python manage.py makemigrations
python manage.py migrate personas zero
python manage.py migrate lugares zero
python manage.py migrate articulo zero
python manage.py migrate user zero

gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application