from tutorias_itsvc.students.models import EstiloAprendizaje
from rest_framework import serializers


class EstiloAprendizajeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstiloAprendizaje
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
