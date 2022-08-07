from tutorias_itsvc.common.models import Income
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
