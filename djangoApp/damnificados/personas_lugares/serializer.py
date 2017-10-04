from rest_framework import serializers
from .models import Personas_Lugares

class Personas_LugaresGet(serializers.Serializer):
    persona = serializers.ForeignKey(Personas, on_delete=models.CASCADE)
    lugar = serializers.ForeignKey(Lugares, on_delete=models.CASCADE)
    fecha = serializers.DateTimeField()
    status = serializers.CharField(max_lenght=2)

class Personas_LugaresCreateSerializer(serializers.Serializer) :
    persona = serializers.ForeignKey(Personas, on_delete=models.CASCADE)
    lugar = serializers.ForeignKey(Lugares, on_delete=models.CASCADE)
    fecha = serializers.DateTimeField()
    status = serializers.CharField(max_lenght=2)
    
    def create(self, validated_data):
        return Personas_Lugares.objects.create(**validated_data)

class Personas_LugaresModifySerializer(serializers.Serializer):
    persona = serializers.ForeignKey(Personas, on_delete=models.CASCADE)
    lugar = serializers.ForeignKey(Lugares, on_delete=models.CASCADE)
    fecha = serializers.DateTimeField()
    status = serializers.CharField(max_lenght=2)