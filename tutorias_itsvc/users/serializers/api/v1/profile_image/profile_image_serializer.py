from rest_framework import serializers
from tutorias_itsvc.users.models import ProfileImage


class ProfileImageSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = ProfileImage
        fields = [
            'user_id',
            'profile_image'
        ]
