from rest_framework import serializers
from tutorias_itsvc.tutor.models import TutorSubject


class TutorSubjectSerializer(serializers.ModelSerializer):
    tutor_id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(source="tutor.user.first_name", read_only=True)
    second_name = serializers.CharField(source="tutor.user.second_name", read_only=True)
    last_name = serializers.CharField(source="tutor.user.last_name", read_only=True)
    second_last_name = serializers.CharField(source="tutor.user.second_last_name", read_only=True)
    subject_id = serializers.IntegerField(required=True)
    subject = serializers.CharField(source="subject.name", read_only=True)
    subject_code = serializers.CharField(source="subject.code", read_only=True)
    school_cycle_id = serializers.IntegerField(required=True)
    school_cycle_name = serializers.CharField(source="school_cycle.name", read_only=True)
    school_cycle_active = serializers.BooleanField(source="school_cycle.is_active", read_only=True)

    class Meta:
        model = TutorSubject
        fields = [
            'id',
            'tutor_id',
            'first_name',
            'second_name',
            'second_last_name',
            'last_name',
            'subject_id',
            'subject',
            'subject_code',
            'school_cycle_id',
            'school_cycle_name',
            'school_cycle_active',
        ]
