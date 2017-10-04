from rest_framework import serializers
from .models import Articulo

class ArticuloGetName(serializers.Serializer):
    nombre = serializers.CharField(max_length = 50)

class ArticuloCreateSerializer(serializers.Serializer) :
    nombre = serializers.CharField(max_length = 50)
    
    def create(self, validated_data):
        return Articulo.objects.create(**validated_data)