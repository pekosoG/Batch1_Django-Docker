from rest_framework import serializers
from .models import Personas

SEXOS =  (('M','Mujer'),('H','Hombre'),('I','Indefinido'))
TIPOS_PERSONAS= (('D','Damnificado'),('Voluntario','Voluntario'),('Otro','Otro'))

def valida_edad(source):
    if source<= 100:
        pass
    else:
        raise serializers.ValidationError("Ay ajaaaaaaa, no seas mamoln!")

class PersonasGetName(serializers.Serializer):
    nombresito = serializers.CharField(max_length = 180)

class PersonasCreateSerializer(serializers.Serializer) :
    nombre = serializers.CharField(max_length = 180)
    edad = serializers.IntegerField(validators=[valida_edad])
    sexo = serializers.CharField(max_length = 5)
    tipo_de_personas = serializers.CharField(max_length=50)

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)