from rest_framework import serializers
from tutorias_itsvc.courses.models import TextAnswer


class TextAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextAnswer
        fields = "__all__"
