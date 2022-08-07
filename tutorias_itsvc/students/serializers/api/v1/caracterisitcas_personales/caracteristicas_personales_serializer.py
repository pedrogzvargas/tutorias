from tutorias_itsvc.students.models import CaracteristicasPersonales
from rest_framework import serializers


class CaracteristicasPersonalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaracteristicasPersonales
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
