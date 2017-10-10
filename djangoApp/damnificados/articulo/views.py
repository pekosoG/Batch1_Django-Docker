from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Articulo
from .serializer import ArticuloGetName, ArticuloCreateSerializer,AtriculosSerializer

# Create your views here.

class ArticulosApi(APIView):

    def get(self, request):
        aticulo = Articulo.objects.all()
        serializer = AtriculosSerializer(aticulo, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        aticulo=AtriculosSerializer(data=request.data)
        if aticulo.is_valid():
            aticulo.save()
            return Response(aticulo.data,status=status.HTTP_201_CREATED)
        else:
            return Response(aticulo, status=status.HTTP_400_BAD_REQUEST)