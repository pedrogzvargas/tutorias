# from rest_framework import serializers
# from tutorias_itsvc.tutor.models import TutorGroup
# from tutorias_itsvc.academy.models import AcademicGroup
#
#
# class TutorGroupSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField(source="tutor.user.first_name", read_only=True)
#     second_name = serializers.CharField(source="tutor.user.second_name", read_only=True)
#     last_name = serializers.CharField(source="tutor.user.last_name", read_only=True)
#     second_last_name = serializers.CharField(source="tutor.user.second_last_name", read_only=True)
#     university = serializers.CharField(
#         source='academic_group.academic_period_number.academic_period.academic_major.university.name',
#         read_only=True)
#     university_id = serializers.IntegerField(
#         source='academic_group.academic_period_number.academic_period.academic_major.university.id',
#         read_only=True)
#     major = serializers.CharField(
#         source='academic_group.academic_period_number.academic_period.academic_major.major.name',
#         read_only=True)
#     major_id = serializers.IntegerField(
#         source='academic_group.academic_period_number.academic_period.academic_major.major.id',
#         read_only=True)
#     period = serializers.CharField(source='academic_group.academic_period_number.academic_period.period.name',
#                                    read_only=True)
#     period_id = serializers.IntegerField(source='academic_group.academic_period_number.academic_period.period.id',
#                                          read_only=True)
#     period_number = serializers.CharField(source='academic_group.academic_period_number.period_number.name',
#                                           read_only=True)
#     period_number_id = serializers.IntegerField(source='academic_group.academic_period_number.period_number.id',
#                                                 read_only=True)
#     group = serializers.CharField(source='academic_group.group.name',
#                                   read_only=True)
#     group_id = serializers.IntegerField(source='academic_group.group.id',
#                                         read_only=True)
#     school_cycle_name = serializers.CharField(source="school_cycle.name", read_only=True)
#     school_cycle_active = serializers.BooleanField(source="school_cycle.is_active", read_only=True)
#
#     class Meta:
#         model = TutorGroup
#         fields = [
#             'id',
#             'tutor_id',
#             'first_name',
#             'second_name',
#             'last_name',
#             'second_last_name',
#             'academic_group_id',
#             'university',
#             'university_id',
#             'major',
#             'major_id',
#             'period',
#             'period_id',
#             'period_number',
#             'period_number_id',
#             'group',
#             'group_id',
#             'school_cycle_id',
#             'school_cycle_name',
#             'school_cycle_active',
#         ]


from rest_framework import serializers
from tutorias_itsvc.tutor.models import TutorSubject
from tutorias_itsvc.tutor.models import Tutor
from tutorias_itsvc.common.models import SchoolCycle
from tutorias_itsvc.academy.models import AcademicGroup


class TutorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    second_name = serializers.CharField(source="user.second_name")
    last_name = serializers.CharField(source="user.last_name")
    second_last_name = serializers.CharField(source="user.second_last_name")
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Tutor
        fields = [
            "id",
            "first_name",
            "second_name",
            "last_name",
            "second_last_name",
            "username",
            "is_active",
        ]

class GroupSerializer(serializers.ModelSerializer):
    university = serializers.CharField(
        source='academic_period_number.academic_period.academic_major.university.name',
        read_only=True)
    university_id = serializers.IntegerField(
        source='academic_period_number.academic_period.academic_major.university.id',
        read_only=True)
    major = serializers.CharField(
        source='academic_period_number.academic_period.academic_major.major.name',
        read_only=True)
    major_id = serializers.IntegerField(
        source='academic_period_number.academic_period.academic_major.major.id',
        read_only=True)
    period = serializers.CharField(source='academic_period_number.academic_period.period.name',
                                   read_only=True)
    period_id = serializers.IntegerField(source='academic_period_number.academic_period.period.id',
                                         read_only=True)
    period_number = serializers.CharField(source='academic_period_number.period_number.name',
                                          read_only=True)
    period_number_id = serializers.IntegerField(source='academic_period_number.period_number.id',
                                                read_only=True)
    group = serializers.CharField(source='group.name',
                                  read_only=True)
    group_id = serializers.IntegerField(source='group.id',
                                        read_only=True)
    class Meta:
        model = AcademicGroup
        fields = [
            'id',
            'university',
            'university_id',
            'major',
            'major_id',
            'period',
            'period_id',
            'period_number',
            'period_number_id',
            'group',
            'group_id',
        ]


class SchoolCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolCycle
        fields = "__all__"


class TutorGroupDetailSerializer(serializers.Serializer):
    tutor = TutorSerializer()
    group = GroupSerializer(source="academic_group")
    school_cycle = SchoolCycleSerializer()

    class Meta:
        model = TutorSubject
        fields = [
            "tutor",
            "subject",
            "school_cycle",
        ]
