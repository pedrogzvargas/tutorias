from rest_framework import serializers
from tutorias_itsvc.students.models import StudentSubject


class SubjectSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(read_only=True)
    tutor_subject_id = serializers.IntegerField(source="tutor_subject.id")
    subject_id = serializers.IntegerField(source="tutor_subject.subject.id", read_only=True)
    subject_name = serializers.CharField(source="tutor_subject.subject.name", read_only=True)
    type_id = serializers.IntegerField()
    type_name = serializers.CharField(source="type.name", read_only=True)
    failure_metric_id = serializers.IntegerField(required=False, allow_null=True)
    school_cycle_id = serializers.IntegerField()
    school_cycle_name = serializers.CharField(source="school_cycle.name", read_only=True)

    class Meta:
        model = StudentSubject
        fields = [
            'id',
            'student_id',
            'tutor_subject_id',
            'subject_id',
            'subject_name',
            'type_id',
            'type_name',
            'approved',
            'final_score',
            'failure_metric_id',
            'comment',
            'school_cycle_id',
            'school_cycle_name',
            'unsubscribed',
            'created_at',
            'updated_at',
        ]
