from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.users.repositories import PersonPhoneRepository

from tutorias_itsvc.students.services.parent.controllers import ParentPhoneGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentPhoneUpdaterController
from tutorias_itsvc.students.services.parent.controllers import ParentPhoneDeleterController
from tutorias_itsvc.students.serializers.api.v1.phone import PersonPhoneSerializer
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class ParentPhoneApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id, type, phone_id):
        repository = PersonPhoneRepository()
        serializer = GetterSerializerService(PersonPhoneSerializer)
        response = ResponseService()
        controller = ParentPhoneGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, type=type, phone_id=phone_id)
        return response

    def put(self, request, student_id, type, phone_id):
        repository = PersonPhoneRepository()
        response = ResponseService()
        request = RequestService(request.data, PersonPhoneSerializer)
        controller = ParentPhoneUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type, phone_id=phone_id)
        return response

    def delete(self, request, student_id, type, phone_id):
        repository = PersonPhoneRepository()
        response = ResponseService()
        controller = ParentPhoneDeleterController(
            repository=repository,
            response=response,
        )
        response = controller(student_id=student_id, type=type, phone_id=phone_id)
        return response
