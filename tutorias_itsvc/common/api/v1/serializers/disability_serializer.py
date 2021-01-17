from tutorias_itsvc.common.models import Disability
from rest_framework import serializers


class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability
        fields = '__all__'
