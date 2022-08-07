from rest_framework import serializers


class TutorCreatorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=True)
    second_name = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=True)
    second_last_name = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    academic_id = serializers.IntegerField(required=True)
    email = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField(required=False, allow_null=True, default=True)
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
