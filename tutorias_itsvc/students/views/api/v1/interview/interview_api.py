from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.interview import InterviewSerializer
from tutorias_itsvc.students.services.interview.controllers import InterviewGetterController


class InterviewApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        repository = StudentRepository()
        serializer = GetterSerializerService(InterviewSerializer)
        response = ResponseService()
        getter_controller = InterviewGetterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=student_id)
        return response
