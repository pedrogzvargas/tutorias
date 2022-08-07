from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorUpdaterSerializer
from tutorias_itsvc.tutor.serializers.api.v1.tutor import TutorSerializer
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.tutor.services.tutor.controllers import TutorGetterController
from tutorias_itsvc.tutor.services.tutor.controllers import TutorUpdaterController
from tutorias_itsvc.tutor.services.tutor.controllers import TutorDeleterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class TutorApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

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
        response = ResponseService()
        request = RequestService(request.data, TutorUpdaterSerializer)
        controller = TutorUpdaterController(
            request=request,
            response=response,
        )
        response = controller(tutor_id=tutor_id)
        return response

    def delete(self, request, tutor_id):
        response = ResponseService()
        deleter_controller = TutorDeleterController(
            response=response
        )
        response = deleter_controller(tutor_id=tutor_id)
        return response
