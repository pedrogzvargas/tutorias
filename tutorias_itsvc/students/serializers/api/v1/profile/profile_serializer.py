from tutorias_itsvc.students.models import Student
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    second_name = serializers.CharField(source='user.second_name', required=False)
    last_name = serializers.CharField(source='user.last_name')
    second_last_name = serializers.CharField(source='user.second_last_name', required=False)
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    is_active = serializers.BooleanField(source='user.is_active')
    date_joined = serializers.DateTimeField(source='user.date_joined')

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'username',
            'email',
            'is_active',
            'date_joined',
        ]
        read_only_fields = [
            'id',
            'is_active',
            'date_joined',
            'username'
        ]
