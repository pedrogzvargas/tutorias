from tutorias_itsvc.students.models import StudentAddress
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    state_id = serializers.IntegerField()
    housing_type_id = serializers.IntegerField()
    home_status_id = serializers.IntegerField()

    class Meta:
        model = StudentAddress
        fields = [
            'street',
            'outdoor_number',
            'indoor_number',
            'colony',
            'locality',
            'state_id',
            'zip_code',
            'housing_type_id',
            'home_status_id',
            'home_status_description',
            'family_relationship',
            'members',
        ]
