from rest_framework import serializers
from tutorias_itsvc.users.models import Sibling


class SiblingSerializer(serializers.ModelSerializer):
    gender_id = serializers.IntegerField()
    academic_degree_id = serializers.IntegerField()
    relationship_id = serializers.IntegerField()
    attitude_id = serializers.IntegerField()

    class Meta:
        model = Sibling
        fields = [
            "id",
            "first_name",
            "second_name",
            "last_name",
            "second_last_name",
            "gender_id",
            "birth_date",
            "academic_degree_id",
            "relationship_id",
            "attitude_id",
        ]
