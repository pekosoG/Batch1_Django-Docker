# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Lugares
from .serializer import LugaresGetName,LugaresCreateSerializer

# Create your views here.

class LugaresApi(APIView):

    def get(self, request):
        gente = Lugares.objects.all()
        serializer = LugaresGetName(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        lugar=LugaresCreateSerializer(data=request.data)
        if lugar.is_valid():
            lugar.save()
            return Response(lugar.data,status=status.HTTP_201_CREATED)
        else:
            return Response(lugar, status=status.HTTP_400_BAD_REQUEST)