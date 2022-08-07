from rest_framework import serializers


class PersonPhoneSerializer(serializers.Serializer):
    home_phone = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    mobile_phone = serializers.CharField(required=False, allow_null=True, allow_blank=True)
