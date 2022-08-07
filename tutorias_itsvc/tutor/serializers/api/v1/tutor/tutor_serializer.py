from rest_framework import serializers
from tutorias_itsvc.tutor.models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    second_name = serializers.CharField(source="user.second_name")
    last_name = serializers.CharField(source="user.last_name")
    second_last_name = serializers.CharField(source="user.second_last_name")
    username = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    university_id = serializers.IntegerField(source="academic.university_id")

    class Meta:
        model = Tutor
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'username',
            'university_id',
            'email',
            'is_active',
            'academic_id',
        ]
