from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService

from tutorias_itsvc.students.serializers.api.v1.subject import StudentSubjectsDetailSerializer
from tutorias_itsvc.students.services.subject.controllers import SubjectDetailsController
from tutorias_itsvc.utils import query_debugger
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class SubjectsDetailApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

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
