from django.conf.urls import url
from .views import LugaresApi

urlpatterns=[
    url(r'^$',LugaresApi.as_view(),name="lugares_endpoint")
]