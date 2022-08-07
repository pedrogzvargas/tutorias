from tutorias_itsvc.students.models import MotivacionEstudio
from rest_framework import serializers


class MotivacionEstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotivacionEstudio
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
