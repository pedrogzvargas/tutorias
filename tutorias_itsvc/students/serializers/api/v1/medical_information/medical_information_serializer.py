from rest_framework import serializers
from tutorias_itsvc.students.models import StudentMedicalInformation


class MedicalInformationSerializer(serializers.ModelSerializer):
    disability_id = serializers.IntegerField(source='disability.id')

    class Meta:
        model = StudentMedicalInformation
        fields = [
            'id',
            'disability_id',
            'description',
        ]
