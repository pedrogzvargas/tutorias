from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.serializers.api.v1.institute import InstituteSerializer
from tutorias_itsvc.students.services.institute.controllers import InstituteGetterController, InstituteUpdaterController


class InstituteApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, institute_id):
        user = request.user
        repository = StudentInstituteRepository()
        serializer = GetterSerializerService(InstituteSerializer)
        response = ResponseService()
        getter_controller = InstituteGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=user.student.id, id=institute_id)
        return response

    def put(self, request, institute_id):
        user = request.user
        repository = StudentInstituteRepository()
        response = ResponseService()
        request = RequestService(request.data, InstituteSerializer)
        updater_controller = InstituteUpdaterController(
            request=request,
            repository=repository,
            response=response,
        )
        response = updater_controller(student_id=user.student.id, institute_id=institute_id)
        return response

    def delete(self, request, institute_id):
        pass
