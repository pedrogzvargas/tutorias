from tutorias_itsvc.common.models import Attitude
from rest_framework import serializers


class AttitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attitude
        fields = '__all__'
