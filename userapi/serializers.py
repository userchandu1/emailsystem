from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class SendMailSerializer(serializers.Serializer):
    subject= serializers.CharField(max_length=100)
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)

