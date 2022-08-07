from rest_framework import serializers


class TutorGroupUpdaterSerializer(serializers.Serializer):
    tutor_id = serializers.IntegerField(required=True)
    university_id = serializers.IntegerField(required=True)
    major_id = serializers.IntegerField(required=True)
    period_id = serializers.IntegerField(required=True)
    group_id = serializers.IntegerField(required=True)
    period_number_id = serializers.IntegerField(required=True)
    school_cycle_id = serializers.IntegerField(required=True)
