from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import SubjectTypeRepository
from tutorias_itsvc.academy.serializers.api.v1.subject_type import SubjectTypeSerializer
from tutorias_itsvc.academy.services.subject_type.controllers import SubjectTypeGetterController
from tutorias_itsvc.academy.services.subject_type import SubjectTypeFilterService
from tutorias_itsvc.utils import query_debugger


class SubjectTypesApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request):
        repository = SubjectTypeRepository()
        service = SubjectTypeFilterService(repository)
        serializer = GetterSerializerService(SubjectTypeSerializer, True)
        response = ResponseService()
        controller = SubjectTypeGetterController(
            service=service,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = controller()
        return response
