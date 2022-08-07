from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationUpdaterController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationGetterController
from tutorias_itsvc.students.services.medical_information.controllers import MedicalInformationDeleterController
from tutorias_itsvc.students.serializers.api.v1.medical_information import MedicalInformationSerializer
from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class MedicalInformationApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

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
        response = ResponseService()
        request = RequestService(request.data, MedicalInformationSerializer)
        controller = MedicalInformationUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, medical_information_id=medical_information_id)
        return response

    def delete(self, request, student_id, medical_information_id):
        response = ResponseService()
        controller = MedicalInformationDeleterController(
            response=response,
        )
        response = controller(student_id=student_id, medical_information_id=medical_information_id)
        return response
