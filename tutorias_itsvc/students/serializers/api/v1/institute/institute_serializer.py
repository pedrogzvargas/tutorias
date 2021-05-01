from tutorias_itsvc.students.models import StudentInstitute
from rest_framework import serializers


class InstituteSerializer(serializers.ModelSerializer):
    academic_degree_id = serializers.IntegerField(source="academic_degree.id")

    class Meta:
        model = StudentInstitute
        fields = [
            "id",
            "institute_name",
            "academic_degree_id",
            "start_date",
            "end_date",
        ]
        read_only_fields = ["id", "student", "academic_degree",]
