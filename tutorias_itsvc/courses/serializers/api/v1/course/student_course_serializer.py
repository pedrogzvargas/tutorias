from rest_framework import serializers
from tutorias_itsvc.courses.models import StudetCourse
from .course_serializer import CourseSerializer


class StudetCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = StudetCourse
        fields = "__all__"
