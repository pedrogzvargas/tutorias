from tutorias_itsvc.common.models import HousingType
from rest_framework import serializers


class HousingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingType
        fields = '__all__'
