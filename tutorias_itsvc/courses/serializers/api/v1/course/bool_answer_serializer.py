from rest_framework import serializers
from tutorias_itsvc.courses.models import BoolAnswer


class BoolAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoolAnswer
        fields = "__all__"
