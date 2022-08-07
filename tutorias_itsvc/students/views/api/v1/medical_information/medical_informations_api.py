from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationCreatorController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationFilterController
from tutorias_itsvc.students.serializers.api.v1.medical_information import MedicalInformationSerializer
from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class MedicalInformationsApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

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
        response = ResponseService()
        request = RequestService(request.data, MedicalInformationSerializer)
        controller = MedicalInformationCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response
