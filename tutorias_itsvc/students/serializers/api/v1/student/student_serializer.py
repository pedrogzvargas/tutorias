from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(source='user.first_name')
    second_name = serializers.CharField(source='user.second_name', required=False, allow_blank="True")
    last_name = serializers.CharField(source='user.last_name')
    second_last_name = serializers.CharField(source='user.second_last_name', required=False, allow_blank="True")
    username = serializers.CharField(source='user.username')
    enrollment = serializers.CharField()
    email = serializers.EmailField(source='user.email')
