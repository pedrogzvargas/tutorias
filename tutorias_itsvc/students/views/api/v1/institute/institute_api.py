from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.serializers.api.v1.institute import InstituteSerializer
from tutorias_itsvc.students.services.institute.controllers import InstituteGetterController
from tutorias_itsvc.students.services.institute.controllers import InstituteUpdaterController
from tutorias_itsvc.students.services.institute.controllers import InstituteDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class InstituteApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id, institute_id):
        repository = StudentInstituteRepository()
        serializer = GetterSerializerService(InstituteSerializer)
        response = ResponseService()
        getter_controller = InstituteGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id, id=institute_id)
        return response

    def put(self, request, student_id, institute_id):
        response = ResponseService()
        request = RequestService(request.data, InstituteSerializer)
        updater_controller = InstituteUpdaterController(
            request=request,
            response=response,
        )
        response = updater_controller(student_id=student_id, institute_id=institute_id)
        return response

    def delete(self, request, student_id, institute_id):
        response = ResponseService()
        deleter_controller = InstituteDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id, institute_id=institute_id)
        return response
