from tutorias_itsvc.students.models import StudentScholarship
from rest_framework import serializers


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentScholarship
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
