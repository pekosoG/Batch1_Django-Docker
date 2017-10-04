# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Personas_Lugares
from .serializer import Personas_LugaresCreateSerializer,Personas_LugaresGet

# Create your views here.

class LugaresApi(APIView):

    def get(self, request):
        persona_lugar = Personas_Lugares.objects.all()
        serializer = Personas_LugaresGet(persona_lugar, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        lugar=Personas_LugaresCreateSerializer(data=request.data)
        if lugar.is_valid():
            lugar.save()
            return Response(lugar.data,status=status.HTTP_201_CREATED)
        else:
            return Response(lugar, status=status.HTTP_400_BAD_REQUEST)