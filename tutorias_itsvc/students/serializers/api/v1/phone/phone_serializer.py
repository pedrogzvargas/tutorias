from tutorias_itsvc.students.models import StudentPhone
from rest_framework import serializers


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentPhone
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
