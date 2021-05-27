from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.student import StudentCreatorSerializer
from tutorias_itsvc.students.serializers.api.v1.student import StudentSerializer
from tutorias_itsvc.students.services.student.controllers import StudentGetterController
from tutorias_itsvc.students.services.student.controllers import StudentCreatorController
from tutorias_itsvc.students.services.student import StudentFilterService


class StudentsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        repository = StudentRepository()
        service = StudentFilterService(repository)
        serializer = GetterSerializerService(StudentSerializer, many=True)
        response = ResponseService()
        controller = StudentGetterController(
            repository=repository,
            serializer=serializer,
            service=service,
            response=response,
        )
        response = controller()
        return response

    def post(self, request):
        repository = StudentRepository()
        response = ResponseService()
        request = RequestService(request.data, StudentCreatorSerializer)
        controller = StudentCreatorController(
            request=request,
            repository=repository,
            response=response,
        )
        response = controller()
        return response
