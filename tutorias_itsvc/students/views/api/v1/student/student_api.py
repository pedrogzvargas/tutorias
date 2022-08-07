from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.student import StudentUpdaterSerializer
from tutorias_itsvc.students.serializers.api.v1.student import StudentSerializer
from tutorias_itsvc.students.services.student.controllers import StudentGetterController
from tutorias_itsvc.students.services.student.controllers import StudentUpdaterController
from tutorias_itsvc.students.services.student.controllers import StudentDeleterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class StudentApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def get(self, request, student_id):
        repository = StudentRepository()
        serializer = GetterSerializerService(StudentSerializer)
        response = ResponseService()
        controller = StudentGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, StudentUpdaterSerializer)
        controller = StudentUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        controller = StudentDeleterController(
            response=response,
        )
        response = controller(student_id=student_id)
        return response
