from rest_framework import serializers


class StudentCreatorSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    second_name = serializers.CharField(required=False, allow_blank="True")
    second_last_name = serializers.CharField(required=False, allow_blank="True")
    email = serializers.EmailField()
