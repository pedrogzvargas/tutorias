from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_subject import TutorSubjectSerializer
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.tutor.services.tutor_subject.controllers import CurrentTutorSubjectsAsCatalogController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin
from tutorias_itsvc.utils import query_debugger


class CurrentTaughtSubjectsApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    @query_debugger
    def get(self, request):
        repository = TutorSubjectRepository()
        serializer = GetterSerializerService(TutorSubjectSerializer, True)
        response = ResponseService()
        getter_controller = CurrentTutorSubjectsAsCatalogController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
