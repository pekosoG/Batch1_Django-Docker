from django.conf.urls import url
from .views import ArticulosApi

urlpatterns=[
    url(r'^$',ArticulosApi.as_view())
]