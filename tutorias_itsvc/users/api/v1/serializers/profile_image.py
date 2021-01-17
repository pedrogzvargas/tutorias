from rest_framework import serializers
from tutorias_itsvc.users.models import ProfileImage as ProfileImageModel


class ProfileImage(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    profile_image = serializers.SerializerMethodField('get_img_url')

    def get_img_url(self, obj):
        request = self.context.get('request')
        url = obj.profile_image.url
        return request.build_absolute_uri(url)

    class Meta:
        model = ProfileImageModel
        fields = [
            'user_id',
            'profile_image'
        ]
