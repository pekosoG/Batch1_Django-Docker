from django.conf.urls import url
from .views import PersonasApi,PersonasHasLugaresApi,PersonaApi


# Auth Header
#       Authorization: Auth <token>
#
urlpatterns=[
    url(r'^$',PersonasApi.as_view()),
    url(r'(?P<pk>[0-9]+)/$',PersonaApi.as_view()),
    url(r'^/hasPersonas$',PersonasHasLugaresApi.as_view())
]