# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Personas
from .serializer import PersonasGetName,PersonasCreateSerializer,PersonasSerializer

# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        gente = Personas.objects.all()
        serializer = PersonasSerializer(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        bato=PersonasSerializer(data=request.data)
        if bato.is_valid():
            bato.save()
            return Response(bato.data,status=status.HTTP_201_CREATED)
        else:
            return Response(bato, status=status.HTTP_400_BAD_REQUEST)