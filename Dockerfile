FROM python:3.6
WORKDIR /djangoApp
COPY djangoApp/damnificados/ /djangoApp

RUN pip install django
RUN pip install mysqlclient
RUN pip install gunicorn

CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application