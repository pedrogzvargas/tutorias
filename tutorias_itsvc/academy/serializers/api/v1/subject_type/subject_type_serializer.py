from rest_framework import serializers
from tutorias_itsvc.academy.models import SubjectType


class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = "__all__"
