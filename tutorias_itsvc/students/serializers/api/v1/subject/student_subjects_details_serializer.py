from rest_framework import serializers
from tutorias_itsvc.students.serializers.api.v1.student import StudentSerializer
from .subjects_detail_serializer import SubjectsDetailSerializer
from tutorias_itsvc.students.models import StudentAcademicInformation


class AcademicInformationSerializer(serializers.ModelSerializer):
    university = serializers.CharField(
        source='academic_information.academic_period_number.academic_period.academic_major.university.name',
        read_only=True)
    university_id = serializers.IntegerField(
        source='academic_information.academic_period_number.academic_period.academic_major.university_id')
    major = serializers.CharField(
        source='academic_information.academic_period_number.academic_period.academic_major.major.name',
        read_only=True)
    major_id = serializers.IntegerField(
        source='academic_information.academic_period_number.academic_period.academic_major.major_id'
    )
    period = serializers.CharField(source='academic_information.academic_period_number.academic_period.period.name',
                                   read_only=True)
    period_id = serializers.IntegerField(source='academic_information.academic_period_number.academic_period.period_id')
    period_number = serializers.CharField(source='academic_information.academic_period_number.period_number.name',
                                          read_only=True)
    period_number_id = serializers.IntegerField(source='academic_information.academic_period_number.period_number.id')
    group = serializers.CharField(source='academic_information.group.name',
                                  read_only=True)
    group_id = serializers.IntegerField(source='academic_information.group_id')

    class Meta:
        model = StudentAcademicInformation
        fields = [
            'id',
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


class StudentSubjectsDetailSerializer(serializers.Serializer):
    student = StudentSerializer()
    subject_details = SubjectsDetailSerializer()
    academic_information = AcademicInformationSerializer()
