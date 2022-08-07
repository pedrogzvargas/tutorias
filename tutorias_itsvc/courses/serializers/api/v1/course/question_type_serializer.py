from rest_framework import serializers
from tutorias_itsvc.courses.models import QuestionType


class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        exclude = ("created_at", "updated_at", )
