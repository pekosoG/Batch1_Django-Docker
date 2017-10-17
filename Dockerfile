FROM python:3.6
WORKDIR /djangoApp
COPY djangoApp/damnificados/requirements.txt /djangoApp/requirements.txt
RUN pip install -r requirements.txt
COPY djangoApp/damnificados/ /djangoApp
CMD sh init.sh