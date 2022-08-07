from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentPhoneRepository
from tutorias_itsvc.students.serializers.api.v1.phone import PhoneSerializer
from tutorias_itsvc.students.services.phone.controllers import PhoneGetterController
from tutorias_itsvc.students.services.phone.controllers import PhoneUpdaterController
from tutorias_itsvc.students.services.phone.controllers import PhoneDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class PhoneApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id, phone_id):
        repository = StudentPhoneRepository()
        serializer = GetterSerializerService(PhoneSerializer)
        response = ResponseService()
        controller = PhoneGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, id=phone_id)
        return response

    def put(self, request, student_id, phone_id):
        repository = StudentPhoneRepository()
        response = ResponseService()
        request = RequestService(request.data, PhoneSerializer)
        controller = PhoneUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, phone_id=phone_id)
        return response

    def delete(self, request, student_id, phone_id):
        repository = StudentPhoneRepository()
        response = ResponseService()
        controller = PhoneDeleterController(
            repository=repository,
            response=response,
        )
        response = controller(student_id=student_id, phone_id=phone_id)
        return response
