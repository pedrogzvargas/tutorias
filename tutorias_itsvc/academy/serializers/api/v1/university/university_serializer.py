from rest_framework import serializers
from tutorias_itsvc.academy.models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = [
            'id',
            'name',
            'acronym',
            'is_active',
        ]
