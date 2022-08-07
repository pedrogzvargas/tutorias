from tutorias_itsvc.students.models import StudentIncome
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentIncome
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
