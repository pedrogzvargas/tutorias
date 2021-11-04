from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.students.services.academic_information.controllers import AcademicInformationUpdaterController
from tutorias_itsvc.students.serializers.api.v1.academic_information import AcademicInformationSerializer


class AcademicInformationApi(APIView):
    permission_classes = [AllowAny]

    def put(self, request, student_id, academic_information_id):
        response = ResponseService()
        request = RequestService(request.data, AcademicInformationSerializer)
        updater_controller = AcademicInformationUpdaterController(
            request=request,
            response=response,
        )
        response = updater_controller(student_id=student_id, academic_information_id=academic_information_id)
        return response
