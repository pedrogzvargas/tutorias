from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_subject import TutorSubjectSerializer
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectCreatorController
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectFilterController


class TutorSubjectsApi(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        repository = TutorSubjectRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorSubjectSerializer)
        controller = TutorSubjectCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller()
        return response

    def get(self, request):
        repository = TutorSubjectRepository()
        serializer = GetterSerializerService(TutorSubjectSerializer, True)
        response = ResponseService()
        getter_controller = TutorSubjectFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
