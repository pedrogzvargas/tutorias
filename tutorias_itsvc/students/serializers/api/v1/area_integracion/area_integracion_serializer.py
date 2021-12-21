from tutorias_itsvc.students.models import AreaIntegracion
from rest_framework import serializers


class AreaIntegracionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaIntegracion
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
