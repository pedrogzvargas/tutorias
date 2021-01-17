from rest_framework import serializers


class LoginCreatorSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
