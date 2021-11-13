from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentPhoneRepository
from tutorias_itsvc.students.serializers.api.v1.phone import StudentPhoneSerializer
from tutorias_itsvc.students.serializers.api.v1.phone import PhoneSerializer
from tutorias_itsvc.students.services.phone.controllers import PhoneGetterController
from tutorias_itsvc.students.services.phone.controllers import PhoneCreatorController
from tutorias_itsvc.students.services.phone import PhoneFilterService


class PhonesApi(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, StudentPhoneSerializer)
        controller = PhoneCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def get(self, request, student_id):
        repository = StudentPhoneRepository()
        serializer = GetterSerializerService(PhoneSerializer, many=True)
        response = ResponseService()
        service = PhoneFilterService(repository)
        controller = PhoneGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
            getter_service=service
        )
        response = controller(student_id=student_id)
        return response
