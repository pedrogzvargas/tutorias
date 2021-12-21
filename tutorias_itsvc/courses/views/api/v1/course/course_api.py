from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.courses.serializers.api.v1.course import CourseSerializer
from tutorias_itsvc.courses.services.course.controllers import CourseGetterController


class CourseApi(APIView):
    permission_classes = ()

    def get(self, request, student_id, course_id):
        serializer = GetterSerializerService(CourseSerializer)
        response = ResponseService()
        getter_controller = CourseGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=course_id)
        return response
