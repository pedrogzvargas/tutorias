from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService

from tutorias_itsvc.students.serializers.api.v1.subject import SubjectsDetailSerializer
from tutorias_itsvc.students.services.subject.controllers import SubjectDetailsController


class SubjectsDetailApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        serializer = GetterSerializerService(SubjectsDetailSerializer)
        response = ResponseService()
        controller = SubjectDetailsController(
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response
