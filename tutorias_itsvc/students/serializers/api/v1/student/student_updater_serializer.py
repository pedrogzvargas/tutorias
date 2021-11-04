from rest_framework import serializers


class StudentUpdaterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=False, allow_blank="True", allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    second_name = serializers.CharField(required=False, allow_blank="True", allow_null=True)
    second_last_name = serializers.CharField(required=False, allow_blank="True", allow_null=True)
    email = serializers.EmailField()
