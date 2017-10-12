from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','email','password')
    
    def create(self, validated_data):
        return User.objects.createUser(**validated_data)