from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorCreatorSerializer
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorSerializer

from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository

from tutorias_itsvc.tutor.services.tutor.controllers import TutorCreatorController
from tutorias_itsvc.tutor.services.tutor.controllers import TutorFilterController


class TutorsApi(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user_repository = UserRepository()
        group_repository = GroupRepository()
        tutor_repository = TutorRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorCreatorSerializer)
        controller = TutorCreatorController(
            user_repository=user_repository,
            group_repository=group_repository,
            tutor_repository=tutor_repository,
            request=request,
            response=response,
        )
        response = controller()
        return response

    def get(self, request):
        repository = TutorRepository()
        serializer = GetterSerializerService(TutorSerializer, True)
        response = ResponseService()
        getter_controller = TutorFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
