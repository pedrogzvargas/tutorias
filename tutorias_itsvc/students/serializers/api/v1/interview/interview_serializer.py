from rest_framework import serializers


class InterviewSerializer(serializers.Serializer):
    file = serializers.CharField()
