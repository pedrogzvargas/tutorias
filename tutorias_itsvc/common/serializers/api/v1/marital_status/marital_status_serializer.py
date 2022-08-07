from tutorias_itsvc.common.models import MaritalStatus
from rest_framework import serializers


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'
