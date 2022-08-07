from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationUpdaterController
from tutorias_itsvc.students.serializers.api.v1.academic_information import AcademicInformationSerializer
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class AcademicInformationApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def put(self, request, student_id, academic_information_id):
        response = ResponseService()
        request = RequestService(request.data, AcademicInformationSerializer)
        updater_controller = AcademicInformationUpdaterController(
            request=request,
            response=response,
        )
        response = updater_controller(student_id=student_id, academic_information_id=academic_information_id)
        return response
