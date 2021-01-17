from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import UniversityRepository
from tutorias_itsvc.academy.serializers.api.v1.university import UniversitySerializer
from tutorias_itsvc.academy.services.university.controllers import UniversityFilterController
from tutorias_itsvc.utils import query_debugger


class UniversitiesApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request):
        repository = UniversityRepository()
        serializer = GetterSerializerService(UniversitySerializer, True)
        response = ResponseService()
        controller = UniversityFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller()
        return response
