from rest_framework import serializers
from tutorias_itsvc.academy.models import SubjectFailureMetric


class SubjectFailureMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectFailureMetric
        fields = "__all__"
