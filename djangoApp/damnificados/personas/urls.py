from django.conf.urls import url
from .views import PersonasApi,PersonasHasLugaresApi,PersonaApi

urlpatterns=[
    url(r'^$',PersonasApi.as_view()),
    url(r'(?P<pk>[0-9]+)/$',PersonaApi.as_view()),
    url(r'^/hasPersonas$',PersonasHasLugaresApi.as_view())
]