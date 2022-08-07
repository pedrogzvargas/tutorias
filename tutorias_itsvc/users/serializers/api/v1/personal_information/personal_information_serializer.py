from rest_framework import serializers
from tutorias_itsvc.users.models import PersonalInformation


class PersonalInformationSerializer(serializers.ModelSerializer):
    marital_status_id = serializers.IntegerField(source='marital_status.id')
    gender_id = serializers.IntegerField(source='gender.id')

    class Meta:
        model = PersonalInformation
        fields = [
            'id',
            'user_id',
            'place_birth',
            'birth_date',
            'has_children',
            'number_of_children',
            'gender_id',
            'marital_status_id',
            'marital_status_description',
            'height',
            'weight',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'user_id',
            'created_at',
            'updated_at',
        ]
