from rest_framework import serializers
from .models import Personas, PersonasHasLugares,Lugares

def valida_edad(source):
    if source<= 100:
        pass
    else:
        raise serializers.ValidationError("Ay ajaaaaaaa, no seas mamoln!")

class PersonasGetName(serializers.Serializer):
    nombre = serializers.CharField(max_length = 180)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['id','nombre','edad','sexo','tipo_de_personas']

class PersonasCreateSerializer(serializers.Serializer) :
    nombre = serializers.CharField(max_length = 180)
    edad = serializers.IntegerField(validators=[valida_edad])
    sexo = serializers.CharField(max_length = 5)
    tipo_de_personas = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasModifySerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)


class PersonasHasLugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonasHasLugares
        fields = ['fecha','status','persona_id','lugar_id']

class PersonasHasLugaresCreate(serializers.Serializer):
    fecha = serializers.DateField()
    status = serializers.CharField(max_length=2)
    #persona_id = serializers.ForeignKey(Personas)
    #lugar_id = serializers.ForeignKey(Lugares)

    def create(self, validated_data):
        return PersonasHasLugares.objects.create(**validated_data)