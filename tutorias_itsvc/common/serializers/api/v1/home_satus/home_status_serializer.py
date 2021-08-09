from tutorias_itsvc.common.models import HomeStatus
from rest_framework import serializers


class HomeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStatus
        fields = '__all__'
