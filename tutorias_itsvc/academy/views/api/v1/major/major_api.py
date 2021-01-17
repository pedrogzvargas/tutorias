from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import MajorRepository
from tutorias_itsvc.academy.serializers.api.v1.major import MajorSerializer
from tutorias_itsvc.academy.services.major.controllers import MajorFilterController
from tutorias_itsvc.utils import query_debugger
from tutorias_itsvc.academy.services.major import MajorGetterService


class MajorApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, major_id):
        repository = MajorRepository()
        serializer = GetterSerializerService(MajorSerializer)
        response = ResponseService()
        service = MajorGetterService(repository)
        controller = MajorFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
            getter_service=service
        )
        response = controller(id=major_id)
        return response
