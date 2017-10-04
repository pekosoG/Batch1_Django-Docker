from rest_framework import serializers
from .models import Lugares

class LugaresGetName(serializers.Serializer):
    nombre = serializers.CharField(max_length = 180)

class LugaresCreateSerializer(serializers.Serializer) :
    nombre = serializers.CharField(max_length = 180)
    calle = serializers.CharField(max_length = 50)
    colonia = serializers.CharField(max_length = 50)
    codigo_postal = serializers.IntegerField()
    
    def create(self, validated_data):
        return Lugares.objects.create(**validated_data)

class LugaresModifySerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length = 180)
    calle = serializers.CharField(max_length = 50)
    colonia = serializers.CharField(max_length = 50)
    codigo_postal = serializers.IntegerField()