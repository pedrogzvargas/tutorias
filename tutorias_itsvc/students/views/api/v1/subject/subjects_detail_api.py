from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService

from tutorias_itsvc.students.serializers.api.v1.subject import StudentSubjectsDetailSerializer
from tutorias_itsvc.students.services.subject.controllers import SubjectDetailsController
from tutorias_itsvc.utils import query_debugger


class SubjectsDetailApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, student_id):
        serializer = GetterSerializerService(StudentSubjectsDetailSerializer)
        response = ResponseService()
        controller = SubjectDetailsController(
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response
