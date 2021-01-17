from rest_framework import serializers
from tutorias_itsvc.academy.models import AcademicPeriod


class AcademicPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPeriod
        fields = '__all__'
