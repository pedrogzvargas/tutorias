from tutorias_itsvc.students.models import StudentInstitute
from rest_framework import serializers


class InstituteSerializer(serializers.ModelSerializer):
    academic_degree_id = serializers.IntegerField(source="academic_degree.id")
    academic_degree_name = serializers.CharField(source="academic_degree.name", required=False)

    class Meta:
        model = StudentInstitute
        fields = [
            "id",
            "institute_name",
            "academic_degree_id",
            "academic_degree_name",
            "start_date",
            "end_date",
        ]
        read_only_fields = ["id", "student", "academic_degree", "academic_degree_name"]
