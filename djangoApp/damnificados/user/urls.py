from django.conf.urls import url
from .views import UserApi

urlpatterns=[
    url(r'register/$',UserApi.as_view())
]