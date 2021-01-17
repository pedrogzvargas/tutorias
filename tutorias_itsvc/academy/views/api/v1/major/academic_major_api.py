from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import MajorRepository
from tutorias_itsvc.academy.serializers.api.v1.major import MajorSerializer
from tutorias_itsvc.academy.services.major.controllers import MajorFilterController
from tutorias_itsvc.utils import query_debugger


class AcademicMajorApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, university_id):
        repository = MajorRepository()
        serializer = GetterSerializerService(MajorSerializer, True)
        response = ResponseService()
        controller = MajorFilterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = controller(university__id=university_id)
        return response
