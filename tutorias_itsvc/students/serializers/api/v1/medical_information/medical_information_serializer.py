from rest_framework import serializers
from tutorias_itsvc.students.models import StudentMedicalInformation


class MedicalInformationSerializer(serializers.ModelSerializer):
    disability_id = serializers.IntegerField(source='disability.id')
    disability_name = serializers.CharField(source='disability.name', read_only=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = StudentMedicalInformation
        fields = [
            'id',
            'disability_id',
            'disability_name',
            'description',
        ]
