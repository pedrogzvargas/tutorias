from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationGetterController
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationCreatorController
from tutorias_itsvc.students.serializers.api.v1.academic_information import AcademicInformationSerializer
from tutorias_itsvc.utils import query_debugger


class AcademicInformationsApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, student_id):
        repository = AcademicInformationRepository()
        serializer = GetterSerializerService(AcademicInformationSerializer)
        response = ResponseService()
        controller = AcademicInformationGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, is_active=True)
        return response

    def post(self, request, student_id):
        repository = AcademicInformationRepository()
        response = ResponseService()
        request = RequestService(request.data, AcademicInformationSerializer)
        creator_controller = AcademicInformationCreatorController(
            request=request,
            repository=repository,
            response=response,
        )
        response = creator_controller(student_id=student_id)
        return response
