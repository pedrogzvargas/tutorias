from tutorias_itsvc.students.models import EstadoPsicofisiologico
from rest_framework import serializers


class EstadoPsicofisiologicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoPsicofisiologico
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
