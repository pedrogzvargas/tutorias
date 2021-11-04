from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.students.services.academic_information.controllers import StudentAcademicInformationFilterController
from tutorias_itsvc.students.serializers.api.v1.academic_information import StudentAcademicInformationSerializer
from tutorias_itsvc.utils import query_debugger


class StudentsAcademicInformationsApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, academic_information_id):
        repository = AcademicInformationRepository()
        serializer = GetterSerializerService(StudentAcademicInformationSerializer, many=True)
        response = ResponseService()
        controller = StudentAcademicInformationFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(academic_information_id=academic_information_id)
        return response
