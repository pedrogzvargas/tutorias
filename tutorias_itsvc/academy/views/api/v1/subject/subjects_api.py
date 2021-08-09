from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import SubjectRepository
from tutorias_itsvc.academy.serializers.api.v1.subject import SubjectSerializer
from tutorias_itsvc.academy.services.subject.controllers import SubjectGetterController
from tutorias_itsvc.academy.services.subject import SubjectFilterService
from tutorias_itsvc.utils import query_debugger


class SubjectsApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request):
        repository = SubjectRepository()
        service = SubjectFilterService(repository)
        serializer = GetterSerializerService(SubjectSerializer, True)
        response = ResponseService()
        controller = SubjectGetterController(
            service=service,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = controller()
        return response
