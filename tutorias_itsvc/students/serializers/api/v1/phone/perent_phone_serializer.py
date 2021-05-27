from tutorias_itsvc.users.models import PersonPhone
from rest_framework import serializers


class PersonPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonPhone
        fields = '__all__'

        read_only_fields = [
            'person',
        ]
