from rest_framework import serializers
from tutorias_itsvc.academy.models import Major


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = [
            'id',
            'name',
            'acronym',
            'is_active',
        ]
