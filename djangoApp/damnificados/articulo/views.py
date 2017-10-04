from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Articulo
from .serializer import ArticuloGetName, ArticuloCreateSerializer

# Create your views here.

class ArticulosApi(APIView):

    def get(self, request):
        gente = Articulo.objects.all()
        serializer = ArticuloGetName(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        lugar=ArticuloCreateSerializer(data=request.data)
        if lugar.is_valid():
            lugar.save()
            return Response(lugar.data,status=status.HTTP_201_CREATED)
        else:
            return Response(lugar, status=status.HTTP_400_BAD_REQUEST)