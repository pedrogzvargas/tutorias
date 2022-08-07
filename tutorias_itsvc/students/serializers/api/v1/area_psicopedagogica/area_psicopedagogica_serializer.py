from tutorias_itsvc.students.models import AreaPsicopedagogica
from rest_framework import serializers


class AreaPsicopedagogicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaPsicopedagogica
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
