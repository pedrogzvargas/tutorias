from rest_framework import serializers
from tutorias_itsvc.courses.models import Question
from .question_type_serializer import QuestionTypeSerializer
from .question_choice_serializer import QuestionChoiceSerializer
from .choice_answer_serializer import ChoiceAnswerSerializer
from .string_answer_serializer import StringAnswerSerializer
from .text_answer_serializer import TextAnswerSerializer
from .bool_answer_serializer import BoolAnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    question_type = QuestionTypeSerializer(read_only=True)
    choice = QuestionChoiceSerializer(read_only=True, many=True)
    choice_answer = ChoiceAnswerSerializer(read_only=True, many=True)
    string_answer = StringAnswerSerializer(read_only=True, many=True)
    text_answer = TextAnswerSerializer(read_only=True, many=True)
    bool_answer = BoolAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        exclude = ("created_at", "updated_at", )
