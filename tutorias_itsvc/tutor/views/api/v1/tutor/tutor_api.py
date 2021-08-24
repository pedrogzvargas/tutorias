from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorUpdaterSerializer
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorSerializer
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.tutor.services.tutor.controllers import TutorGetterController
from tutorias_itsvc.tutor.services.tutor.controllers import TutorUpdaterController
from tutorias_itsvc.tutor.services.tutor.controllers import TutorDeleterController


class TutorApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, tutor_id):
        repository = TutorRepository()
        serializer = GetterSerializerService(TutorSerializer)
        response = ResponseService()
        getter_controller = TutorGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=tutor_id)
        return response

    def put(self, request, tutor_id):
        user_repository = UserRepository()
        tutor_repository = TutorRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorUpdaterSerializer)
        controller = TutorUpdaterController(
            user_repository=user_repository,
            tutor_repository=tutor_repository,
            request=request,
            response=response,
        )
        response = controller(tutor_id=tutor_id)
        return response

    def delete(self, request, tutor_id):
        repository = TutorRepository()
        response = ResponseService()
        deleter_controller = TutorDeleterController(
            repository=repository,
            response=response
        )
        response = deleter_controller(tutor_id=tutor_id)
        return response
