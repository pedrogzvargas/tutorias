from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.serializers.api.v1.institute import InstituteSerializer
from tutorias_itsvc.students.services.institute import InstituteFilterService
from tutorias_itsvc.students.services.institute.controllers import (
    InstituteCreatorController,
    InstituteGetterController
)
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class InstitutesApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, InstituteSerializer)
        creator_controller = InstituteCreatorController(
            request=request,
            response=response,
        )
        response = creator_controller(student_id=student_id)
        return response

    def get(self, request, student_id):
        repository = StudentInstituteRepository()
        serializer = GetterSerializerService(InstituteSerializer, many=True)
        response = ResponseService()
        filter_service = InstituteFilterService(repository=repository)
        getter_controller = InstituteGetterController(
            repository=repository,
            getter_service=filter_service,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response
