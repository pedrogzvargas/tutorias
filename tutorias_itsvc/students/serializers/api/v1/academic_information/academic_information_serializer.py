from rest_framework import serializers
from tutorias_itsvc.students.models import StudentAcademicInformation


class AcademicInformationSerializer(serializers.ModelSerializer):
    university = serializers.CharField(
        source='academic_information.academic_period_number.academic_period.academic_major.university.name')
    university_id = serializers.IntegerField(
        source='academic_information.academic_period_number.academic_period.academic_major.university_id')
    major = serializers.CharField(
        source='academic_information.academic_period_number.academic_period.academic_major.major.name')
    major_id = serializers.IntegerField(
        source='academic_information.academic_period_number.academic_period.academic_major.major_id'
    )
    period = serializers.CharField(source='academic_information.academic_period_number.academic_period.period.name')
    period_id = serializers.IntegerField(source='academic_information.academic_period_number.academic_period.period_id')
    period_number = serializers.CharField(source='academic_information.academic_period_number.period_number.name')
    period_number_id = serializers.IntegerField(source='academic_information.academic_period_number.period_number.id')
    group = serializers.CharField(source='academic_information.group.name')
    group_id = serializers.IntegerField(source='academic_information.group_id')

    class Meta:
        model = StudentAcademicInformation
        fields = [
            'id',
            'student_id',
            'university',
            'university_id',
            'university',
            'major',
            'major_id',
            'period',
            'period_id',
            'period_number',
            'period_number_id',
            'group',
            'group_id',
            'is_active',
            'registered_at',
        ]
        read_only_fields = [
            'id',
            'student_id',
            'university',
            'major',
            'period',
            'period_number',
            'group',
            'is_active',
            'registered_at',
        ]
