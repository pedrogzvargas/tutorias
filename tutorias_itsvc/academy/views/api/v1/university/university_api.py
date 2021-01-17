from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import UniversityRepository
from tutorias_itsvc.academy.serializers.api.v1.university import UniversitySerializer
from tutorias_itsvc.academy.services.university.controllers import UniversityFilterController
from tutorias_itsvc.academy.services.university import UniversityGetterService
from tutorias_itsvc.utils import query_debugger


class UniversityApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, university_id):
        repository = UniversityRepository()
        serializer = GetterSerializerService(UniversitySerializer)
        response = ResponseService()
        service = UniversityGetterService(repository)
        controller = UniversityFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
            getter_service=service
        )
        response = controller(id=university_id)
        return response
