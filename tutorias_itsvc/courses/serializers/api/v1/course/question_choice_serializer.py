from rest_framework import serializers
from tutorias_itsvc.courses.models import QuestionChoice


class QuestionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionChoice
        exclude = ("created_at", "updated_at", )
