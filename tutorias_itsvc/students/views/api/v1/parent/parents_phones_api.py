from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.users.repositories import PersonPhoneRepository

from tutorias_itsvc.students.services.parent.controllers import ParentPhoneCreatorController
from tutorias_itsvc.students.services.parent.controllers import ParentPhoneFilterController
from tutorias_itsvc.students.serializers.api.v1.phone import PersonPhoneSerializer


class ParentPhonesApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id, type):
        repository = PersonPhoneRepository()
        serializer = GetterSerializerService(PersonPhoneSerializer, many=True)
        response = ResponseService()
        controller = ParentPhoneFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def post(self, request, student_id, type):
        repository = PersonPhoneRepository()
        response = ResponseService()
        request = RequestService(request.data, PersonPhoneSerializer)
        controller = ParentPhoneCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response
