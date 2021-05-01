from rest_framework import serializers
from tutorias_itsvc.common.models import Address


class AddressSerializer(serializers.ModelSerializer):
    state_id = serializers.IntegerField()

    class Meta:
        model = Address
        fields = [
            'street',
            'outdoor_number',
            'indoor_number',
            'colony',
            'locality',
            'state_id',
            'zip_code',
        ]
