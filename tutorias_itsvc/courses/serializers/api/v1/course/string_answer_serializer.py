from rest_framework import serializers
from tutorias_itsvc.courses.models import StringAnswer


class StringAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StringAnswer
        fields = "__all__"
