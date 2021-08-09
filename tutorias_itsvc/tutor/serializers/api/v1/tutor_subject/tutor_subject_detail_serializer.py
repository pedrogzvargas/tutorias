from rest_framework import serializers
from tutorias_itsvc.tutor.models import TutorSubject
from tutorias_itsvc.tutor.models import Tutor
from tutorias_itsvc.academy.models import Subject
from tutorias_itsvc.common.models import SchoolCycle


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


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SchoolCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolCycle
        fields = "__all__"


class TutorSubjectDetailSerializer(serializers.Serializer):
    tutor = TutorSerializer()
    subject = SubjectSerializer()
    school_cycle = SchoolCycleSerializer()

    class Meta:
        model = TutorSubject
        fields = [
            "tutor",
            "subject",
            "school_cycle",
        ]
