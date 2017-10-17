from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'damnificados',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'mysql-docker',
        'PORT':'3306'
    }
}