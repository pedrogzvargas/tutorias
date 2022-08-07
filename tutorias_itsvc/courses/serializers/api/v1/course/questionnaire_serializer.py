from rest_framework import serializers
from tutorias_itsvc.courses.models import Questionnaire
from .module_serializer import ModuleSerializer
from .question_serializer import QuestionSerializer


class QuestionnaireSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)
    question = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Questionnaire
        exclude = ("created_at", "updated_at", )
