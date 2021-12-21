from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.courses.serializers.api.v1.course import StudetCourseSerializer
from tutorias_itsvc.courses.services.student_course.controllers import StudentCourseGetterController


class StudentCourseApi(APIView):
    permission_classes = ()

    def get(self, request, student_id, course_id):
        serializer = GetterSerializerService(StudetCourseSerializer)
        response = ResponseService()
        getter_controller = StudentCourseGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(course_id=course_id, student_id=student_id, course__is_active=True)
        return response
