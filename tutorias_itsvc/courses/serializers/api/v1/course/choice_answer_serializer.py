from rest_framework import serializers
from tutorias_itsvc.courses.models import ChoiceAnswer


class ChoiceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChoiceAnswer
        fields = "__all__"
