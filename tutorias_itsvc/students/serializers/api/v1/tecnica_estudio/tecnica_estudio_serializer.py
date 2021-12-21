from tutorias_itsvc.students.models import TecnicaEstudio
from rest_framework import serializers


class TecnicaEstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = TecnicaEstudio
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
