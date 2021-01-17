from rest_framework import serializers
from tutorias_itsvc.academy.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'is_active',
        ]
