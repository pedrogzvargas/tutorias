from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    second_name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    second_last_name = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'email',
        ]
