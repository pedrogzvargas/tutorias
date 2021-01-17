from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, username):
        user = self.context.get("user")
        if user and user.username != username:
            if UserModel.objects.filter(username=username).exists():
                raise Exception("Ya existe un usuario con este username")
        return username

    def validate_email(self, email):
        user = self.context.get("user")
        if user and user.email != email:
            if UserModel.objects.filter(email=email).exists():
                raise Exception("Ya existe un usuario con este email")
        return email

    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'username',
            'email',
            'is_active',
            'date_joined',
        ]
