from rest_framework import serializers
from tutorias_itsvc.courses.models import Course
from .questionnaire_serializer import QuestionnaireSerializer


class CourseSerializer(serializers.ModelSerializer):
    questionnaire = QuestionnaireSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "questionnaire",
        ]
