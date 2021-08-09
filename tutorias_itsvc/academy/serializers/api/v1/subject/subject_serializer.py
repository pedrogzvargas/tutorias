from rest_framework import serializers
from tutorias_itsvc.academy.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
