from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationCreatorController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationFilterController
from tutorias_itsvc.students.serializers.api.v1.medical_information import MedicalInformationSerializer
from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        repository = MedicalInformationRepository()
        serializer = GetterSerializerService(MedicalInformationSerializer, many=True)
        response = ResponseService()
        controller = MedicalInformationFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        repository = MedicalInformationRepository()
        response = ResponseService()
        request = RequestService(request.data, MedicalInformationSerializer)
        controller = MedicalInformationCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response
