from tutorias_itsvc.common.models import Relationship
from rest_framework import serializers


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'
