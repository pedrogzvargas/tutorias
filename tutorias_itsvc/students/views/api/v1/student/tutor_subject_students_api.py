from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService

from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.student import StudentSerializer
from tutorias_itsvc.students.services.student.controllers import StudentFilterController


class StudentsApi(APIView):
    permission_classes = (IsAuthenticated, )

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
