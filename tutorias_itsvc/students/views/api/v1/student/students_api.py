from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.student import StudentCreatorSerializer
from tutorias_itsvc.students.serializers.api.v1.student import StudentSerializer
from tutorias_itsvc.students.services.student.controllers import StudentCreatorController
from tutorias_itsvc.students.services.student.controllers import StudentFilterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class StudentsApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def post(self, request):
        response = ResponseService()
        request = RequestService(request.data, StudentCreatorSerializer)
        controller = StudentCreatorController(
            request=request,
            response=response,
        )
        response = controller()
        return response

    def get(self, request):
        repository = StudentRepository()
        serializer = GetterSerializerService(StudentSerializer, many=True)
        response = ResponseService()
        controller = StudentFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller()
        return response
