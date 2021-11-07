from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.users.repositories import PersonalInformationRepository
from tutorias_itsvc.users.serializers.api.v1.personal_information import PersonalInformationSerializer
from tutorias_itsvc.students.services.personal_information.controllers import PersonalInformationGetterController
from tutorias_itsvc.students.services.personal_information.controllers import PersonalInformationUpdaterController
from tutorias_itsvc.students.services.personal_information.controllers import PersonalInformationDeleterController
from tutorias_itsvc.students.services.personal_information.controllers import PersonalInformationCreatorController


class PersonalInformationApi(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, PersonalInformationSerializer)
        controller = PersonalInformationCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def get(self, request, student_id):
        repository = PersonalInformationRepository()
        serializer = GetterSerializerService(PersonalInformationSerializer)
        response = ResponseService()
        controller = PersonalInformationGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, PersonalInformationSerializer)
        controller = PersonalInformationUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        controller = PersonalInformationDeleterController(
            response=response,
        )
        response = controller(student_id=student_id)
        return response
