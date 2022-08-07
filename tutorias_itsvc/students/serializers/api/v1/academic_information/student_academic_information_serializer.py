from rest_framework import serializers
from tutorias_itsvc.students.models import StudentAcademicInformation


class StudentAcademicInformationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="student.id")
    first_name = serializers.CharField(source="student.user.first_name")
    second_name = serializers.CharField(source="student.user.second_name")
    last_name = serializers.CharField(source="student.user.last_name")
    second_last_name = serializers.CharField(source="student.user.second_last_name")
    email = serializers.CharField(source="student.user.email")
    username = serializers.CharField(source="student.user.username")

    class Meta:
        model = StudentAcademicInformation
        fields = [
            "id",
            "first_name",
            "second_name",
            "last_name",
            "second_last_name",
            "email",
            "username",
        ]
