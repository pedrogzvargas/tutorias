from rest_framework import serializers


class StudentsSubjectLoadDataSerializer(serializers.Serializer):
    file = serializers.CharField(required=True, allow_null=False, allow_blank=False)
