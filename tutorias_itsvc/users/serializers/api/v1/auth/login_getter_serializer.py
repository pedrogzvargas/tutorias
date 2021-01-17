from rest_framework import serializers
from rest_framework.authtoken.models import Token
from tutorias_itsvc.users.serializers.api.v1.user import GroupSerializer, RoleSerializer


class LoginGetterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="key")
    groups = GroupSerializer(source='user.groups', many=True, read_only=True)
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Token
        fields = [
            'user_id',
            'token',
            'roles',
            'groups',
        ]
