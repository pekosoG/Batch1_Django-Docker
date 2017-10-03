FROM python:3.6
COPY djangoApp/damnificados/requirements.txt /djangoApp/requirements.txt
RUN pip install -r requirements.txt
WORKDIR /djangoApp
COPY djangoApp/damnificados/ /djangoApp
CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application