FROM python:3.6
WORKDIR /djangoApp
COPY djangoApp/damnificados/requirements.txt /djangoApp/requirements.txt
RUN pip install -r requirements.txt
COPY djangoApp/damnificados/ /djangoApp
CMD manage.py makemigrations
CMD manage.py migrate
CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application