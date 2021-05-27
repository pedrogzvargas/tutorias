from rest_framework import serializers
from tutorias_itsvc.students.models import StudentSubject


class SubjectSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(read_only=True)
    subject_id = serializers.IntegerField()
    type_id = serializers.IntegerField()
    failure_metric_id = serializers.IntegerField(required=False, allow_null=True)
    semester_added_id = serializers.IntegerField()
    school_cycle_id = serializers.IntegerField()

    class Meta:
        model = StudentSubject
        fields = [
            'id',
            'student_id',
            'subject_id',
            'type_id',
            'approved',
            'final_score',
            'failure_metric_id',
            'comment',
            'semester_added_id',
            'school_cycle_id',
            'unsubscribed',
            'created_at',
            'updated_at',
        ]
