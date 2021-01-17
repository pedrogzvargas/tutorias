from tutorias_itsvc.academy.models import PeriodNumber
from rest_framework import serializers


class PeriodNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodNumber
        fields = '__all__'
