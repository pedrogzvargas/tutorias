from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationUpdaterController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationGetterController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationDeleterController
from tutorias_itsvc.students.serializers.api.v1.medical_information import MedicalInformationSerializer
from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id, medical_information_id):
        repository = MedicalInformationRepository()
        serializer = GetterSerializerService(MedicalInformationSerializer)
        response = ResponseService()
        controller = MedicalInformationGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, id=medical_information_id)
        return response

    def put(self, request, student_id, medical_information_id):
        repository = MedicalInformationRepository()
        response = ResponseService()
        request = RequestService(request.data, MedicalInformationSerializer)
        controller = MedicalInformationUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, medical_information_id=medical_information_id)
        return response

    def delete(self, request, student_id, medical_information_id):
        repository = MedicalInformationRepository()
        response = ResponseService()
        controller = MedicalInformationDeleterController(
            repository=repository,
            response=response,
        )
        response = controller(student_id=student_id, medical_information_id=medical_information_id)
        return response
