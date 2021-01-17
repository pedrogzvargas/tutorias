from tutorias_itsvc.academy.models import Period
from rest_framework import serializers


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'
