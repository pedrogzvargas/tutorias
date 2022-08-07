from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.job import JobSerializer
from tutorias_itsvc.students.services.job.controllers import StudentJobCreatorController
from tutorias_itsvc.students.services.job.controllers import StudentJobUpdaterController
from tutorias_itsvc.students.services.job.controllers import StudentJobDeleterController
from tutorias_itsvc.students.services.job.controllers import StudentJobGetterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class JobApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        serializer = GetterSerializerService(JobSerializer)
        response = ResponseService()
        getter_controller = StudentJobGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, JobSerializer)
        controller = StudentJobCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, JobSerializer)
        controller = StudentJobUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = StudentJobDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
