from rest_framework import serializers


class GeneralInformationSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    mobile_phone = serializers.CharField()
    home_phone = serializers.CharField()
    birth_date = serializers.DateField()
    place_birth = serializers.CharField()
    gender_id = serializers.IntegerField()
    marital_status_id = serializers.IntegerField()
    marital_status_description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    has_children = serializers.BooleanField()
    number_of_children = serializers.IntegerField(required=False, allow_null=True)
    height = serializers.FloatField()
    weight = serializers.FloatField()
