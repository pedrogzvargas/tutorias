from tutorias_itsvc.users.models import PersonalInformation
from rest_framework import serializers


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = "__all__"
