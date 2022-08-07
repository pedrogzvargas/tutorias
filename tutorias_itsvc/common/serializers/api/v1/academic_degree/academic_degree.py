from tutorias_itsvc.common.models import AcademicDegree
from rest_framework import serializers


class AcademicDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegree
        fields = '__all__'
