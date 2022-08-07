from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationGetterController
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationCreatorController
from tutorias_itsvc.students.serializers.api.v1.academic_information import AcademicInformationSerializer
from tutorias_itsvc.utils import query_debugger
from tutorias_itsvc.custom_permission import StudentRecordOwner


class AcademicInformationsApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

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
        response = ResponseService()
        request = RequestService(request.data, AcademicInformationSerializer)
        creator_controller = AcademicInformationCreatorController(
            request=request,
            response=response,
        )
        response = creator_controller(student_id=student_id)
        return response
