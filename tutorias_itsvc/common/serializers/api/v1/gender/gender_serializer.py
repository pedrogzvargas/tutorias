from tutorias_itsvc.common.models import Gender
from rest_framework import serializers


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'
