from rest_framework import serializers
from tutorias_itsvc.students.models import StudentParent


class ParentSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(read_only=True)
    academic_degree_id = serializers.IntegerField()
    type = serializers.CharField(read_only=True)

    class Meta:
        model = StudentParent
        fields = [
            'student_id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'type',
            'birth_date',
            'academic_degree_id',
            'has_job',
            'workplace',
            'type_of_job',
            'profession_occupation',
            'is_alive',
        ]
