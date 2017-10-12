# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import User
from .serializer import UserSerializer

class UserApi(APIView):

    def post(self, request):
        bato=UserSerializer(data=request.data)
        if bato.is_valid():
            bato.save()
            return Response(bato.data,status=status.HTTP_201_CREATED)
        else:
            return Response(bato.errors, status=status.HTTP_400_BAD_REQUEST)
