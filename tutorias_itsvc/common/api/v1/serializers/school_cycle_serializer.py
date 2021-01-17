from tutorias_itsvc.common.models import SchoolCycle
from rest_framework import serializers


class SchoolCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolCycle
        fields = '__all__'
