from django.conf.urls import url
from .views import UserApi

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns=[
    url(r'register/$',UserApi.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token)
]