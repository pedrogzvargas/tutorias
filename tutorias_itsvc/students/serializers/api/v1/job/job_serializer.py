from tutorias_itsvc.students.models import StudentJob
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentJob
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
